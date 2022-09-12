# 返回元组中找出元素索引号
a = ('Python', 'C', 'Java')
count = len(a)
b = input("请输入想要查询的下标元素:")
i = 0
for i in range(count):
    if a[i] == b:
        print(a[i] + "的下标：", i)

print(a.index("Python"))

# 在成绩列表中计算80分以上的人数
grade = [63, 84, 54, 82, 64, 95, 76, 45, 85, 69, 91, 84, 81, 68]
count = 0
for i in grade:
    if i > 80:
        count += 1
print("count=", count)
