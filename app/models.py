from app import db
from flask_login import UserMixin
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, nullable=False, index=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String(256), nullable=False)
    
    # User -> Tasks bire-çok (one-to-many) ilişkisi
    # SQLAlchemy 2.x stili modern ilişki tanımı
    tasks: Mapped[list["Task"]] = relationship(back_populates="author", cascade="all, delete-orphan")
    
    # Şifre güvenliği metotları (werkzeug.security)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    def avatar_url(self, size=150):
        import hashlib
        email_hash = hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()
        return f"https://www.gravatar.com/avatar/{email_hash}?d=identicon&s={size}"
        
    def __repr__(self):
        return f'<User {self.username}>'

class Task(db.Model):
    __tablename__ = 'tasks'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    
    # Görev durumları varsayılan olarak 'Todo' (Ders projesi isterlerine göre)
    status: Mapped[str] = mapped_column(String(20), default="Todo") # Todo, In Progress, Done
    priority: Mapped[str] = mapped_column(String(20), default="Medium") # Low, Medium, High
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    # Kullanıcı ilişkisi (Yabancı Anahtar)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    author: Mapped["User"] = relationship(back_populates="tasks")
    
    def __repr__(self):
        return f'<Task {self.title}>'
