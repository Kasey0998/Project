from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app import db
from models.user import User
from models.apartment import Apartment, Flat
from models.apartment import Apartment, Flat, ClientLead # Ensure this is your lead model

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


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