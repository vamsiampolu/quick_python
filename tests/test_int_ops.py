import pytest
from quick_python.int_ops import IntegerOperations

subject = IntegerOperations()


class TestIntegerOperations:
    def test_add(self):
        assert subject.add(3, 4) == 7

    def test_add_zero(self):
        assert subject.add(3, 0) == 3

    def test_add_to_zero(self):
        assert subject.add(0, 3) == 3

    def test_add_neg(self):
        assert subject.add(3, -1) == 2

    def test_add_both_neg(self):
        assert subject.add(-3, -2) == -5

    def test_add_both_zero(self):
        assert subject.add(0, 0) == 0

    def test_sub(self):
        assert subject.sub(4, 2) == 2

    def test_sub_zero(self):
        assert subject.sub(4, 0) == 4

    def test_sub_one_neg_num(self):
        assert subject.sub(-4, 2) == -6
        assert subject.sub(4, -2) == 6

    def test_sub_both_neg_num(self):
        assert subject.sub(-4, -2) == -2
        assert subject.sub(-2, -4) == 2

    def test_mul(self):
        assert subject.mul(2, 3) == 6

    def test_mul_zero(self):
        assert subject.mul(4, 0) == 0

    def test_mul_one(self):
        assert subject.mul(7, 1) == 7

    def test_mul_one_neg_num(self):
        assert subject.mul(-2, 1) == -2

    def test_mul_two_neg_num(self):
        assert subject.mul(-3, -2) == 6

    def test_div(self):
        assert subject.div(8, 2) == 4

    def test_div_by_one(self):
        assert subject.div(4, 1) == 4

    def test_div_returns_floor_when_not_exactly_divisible(self):
        assert subject.div(7, 2) == 3

    def test_div_by_zero_raises_error(self):
        with pytest.raises(ZeroDivisionError):
            subject.div(3, 0)

    def test_mod(self):
        assert subject.mod(4, 2) == 0
        assert subject.mod(5, 2) == 1
        assert subject.mod(3, 1) == 0

    def test_mod_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            subject.mod(3, 0)

    def test_cast_nonnumber_to_int(self):
        with pytest.raises(ValueError):
            subject.cast_to_int("mega")

    def test_cast_number_to_int(self):
        assert subject.cast_to_int("44") == 44

    def test_cast_float_string_to_int(self):
        with pytest.raises(ValueError):
            subject.cast_to_int("44.234") == 44

    def test_exponentiation_where_exponent_is_zero(self):
        subject.exponentiation(2, 0) == 1

    def test_exponentiation_where_exponent_is_one(self):
        subject.exponentiation(3, 1) == 3

    def test_exponentiation_where_exponent_is_a_positive_integer(self):
        subject.exponentiation(3, 2) == 9

    def test_exponentiation_where_exponent_is_a_negative_number(self):
        subject.exponentiation(3, -1) == 1 / 3

    def test_exponentiation_where_exponent_is_a_fraction(self):
        subject.exponentiation(9, 1 / 2) == 3
