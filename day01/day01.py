lines = None
with open('input.txt') as f:
    lines = f.readlines()

a = []
b = []
for line in lines:
    aa, bb = line.split('   ')
    a.append(int(aa))
    b.append(int(bb))

a.sort()
b.sort()

s = 0
for i in range(len(lines)):
    s += abs(a[i] - b[i])

print(s)

# part 2
s = 0
for i in range(len(lines)):
    s += a[i] * b.count(a[i])

print(s)
