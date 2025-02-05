print("Ini Sudah Masuk ke Github Guyss")


print("Aplikasi Menghitung Luas Segitiga\n")

def segitiga(alas,tinggi) :
    return (alas * tinggi)/2

def keliling(s1,s2,a):
    return s1+s2+a


a = int(input("Masukan alas Segitiga :"))
t = int(input("Masukan tinggi Segitiga :"))
s1 = int(input("Masukan sisi 1 : "))
s2 = int(input("Masukan sisi 2 : "))



hasil1 = segitiga(a,t)
hasil2 = keliling(s1,s2,a)


print("Hasilnya adalah :",hasil1)
print("Keliling : ",hasil2)