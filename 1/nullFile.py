import os
path = "G:/工作/中科/项目/06_南和智慧城市/资源"
# print(os.path.isdir("D:\新建文件夹\1\5"))
# if os.listdir("D:/新建文件夹/1"):
#     print("T")
# else:
#     print("F")

'''
1、获取到文件夹和文件；
2、找出每一个文件夹即目录；
3、如果目录不为空，则递归调用；如果为空则删除此目录
'''
def null_file(dirr):
    # 将目录下的文件夹以列表形成返回
    files = os.listdir(dirr)
    for file in files:

        # 使用方法将文件夹拼成目录
        d = os.path.join(dirr,file)
        # 判断是否为目录
        if os.path.isdir(d):

            # 判断目录是否为空
            if os.listdir(d):
                null_file(d)
            else:
                print("****",d)
                os.rmdir(d)
# def file_size(fil):
#     pa = os.listdir(fil)
#     for
#
#         # fileSize = os.path.getsize(files)
#         # print(fileSize)

if __name__ == "__main__":
    null_file(path)