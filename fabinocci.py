
n = int(input("enter any number ->"))
a = 0
b = 1
sum = 0

if(n == 0):
    print('sorry')

else:
    for i in range(0,n):
        print(sum,sep='  ')
        a = b
        b = sum
        sum = a + b
       
