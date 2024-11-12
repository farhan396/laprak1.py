#fungsi mencari luas persegi panjang
def Luaspersegipanjang (panjang,lebar):
    return panjang*lebar 

#fungsi mencari keliling persegi panjang
def Kelilingpersegipanjang(panjang,lebar):
    return 2*(panjang+lebar)

p = int(input("masukkan nilai panjang : "))
l = int(input("masukkan nilai lebar : "))
#nilai luas jika panjang=10, dan lebar=5
hasil_luas = Luaspersegipanjang(p,l)
hasil_keliling = Kelilingpersegipanjang(p,l) 

print("luasnya adalah ", hasil_luas)
print("kelilingnya adalah", hasil_keliling)
