'''
Aşağıdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde saklayınız.
Toplam ödenen ücret nedir?
Ödenen miktarın kdv oranı nedir? %18
'''
# Müşteri bilgileri
musteriAd = "Didem"
musteriSoyad = "Kış"
musteriTelefon = "44444444"
musteriMail = "aaa@mail.com"
musteriAdres = "İzmir"

# Ürün bilgileri
urun1_ad = "Kablosuz Mouse"
urun1_fiyat = 550

urun2_ad = "Kablosuz Klavye"
urun2_fiyat = 650

urun3_ad = "Dizüstü Bilgisayar"
urun3_fiyat = 55000

toplamOdenenUcret = urun1_fiyat + urun2_fiyat + urun3_fiyat 
print("Toplam ödenen miktar: " , toplamOdenenUcret)

print("Toplam kdv oranı: " , toplamOdenenUcret * 0.18)

'''
# Veri tipi dönüşümü
sayi = "100"  # str
gercek_sayi = int(sayi)  # str'den int'e dönüşüm

# Sonuç
print(f"Gerçek sayı: {gercek_sayi + 50}")  # 100 + 50 = 150

'''