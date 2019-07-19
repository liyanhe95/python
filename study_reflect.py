#反射
#魔法一样
#静态---运行前，如果要调用类的属性或者方法，我需要实例化它的对象
#动态---运行时，我就获取类的属性或者方法，甚至更改它的属性或者方法
class Girls:
    single = False
    def __init__(self,name,age):
        self.name = name  #实例属性 ，初始化被调用的时候，这个属性才会有
        self.age = age

    def singe(self):
        print(self.name+"会唱歌")

if __name__ == '__main__':
    girls = Girls("huahua",18)
    # # print(girls.name)
    # girls.singe()
    print(girls.__dict__) #__dict__返回类的所有属性
    # #setattr 是运行时
    # setattr(Girls,"hobby","music")#给类或者是实例对象动态的去添加属性或者方法
    # #girls 是一个实例 如果是对象的话仅仅限于当前的这个实例对象
    # #给Girls这个类对象去增加属性的话，每个实例对象都有这个属性
    # # print(girls.hobby)
    #
    # # girls2 = Girls("lucy",20)
    # # print(girls2.hobby)
    # print(getattr(Girls,"hobby"))  #根据属性名获取类的属性，动态的去获取
    # # print(getattr(Girls,"male"))#根据属性名获取类的属性，当属性不存在的时候，报AttributeError
    # #获取之前先动态的去判断
    # print(hasattr(Girls,"male")) #判断当前这个类，有没有这个属性,有就返回True，没有就返回False
    # print(hasattr(Girls,"single")) #判断类是否有这个属性
    # print(hasattr(girls,"name"))#判断对象是否有实例属性
    #
    # # delattr(girls,"name") #删除对象属性
    # # print(girls.name)
    # delattr(Girls, "single")#删除类属性
    # print(getattr(Girls,"single"))



