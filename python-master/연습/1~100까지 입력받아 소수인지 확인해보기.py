n = int(input())
list1 = list()

for i in range (1, 101):
    sj = True 
    if i ==1 : sj = False
    for j in range(2, i): #2부터 i-1까지 나눴을때 (ex. 5/2, 5/3, 5/4) 나머지가 0인지 판별하기 위해 2~ i // 1~i는 나머지가 다 0 이라 안됌
        if(i%j) == 0:
            sj = False
            break
            
    if sj == False:
        list1.append(i)
        print (list1)
if n in list1:
    print("소수가아닙니다")
else:
    print("소수입니다")    

