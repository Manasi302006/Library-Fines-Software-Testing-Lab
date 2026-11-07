import pytest

from library_fines import late_fine, can_borrow, renewal_status


# Tests for late_fine()

def test_returned_on_time():
    assert late_fine("student", 10, False) == 0


def test_student_late_return():
    assert late_fine("student", 20, False) == 12


def test_faculty_late_return():
    assert late_fine("faculty", 35, False) == 5


def test_fine_exceeds_maximum():
    assert late_fine("guest", 100, False) == 200


def test_damaged_book():
    assert late_fine("student", 10, True) == 150


def test_unknown_member():
    with pytest.raises(ValueError, match="unknown member"):
        late_fine("invalid", 10, False)


def test_negative_days():
    with pytest.raises(ValueError, match="invalid days"):
        late_fine("student", -1, False)

# Tests for can_borrow()

def test_borrow_with_high_pending_fine():
    assert can_borrow(1, 150, "student") is False


def test_faculty_can_borrow():
    assert can_borrow(5, 0, "faculty") is True


def test_faculty_reaches_book_limit():
    assert can_borrow(10, 0, "faculty") is False


def test_student_can_borrow():
    assert can_borrow(2, 0, "student") is True


def test_student_reaches_book_limit():
    assert can_borrow(3, 0, "student") is False

# Tests for renewal_status()

def test_renewal_denied_due_to_reservation():
    assert renewal_status(0, True, 5) == "denied"


def test_renewal_limit_reached():
    assert renewal_status(2, False, 5) == "limit reached"


def test_renewal_overdue():
    assert renewal_status(1, False, -2) == "overdue"


def test_renewal_successful():
    assert renewal_status(1, False, 5) == "renewed"