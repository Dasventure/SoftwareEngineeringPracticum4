## Issue choice argumentation

The selected issues directly undermine core functionality or security: facility extensibility, administrator-only access,
complete facility management, and reliable user registration. Typing/TODO issues are less immediately dangerous, and streaming, reporting, and legacy utility concerns are not relevant to this PR.

## Issue list

### 1. Facility types are still hardcoded

**Location:** `src/special_facilities.py:9-15,57-71`

**Issue:** Facility types use an enum and a `match` block instead of database-backed configuration. Several names are undefined or misspelled, and new types require source-code changes.

**Why it matters now:** **NF-01 / NF-02 —** This blocks easy evolution and prevents developers from quickly adding or removing facility types as required.

**Suggestion:** Store facility definitions in a database or repository and expose CRUD operations. For example:

```python
class FacilityRepository(Protocol):
    def list(self) -> list[Facility]: ...
    def add(self, facility: Facility) -> None: ...
```

Then retrieve names dynamically rather than using `match`.

### 2. Facility access is not restricted to administrators

**Location:** `src/special_facilities.py:39-54`, `src/user_registration/manager.py:18-20`

**Issue:** `get_special_facilities()` and `edit_user()` accept no administrator context or authorization check. Any caller can retrieve or modify another student’s facilities.

**Why it matters now:** **NF-08 / NF-09 —** Facility assignments expose sensitive student and disability-related data. Missing authorization risks confidentiality and GDPR compliance before merging.

**Suggestion:** Add an explicit authorization check using a typed `Admin` role:

```python
def edit_user(self, admin: Admin, user_name: str, facilities: list[Facility]) -> None:
    if not isinstance(admin, Admin):
        raise PermissionError
```

Apply the same check to retrieval.

### 3. Facility retrieval and modification are incomplete

**Location:** `src/special_facilities.py:39-54`, `src/user_registration/manager.py:18-24`

**Issue:** Retrieval returns only `facilities[0]`, ignores missing facilities, and is typed as `int` although it returns a string. There is no clear facility-add or facility-remove operation.

**Why it matters now:** **NF-01 —** Partial CRUD behavior makes the system incorrect and forces future callers to implement inconsistent changes, reducing maintainability.

**Suggestion:** Return a complete typed collection and define explicit add/remove operations:

```python
def get_special_facilities(
    user_id: int, manager: UserManager
) -> list[EnumSpecialFacilties]:
    return manager.get_user(user_id).facilities
```

Implement and test add/remove methods through `UserManager`.

### 4. User registration contains broken control flow

**Location:** `src/user.py:19-25,48-51,80-91`, `src/user_registration/manager.py:27-44`

**Issue:** `User` is abstract yet is instantiated directly; the constructor also passes `user.get_name()` tuple data as `first_name`. Exception handling catches the general exception first, and integer values are raised as exceptions.

**Why it matters now:** **NF-04 —** These defects can make registration fail at runtime, preventing users from being added and creating an availability/reliability risk.

**Suggestion:** Use a concrete user construction path, validate specific fields, and raise typed exceptions:

```python
except ValueError as exc:
    raise UserRegistrationException("Invalid registration data") from exc
except UserRegistrationException:
    raise
```

Add fully typed `register_user(...) -> None` signatures and remove integer exception values.