import numpy

def Recursion(x,y,num,length,array):
    if(length<=0):
        return
    L = length 
    while L > 0:
        L -= 1
        y += 1
        num += 1
        array[x][y] = num
    L = length-1
    while L > 0:
        L -= 1
        num += 1
        x += 1
        y -= 1
        array[x][y]=num
    L = length-2
    while L > 0:
        L -= 1
        num += 1
        x -= 1
        array[x][y]=num
    Recursion(x,y,num,length-3,array)  

def main():
    num=int(input("请输入矩阵行数："))
    array=numpy.zeros((num,num),dtype=numpy.int16)
    Recursion(0,-1,0,num,array)
    print(array)

if __name__ == "__main__":
    main()