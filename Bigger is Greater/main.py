'''
https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true
'''


import itertools
def biggerIsGreater(w):
    # lst = [ord(l) for l in w]
    lst = list(w)
    # f = sorted(list(itertools.permutations(lst)))
    for i in range(-1, -len(w), -1):
        if lst[i] > lst[i-1]:
            key = lst[i-1]
            first_part = lst[:i - 1]
            last_part = sorted(lst[i - 1:])
            center = last_part[''.join(last_part).rfind(key) + 1]
            last_part.remove(center)
            return ''.join(first_part) + center + ''.join(last_part)

    return 'no answer'

if __name__ == '__main__':
    print(biggerIsGreater('pqommldkafmnwzidydgjghxcbnwyjdxpvmkztdfmcxlkargafjzeye'))
    # Expected :'pqommldkafmnwzidydgjghxcbnwyjdxpvmkztdfmcxlkargafjzyee'