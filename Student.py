class Student:
    number = 0
    # 定义学生属性，初始化方法
    def __init__(self, name, score):
        self.name = name
        self.__score = score
        Student.number = self.__class__.number + 1

    # 定义打印学生信息的方法
    def show(self):
        print("Name: {}. Score: {}".format(self.name, self.score))

    @classmethod  # 定义类方法
    def total(cls):
        print("Total: {0}".format(cls.number))


if __name__ == '__main__':
    student1 = Student("John", 100)
    student2 = Student("Lucy", 99)
    print(student1.name)
    print(student1.__score)

    Student.total()
