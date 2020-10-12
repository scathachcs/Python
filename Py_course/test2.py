import numpy

class chess:
    def __init__(self):
        self.board=numpy.zeros((10,10),dtype=numpy.int16)
    
    def judge(self,x,y,color):
        total = 1
        x_pos=x+1
        y_pos=y
        while x_pos<=9 and x_pos>=0 and y_pos<=9 and y_pos>=0 and self.board[x_pos][y_pos]==color :
            total += 1
            x_pos += 1
        x_pos=x-1
        y_pos=y
        while x_pos<=9 and x_pos>=0 and y_pos<=9 and y_pos>=0 and self.board[x_pos][y_pos]==color:
            total += 1
            x_pos -= 1
        if total == 5:
            return True
        else :
            total = 1

        x_pos=x
        y_pos=y+1
        while x_pos<=9 and x_pos>=0 and y_pos<=9 and y_pos>=0 and self.board[x_pos][y_pos]==color:
            total += 1
            y_pos += 1
        x_pos=x
        y_pos=y-1
        while x_pos<=9 and x_pos>=0 and y_pos<=9 and y_pos>=0 and self.board[x_pos][y_pos]==color :
            total += 1
            x_pos -= 1
        if total == 5:
            return True
        else :
            total = 1
        
        x_pos=x+1
        y_pos=y-1
        while x_pos<=9 and x_pos>=0 and y_pos<=9 and y_pos>=0 and self.board[x_pos][y_pos]==color :
            total += 1
            x_pos += 1
            y_pos -= 1
        x_pos=x-1
        y_pos=y+1
        while x_pos<=9 and x_pos>=0 and y_pos<=9 and y_pos>=0 and self.board[x_pos][y_pos]==color:
            total += 1
            x_pos -= 1
            y_pos += 1
        if total == 5:
            return True
        else :
            total = 1

        x_pos=x-1
        y_pos=y-1
        while x_pos<=9 and x_pos>=0 and y_pos<=9 and y_pos>=0 and self.board[x_pos][y_pos]==color:
            total += 1
            x_pos -= 1
            y_pos -= 1
        x_pos=x+1
        y_pos=y+1
        while x_pos<=9 and x_pos>=0 and y_pos<=9 and y_pos>=0 and self.board[x_pos][y_pos]==color:
            total += 1
            x_pos += 1
            y_pos += 1
        if total == 5:
            return True
        else :
            total = 1
        return False

    def play(self,x,y,color):
        if self.board[x][y] != 0 or x>9 or x<0 or y>9 or y<0:
            return False
        self.board[x][y] = color 
        return True

    def print(self):
        print(self.board)

def main():
    CHESS = chess()
    color = 1 #白方先
    x=int(input("请输入x坐标"))
    y=int(input("请输入y坐标"))
    while not CHESS.play(x,y,color) :
        print('请重新输入')
        x=int(input("请输入x坐标"))
        y=int(input("请输入y坐标"))
    CHESS.print()
    while  CHESS.judge(x,y,color) ==False :
        color = -color
        x=int(input("请输入x坐标"))
        y=int(input("请输入y坐标"))
        while not CHESS.play(x,y,color) :
            print('请重新输入')
            x=int(input("请输入x坐标"))
            y=int(input("请输入y坐标"))
        CHESS.print()
    if color ==1:
        print('white win')
    else:
        print('black win')


if __name__ == "__main__":
    main()