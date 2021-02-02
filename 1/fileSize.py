import os
path = "d:\桌面文件\桌面\新建文件夹"

def file_size(path):
    # 获取所有文件夹名称
    for file in os.listdir(path):

        # 组合成完事的路径
        filePath = os.path.join(path,file)

        # 判断是否是文件夹，如果是文件夹则递归，如果不是文件夹则是文件
        if os.path.isdir(filePath):
            file_size(filePath)
        else:
            # 获取文件大小
            fileSize = os.path.getsize(filePath)
            if fileSize == 0:
                print(filePath)
                os.remove(filePath)


if __name__ == "__main__":
    file_size(path)