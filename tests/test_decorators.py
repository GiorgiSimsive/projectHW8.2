from typing import Any

from src.decorators import log, my_function


def test_my_function_success(capsys: Any) -> None:
    assert my_function(1, 2) == 3
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


def test_my_function_error(capsys: Any) -> None:
    my_function(1, "a")
    captured = capsys.readouterr()
    assert "my_function error: TypeError" in captured.out


def test_log_to_file(tmp_path: Any) -> None:
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def test_func(a: int, b: int) -> int:
        return a + b

    test_func(3, 4)
    with open(log_file, "r") as f:
        log_content = f.read()

    assert "test_func ok" in log_content
