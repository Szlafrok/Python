import pytest

import main

def test_main():
    assert main.add(1, 2) == 3
    assert main.add(1, 2) != 4

def test_palindrom():
    assert main.if_palindrom("kajak") # == True

def test_divide_exception(capsys):
    main.divide(3, 0)
    captured = capsys.readouterr()
    assert captured.out == "Dzielenie przez 0\n"

@pytest.mark.parametrize(
    "strings, expected",
    [
    (['kot', 'dziobak', 'pies'], ['kot', 'pies', 'dziobak']),
    (["minecraft", "roblox", "cs"], ['cs', 'roblox', 'minecraft'])
    ])
def test_sort_strings_by_len(strings, expected):
    assert main.sort_strings_by_length(strings) == expected