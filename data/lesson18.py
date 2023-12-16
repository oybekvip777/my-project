

def full_name(f_name,l_name):
    return f'{f_name}, {l_name}'
def done(name1,name2,):
    return full_name(name1,name2)
obj=done('fayzulloh','abdulleayv')
print(obj)


# def make(name,color,price=10000):
#     return name,color,price


# print(make('matiz','red'))



def make(name,color,price=20000):
    return name,color,price
print(make('matiz','red',250000))