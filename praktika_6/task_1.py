import re

n = 4052
pattern = re.compile(r"2\d*82[4-6]\d4")
sp1 = []

for x in range(1, 110):
    if pattern.fullmatch(str(x)) and x % n == 0:
        sp1.append(x // n)

print(sp1)
