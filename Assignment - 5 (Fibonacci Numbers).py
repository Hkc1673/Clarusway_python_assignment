fn=[0,1]
if 11>2:
    for i in range(2, 11):
        a= fn[i-1] + fn[i-2]
        fn.append(a)
print(fn)