
s = input()
a = s.split()

for i in range(len(a)):
    a[i] = a[i][::-1]

print(" ".join(a))
