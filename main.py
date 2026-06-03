"""
HUKUKİ BENZER KARAR BULUCU

Bu dosya uygulamanın başlangıç noktasıdır.

Amaç:
Kullanıcının anlattığı olaya en çok benzeyen kararları bulmak.

Buradaki yapı gerçek hukuk yapay zekâlarında kullanılan
retrieval mantığının sadeleştirilmiş bir örneğidir.
"""

from sentence_transformers import SentenceTransformer
import numpy as np


def kararlari_yukle():
    """
    Kararları metin dosyasından okur.

    Her satır bir karar kabul edilir.
    """
    with open("veri/kararlar.txt", "r", encoding="utf-8") as dosya:
        return [satir.strip() for satir in dosya.readlines() if satir.strip()]


def embedding_modelini_yukle():
    """
    Embedding modeli metinleri sayısal vektörlere dönüştürür.

    Böylece anlam benzerliği hesaplayabiliriz.
    """
    model_adi = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    return SentenceTransformer(model_adi)


def benzerlik_hesapla(sorgu_vektoru, karar_vektorleri):
    """
    Sorgu ile kararlar arasındaki benzerlik skorlarını hesaplar.
    """
    return np.dot(karar_vektorleri, sorgu_vektoru)


def main():

    print("\nHukuki Benzer Karar Bulucu\n")

    kararlar = kararlari_yukle()

    print("Embedding modeli yükleniyor...")
    model = embedding_modelini_yukle()

    # Kararları vektörlere dönüştürüyoruz.
    karar_vektorleri = model.encode(kararlar)

    olay = input("\nOlayı giriniz: ")

    # Kullanıcının anlattığı olayı da vektöre dönüştürüyoruz.
    sorgu_vektoru = model.encode([olay])[0]

    skorlar = benzerlik_hesapla(sorgu_vektoru, karar_vektorleri)

    # En yüksek benzerlik skoruna sahip kararın indeksini buluyoruz.
    en_iyi_indeks = int(np.argmax(skorlar))

    print("\nEn benzer karar:")
    print(kararlar[en_iyi_indeks])


if __name__ == "__main__":
    main()
