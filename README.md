# ER&BAY SmartLead AI

ER&BAY SmartLead AI, Python ile Ürün Geliştirme eğitimi kapsamında geliştirilen bir Akıllı Satış Asistanı projesidir.

Sistem, ER&BAY internet sitesindeki ziyaretçilerin ürün ve üretim süreçleri hakkında yapay zekâ üzerinden bilgi almasını ve potansiyel müşteri iletişim bilgilerinin kayıt altına alınmasını hedeflemektedir.

## Kullanılan Teknolojiler

- Python
- Flask
- SQLite
- Groq API
- Requests
- python-dotenv
- flask-cors
- Git / GitHub
- Wix Studio (hedef arayüz)

## Mimari Yapı

Proje Separation of Concerns prensibine göre modüler olarak hazırlanmıştır.

- `config.py`: API ve uygulama ayarları
- `app/database.py`: SQLite veritabanı işlemleri
- `app/services/ai_service.py`: Yapay zekâ API iletişimi
- `app/routes.py`: HTTP ve API rotaları
- `app/__init__.py`: Flask uygulama fabrikası
- `run.py`: Uygulamayı başlatan giriş noktası
- `app/templates/`: Arayüz şablonları

## Temel Endpointler

- `GET /health` — Backend çalışma kontrolü
- `POST /api/sohbet` — Yapay zekâ haberleşmesi
- `POST /api/leads` — Müşteri adayı kaydı
- `GET /api/leads` — Müşteri adaylarının listelenmesi

## Testler

Backend lokal ortamda çalıştırılmıştır.

- `/health` testi başarılı
- Yapay zekâ haberleşme testi başarılı
- Hatalı/boş mesaj testi başarılı
- Güvenli JSON hata yanıtı doğrulanmıştır

## Güvenlik

API anahtarları `.env` dosyasında saklanmaktadır. `.env`, sanal ortam ve yerel SQLite veritabanı `.gitignore` ile GitHub deposunun dışında tutulmaktadır.
