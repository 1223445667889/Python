def haha(c):
    i = 0
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    if c(i) >= 65 & c(i) <= 90 & c(i) >= 97 & c(i) <= 122:
       count += 1
    if c(i) >= 48 & c(i) <= 89:
       count1 += 1
    if c(i) == ' ':
       count2 += 1
    else:
       count3 += 1
    i += 1
    print("字母=", count)
    return count
b = (1,2,3)
aff=haha(b)
print("字母=", aff)



# def ll(p, h):
#    daf = p+h
#    print(daf)
#    return daf
# a = input()
# b = input()
# c = ll(a, b)
# print(c)
