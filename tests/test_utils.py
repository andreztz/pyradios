import pytest

from pyradios.utils import types
from pyradios.utils import bool_to_string
from pyradios.utils import validate_input


@pytest.mark.parametrize('inp, expected', [(True, 'true'), (False, 'false')])
def test_bool_to_string(inp, expected):
    assert bool_to_string(inp) == expected


@pytest.mark.parametrize(
    'inp, expected',
    [
        ('a', pytest.raises(TypeError)),
        (1, pytest.raises(TypeError)),
    ],
)
def test_bool_to_string_value_error(inp, expected):
    with expected as exc_info:
        bool_to_string(inp)
    assert 'Value must be True or False.' == str(exc_info.value)


@pytest.mark.parametrize(
    'input_data',
    [{'limit': 10, 'offset': 0}, {'limit': '10', 'offset': '0'}],
)
def test_validate_input(input_data):
    """
    Allow `str` and `int` for limit and offset
    """
    validate_input(types['search'], input_data)


@pytest.mark.parametrize(
    'input_data, expected',
    [
        ({'limit': 10, 'offset': 'a'}, ('offset', '`int` or `str`', 'str')),
        ({'limit': 10.1}, ('limit', '`int` or `str`', 'float')),
        (
            {'offset': True, 'limit': None},
            ('offset', '`int` or `str`', 'bool'),
        ),
        ({'limit': None}, ('limit', '`int` or `str`', 'NoneType')),
    ],
)
def test_validate_input_with_invalid_limit_and_offset(input_data, expected):
    with pytest.raises(TypeError) as exc:
        validate_input(types['search'], input_data)

    assert str(exc.value) == 'Argument {!r} must be {}, not {}'.format(
        *expected
    )
