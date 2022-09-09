str = "Hello,Python3!"
print(str[2])
print(str[0:3])
substr = "o"
print(str.split(substr))

str1 = "I am LOL!"
print(str1.upper())
print(str1.lower())
print(str1.find("a"))
print(str1.replace('L', 'o'))

for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%2d" % (j, i, i*j), end='   ')
    print("  ")

i = 1
while i < 10:
    j = 1
    while j <= i:
        print("%d*%d=%2d" % (i, j, i*j), end='   ')
        j += 1
    print("")
    i += 1

Sname = ['赵大', '钱二', '张三', '李四', '王五', '马六', '赵大']
position = 0
for name in Sname:
    if name=='赵大':
        pass
        Sname[position] = "赵大明"
        print("位置:", position)
    position += 1
print(Sname)


a = ['ha', 'haha', 'hahaha', 'eew']
len(a)
b = a[0]
a[0] = a[len(a)-1]
a[len(a)-1] = b
print('a=', a)

b = [2, 3, 4, 5, 6]
b.insert(0, 1)
b.append(7)
print("b=", b)

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
coun = 0
coun1 = 0
for i in range(1, 10):
    if c[i] % 2 == 0:
        coun += c[i]
    if c[i] % 2 != 0:
        coun1 += c[i]
print("coun=", coun)
print("coun1=", coun1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name)  # 郑俊杰
        print(self.age)


P = Person('peter', 20)
print("\n")


class Student:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s

    def set_score(self):
        self.score = 100

    def print_all(self):
        print("姓名 %s ,年龄 %d，分数%d" % (self.name, self.age, self.score))
        # print("姓名,年龄，分数", self.name, self.age, self.score)


a1 = Student("张三", 22, 130)
a1.print_all()
a1.set_score()
a1.print_all()
print('\n')


class A:
    def fun(self):
        print("A.fun")


class B(A):
    def fun(self):
        super().fun()
        print('B.fun')


B().fun()
print('\n')


class Computer:
    name = ''
    price = 0
    size = 0

    def __init__(self, n, p, s):
        self.name = n
        self.price = p
        self.size = s

    def speak(self):
        print("%s 的价格是%d元：，大小是%d英寸:" % (self.name, self.price, self.size))


class Indicator(Computer):
    def __init__(self, n, p, s):
        super().__init__(n, p, s)
        # super(Indicator, self).__init__(n, p, s)
        self.name = n
        self.price = p
        self.size = s

    def speak(self):
        print("%s 的价格是%d元：，大小是%d英寸:" % (self.name, self.price, self.size))


class Internal(Computer):
    def __init__(self, n, p, s):
        super().__init__(n, p, s)
        self.name = n
        self.price = p
        self.size = s

    def speak(self):
        print("%s 的价格是%d元：，大小是%d英寸:" % (self.name, self.price, self.size))


information = Indicator("显示器", 1000, 25)
information.speak()
information = Internal("内存", 500, 2)
information.speak()


class AbnormalRatio(Exception):
    def __init__(self,message):
        self.message = message

    def __str__(self):
        return self.message
try:
    StandardFatRatio=0.2
    Weight = input('请输入你的体重')
    Fat=input('请输入你的脂肪重量')
    if(not Weight.isdigit()):
        raise ValueError('体重必须是数字')
    if(not Fat.isdigit()):
        raise ValueError('脂肪重量必须是数字')

    FatRatio = float(Fat)/float(Weight)
    RatioError = abs((FatRatio-StandardFatRatio)/StandardFatRatio)

    if FatRatio>0.1:
         if RatioError<=0.1:
            print('体脂含量正常')
         else:
            print('体脂含量不达标')
    elif FatRatio<0.1:
         raise AbnormalRatio('体脂含量异常')

except ZeroDivisionError:
    print('发生异常，体重不能为0')
except AbnormalRatio as e:
    print('发生异常，体重不能为0')
except Exception as e:
    print('输入有误:%s:%s'%(e.Error,e.Error))
















