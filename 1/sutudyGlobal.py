num = 100
def studyGlobal():
    # 此num为局部变量，对外部的全局变量num不重新赋值
    num = 200
    return num

# def studyGlobal_2():
#     #此num为全局变量，对变量量重新赋值
#     global num
#     num = 200
#     return num

if __name__ == "__main__":
    num1 = studyGlobal()
    # num2 = studyGlobal_2()
    print(num1,"****",num)
    # print(num2,"****",num)