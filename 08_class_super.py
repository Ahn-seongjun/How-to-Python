# 08_class_super.py

class person:
    # 생성자 함수
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def eat(self,food):
        print('{}은 {}을 먹습니다.'.format(self.name,food))
    def sleep(self,minute):
        print('{}은 {}분동안 잡니다'.format(self.name,minute))

    def work(self,minute):
        print('{}은 {}분동안 일합니다'.format(self.name, minute))

# 상속 : class 클래스명(부모클래스명)

# child클래스 생성(Student, Employee)
class Student(person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 하위 클래스에서 부모 클래스가 갖고 있는 함수 재정의 하는 것 - 매서드 오러라이드
    def work(self,minute):
        super().work(minute) # 부모 클래스에 있는 매서드를 호출해서 실행
        print('{}은 {}분동안 강의를 듣습니다'.format(self.name, minute))

class Employee(person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

bob = Employee("Bob",25)
bob.eat("BBQ")
bob.sleep(30)
bob.work(60)

lee = Student("Lee",19)
lee.eat("NOODLE")
lee.sleep(60)
lee.work(30)