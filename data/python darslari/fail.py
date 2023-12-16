# print 

# print(43-22)
# print('oybek')


# ozgaruvchi

# ism='oybek'
# print(ism)

# son=100
# son1=200
# print(son1+son)


# turini aniqlash

# son=12
# d=type(son)
# print(d)


# print(type('mastura'))



# str ozgaruvchi

# ism='sobijon'
# print(ism)

# ism='oybek'
# print(ism)




# str index

# ism='ulugbek'
# d=ism[3]
# print(d)

# ism='manzura'
# g=ism[6]
# print(g)



# str koptirish

# ism='jam'
# ism1='shid'
# print(ism+ism1)


# ism='jamshid'
# print(10*ism)




# str len


# ism='oybek'
# p=len(ism)
# print(p)



# ism='fayzulloh    '
# o=len(ism)
# print(o)





# str find


# ism='komiljon'
# l=ism.find('ko')
# print(l)




# ism='sobirova nuriya'
# s=ism.find('ri')
# print(s)




# str index 2usulli


# ism='komiljon'
# u=ism.index('j',0,7)
# print(u)




# ism='sevara'
# i=ism.index('a',2,5)
# print(i)





# str isdigit


# h='201020132019'
# q=h.isdigit()
# print(q)




# t='19831981'
# x=t.isdigit()
# print(x)





# str isalpha


# ism='QWERTYUIOP'
# Y=ism.isalpha()
# print(Y)



# ism='asdfghjkl'
# u=ism.isalpha()
# print(u)




# islower str


# ism='llkjhgfdsa'
# e=ism.islower()
# print(e)



# ism='oybek'
# d=ism.islower()
# print(d)



# str ispase


# bosh='                '
# i=bosh.isspace()
# print(i)




# bosh='        '
# e=bosh.isspace()
# print(e)




# str istitle


# ism='Diloram'
# l=ism.istitle()
# print(l)


# ism='Komiljonov'
# b=ism.istitle()
# print(b)



# str title


# ism='sobirov ulugbek'
# g=ism.istitle()
# print(g)



# ism='sobirova mastura'
# d=ism.istitle()
# print(d)




# str capitaliz


# ism='komiljon sobirjon'
# q=ism.capitalize()
# print(q)


# ism='habibloh'
# v=ism.capitalize()
# print(v)




# random choise


import random

# random choice

# run=['sobir','oybek','nuriya']

# ran=random.choice(run)
# print(ran)



# q=['aziz','komil','habib']

# g=random.choice(q)
# print(g)


# random choices

# ism=['sobir','oybek','mastura','fayzulloh','shukurjon','komiljon']
# natija=random.choices(ism,k=3)
# print(natija)

# sonlar=[1,2,3,4,5,6,7,8]
# natija=random.choices(sonlar,k=1)
# print(natija)

# random randint

# son=random.randint(20,1000)
# print(son)



# son=random.randint(1,10000)
# print(son)

# random shuffle

# sonlar=[12,13,14,15,16,17,18,19,20]
# random.shuffle(sonlar)
# print(sonlar)


# ismlar=['oybek','sobirjon','azizbek','komiljon','habibulloh']
# random.shuffle(ismlar)
# print(ismlar)

# random.sample

# sonlar=['oybek','sobirjon','mastura','ulugbek','nuriya']
# natija=random.sample(sonlar,k=1)
# print(natija)


# sonlar=[1,2,3,4,4,45,34,24,232323]
# natija=random.sample(sonlar,k=2)
# print(natija)


# random.randrange

# natija=random.randrange(1,201,2)
# print(natija)



# natija=random.randrange(10,10001,10)
# print(natija)



# random.uniform

# natija=random.uniform(1,101)
# print(natija)

# natija=random.uniform(10,1000001)
# print(natija)

# < va > nima qilishi

# yosh=10
# yosh1=23




# w=yosh1>yosh
# print(w)


# yosh=55
# yosh1=55




# d=yosh1<yosh
# print(d)

# <= nima qilishi

# son=2000
# son1=2001


# o=son>=son1
# print(o)

