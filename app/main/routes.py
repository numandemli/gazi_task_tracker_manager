from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required
from app import db
from app.main import main
from app.main.forms import TaskForm
from app.models import Task
from datetime import datetime, date, time

@main.route('/')
@login_required
def index():
    # Sayfa numarasını, durum filtresini, arama kelimesini ve bugün filtresini urlden yakala
    page = request.args.get('page', 1, type=int)
    status_filter = request.args.get('status')
    search_query = request.args.get('q', '').strip()
    today_filter = request.args.get('today') == 'true'
    
    # SQLAlchemy 2.x standardına uygun temel sorgu
    query = db.select(Task).where(Task.user_id == current_user.id)
    
    # 1. Durum Filtresi
    if status_filter in ['Todo', 'In Progress', 'Done']:
        query = query.where(Task.status == status_filter)
        
    # 2. Arama Filtresi (Case-insensitive SQL ILIKE)
    if search_query:
        query = query.where(Task.title.ilike(f"%{search_query}%"))
        
    # 3. Bugün Görünümü Filtresi
    if today_filter:
        today_start = datetime.combine(date.today(), time.min)
        today_end = datetime.combine(date.today(), time.max)
        query = query.where(Task.created_at.between(today_start, today_end))
        
    # Sayfa başına 10 görev olacak şekilde paginator çalıştırılması (en yeni en üstte)
    pagination = db.paginate(
        query.order_by(Task.created_at.desc()), 
        page=page, 
        per_page=10, 
        error_out=False
    )
    tasks = pagination.items
    
    return render_template(
        'index.html', 
        tasks=tasks, 
        pagination=pagination, 
        current_status=status_filter,
        search_query=search_query,
        today_filter=today_filter
    )

@main.route('/task/new', methods=['GET', 'POST'])
@login_required
def task_create():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            status=form.status.data,
            priority=form.priority.data, # Öncelik eklendi
            user_id=current_user.id
        )
        db.session.add(task)
        db.session.commit()
        flash('Görev başarıyla oluşturuldu.', 'success')
        return redirect(url_for('main.index'))
        
    return render_template('task_form.html', title='Yeni Görev', form=form)

@main.route('/task/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def task_update(id):
    # Görevi veri tabanından çek
    task = db.session.get(Task, id)
    
    # 404 Hata Yönetimi: Görev hiç yoksa
    if task is None:
        abort(404)
        
    # 403 Hata Yönetimi: Görev var fakat aktif kullanıcıya ait değilse (Yetkisiz Erişim)
    if task.user_id != current_user.id:
        abort(403)
        
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.status = form.status.data
        task.priority = form.priority.data # Öncelik eklendi
        db.session.commit()
        flash('Görev başarıyla güncellendi.', 'success')
        return redirect(url_for('main.index'))
        
    return render_template('task_form.html', title='Görevi Düzenle', form=form, task=task)

@main.route('/task/<int:id>/delete', methods=['POST'])
@login_required
def task_delete(id):
    task = db.session.get(Task, id)
    
    # 404 Hata Yönetimi: Görev hiç yoksa
    if task is None:
        abort(404)
        
    # 403 Hata Yönetimi: Görev var fakat aktif kullanıcıya ait değilse (Yetkisiz Erişim)
    if task.user_id != current_user.id:
        abort(403)
        
    db.session.delete(task)
    db.session.commit()
    flash('Görev silindi.', 'success')
    return redirect(url_for('main.index'))

@main.route('/task/<int:id>/quick-status/<string:new_status>')
@login_required
def task_quick_status(id, new_status):
    task = db.session.get(Task, id)
    
    # 404 Hata Yönetimi: Görev hiç yoksa
    if task is None:
        abort(404)
        
    # 403 Hata Yönetimi: Görev var fakat aktif kullanıcıya ait değilse (Yetkisiz Erişim)
    if task.user_id != current_user.id:
        abort(403)
        
    if new_status in ['Todo', 'In Progress', 'Done']:
        task.status = new_status
        db.session.commit()
        flash('Görev durumu güncellendi.', 'success')
        
    return redirect(url_for('main.index'))

@main.route('/profile')
@login_required
def profile():
    # Toplam görev ve tamamlanan görev sayısını al (SQL COUNT)
    total_count = db.session.scalar(
        db.select(db.func.count(Task.id)).where(Task.user_id == current_user.id)
    )
    completed_count = db.session.scalar(
        db.select(db.func.count(Task.id))
        .where(Task.user_id == current_user.id)
        .where(Task.status == 'Done')
    )
    
    # Sıfıra bölünme (ZeroDivisionError) korumalı başarı yüzdesi hesabı
    if total_count > 0:
        success_percentage = int((completed_count / total_count) * 100)
    else:
        success_percentage = 0
        
    return render_template(
        'profile.html',
        title='Profilim',
        total_count=total_count,
        completed_count=completed_count,
        success_percentage=success_percentage
    )
