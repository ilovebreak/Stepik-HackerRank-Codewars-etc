'''
https://www.codewars.com/kata/54ce4c6804fcc440a1000ecb/solutions/python
'''


def encode(s):
	if not s:
		return '', 0
	result = []
	matrix = [s]
	[matrix.append(matrix[-1][1:] + matrix[-1][:1]) for _ in range(len(s) - 1)]
	result.append("".join([i[-1] for i in sorted(matrix)]))
	n = sorted(matrix).index(s)
	return *result, n


def decode(s, n):
	result = ""
	p = sorted((t, i) for i, t in enumerate(s))
	for _ in s:
		t, n = p[n]
		result += t
	return result


text = "Humble Bundle"
text2, n = 'e emnllbduuHB', 2

print(encode(text))
print(decode(text2, n))
