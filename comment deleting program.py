k = input().split("#")
n = int(k[1])
l = []
for i in range(n):
    s = input()
    if "#" in s:
        s = s[:s.find("#")]
    s = s.rstrip()
    l.append(s)
for i in l:
    print(i)