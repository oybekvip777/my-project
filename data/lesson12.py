# 6.	 Dictionry
    # a.	Dicintry nima va qachon foydalanamiz
    # b.	Elementlarga murojat 
    # c.	Qiymatlarini o’zgartirish
    # d.	Clear, 
    # e.	Copy
    # f.	Get
    # g.	Items
    # h.	Key
    # i.	Value
    # j.	Update
    # k.	Len
    # l.	Elementlarni qo’shish
    # m.	Elementlarni o’chirish
    # n.	Ichma ich dect xosil qilish

# a.	Dicintry nima va qachon foydalanamiz

# full_data={'ism':'shahnoza','age':14,'familya':'Ortiqova','level class':8}
# print(type(full_data))
# print(full_data)


# b.	Elementlarga murojat: itmes har bir ilementni alohida tuplega saqlaydi
# d=full_data.items()
# print(d)

# c.	Qiymatlarini o’zgartirish

# full_data={'ism':'shahnoza','age':14,'familya':'Ortiqova','level class':8}
# full_data['ism']='guli'
# print(full_data)

# d.	Clear, 

# full_data.clear()
# print(type(full_data))

# e.	Copy
# d=full_data.copy()
# print(d)


# f.	Get(a,b): a kalit so'zga tegishli ilement chiqaradi
# full_data={'ism':'shahnoza','age':14,'familya':'Ortiqova','level class':8}
# result=full_data.get('ism','bunaqa ma\'lumot yo\'q')
# print(result)

# h.	Key: faqat kalit so'zlarni chiqaradi
# full_data={'ism':'shahnoza','age':14,'familya':'Ortiqova','level class':8}
# d=full_data.keys()
# print(d)

# value(): faqat qiymatlarni chiqaradi
# full_data={'ism':'shahnoza','age':14,'familya':'Ortiqova','level class':8}
# d=full_data.values()
# print(d)


# j.Update dictga dictni qo'shadi
# full_data={'ism':'shahnoza','age':14,'familya':'Ortiqova','level class':8}
# full_data.update({'mashina':'matiza','sonlar':[1,2,3,4]})
# print(full_data)

# len: uzunlik oladi
# full_data={'ism':'shahnoza','age':14,'familya':'Ortiqova','level class':8}
# print(len(full_data))

# ileemnt qo'shish
# full_data={'ism':'shahnoza','age':14,'familya':'Ortiqova','level class':8}
# full_data['mashina']='matiz'
# print(full_data)


# m.Elementlarni o’chirish: del o'chiradi
# full_data={'ism':'shahnoza','age':14,'familya':'Ortiqova','level class':8}
# del full_data['age']
# print(full_data)


# full_data={'ism':'shahnoza','age':14,'familya':'Ortiqova','level class':8,'ismalar':['anvar','alisher',{1:2,3:4,5:6}]}
# d=full_data['ismalar'][2][3]
# print(d)
