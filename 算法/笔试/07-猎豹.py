# 矩阵空水的地方计数


src_str = input()
s = src_str.split(",")
l = len(s)
a = [[] for i in range(l)]
seen = []
max_list = max(s)
for i in range(l):
    if int(s[i]) == 0:
        for j in range(int(max_list)):
            a[i].append(0)
    else:
        for k in range(int(s[i])):
            a[i].append(1)
        if len(a[i]) < int(max_list):
            for m in range(int(max_list)-len(a[i])):
                a[i].append(0)
print(a)
floor_v = 0
total_v = 0
for i1 in range(int(max_list)):
    for j1 in range(l):
        if a[j1][i1] == 1:
            seen.append(j1)
    print(seen)
    for k1 in range(len(seen)-1):
        if seen[k1+1]-seen[k1] > 1:
            num = seen[k1+1]-seen[k1]-1
            floor_v += num
    total_v += floor_v
    floor_v = 0
    seen = []

print(total_v)
