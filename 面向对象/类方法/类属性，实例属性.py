class Tool(object):
    
    #类属性
    num=0

    #方法
    def __init__(self,new_name):
        #实例属性（和类有关）
        self.name=new_name
        Tool.num+=1
tool1=Tool("铁锹")
tool1=Tool("工兵铲")
tool1=Tool("水桶")
print(Tool.num)
