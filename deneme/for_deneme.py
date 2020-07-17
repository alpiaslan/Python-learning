faktoriyel=1

while True:
    sayi = int(input("Lütfen Pozitif bir sayı giriniz:"))
    if (sayi<=0):
        print("Lütfen negatif olmayan bir sayı ile tekrar deneyiniz!")
    else:
        for i in range(1,sayi+1):
            faktoriyel = faktoriyel*i

        print("Faktöriyel:",faktoriyel)
        break
