def nameOfBestCustomers(sales,customers):
    y=-1
    for x in sales:
        if(x>y):
            y=x
    num = sales.index(y)
    print(customers[num]+" "+str(y))

sales = list()
customers =list()
x=1
while x==1:
    customers.append(input("请输入顾客名："))
    sales.append(float(input("请输入消费金额：")))
    x =int(input("是否还要继续输入？是/1 否/0 ："))
nameOfBestCustomers(sales,customers)