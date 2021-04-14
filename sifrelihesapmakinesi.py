sifre="1234"

print("Şifreli Hesap Makinesi")
print("**********************")

while True:
    gsifre=input("Şifreyi Giriniz: ")
    if sifre == gsifre:
        print("Giriş Yapılmıştır")
        break
    else:
        print("Şifre Yanlıştır")
        print("Yeniden Girin")
    continue

print("*************************")
print("     Hesap Makinesi")
print("*************************")

print(" 1 - Toplama\n 2 - Çıkma\n 3 - Vurma\n 4 - Bölme\n")

i = int(input("Seçim Yapınız: "))

if i == 1:
    st1 = float(input("İlk rakamı girin: "))
    st2 = float(input("İkinci rakamı girin: "))
    print("")

    t1 = st1 + st2

    print("Cevap: {}".format(t1))
    input()

if i == 2:
    sc1 = float(input("İlk rakamı girin: "))
    sc2 = float(input("İkinci rakamı girin: "))
    print("")

    t2 = sc1 - sc2

    print("Cevap: {}".format(t2))
    input()

if i == 3:
    sv1 = float(input("İlk rakamı girin: "))
    sv2 = float(input("İkinci rakamı girin: "))
    print("")

    t3 = sv1 * sv2

    print("Cevap: {}".format(t3))
    input()

if i == 4:
    sb1 = float(input("İlk rakamı girin: "))
    sb2 = float(input("İkinci rakamı girin: "))
    print("")

    t4 = sb1 / sb2

    print("Cevap: {}".format(t4))
    input()
