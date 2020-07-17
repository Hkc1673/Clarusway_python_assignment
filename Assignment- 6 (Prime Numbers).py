n=int(input("Please, write a number: "))
list=[]
for num in range(2, n + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           list.append(num)
print(list)
