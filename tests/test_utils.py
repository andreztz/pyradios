import pytest

from pyradios.utils import bool_to_string


@pytest.mark.parametrize(
    "inp, expected",
    [(True, "true"), (False, "false")]
)
def test_bool_to_string(inp, expected):
    assert bool_to_string(inp) == expected


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("a", pytest.raises(TypeError)),
        (1, pytest.raises(TypeError)),
    ],
)
def test_bool_to_string_value_error(inp, expected):
    with expected as exc_info:
        bool_to_string(inp)
    assert "Value must be True or False." == str(exc_info.value)
