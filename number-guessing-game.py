import random

# 1 ve 100 arasında random sayı oluştur
hedef = random.randint(1, 100)

skor = 10

while True:
    # Kullanicidan tahmin al
    tahmin = int(input("Aklımdan bir sayı tuttum."+str(skor)+" Hakkiniz var.Tahmin ediniz: "))

    if tahmin == hedef:
        # Doğruysa, oyun biter
        print("Tebrikler, doğru sayıyı bildiniz!")
        break
    elif tahmin < hedef:
        # Girilen sayi kucukse bir ipucu ver
        print("Küçük bir sayı girdiniz. Daha büyük bir sayı girmeyi deneyiniz.")
        skor -= 1
    else:
        # Girilen sayi buyukse bir ipucu ver
        print("Büyük bir sayı girdiniz. Daha küçük bir sayı girmeyi deneyiniz.")
        skor -= 1

    #10 seferde bilemezse oyun biter
    if skor == 0:
        print("10 hakkınız doldu. Sayı buydu: ", hedef)
        break
