year=int(input("Bir yıl giriniz: "))

leap=((year%400==0) and ((year%4==0) or (year%100 !=0))) 
if leap  == True:
    print("{} is a leap year".format(year)) 
else :
    print("{} is not a leap year".format(year))