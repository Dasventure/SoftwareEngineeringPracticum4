# A brief explanation of the additional comments in the PUML file.

PUML files also includes copies of the code from the corresponding .py file. These are merely notes or comments intended to make the diagram easier to read, and by default, they are DISABLED.

To view code comments in PUML files, simply remove the **[‘]** character from **[’!define SHOW_CODE_MIN]** (for if-else and while code) and **['!define SHOW_CODE_MAX]** (for other code), which are located at the beginning of the files:

```puml
@startuml step_*
start
!ifndef STEP_*
!define STEP_*

!define SHOW_CODE_MIN
!define SHOW_CODE_MAX

...
```