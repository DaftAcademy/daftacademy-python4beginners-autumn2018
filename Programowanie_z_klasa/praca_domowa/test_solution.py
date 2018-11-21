import pytest

from .solution import MyFraction


@pytest.mark.parametrize(
	'numerator,denominator,expected_numerator,expected_denominator', [
		(1, 1, 1, 1),
		(2, 1, 2, 1),
		(1, 2, 1, 2),
		(1, 3, 1, 3),
		(3, 5, 3, 5)
	]
)
def test_creation_simple_positional_args(
	numerator, denominator, expected_numerator, expected_denominator
):
	result = MyFraction(numerator, denominator)
	assert result.numerator == expected_numerator
	assert result.denominator == expected_denominator
	assert isinstance(result.numerator, int)
	assert isinstance(result.denominator, int)


@pytest.mark.parametrize(
	'numerator,denominator,expected_numerator,expected_denominator', [
		(2, 2, 1, 1),
		(3, 3, 1, 1),
		(10, 20, 1, 2),
		(9, 27, 1, 3),
		(6, 10, 3, 5)
	]
)
def test_creation_composite_positional_args(
	numerator, denominator, expected_numerator, expected_denominator
):
	result = MyFraction(numerator, denominator)
	assert result.numerator == expected_numerator
	assert result.denominator == expected_denominator


@pytest.mark.parametrize(
	'numerator,denominator,expected_numerator,expected_denominator', [
		(1, 1, 1, 1),
		(2, 1, 2, 1),
		(1, 2, 1, 2),
		(1, 3, 1, 3),
		(3, 5, 3, 5)
	]
)
def test_creation_simple_keyword_args(
	numerator, denominator, expected_numerator, expected_denominator
):
	result = MyFraction(numerator=numerator, denominator=denominator)
	assert result.numerator == expected_numerator
	assert result.denominator == expected_denominator
	assert isinstance(result.numerator, int)
	assert isinstance(result.denominator, int)


@pytest.mark.parametrize(
	'numerator,denominator,expected_numerator,expected_denominator', [
		(2, 2, 1, 1),
		(3, 3, 1, 1),
		(10, 20, 1, 2),
		(9, 27, 1, 3),
		(6, 10, 3, 5)
	]
)
def test_creation_composite_keyword_args(
	numerator, denominator, expected_numerator, expected_denominator
):
	result = MyFraction(numerator=numerator, denominator=denominator)
	assert result.numerator == expected_numerator
	assert result.denominator == expected_denominator


def test_numerator_required():
	with pytest.raises(TypeError) as e:
		MyFraction()


@pytest.mark.parametrize(
	'numerator,expected_numerator', [
		(1, 1),
		(2, 2),
		(3, 3),
		(5, 5),
		(101, 101)
	]
)
def test_denominator_defaults_to_one(numerator, expected_numerator):
	result = MyFraction(numerator)
	assert result.numerator == expected_numerator
	assert result.denominator == 1


@pytest.mark.parametrize(
	'a_num,a_den,b_num,b_den,expected_num,expected_den', [
		(1, 1, 1, 1, 2, 1),
		(1, 2, 1, 2, 1, 1),
		(1, 2, 1, 3, 5, 6),
	]
)
def test_adding(a_num, a_den, b_num, b_den, expected_num, expected_den):
	a = MyFraction(a_num, a_den)
	b = MyFraction(b_num, b_den)
	result = a + b
	assert isinstance(result, MyFraction)
	assert result.numerator == expected_num
	assert result.denominator == expected_den


@pytest.mark.parametrize(
	'numerator,denominator', [
		(1, 1),
		(2, 2),
		(3, 3),
		(5, 5),
		(101, 101),
		(1, 2),
		(2, 1),
		(10,12234),
	]
)
def test_equality(numerator, denominator):
	left = MyFraction(numerator, denominator)
	right = MyFraction(numerator, denominator)
	assert left == right
	assert right == left
	assert left is not right


@pytest.mark.parametrize(
	'a_num,a_den,b_num,b_den', [
		(1, 1, 1, 2),
		(2, 1, 1, 2),
		(2, 3, 1, 3),
		(10, 9, 9, 10)
	]
)
def test_inequality(a_num, a_den, b_num, b_den):
	a = MyFraction(a_num, a_den)
	b = MyFraction(b_num, b_den)
	assert a != b


@pytest.mark.parametrize(
	'a_num,a_den,b_num,b_den,expected_num,expected_den', [
		(1, 1, 1, 2, 3, 2),
		(2, 1, 1, 2, 5, 2),
		(2, 3, 1, 3, 1, 1),
		(10, 9, 9, 10, 181, 90),
		(1, 1, 1, 1, 2, 1),
		(1, 2, 1, 2, 1, 1),
		(1, 2, 1, 3, 5, 6),
	]
)
def test_incerase_value(
	a_num, a_den, b_num, b_den, expected_num, expected_den
):
	a = MyFraction(a_num, a_den)
	b = MyFraction(b_num, b_den)
	result = a
	result += b
	assert result is a
	assert result.numerator == expected_num
	assert result.denominator == expected_den


@pytest.mark.parametrize(
	'num,den,expected', [
		(1, 1, 'MyFraction(numerator=1, denominator=1)'),
		(3, 3, 'MyFraction(numerator=1, denominator=1)'),
		(1, 2, 'MyFraction(numerator=1, denominator=2)'),
		(2, 1, 'MyFraction(numerator=2, denominator=1)'),
		(11,12234, 'MyFraction(numerator=11, denominator=12234)'),
		(15,20, 'MyFraction(numerator=3, denominator=4)'),
	]
)
def test_repr(num, den, expected):
	a = MyFraction(num, den)
	result = repr(a)
	assert result == expected


@pytest.mark.parametrize(
	'num,den,value,expected_num,expected_den', [
		(1, 1, 1, 2, 1),
		(2, 1, 1, 3, 1),
		(123, 1234, 34, 34*1234+123, 1234)
	]
)
def test_add_int_to_my_fraction(num, den, value, expected_num, expected_den):
	a = MyFraction(num, den)
	result = a + value
	assert a is not result
	assert result.numerator == expected_num
	assert result.denominator == expected_den


@pytest.mark.parametrize(
	'num,den,value,expected_num,expected_den', [
		(1, 1, 1, 2, 1),
		(2, 1, 1, 3, 1),
		(123, 1234, 34, 34*1234+123, 1234),
	]
)
def test_add_my_fraction_to_int(num, den, value, expected_num, expected_den):
	a = MyFraction(num, den)
	result = value + a
	assert a is not result
	assert result.numerator == expected_num
	assert result.denominator == expected_den


@pytest.mark.parametrize(
	'a_num,a_den,value,expected_num,expected_den', [
		(1, 1, 1, 2, 1),
		(2, 1, 1, 3, 1),
		(2, 3, 1, 5, 3),
		(11, 9, 11, 110, 9),
	]
)
def test_test_incerase_value_by_int(
	a_num, a_den, value, expected_num, expected_den
):
	a = MyFraction(a_num, a_den)
	result = a
	result += value
	assert result is a
	assert result.numerator == expected_num
	assert result.denominator == expected_den

