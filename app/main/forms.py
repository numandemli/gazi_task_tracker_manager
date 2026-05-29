from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    title = StringField('Görev Başlığı', validators=[
        DataRequired(message='Görev başlığı gereklidir.'),
        Length(max=100, message='Görev başlığı en fazla 100 karakter olabilir.')
    ])
    description = TextAreaField('Açıklama', validators=[
        Length(max=500, message='Açıklama en fazla 500 karakter olabilir.')
    ])
    status = SelectField('Durum', choices=[
        ('Todo', 'Yapılacak'),
        ('In Progress', 'Devam Ediyor'),
        ('Done', 'Tamamlandı')
    ], default='Todo')
    priority = SelectField('Öncelik Seviyesi', choices=[
        ('Low', 'Düşük'),
        ('Medium', 'Orta'),
        ('High', 'Yüksek')
    ], default='Medium')
    submit = SubmitField('Kaydet')
