x = input("Masukan Kata: ")
palindrome = True 

panjang_x = len(x)

for y in range(panjang_x//2):
    if (x[y] != x[panjang_x-y-1]):
        palindrome = False
        break
if palindrome:
    print ("Yes")
    print ("Jika dibalik: ", x)
else :
    print ("No")
    print ("Jika dibalik: ", X)
    