# 不能， 他改变了data的指向，指向新实例

def scale(data, factor):
    for val in data:
        val*=factor
    print(data)
        
def scale_2(data, factor):
    for val in range(len(data)):
        data[val]*=factor
    print(data)
        
data = [1,2,3,4,5]

scale(data, 3)
scale_2(data, 3)