#클래스는 함수+변수의 합 / 빵틀
#인스턴스 = 오브젝트는 클래스를 이용해 낸 물체 / 빵




class Person:
    def __init__(self, name, age):  #person이란 object를 만들때 name이란 인자를 받아서 name이란 변수안에 값을 넣어라
        self.name = name
        self.age = age



    def say_Hello(self, to_name): #sayheelo할때 toname이란 인자를 받아서 함수 안에서 활용
        print("안녕"+to_name+"나는"+self.name)

    def introduce(self):
        print("내 이름은 "+ self.name + "그리고 나는"+ str(self.age)+ "살 이야")




# 상속
class Police(Person): #폴리스가 펄슨을 상속
    def arrest(self, to_arrest):
        print("넌 체포됐다,"+to_arrest)

class Progarmmer(Person):
    def program(self, to_program):
        print("다음에 뭘 만들지 ? 아 이걸만들어야겠따:" + to_program)


sejin = Person("세진", 27)        #세진은 person
jiwoo = Police("지우", 21)       #지우는 경찰
jenny = Progarmmer("제니", 22)   #제니는 프로그래머

sejin.introduce() #세진소개
jiwoo.arrest("세진") #지우는 세진 체포
jenny.introduce #제니소개
jenny.program("매크로") #제니는 프로그래머 매크로만들자!!

# sejin.arrest("제니") #세진은 경찰이 아니라서 제니를 체포못해


