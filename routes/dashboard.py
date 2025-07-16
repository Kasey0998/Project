from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from models.apartment import Apartment, Flat, ClientLead

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    role = current_user.role

    if role == 'admin':
        apartments = Apartment.query.all()
        total_sold = Flat.query.filter_by(status='sold').count()
        pending = ClientLead.query.filter_by(status='pending').count()
        not_interested = ClientLead.query.filter_by(status='not_interested').count()
        return render_template('admin.html', apartments=apartments,
                               total_sold=total_sold,
                               pending=pending,
                               not_interested=not_interested)

    elif role == 'marketing':
        leads = ClientLead.query.filter_by(status='pending').all()
        apartments = Apartment.query.all()
        return render_template('marketing.html', leads=leads, apartments=apartments)

    elif role == 'sales':
        leads = ClientLead.query.filter_by(status='pending').all()
        return render_template('sales.html', leads=leads)

    return redirect(url_for('auth.login'))