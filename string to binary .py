n = input("enter any string-->")
for i in n:
    result = ''.join(format(ord(i), 'b'))
    print("the binary result of",n,"is --> ",result)
