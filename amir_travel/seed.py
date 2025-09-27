"""
Quick seeding script to populate the database with sample data.
Run with: python seed.py
"""
from app import create_app, db
from models import Trip

app = create_app()

with app.app_context():
    if not Trip.query.first():
        trips = [
            Trip(title='باريس الرومانسية', country='فرنسا', trip_type='شهر عسل', duration_days=5, price=899,
                 description='برنامج مثالي للأزواج يشمل جولة في نهر السين وزيارة برج إيفل.',
                 images=''),
            Trip(title='جمال الألب السويسرية', country='سويسرا', trip_type='عائلي', duration_days=7, price=1290,
                 description='طبيعة خلابة وزيارات لعدة مدن مع سائق عربي.',
                 images=''),
            Trip(title='مدن ألمانيا التاريخية', country='ألمانيا', trip_type='مغامرة', duration_days=6, price=990,
                 description='اكتشف التاريخ والحداثة في آن واحد.',
                 images=''),
        ]
        db.session.add_all(trips)

    # Reviews and Blog removed

    db.session.commit()
    print('Trips seeded.')
