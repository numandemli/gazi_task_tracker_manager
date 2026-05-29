import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv

# Eklentileri tanımla
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Lütfen bu sayfaya erişmek için giriş yapın.'
login_manager.login_message_category = 'warning'

def create_app():
    # Çevre değişkenlerini yükle
    load_dotenv()
    
    app = Flask(__name__)
    
    # Yapılandırma ayarları
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'gazi-blg106-varsayilan-anahtar')
    
    # SQLite Veritabanı yapılandırması
    database_url = os.environ.get('DATABASE_URL', 'sqlite:///gazi_tasks.db')
    # PostgreSQL uyumluluğu için düzeltme (gerekirse)
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
        
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Eklentileri uygulama örneği ile ilişkilendir
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    # Blueprint (Modül) kayıtları
    from app.auth import auth as auth_blueprint
    from app.main import main as main_blueprint
    
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    
    # Flask-Login kullanıcı yükleyici (User Loader)
    from app.models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        # SQLAlchemy 2.0 get metodu ile sorgu
        return db.session.get(User, int(user_id))
        
    return app
