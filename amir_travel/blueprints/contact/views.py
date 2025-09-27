from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

contact_bp = Blueprint('contact', __name__)


class ContactForm(FlaskForm):
    name = StringField('الاسم', validators=[DataRequired(), Length(max=100)])
    email = StringField('البريد الإلكتروني', validators=[DataRequired(), Email()])
    message = TextAreaField('الرسالة', validators=[DataRequired(), Length(max=1000)])


@contact_bp.route('/', methods=['GET', 'POST'])
def page():
    form = ContactForm()
    whatsapp = '+971565598682'
    if form.validate_on_submit():
        # Here you would send an email or store the message
        flash('تم استلام رسالتك وسنقوم بالتواصل معك قريباً.', 'success')
        return redirect(url_for('contact.page'))
    return render_template('contact.html', form=form, whatsapp=whatsapp)
