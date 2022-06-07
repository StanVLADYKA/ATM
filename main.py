import time
lanlist=[["Insert our card","Reading bank card details","Enter your PIN(1111)","Invalid pin","Choose an operation"],
        ["Вставьте карту","Идет считываение карты","Введите ПИН-код(1111)","Неверный пин","Выберите операцию"],
        ["Устаўце картку","Ідзе счытванне карты","Увядзіце ПІН-код(1111)","Няверны пін","Абярыце аперацыю"],
        ["插卡","刷卡进行中","输入您的代码(1111)","无效的引脚","选择一个操作"]]


def Lang(l):
    if l<=4:
        o=lanlist[l-1][0]
    else:
        o="Error, Ошибка, Памылка, 错误"
    return o

def Ins(l):
    i=lanlist[l-1][1]
    return i
def Pin(l):
    p=lanlist[l-1][2]
    return p
def Check(l,pin):
    if pin==1111:
        m=lanlist[l-1][4]
    else:
        m=lanlist[l-1][3]
    return m

def maneger():
    l=int(input("1 -English\n2 -Русский\n3 -Беларуский\n4 -汉语\n :"))
    print(Lang(l))
    if "Error" in Lang(l):
        l = int(input("1 -English\n2 -Русский\n3 -Беларуский\n4 -汉语\n"))
        print(Lang(l))
    time.sleep(3)
    print(Ins(l))
    time.sleep(3)
    print(Pin(l))
    pin=int(input())
    time.sleep(2)
    print(Check(l,pin))
    time.sleep(2)
    print("The END")

maneger()