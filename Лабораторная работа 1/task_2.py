disk = 1.44 * (1024 ** 2)
p = 100
st = 50
symb = 25
weight = 4
book = p*st*symb*weight
count = int(disk//book)
print("Количество книг, помещающихся на дискету:", count)