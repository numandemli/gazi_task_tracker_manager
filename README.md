# Gazi Task Tracker Manager

Gazi Üniversitesi BLG106 dersi kapsamında geliştirilmiş, modern ve minimalist bir **Görev Yönetimi Uygulaması**dır. Uygulama, "Vibe Coding" disipliniyle, yapay zeka yardımlı geliştirme süreçleri ve modern web standartları (Flask 3.x, SQLAlchemy 2.0) kullanılarak inşa edilmiştir.

## 🚀 Öne Çıkan Özellikler
* **Modern Kimlik Doğrulama:** Flask-Login ile güvenli oturum yönetimi ve şifre hashleme.
* **Gelişmiş Görev Yönetimi:** Görev oluşturma, düzenleme, silme ve durum (Todo, In Progress, Done) takibi.
* **Öncelik Seviyeleri:** Düşük, Orta ve Yüksek öncelik etiketleri ile görsel ayrım.
* **Akıllı Filtreleme:** Başlık bazlı arama ve "Bugün" filtresi ile hızlı erişim.
* **Kullanıcı Profili:** Gravatar entegrasyonu ve tamamlanma istatistikleri.
* **Docker Desteği:** PostgreSQL ve Gunicorn ile üretim (production) ortamına hazır mimari.

## 🛠️ Kurulum ve Çalıştırma

### Docker ile (Önerilen)
1. Docker Desktop'ı başlatın.
2. Proje dizininde şu komutu çalıştırın:
   ```bash
   docker-compose up --build