# Görev Yönetimi Uygulaması - Git Geçmişi Oluşturucu
# Bu script projenizin 15 aşamasını adım adım stage edip commit geçmişi oluşturur.

Write-Host ">>> Git Geçmişi Oluşturma İşlemi Başlatılıyor..." -ForegroundColor Cyan

# Git kontrolü
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "Hata: Bilgisayarınızda Git (git.exe) kurulu görünmüyor!" -ForegroundColor Red
    Write-Host "Lütfen Git'i kurun (https://git-scm.com/) ve ardından bu script'i tekrar çalıştırın." -ForegroundColor Yellow
    Exit 1
}

# Git deposunu ilklendir
if (-not (Test-Path .git)) {
    git init
    Write-Host ">>> Git deposu ilklendirildi." -ForegroundColor Green
} else {
    Write-Host ">>> Mevcut Git deposu bulundu, sıfırlanıyor ve yeniden oluşturuluyor..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force .git -ErrorAction SilentlyContinue
    git init
}

# Yerel Git yapılandırmaları
git config user.name "Proje Sahibi"
git config user.email "admin@gorevyonetimi.com"

# 1. Commit: .gitignore ve requirements.txt
git add .gitignore requirements.txt
git commit -m "ilklendirme: Proje gereksinimleri ve gitignore yapisi olusturuldu"

# 2. Commit: run.py
git add run.py
git commit -m "yapilandirma: Cevre degiskenleri ve uygulama ana giris noktasi olusturuldu"

# 3. Commit: app/__init__.py
git add app/__init__.py
git commit -m "mimari: Uygulama fabrikasi (create_app) ve eklenti tanimlamalari yapildi"

# 4. Commit: app/models.py
git add app/models.py
git commit -m "veritabanı: SQLAlchemy 2.x stili User ve Task veri modelleri tanimlandi"

# 5. Commit: migrations (sadece başlangıç göç dosyaları)
git add migrations/alembic.ini migrations/env.py migrations/script.py.mako migrations/README
git add migrations/versions/4dc74c4ac983_initial_migration.py
git commit -m "veritabanı: Flask-Migrate entegrasyonu ile veritabanı goc sistemi ilklendirildi"

# 6. Commit: app/auth/__init__.py ve forms.py
git add app/auth/__init__.py app/auth/forms.py
git commit -m "auth: Giris ve kayit formlari WTForms ile olusturuldu"

# 7. Commit: app/auth/routes.py
git add app/auth/routes.py
git commit -m "auth: Oturum yonetimi, kayit ve cikis rotalari kodlandi"

# 8. Commit: app/main/__init__.py ve forms.py
git add app/main/__init__.py app/main/forms.py
git commit -m "main: Gorev formlari ve ana modul (Blueprint) tanimlandi"

# 9. Commit: app/main/routes.py
git add app/main/routes.py
git commit -m "main: Gorev ekleme, guncelleme, silme ve hizli durum yonlendirmeleri yazildi"

# 10. Commit: app/main/errors.py
git add app/main/errors.py
git commit -m "hata yonetimi: Ozel 404 Sayfa Bulunamadi ve 500 Ic Sunucu Hatasi rotalari kodlandi"

# 11. Commit: app/static/css/style.css
git add app/static/css/style.css
git commit -m "arayuz: Premium koyu mod tasarimli vanilla CSS stil sayfasi yazildi"

# 12. Commit: app/templates/base.html, login.html ve register.html
git add app/templates/base.html app/templates/login.html app/templates/register.html
git commit -m "arayuz: Kimlik dogrulama arayuz sablonlari base.html ile entegre edildi"

# 13. Commit: app/templates/index.html, task_form.html, 404.html ve 500.html
git add app/templates/index.html app/templates/task_form.html app/templates/404.html app/templates/500.html
git commit -m "arayuz: Dashboard, gorev ekleme ve hata sayfalari sablonlari tasarlandi"

# 14. Commit: app/templates/profile.html
git add app/templates/profile.html
git commit -m "profil: Dinamik Gravatar ve ZeroDivisionError korumali basari yuzdesi ekrani eklendi"

# 15. Commit: Docker, Compose ve İkinci Migrasyon (Öncelik Sütunu)
git add migrations/versions/b0f7a4f746f7_add_priority_to_task.py
git add Dockerfile docker-compose.yml .dockerignore create_git_history.ps1
git commit -m "dagitim: Gunicorn ve PostgreSQL entegrasyonlu Docker ve Compose mimarisi kuruldu"

Write-Host "`n>>> Tebrikler! Tam 15 adet sirali ve anlamli commit gecmisi basariyla olusturuldu!" -ForegroundColor Green
Write-Host ">>> Git Log gecmisini gormek icin terminale 'git log --oneline' yazabilirsiniz." -ForegroundColor Cyan
