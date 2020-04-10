String = input("请输入字符串：")
for length in range(1,len(String)+1,1):
    for begin in range(0,len(String),1):
       if begin+length <= len(String):
            print(String[begin:begin+length])