from project import check_sys, option, a_to_f
import pytest


def main():
    test_a_to_f()
    test_check_sys()
    test_choice()
    test_search_grade()
    test_letter_grade()


def test_check_sys():
    with pytest.raises(SystemExit):
        check_sys()


def test_option():
    with pytest.raises(ValueError):
        option("search")


def test_a_to_f():
    assert a_to_f("95") == "A"
    assert a_to_f("40") == "Fail"
    assert a_to_f("60") == "F"


if __name__ == "__main__":
    main()
