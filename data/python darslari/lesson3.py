
# 2)	Pythonda Sonlar
    # a.	.Int(),Float()
    # b.	Sonlarni o’girish
    # 3)	Tasodifiy son (RANDOM)¬¬¬
# a.	Random nima
    # b.	random.choice(list,tuple,str) 
    # c.	random.choices(list,tuple,str)
    # d.	random.randint(start,end)
    # e.	random.shuffle(list)
    # f.	random.sample(list,n)
    # g.	random.randrange(start,stop,skip)
    # h.	random.uniform(start,stop)

# --------------------------------------------------------------


import random

# b.	random.choice(list,tuple,str) 

# sonlar=['sobir','oybek']
# natija=random.choice(sonlar)
# print(natija)



# c.	random.choices(list,tuple,str)

# sonlar=['Habibulloh','Oybek','Komil']
# natija=random.choices(sonlar,k=2)
# print(natija)



# d.	random.randint(start,end)

# natija=random.randint(1,100)
# print(natija)



 # e.	random.shuffle(list)
# sonlar=['Habibulloh','Oybek','Komil']
# random.shuffle(sonlar)
# print(sonlar)



# f.	random.sample(list,n)

# sonlar=[1,2,3,4,4,45,34,24,232323]
# natija=random.sample(sonlar,k=2)
# print(natija)



# g.	random.randrange(start,stop,skip)

# natija=random.randrange(0,101,3)
# print(natija)



# h.	random.uniform(start,stop)

# natija=random.uniform(1,10)
# print(natija)

# i=1
# while True:
#     i=i+1000
#     print(i)