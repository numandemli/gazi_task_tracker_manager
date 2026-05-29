from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models import User
from app import db

class LoginForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[
        DataRequired(message='Kullanıcı adı gereklidir.'),
        Length(min=3, max=64, message='Kullanıcı adı 3 ila 64 karakter arasında olmalıdır.')
    ])
    password = PasswordField('Şifre', validators=[
        DataRequired(message='Şifre gereklidir.')
    ])
    remember_me = BooleanField('Beni Hatırla')
    submit = SubmitField('Giriş Yap')

class RegistrationForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[
        DataRequired(message='Kullanıcı adı gereklidir.'),
        Length(min=3, max=64, message='Kullanıcı adı 3 ila 64 karakter arasında olmalıdır.')
    ])
    email = StringField('E-posta Adresi', validators=[
        DataRequired(message='E-posta adresi gereklidir.'),
        Email(message='Geçerli bir e-posta adresi girin.'),
        Length(max=120, message='E-posta adresi en fazla 120 karakter olabilir.')
    ])
    password = PasswordField('Şifre', validators=[
        DataRequired(message='Şifre gereklidir.'),
        Length(min=6, message='Şifre en az 6 karakter olmalıdır.')
    ])
    password_confirm = PasswordField('Şifre Tekrarı', validators=[
        DataRequired(message='Şifre tekrarı gereklidir.'),
        EqualTo('password', message='Şifreler eşleşmelidir.')
    ])
    submit = SubmitField('Kayıt Ol')

    def validate_username(self, username):
        # SQLAlchemy 2.0 tarzı scalar sorgusu
        user = db.session.scalar(db.select(User).filter_by(username=username.data))
        if user is not None:
            raise ValidationError('Bu kullanıcı adı zaten alınmış. Lütfen başka bir tane seçin.')

    def validate_email(self, email):
        # SQLAlchemy 2.0 tarzı scalar sorgusu
        user = db.session.scalar(db.select(User).filter_by(email=email.data))
        if user is not None:
            raise ValidationError('Bu e-posta adresi zaten kayıtlı. Lütfen başka bir tane seçin.')
