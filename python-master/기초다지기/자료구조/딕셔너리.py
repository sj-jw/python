# 키(x)값은 불변해야함
x = {
    "name" : "원",
    "age" : 20,
    0 :"sejin",
    "ni" : 27,
}

print(x)
print(x["name"])
print(x["age"])

print(x[0])
print(x["ni"])

print("age" in x)

print(x.keys()) #딕셔너리 키 보여줘(왼쪽거들임 name age 0 ni)
print(x.values())#벨류들보여줘 (오른쪽꺼들 (원,20,sejin,27))

for key in x:
    print(key)
    print(x[key])


x[0] = "세진"
print(x)

x["school"] = "한빛"
print(x)