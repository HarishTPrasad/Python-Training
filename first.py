# for i in range(10, 0, -1):
#
#     print(i)

# a = range(5)
# for i in a :
#     print(i)

# for i in range(5) :
#     print(i)

# st = "Parul University"
# for ch in st :
#     print (ch)


from array import *

roll = array('i',[101,102,103,104,105])
n = len(roll)
for i in range(n) :
    print (roll[i])


stu = array('i',[])
n=int (input("how many elements?"))
for i in range (n) :
    stu.append(int(input("Enter element")))
