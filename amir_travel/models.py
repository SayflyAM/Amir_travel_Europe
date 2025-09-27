from datetime import datetime
from extensions import db


class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    trip_type = db.Column(db.String(80), nullable=False)  # عائلي، مغامرة، شهر عسل
    duration_days = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    images = db.Column(db.Text, default='')  # روابط الصور مفصولة بفواصل


"""
Only Trip model remains after removing Reviews and Blog features.
"""
