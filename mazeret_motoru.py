#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABARTILI MAZERET MOTORU v1.0
Evrenin resmi mazeret üreticisi.
Bu kod, insanlığın en büyük problemini çözmek için yazılmıştır:
"Neden bir şey yapmıyorum?" sorusuna bilimsel, felsefi ve bürokratik cevaplar üretmek.
"""

import random
import time
import sys

# Resmi mazeret veritabanı (çok ciddi)
MAZERETLER = [
    "Kuantum belirsizlik prensibi nedeniyle bugün herhangi bir iş yapmak, evrenin temel yasalarını ihlal ederdi.",
    "Atalarımın ruhları bana rüyamda 'bugün dinlen' diye fısıldadı. Aile bağlarına saygı göstermek zorundayım.",
    "Kahve makinemle aramda yaşanan duygusal kriz henüz çözülmedi. Odaklanamıyorum.",
    "Bugün ayın evreleri mazeret üretmeye uygun değil. Astrologum onaylamadı.",
    "Zaman-uzay continuum'unda küçük bir çatlak fark ettim. Önce onu kapatmam lazım, yoksa işler karışır.",
    "Bilgisayarımın klavyesi bana karşı bir isyan başlattı. Tuşlar kendi başına yazıyor, kontrol edemiyorum.",
    "Bu işi yapmak, paralel evrendeki versiyonumun mutluluğunu olumsuz etkileyebilir. Sorumluluk almam.",
    "Hava durumu raporunda 'yoğun tembellik' uyarısı var. Dışarı çıkmak bile riskli.",
    "En son yediğim yemek henüz sindirilmedi. Enerji seviyem bilimsel olarak yetersiz.",
    "Bir kelebeğin kanat çırpışı nedeniyle bu işi yapmam, Amazon ormanlarında yağmur yağmasına sebep olabilir.",
    "Resmi tatil ilan edilmemiş olsa da, ruhum tatilde. Yasal olarak zorlanamam.",
    "Bu görevi yerine getirmek, evrensel dengeyi bozacak kadar önemli bir eylem. Risk alamam.",
    "Telefonumun bataryası %1'in altına düştü. Acil şarj operasyonu başlatıldı, diğer her şey ertelendi.",
    "Dün gece gördüğüm rüya bu işi yapmamı yasaklıyor. Rüyalar kutsal kabul edilmeli.",
    "Çalışma masamın üzerindeki toz tabakası henüz arkeolojik kazı aşamasında. Önce onu incelemeliyim.",
]

CIDLEK_GIRISLER = [
    "Sayın yetkili,",
    "Değerli iş arkadaşım,",
    "Saygıdeğer evren yöneticisi,",
    "Çok saygıdeğer zaman yönetimi komisyonu,",
    "Sayın sorumluluk sahibi varlık,",
]

SONUCLAR = [
    "Bu nedenle şu anda herhangi bir üretkenlik gösteremem.",
    "Dolayısıyla bu işi ertelemek, evrensel bir zorunluluktur.",
    "Bu yüzden lütfen anlayışınızı esirgemeyiniz.",
    "Sonuç olarak, bugün tamamen mazeretli kabul edilmeliyim.",
    "Bu şartlar altında çalışmak, insan hakları ihlali sayılabilir.",
]

def yavas_yaz(metin, hiz=0.03):
    """Ciddiyet katmak için yavaş yazdırır."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def mazeret_uret():
    print("\n" + "="*60)
    yavas_yaz("  ABARTILI MAZERET MOTORU v1.0 BAŞLATILIYOR...")
    print("="*60)
    time.sleep(1)
    
    yavas_yaz("\nSistem taranıyor...")
    time.sleep(0.8)
    yavas_yaz("Evren durumu kontrol ediliyor...")
    time.sleep(0.8)
    yavas_yaz("Mazeret veritabanı yükleniyor...")
    time.sleep(1)
    
    print("\n" + "-"*60)
    giris = random.choice(CIDLEK_GIRISLER)
    mazeret = random.choice(MAZERETLER)
    sonuc = random.choice(SONUCLAR)
    
    yavas_yaz(f"\n{giris}")
    time.sleep(0.5)
    yavas_yaz(f"\n{mazeret}")
    time.sleep(0.5)
    yavas_yaz(f"\n{sonuc}")
    print("-"*60)
    
    print("\n[!] Bu mazeret resmi olarak kaydedilmiştir.")
    print("[!] Artık hiçbir şey yapmak zorunda değilsiniz.")
    print("[!] İyi tembellikler dileriz.\n")

if __name__ == "__main__":
    try:
        mazeret_uret()
    except KeyboardInterrupt:
        print("\n\nMazeret üretimi iptal edildi... ama bu da bir mazeret sayılır.")
