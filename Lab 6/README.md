# Lab 6 – Library Fines

## 1. Objective

The objective of this lab is to perform code coverage and branch coverage testing on the Library Fines application using Python and pytest. The aim is to achieve at least 90% code coverage and branch coverage by writing suitable test cases.

## 2. Application Details

The application is implemented in Python and contains the following three functions:

- **late_fine():** Calculates the fine based on the member type, number of days a book is kept, and whether the book is damaged.
- **can_borrow():** Checks whether a library member is eligible to borrow books based on the number of books held, pending fine, and member type.
- **renewal_status():** Determines the renewal status based on the number of previous renewals, reservation status, and remaining days.

## 3. Code Coverage Testing

**Test file:** `CodeCoverageTest_library_fines_application.py`

**Tools used:** Python, pytest, pytest-cov, and coverage.

The test cases were written to execute the statements in the application, including normal inputs and error conditions.

**Results:**
- Total test cases passed: 16
- Total statements: 32
- Missed statements: 0
- Code coverage achieved: 100%

The code coverage result is available in `Code_Coverage_Terminal.png`.

## 4. Branch Coverage Testing

**Test file:** `BranchCoverageTest_library_fines_application.py`

Branch coverage testing was performed to check the different decision outcomes and execution paths in the application.

The test cases cover the conditions and branches present in the application functions.

**Results:**
- Total test cases passed: 22
- Total branches: 22
- Missed branches: 0
- Branch coverage achieved: 100%

The branch coverage result is available in `Branch_Coverage_Terminal.png`.

## 5. Files Included

| File | Description |
|---|---|
| `library_fines.py`