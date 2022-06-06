
a1="Cash or bank card transactions"
a2="Операции с наличными или с банковской картой"
a3="Аперацыі з наяўнымі або з банкаўскай карткай"
a4="使用现金或银行卡操作"
a5="Error"
b1="1 - Cash\n2-bank card\n"
b2="1- Операции с наличными\n2 банковской картой\n"
b3="1 - Аперацыі з наяўнымі\n2банкаўскай карткай\n"
b4="1 -使用现金或\n银行卡操作\n"

def Lang(l):
    if l==1:
        o=a1
    elif l==2:
        o=a2
    elif l==3:
        o=a3
    elif l==4:
        o=a4
    else:
        o=a5
    return o

def Oper(s):
    if l==1:
        o2=b1
    elif l==2:
        o2=b2
    elif l==3:
        o2=b3
    elif l==4:
        o2=b4
    else:
        o="Error"
    return o2


def maneger():
    l=int(input("1 -English\n2 -Русский\n3 -Беларуский\n4 -汉语\n"))
    print(Lang(l))
    if l==1:
        b=b1
    elif l == 2:
        b = b2
    elif l == 3:
        b = b3
    elif l == 4:
        b = b4
    s = int(input(b))
    print(Oper(s))



maneger()