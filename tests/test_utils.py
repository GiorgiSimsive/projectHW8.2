import json
from pathlib import Path

from src.utils import load_transactions


def test_load_transactions(tmp_path: Path) -> None:
    valid_data = tmp_path / "valid.json"
    with open(valid_data, "w", encoding="utf-8") as f:
        json.dump([{"id": 1, "amount": 100}], f)
    assert load_transactions(str(valid_data)) == [{"id": 1, "amount": 100}]

    empty_file = tmp_path / "empty.json"
    empty_file.touch()
    assert load_transactions(str(empty_file)) == []

    invalid_json = tmp_path / "invalid.json"
    with open(invalid_json, "w", encoding="utf-8") as f:
        f.write("invalid json")
    assert load_transactions(str(invalid_json)) == []

    missing_file = tmp_path / "missing.json"
    assert load_transactions(str(missing_file)) == []
