'''
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python
'''

def zero(action=None): return action(0) if action else 0
def one(action=None): return action(1) if action else 1
def two(action=None): return action(2) if action else 2
def three(action=None): return action(3) if action else 3
def four(action=None): return action(4) if action else 4
def five(action=None): return action(5) if action else 5
def six(action=None): return action(6) if action else 6
def seven(action=None): return action(7) if action else 7
def eight(action=None): return action(8) if action else 8
def nine(action=None): return action(9) if action else 9

def plus(number): return lambda x: x + number
def minus(number): return lambda x: x - number
def times(number): return lambda x: x * number
def divided_by(number): return lambda x: x // number


print(three(times(two())))
print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))