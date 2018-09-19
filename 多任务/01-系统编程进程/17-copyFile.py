import os
from multiprocessing import Pool,Manager


def copyFileTask(name,oldFolderName,newFolderName,queue):
    "完成copy一个文件的功能"
    #print(name)
    fr=open(oldFolderName+"/"+name)
    fw=open(newFolderName+"/"+name,"w")
    #print("-----")
    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

    queue.put(name)

def main():
    #0.获取用户要copy的文件夹的名字
    oldFolderName = input("请输入文件夹的名字：")

    #1.创建一个新的文件夹。
    newFolderName=oldFolderName+"-复件"
    #print(newFolderName)
    os.mkdir(newFolderName)

    #2.获取old文件夹中所有的文件的名字。
    fileNames = os.listdir(oldFolderName)
    #print(fileNames)
    #3.使用多进程的方式copy原文件夹中的所有文件到新的文件夹中
    pool=Pool(5)
    queue=Manager().Queue()

    for name in fileNames:
        pool.apply_async(copyFileTask,args=(name,oldFolderName,newFolderName,queue))

    num=0
    allNum=len(fileNames)
    while True:
        queue.get()
        num+=1
        copyRate=num/allNum
        print("\rcopy的进度是:%.2f%%"%(copyRate*100),end="")
        if num==allNum:
            break
    print("\n已完成c o p y!!!")
    
if __name__=="__main__":
    main()
