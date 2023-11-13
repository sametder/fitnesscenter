import datetime 
import random

file = open("fitnesscenter.txt","a",encoding='utf-8')
random = random.randint(1, 1000000)

admin = "admin"
password= "admin"
last_day = datetime.datetime.today()

giris = input("Kullanici adinizi giriniz: ")
sifre = input("Şifrenizi Giriniz: ")




if admin == giris and password == sifre:
    print("Yapmak istediği  niz işlemi seçiniz: ")
    print("1-) Üye Ekleme")
    print("2-) Aylik Ücretler")
    print("3-) Üye Görüntüleme")

    
else:
    print("Kullanici adi veya parola yanliş girildi! ")

secim = input("Seçiminiz (1, 2, 3)")

if secim == '1':
   
    try: 
        bugün = datetime.datetime.today()
        isim = input("İsminizi Giriniz: ")
        telefon = int(input("Numaranizi Giriniz: "))
        yas = input("Yaşinizi Giriniz: ")
        cinsiyet = input("Cinsiyet Giriniz: (E/K) ")
        boy = float(input("Boyunuzu Giriniz (1.70m): "))
        kilo = int(input("Kilonuzu Giriniz: "))
        kayit_sonu = int(input("Spor yapacaği süre (Ay olarak): "))
        

        bki = kilo / (boy*boy)

        if bki < 18:
            print("İdeal kilonun altindasiniz! ")
        elif bki >= 18 and bki < 25:
            print("İdeal kilodasiniz! ")
        elif bki >= 25 and bki < 30:
            print("İdeal kilonun üstündesiniz! ")
        elif bki >= 30 and bki < 40:
            print("İdeal kilonun çok üstündesiniz!")
        elif bki > 40 :
            print("Morbid obez durumundasiniz!! ")



    except ValueError:
        print("Boşluk Birakmadan Giriniz! ")
        telefon = int(input("Numaranizi Giriniz: "))
        
    
    
       
    finally: 
        print("Üye Ekleme başariyla tamamlandi! ")


    file.write(f'Üye Numarasi: {random}\n')
    file.write(f'İsim: {isim}\n')
    file.write(f'Telefon: {telefon}\n')
    file.write(f'Yaş: {yas}\n')
    file.write(f'Cinsiyet: {cinsiyet}\n')
    file.write(f'Boy: {boy}\n')
    file.write(f'Kilo: {kilo}\n')
    file.write(f'BKİ: {bki}\n')
    file.write(f'Kayit Tarihi: {bugün}\n')
    file.write(f'Kayit Süresi: {kayit_sonu} ay \n\n')


if secim == '2':
    print("Minimum aylik kayit süresi 3 aydir \n 3 AY: 900 TL \n 6 AY: 1600 TL \n 9 AY: 2300 TL \n 1 YIL: 3000 TL ")
   

if secim == '3':
    file = open("fitnesscenter.txt","r",encoding='utf-8')
    for x in file:
        print(x,end="")



file.close()