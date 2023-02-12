import pytest

from main import onetwothree

FIXTURE = []

files_qty = 13

for filename in range(1, files_qty + 1):
    with open(f'{filename}', 'r', encoding='utf-8') as input:
        number = int(input.readline())

    with open(f'{filename}.clue', 'r', encoding='utf-8') as output:
        answer = int(output.readline())
    FIXTURE.append((number, answer))
# [(10, 0), (1, 1), (100, 5), (5, 5), (9, 9), (2, 2), (24, 7), (2194, 8), (52901, 0), (99999999, 8), (100000000000, 1),
# (1941021920494, 7), (3428981920094209410981249124912477124, 9)]
print(FIXTURE)

@pytest.mark.parametrize("number, answer", FIXTURE)
def test_onetwothree(number, answer):
    result = onetwothree(number)
    assert result == answer