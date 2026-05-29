from flask import render_template
from app.main import main
from app import db

@main.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_error(error):
    # Veritabanı çökmesi durumunda session rollback yapılır
    db.session.rollback()
    return render_template('500.html'), 500
