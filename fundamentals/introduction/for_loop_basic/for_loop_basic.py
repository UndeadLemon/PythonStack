for i in range(151):
    print(i)

for i in range (0,1001,5):
    print(i)

for i in range (1,101):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)
# x = 0
# for i in range (1,500000,2):
#     x = x + i
# print(x)
sum = 0
for i in range (0,500001):
    if i%2 != 0:
        sum += i

print(sum)

for i in range (2018,-1,-4):
    print(i)

def counting(lowNum, highNum, mult):
    for i in range (lowNum, highNum+1):
        if i%mult == 0:
            print(i)

counting(1,100,3)

