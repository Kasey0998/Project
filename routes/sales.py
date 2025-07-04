from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from models.apartment import ClientLead, Flat

sales_bp = Blueprint('sales', __name__, url_prefix='/sales')

@sales_bp.route('/mark_sold/<int:lead_id>', methods=['POST'])
@login_required
def mark_sold(lead_id):
    if current_user.role != 'sales':
        return redirect(url_for('dashboard.dashboard'))

    lead = ClientLead.query.get_or_404(lead_id)
    if lead.status != 'pending':
        flash("Lead is already processed.")
        return redirect(url_for('dashboard.dashboard'))

    # Mark a flat in the apartment as sold
    flat = Flat.query.filter_by(apartment_id=lead.interested_apartment_id, status='available').first()
    if flat:
        flat.status = 'sold'
        lead.status = 'sold'
        db.session.commit()
        flash("Lead marked as sold.")
    else:
        flash("No available flats in this apartment.")
    return redirect(url_for('dashboard.dashboard'))

@sales_bp.route('/mark_not_interested/<int:lead_id>', methods=['POST'])
@login_required
def mark_not_interested(lead_id):
    if current_user.role != 'sales':
        return redirect(url_for('dashboard.dashboard'))

    lead = ClientLead.query.get_or_404(lead_id)
    if lead.status != 'pending':
        flash("Lead is already processed.")
        return redirect(url_for('dashboard.dashboard'))

    lead.status = 'not_interested'
    db.session.commit()
    flash("Lead marked as not interested.")
    return redirect(url_for('dashboard.dashboard'))