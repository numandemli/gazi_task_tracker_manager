# BLG106 Proje Teknik Raporu

**Proje Adı:** Minimalist Görev Yönetimi Sistemi  
**Geliştirici:** Numan Demli  
**Teknoloji Yığını:** Flask 3.0, SQLAlchemy 2.0, PostgreSQL, Docker  

## 1. Mimari Tasarım
Uygulama, Flask'ın "Application Factory" deseni kullanılarak modüler bir yapıda (Blueprints) inşa edilmiştir. Bu sayede kimlik doğrulama (auth) ve ana uygulama (main) mantıkları birbirinden ayrılmıştır.

## 2. Veritabanı Modeli
SQLAlchemy 2.0'ın modern `Mapped` ve `mapped_column` sözdizimi kullanılarak `User` ve `Task` modelleri oluşturulmuştur. Görevler; başlık, açıklama, durum, öncelik ve son tarih gibi meta verilerle zenginleştirilmiştir.

## 3. Güvenlik Uygulamaları
* **Bcrypt Hashing:** Kullanıcı şifreleri veritabanında asla açık metin olarak tutulmamış, tek yönlü hashleme uygulanmıştır.
* **CSRF Protection:** Flask-WTF ile tüm formlar arası sahte istek saldırılarına karşı korunmuştur.
* **Authorization:** Kullanıcıların sadece kendi oluşturdukları görevlere erişebilmesi için backend seviyesinde mülkiyet doğrulaması yapılmaktadır.

## 4. Gelişmiş Özellikler
Uygulama; dinamik arama motoru, tarih bazlı filtreleme ve kullanıcı performansını ölçen istatistik paneli gibi standart üstü özellikler içermektedir.

## 5. Dağıtım ve Konteynerleştirme
Sistem, Docker Compose orkestrasyonu ile yapılandırılmıştır. Web servisi Gunicorn (WSGI) ile çalışırken, veri depolama için PostgreSQL alpine imajı kullanılmaktadır.