# son=2010
# son1=2010

# d=son1>=son
# print(d)




# and

# z=True
# s=False

# q=s and z
# print(q)


# a=True
# k=False

# d=k and a
# print(d)

# or

# q=False
# z=True

# a=q or z
# print(d)


# k=True
# a=False

# d=k or a
# print(d)



# list qoyish


# son=[2013,2019,2011,1983,1981,2009]
# son[5]=2010
# print(son)


# ism=['oybek','ulugbek','habibulloh','komiljon','sobirjon','mastura']
# ism[-1]='malika'
# print(ism)


# append


# oila=['adam','oyim','ukam','man','singlim']
# oilar.append('buvam')
# print(oila)



# sonlar=[2000,2001,2002,2003,2004,2005]
# sonlar.append(2006)
# print(sonlar)


# extend

# sonlar=[1,2,3,4,5,6,]
# sonlar1=[7,8,,9,10,]

# sonlar1.extend(sonlar)
# print(sonlar1)



# son=[11,12,13,14,15]
# son1=[16,17,18,19,20]

# son1.extend(son)
# print(son1)

# insert 

# ism=['sobir','shukurjon','oybek',',manzura']

# ism.insert(0,'guli')
# print(ism)


# sonlar=[2001,2002,2003,2005]

# sonlar.insert(3,2004)
# print(sonlar)


# remove

# sonlar=[1,2,3,4,5,6,78,9,0,]

# sonlar.remove(5)
# print(sonlar)

# sonlar=[1,2,3,4,,5,,6,]

# sonlar.remove(5)
# print(sonlar)



# pop


# sonlar=[2010,2013,2019,2023]

# sonlar.pop(3)
# print(sonlar)

# sonlar=[1,2,3,4,5,6,]

# sonlar.pop(4)
# print(sonlar)



# count


# w=[1,1,2,3,4,5,6,7,8,9]
# d=w.count(1)
# print(d)

# t=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
# q=w.count(2)
# print(q)




#  sort


# q=[100,99,98,97,96,95,94,93,92,91,90]
# q.sort(reverse=True)
# print(q)


# c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# c.sort(reverse=True)
# print(c)



# reverse

# a=list(range(1,201,2))
# a.reverse()
# print(a)

# h=list(range(1,1001))
# h.reverse()
# print(h)


# add set


# q={1,2,3,4,5,6,7,8,9}
# q.add(10)
# print(q)


# a={95,96,97,98,99,}
# a.add(100)
# print(a)

# update set

# a={10,11,12,13,14,15,16,17,18,19}
# b={20,21,22,23,24}
# b.update(a)
# print(b)

# s={1990,1991,1992,1993,1994,1995}
# w={1996,1997,1998,1999,2000}
# w.update(s)
# print(b)



# len set

# a={1,2,3,4,5,6,7,8,9}
# s=len(a)
# print(s)

# a={1590,8381,546,746,744,745}
# lena=len(a)
# print(lena)


# remove

# z={'oybek','sobir','nuriya','malika'}
# z.remove(3)
# print(z)


# x={'fayzulloh','oybek','habibulloh','sobirjon','azizbek','shahnoza','komiljon'}
# x.remove(3)
# print(x)



# discard

# a={43,40,13,10,4}
# a.discard(-3)
# print(a)

# s={'mastura','ulugbek','oybek','nuriya','sobirjon'}
# s.discard(-1)
# print(s)

# pop

# d={'matematika','j/t','informatika'}
# d.pop()
# print(d)

# a={'a','b','c'}
# a.pop()
# print(a)


# union

# a={'a','b','c'}
# b={1,2,3,4,5}
# d=a.union(b)
# print(d)


# w={'o','y','b','e','k'}
# x={'s','o','b','i','r'}
# d=w.union(x)
# print(d)




# tuple count


# h=(,89,88,8,8,88989,9,8,89,9,89,8,9,89)
# g=h.count(9)
# print(g)

# a=(12,1,3,3,2,2,4,1,1,4,1)
# b=a.count(1)
# print(b)




















































































































