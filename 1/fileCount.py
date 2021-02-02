import os
#文件路径
path = "d:\桌面文件\桌面\新建文件夹"

print(os.path.isdir(path))
for p in os.listdir(path):
    d = os.path.join(path,p)
    if (os.path.isdir(d)) == True:
        print(os.path.isdir(d))
    if not os.listdir(path):
        print(os.listdir(path))
# 删除空文件夹
# def deleteNullDir(dirr):
#     if os.path.isdir(dirr):
#         for p in os.listdir(dirr):
#             d = os.path.join(dirr,p)
#             if (os.path.isdir(d)) == True:
#                 deleteNullDir(d)
#     if not os.listdir(dirr):
#         os.remove(dirr)
#         print(dirr)
# if __name__ == "__main__":
#     deleteNullDir(path)



# print(os.listdir(path))
# os.walk（）遍历目录下文件，返回三元组
# for root,dirs,files in os.walk(path):
#     for file in files:
#         fileDir = os.path.join(root,file)
#         print(fileDir)
    # for di in dirs:
    #     print(di)
    #     print("**"*5)
#    for file in files:
#        print(file)
#         fileDir = os.path.relpath(file)
#         print(fileDir)