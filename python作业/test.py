from random import *
def fun(n):
    for i in range(n):
        n=randint(1,100)
        print(n)
        if n>50:
            print("大师兄")
        else:
            print("二师x")
        print("师傅")

fun(10)