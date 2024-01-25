makanan = ["steak", "tempe", "tahu", "ayam geprek"]
minuman = ["sprite", "cocacola", "americano", "wine"]

print(makanan)
print(minuman)

print(minuman[1])
print(makanan[1])
print(len(minuman))

minuman[1] = "cocacola"
del minuman[1]
print(minuman)
makanan.append("ayam geprek")
print(makanan)