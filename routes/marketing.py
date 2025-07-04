from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from models.apartment import Apartment, ClientLead

marketing_bp = Blueprint('marketing', __name__, url_prefix='/marketing')
