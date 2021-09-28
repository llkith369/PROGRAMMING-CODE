n = input("--")
n1 = input("--")

if(len(n)==len(n1)):
    if(sorted(n) == sorted(n1)):
        print("these are anagrams")

    else:
        print("not anagrams")

else:
    print("no")
