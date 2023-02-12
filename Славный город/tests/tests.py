import pytest

from main import deikstra, print_way, main

FIXTURE = []

for filename in range(1, 21):
    with open(f'{filename}', 'r', encoding='utf-8') as input:
        rows = int(input.readline())
        matrix = [[int(x) for x in list(input.readline().strip())] for _ in range(rows)]
        # print(rows)
        # print(matrix)
    with open(f'{filename}.clue', 'r', encoding='utf-8') as output:
        answer = [list(x.strip()) for x in output.readlines()]
    FIXTURE.append((rows, matrix, answer))


@pytest.mark.parametrize("rows, matrix, answer", FIXTURE)
def test_good_city(rows, matrix, answer):
    deikstra_matrix = deikstra(rows, matrix)
    result = print_way(rows, main(rows, deikstra_matrix, [(-1, -1)]))
    assert result == answer

# print_way(main(deikstra(rows, city), result))
