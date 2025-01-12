import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state() -> None:
    data = [{"state": "EXECUTED", "value": 100}, {"state": "PENDING", "value": 50}]
    expected = [{"state": "EXECUTED", "value": 100}]
    assert filter_by_state(data, "EXECUTED") == expected


def test_filter_with_no_matching_state() -> None:
    data = [{"state": "PENDING", "value": 50}]
    expected = []  # type: ignore
    assert filter_by_state(data, "EXECUTED") == expected


def test_filter_with_invalid_data_type() -> None:
    with pytest.raises(TypeError):
        filter_by_state("not_a_list", "EXECUTED")  # type: ignore


def test_filter_with_non_dict_elements() -> None:
    data = [{"state": "EXECUTED"}, "not_a_dict", {"state": "PENDING"}]
    with pytest.raises(ValueError):
        filter_by_state(data, "EXECUTED")


@pytest.mark.parametrize(
    "state,expected",
    [
        ("PENDING", [{"state": "PENDING", "value": 50}]),
        ("CANCELED", [{"state": "CANCELED", "value": 25}]),
        ("EXECUTED", [{"state": "EXECUTED", "value": 100}]),
    ],
)
def test_filter_with_different_states(state, expected):  # type: ignore
    data = [
        {"state": "EXECUTED", "value": 100},
        {"state": "PENDING", "value": 50},
        {"state": "CANCELED", "value": 25},
    ]
    assert filter_by_state(data, state) == expected


def test_sort_descending() -> None:
    data = [{"date": "2025-01-10"}, {"date": "2025-01-11"}, {"date": "2025-01-09"}]
    expected = [{"date": "2025-01-11"}, {"date": "2025-01-10"}, {"date": "2025-01-09"}]
    assert sort_by_date(data) == expected


def test_sort_ascending() -> None:
    data = [{"date": "2025-01-10"}, {"date": "2025-01-11"}, {"date": "2025-01-09"}]
    expected = [{"date": "2025-01-09"}, {"date": "2025-01-10"}, {"date": "2025-01-11"}]
    assert sort_by_date(data, descending=False) == expected


def test_key_error_missing_date() -> None:
    data = [{"date": "2025-01-10"}, {"value": 100}]
    with pytest.raises(KeyError):
        sort_by_date(data)


def test_value_error_non_dict_elements() -> None:
    data = [{"date": "2025-01-10"}, "not_a_dict", {"date": "2025-01-09"}]
    with pytest.raises(ValueError):
        sort_by_date(data)


def test_type_error_non_list_input() -> None:
    with pytest.raises(TypeError):
        sort_by_date("not_a_list")  # type: ignore
