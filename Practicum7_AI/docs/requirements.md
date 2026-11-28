# Requirements

## Context

Given that the University of Antwerp wishes to accommodate as many students as possible, it offers so-called "bijzondere faciliteiten" to certain students.

## Facilities that should be present

- Extra time during exams.
- Exam papers in large fonts.
- The option to orally clarify exam answers.
- Exam papers in braille.
- Text-to-speech software.
- Different exam dates for students who work or practice sports (werkstudenten, topsportstatuut).

## Requirements for these facilities

- The different types of facilities should not be hardcoded. Instead, they should be stored in a database such that adding and removing types of facilities is easy.
- The facilities should be able to be added to and removed from a user.
- The facilities should be able to be retrieved for a given user.
- Only admins should be able to view and modify the facilities.
- Legacy code should be re-used:
  - the `user_registration` package, which will be responsible for adding users, as well as modifying the special facilities,
  - the `utils` package.