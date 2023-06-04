# 1.输入一个整数n，打印输出n以内的全部大于0的偶数
# 2.输入三个整数，要求打印输出最大的和最小的数字
# 3.使用循环实现输出2-3+4-5+6-7+8-9+10
# 4.使用循环输出1,2,3,4,5,7,8,9,11,12
# 5.使用while循环从大到小输出100-50,然后再从0循环输出到50

n = int(input("请输入一个整数："))
print(n, "以内的全部大于0的偶数为：")
for i in range(2, n+1, 2):
    print(i, end=" ")
print()
print("输出结束")
print()

li = []
for i in range(1,4):
    n = input("请输入整数：")
    li.append(n)
print(li)
print("其中最大的数为：", max(li))
print("最小的数为：", min(li))
print()

sum1 = 0
sum2 = 0
for i in range(2, 11, 2):
    sum1 += i
for i in range(3, 10, 2):
    sum2 += i
nou = int(sum1 - sum2)
print("2-3+4-5+6-7+8-9+10 =", nou)
print()

for num in range(1, 13):
    if num == 6 or num == 10:
        continue
    print(num, end=" ")
print()

print()
n = 100
m = 0
while n >= 50:
    print(n, end=" ")
    n -= 1
print()
while m <= 50:
    print(m, end=" ")
    m += 1
