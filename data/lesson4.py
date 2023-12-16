# 5)	Pyhtonda satrlar
    # a.	Satrni o’zgaruvchiga beriktirish
    # b.	Ko’p qatorli satr
    # c.	Satirdagi elementga index buyicha murojat
    # d.	Satrlar ustuda amallar, satrlarni qushish, satrni songa kupaytirish, 
    # e.	satr uzunligi len(), index buyicha murojat
    # f.	Satrdan kesma ajratish
    # g.	Len()
    # h.	S.find(‘word in S’,start,end) S  str
    # i.	S.index(‘word in S’,start,end) 
    # j.	S.isdigit()
    # k.	S.isalpha()
    # l.	S.Isalnum()
    # m.	S.Islower()
    # n.	S.ispace()
    # o.	S.istitle()
    # p.	S.title()
    # q.	S.capitalize()
    # r.	S.lstrip()
    # s.	S.rstrip()
    # t.	S.lower()
    # u.	S.upper()
    # v.	S.replace()
    # w.	S.split()
    # x.	Qolganlarini mustaqil urganish
    # i.	Satrelarni tekshirish


# 5)	Pyhtonda satrlar


# a.	Satrni o’zgaruvchiga beriktirish
# ism='Fayzulloh'

# c.	Satirdagi elementga index buyicha murojat

# ism='Ali Vali'
# d=ism[4]
# print(d)

# d.	Satrlar ustuda amallar, satrlarni qushish, satrni songa kupaytirish,
# ism='ali'
# ism1='vali'
# print(ism+ism1)

# print(10*ism1)


# e.satr uzunligi len(), index buyicha murojat

# ism='vali '
# d=len(ism)
# print(d)



# h.	S.find(‘word in S’,start,end) S  str
# ism='Habililloh abdullayev'
# d=ism.find('abd')
# print(d)


# i.	S.index(‘word in S’,start,end) 

# ism='xaifiza '
# d=ism.index('i',3,5)
# print(d)

# j.	S.isdigit()
a='23323232323'
d=a.isdigit()
print(d)


# k.	S.isalpha()

# ism='cvdedesdedd '
# d=ism.isalpha()
# print(d)


# l.	S.Isalnum()#
ism='dsadswdedf4325'
d=ism.isalnum()
print(d)


# .	S.Islower()
# ism='bdullayev'
# d=ism.islower()
# print(d)


 # n.	S.ispace()

# ism='  .  '
# d=ism.isspace()
# print(d)


# o.	S.istitle()
# ism='abdullayev fayzulloh'
# d=ism.istitle()
# print(d)


# p.	S.title()
# ism='abdullayev fayzulloh'
# d=ism.istitle()
# print(d)


# q.	S.capitalize()

ism='abdullayev fayzulloh'
d=ism.capitalize()
print(d)