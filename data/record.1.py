# 1). 

# Dadangiz va Onangizni isimlarini chiqaradigan funksiya yozing:

# 2).

# my_family nomli list bor va oila a'zolaringiz isimlari saqlangan.
# Shularni alohida ekranga chiqaradigan funksiya yozing.

# 3).
# 1 dan 20 gacha bo'lgan sonlarni listi bor.  Shu listdan toq sondi va juft sondi mos holda toq_son va juft_son nomli bo'sh listga o'zlashtirsi.

# 4).
#  5 ta do'stingizni ismini friend nomli listga saqlang. Shu list 3-ilementda o'zingizning ismingiz turubdi.

# Shunday funksiya yozingki, friend nomli listdagi 1-ilementdan isimingizgacha bo'lgan ilementlarni ekranga chiqarsin



# 1-misol

# def my_mother_father():
#     print("mastura","ulug'bek")

# print(my_mother_father())

# 2-misol

# my_family=['mastura',"ulug'bek",'oybek','sobirjon','nuriya']

# def family():
#     for i in my_family:
#         print(i)

# print(family())    

# 3-misol

toq_son=[]
juft_son=[]

def my_list():
    for i in list(range(1,21)):
        if i %2==0:
            juft_son.append(i)
        else:
            toq_son.append(i)
        
    print("toq_sonlar:",toq_son)
    print("juft_sonlar",juft_son)

print(my_list())          

# 4-misol

# my_nema=['abubakir','sobirjon',"g'ofur",'oybek','shukurjon']

# def my_nemis():
#     for i in my_nema:
#         if i=='oybek':
#             print(i)
#             break
# print(my_nemis())        




