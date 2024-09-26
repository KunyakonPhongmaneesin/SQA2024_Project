import pytest
from your_module import NewSystemAdapter

@pytest.mark.parametrize("data, expected", [
    ("data1", "Legacy result: data1"),
    ("data2", "Legacy result: data2"),
])
def test_new_operation(data, expected):
    legacy_system = LegacySystem()
    adapter = NewSystemAdapter(legacy_system)

    result = adapter.new_operation(data)

    assert result == expected