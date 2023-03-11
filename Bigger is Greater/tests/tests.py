import pytest
from main import biggerIsGreater

with open('input.txt', 'r') as input_file:
    with open('output.txt') as output_file:
        input_text = [line.strip() for line in input_file.readlines()]
        output_text = [line.strip() for line in output_file.readlines()]
        FIXTURE = list(zip(input_text, output_text))

@pytest.mark.parametrize("inp, outp", FIXTURE)
def test_biggerIsGreater(inp, outp):
    result = biggerIsGreater(inp)
    assert result == outp