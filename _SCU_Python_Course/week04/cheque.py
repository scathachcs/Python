import turtle
import datetime

class Account:
    def __init__(self, name, work_hours, hoursalary):
        self.name = name
        self.work_hours = int(work_hours)
        self.hoursalary = float(hoursalary)

    def IntName(self):
        if self.work_hours > 40:
            return 40 * self.hoursalary + (self.work_hours -
                                           40) * self.hoursalary * 1.5
        else:
            return self.work_hours * self.hoursalary

    def PrintCheque(self):
        turtle.setup(width=500, height=250)
        turtle.penup()
        turtle.goto(-140, 70)
        turtle.pendown()
        turtle.seth(0)
        turtle.fd(280)
        turtle.right(90)
        turtle.fd(140)
        turtle.right(90)
        turtle.fd(280)
        turtle.right(90)
        turtle.fd(140)
        turtle.penup()
        turtle.goto(-130, 50)
        turtle.pendown()
        turtle.write("中国银行支票", font=('arial', 12, 'normal'))
        turtle.penup()
        turtle.bk(20)
        turtle.pendown()
        x = datetime.datetime.now()
        turtle.write("日期：" + x.strftime("%x"))
        turtle.penup()
        turtle.bk(20)
        turtle.pendown()
        turtle.write("收款人:" + self.name)
        turtle.penup()
        turtle.bk(20)
        turtle.pendown()
        n = self.IntName()
        turtle.write("人民币:{}".format(n))
        turtle.done()


def main():
    name = input("请输入你的名字：")
    hour = input("请输入你的工作时长：")
    hoursalary = input("请输入你的时薪：")
    person = Account(name, hour, hoursalary)
    person.PrintCheque()


if __name__ == "__main__":
    main()
