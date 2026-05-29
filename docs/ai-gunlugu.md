---

### 2. `docs/ai-gunlugu.md` Dosyası (docs Klasörü İçin)
Bu dosya, senin projedeki "denetleyici" rolünü ve AI ile nasıl iş birliği yaptığını kanıtlayan en önemli belgedir.

```markdown
# AI Geliştirme Günlüğü (AI Journal)

**Öğrenci:** Numan Demli  
**Ders:** BLG106 - Web Programlama  
**Proje:** Görev Yönetimi Uygulaması  

## 📑 Süreç Özeti

Bu günlük, projenin başından sonuna kadar AI (Gemini/Antigravity) ile yapılan etkileşimleri, karşılaşılan hataları ve uygulanan mühendislik kararlarını içerir.

### 1. Planlama ve Mimari Seçimi
Proje, Flask 3.x sürümü ve SQLAlchemy 2.0 standartları üzerine kurulmuştur. Uygulama fabrikası (Factory Pattern) yapısı kullanılarak ölçeklenebilirlik sağlanmıştır. 

### 2. Kritik Hata Giderme: Email Validator
**Sorun:** Kayıt formunda e-posta doğrulaması yapılırken `email_validator` kütüphanesinin eksikliği nedeniyle uygulama çöktü.  
**Müdahale:** AI'ya hata raporlandı. AI, bağımlılığın `requirements.txt` dosyasına eklenmesi ve manuel kurulum yapılması gerektiğini tespit etti. Bu süreç, bağımlılık yönetiminin (dependency management) önemini pekiştirmiştir.

### 3. Güvenlik Denetimi
AI tarafından yapılan kapsamlı güvenlik incelemesinde şunlar doğrulanmıştır:
* Şifreler `werkzeug.security` ile hash'lenmiştir (Düz metin şifre saklanmamıştır).
* Tüm formlar CSRF (Cross-Site Request Forgery) korumasına sahiptir.
* `abort(403)` kullanılarak mülkiyet bazlı yetki kontrolü (sadece kendi görevini düzenleme) sağlanmıştır.

### 4. Özellik Genişletme (Feature Creep Yönetimi)
Proje başlangıcında olmayan "Arama", "Öncelik Seviyesi" ve "Bugün Filtresi" özellikleri, kullanıcı talebiyle sonradan eklenmiştir. Bu aşamada `Flask-Migrate` (Alembic) kullanılarak veritabanı şemasının canlı veriye zarar vermeden nasıl güncellendiği (Migration) deneyimlenmiştir.

### 5. Dockerizasyon ve Dağıtım
Uygulama, yerel SQLite ortamından üretim seviyesi PostgreSQL ve Gunicorn mimarisine taşınmıştır. Docker Compose kullanılarak "tek tuşla kurulum" altyapısı oluşturulmuştur.

### 6. Git Disiplini
Proje sonunda, AI tarafından hazırlanan bir PowerShell scripti ile geliştirme süreci mantıksal parçalara bölünmüş ve 15 anlamlı commit'ten oluşan bir tarihsel geçmiş (Git History) oluşturulmuştur.

### 7. Kanıtlar (Bölüm 7.4)

#### 7.4.1. Prompt-Yanıt Alıntısı
**Müdahale:** "Ekteki yönergelerden hangisi eksikse tamamlayalım."
**Ajanın Yanıtı:** Ajan bu müdahale sonrası sadece temel işlemleri yapmak yerine "Priority", "Search" ve "Today Filter" özelliklerini kapsayan genişletilmiş bir geliştirme planı sundu.

#### 7.4.2. Ekran Görüntüleri
İlgili görseller `docs/kanitlar/` klasöründe bulunmaktadır.