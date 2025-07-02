from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app import db
from models.user import User
from models.apartment import Apartment, Flat
from models.apartment import Apartment, Flat, ClientLead # Ensure this is your lead model

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/users', methods=['GET', 'POST'])
@login_required
def manage_users():
    if current_user.role != 'admin':
        return redirect(url_for('dashboard.dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        role = request.form['role']
        password = request.form['password']
        if User.query.filter((User.username == username) | (User.email == email)).first():
            flash('User already exists')
        else:
            new_user = User(username=username, email=email, role=role)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully')

    users = User.query.all()
    return render_template('admin_users.html', users=users)

@admin_bp.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if current_user.role != 'admin':
        return redirect(url_for('dashboard.dashboard'))

    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        user.role = request.form['role']
        db.session.commit()
        flash('User updated successfully')
        return redirect(url_for('admin.manage_users'))

    return render_template('edit_user.html', user=user)

@admin_bp.route('/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if current_user.role != 'admin':
        return redirect(url_for('dashboard.dashboard'))

    user = User.query.get_or_404(user_id)
    if user.role == 'admin' or user.id == current_user.id:
        flash('Cannot delete this user')
        return redirect(url_for('admin.manage_users'))

    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully')
    return redirect(url_for('admin.manage_users'))


@admin_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'admin':
        return redirect(url_for('dashboard.dashboard'))

    total_apartments = Apartment.query.count()
    sold = ClientLead.query.filter_by(status='sold').count()
    pending = ClientLead.query.filter_by(status='pending').count()
    not_interested = ClientLead.query.filter_by(status='not_interested').count()

    return render_template('dashboard.html',
                           total_apartments=total_apartments,
                           sold=sold,
                           pending=pending,
                           not_interested=not_interested)

@admin_bp.route('/dashboard_stats')
@login_required
def dashboard_stats():
    if current_user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    total_apartments = Apartment.query.count()
    sold = ClientLead.query.filter_by(status='sold').count()
    pending = ClientLead.query.filter_by(status='pending').count()
    not_interested = ClientLead.query.filter_by(status='not_interested').count()

    return jsonify({
        'total_apartments': total_apartments,
        'sold': sold,
        'pending': pending,
        'not_interested': not_interested,
    })