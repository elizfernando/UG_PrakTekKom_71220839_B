print("SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERLUBANG")
k = int(input("Masukkan Angka: "))
print(' '*(k-1),"*")
for z in range ((k-1),0,-1):
    print(' '*(z-1),"**")
print("**"*k)

