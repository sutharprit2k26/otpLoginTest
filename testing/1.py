def fun1():
    fun1.var = 100

    # print(fun1.var)
fun1()
def fun2():
    x = 1000
    if fun1.var == x:
        return True
    else:
        return False

if fun2():
    print("Yes")
else:
    print("No")


# print(fun1.var)