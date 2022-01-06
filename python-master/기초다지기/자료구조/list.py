x = [4,2,3,1]
e = ["Hello", "there"]
num = len(x)
print(num)

y= sorted(x)
print(y)


z = sum(x) 
print(z)


for n in x:  #n에 x를 하나씩 넣어서 보여줘
    print(n)

for c in e:
    print(c)


print(x.index(3)) #어느자리에있니?
print(e.index("Hello"))


print("Hello" in e) #있니?
print(e)


if "Hello" in e:
    print("ㅇㅇ")


