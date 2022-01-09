print("="*20)
print("\tmanajen ram dalam komputer")
print("="*20)

RAM = int(input("masukan kapasitas total ram\t: "))
petabit = int(input("masukan kapasitas total petabit\t: "))
blok = 2
print("="*20)
opssistem = int(input("masukan kapasitas ram yang digunakan operasisistem\t: "))
isi1 = int(input("masukan kapasitas ram yang digunakan program 1\t: "))
isi2 = int(input("masukan kapasitas ram yang digunakan program 2\t: "))

petabit = (RAM / petabit)
proter = (opssistem + isi1 + isi2)
protdk = (RAM - opssistem - isi1 - isi2)
jmlblok = (isi1 + isi2) / petabit

print("output :")
print("total RAM\t :",RAM)
print("total petabit\t :",petabit)
print("total kapasitas per petabit\t :",petabit)
print("total RAm terpakai\t\t :",petabit)
print("total Ram tidak terpakai\t :",proter, "Gbps")
print("total blok yang bernilai 1\t :",protdk, "Gbps")
print("total blok yang bernilai 2\t :",jmlblok)
print("total blok yang bernilai 0\t :",blok - jmlblok)
print("="*20)

