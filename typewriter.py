import sys,time
import os
import operator

filename=sys.argv[1]
 
#f= open(filename,'r')
#后面加上encoding 参数，然后就可以解决一些中文字符显示异常的问题了
sourcefile= open(filename,'r',encoding='utf-8')   
def print_one_by_one(text):
    sys.stdout.write("\r " + " " * 60 + "\r") # /r 光标回到行首
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.flush() #把缓冲区全部输出
    #sys.stdout.write('\n')
        
for text in sourcefile.readlines():
    sourceStr = text.splitlines()
    print(sourceStr[0])
    inputStr = input ()
    result = operator.eq(sourceStr[0], inputStr)    #python3用operator裡的函式取代cmp()
    if result == True:
        print('Good Job!!')
    else:
        print('try again')

sourcefile.close()
 
sys.stdout.write('\n')

# reference: https://blog.csdn.net/qiqiyingse/article/details/81281658

# targetStr = '123123 123'
# print (targetStr, end='\n')
# inputStr = input ()

# result = operator.eq(targetStr, inputStr)
# if result == True:
#     print('Good Job!!')
# else:
#     print('try again')

