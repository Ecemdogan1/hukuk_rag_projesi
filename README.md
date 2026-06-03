# Hukuki Benzer Karar Bulucu

Bu proje, kullanıcının anlattığı olaya en çok benzeyen kararları bulmak amacıyla hazırlanmıştır.

## Projenin Mantığı

1. Kullanıcı olayını yazar.
2. Metin embedding modeline gönderilir.
3. Metnin sayısal karşılığı oluşturulur.
4. Sistemde kayıtlı kararlar ile benzerlik karşılaştırması yapılır.
5. En yüksek benzerlik skoruna sahip kararlar listelenir.

Bu proje NLP, Embedding, Similarity Search ve RAG mantığını öğrenmek için hazırlanmıştır.

## Kurulum

pip install -r requirements.txt

## Çalıştırma

python main.py
