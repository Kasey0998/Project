from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from models.apartment import Apartment, ClientLead

marketing_bp = Blueprint('marketing', __name__, url_prefix='/marketing')

@marketing_bp.route('/add_lead', methods=['POST'])
@login_required
def add_lead():
    if current_user.role != 'marketing':
        return redirect(url_for('dashboard.dashboard'))

    name = request.form['name']
    contact = request.form['contact']
    email = request.form['email']
    apartment_id = request.form['apartment_id']

    existing = ClientLead.query.filter((ClientLead.contact == contact) | (ClientLead.email == email)).first()
    if existing:
        flash("Client already exists.")
        return redirect(url_for('dashboard.dashboard'))

    new_lead = ClientLead(
        name=name,
        contact=contact,
        email=email,
        interested_apartment_id=apartment_id,
        status='pending',
        created_by=current_user.id
    )
    db.session.add(new_lead)
    db.session.commit()
    flash("Lead added.")
    return redirect(url_for('dashboard.dashboard'))