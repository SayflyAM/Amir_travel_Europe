from flask import Blueprint, render_template, request
from models import Trip

trips_bp = Blueprint('trips', __name__)


@trips_bp.route('/')
def list_trips():
    # Filters: country, type, duration
    country = request.args.get('country')
    trip_type = request.args.get('type')
    duration = request.args.get('duration', type=int)

    query = Trip.query
    if country:
        query = query.filter_by(country=country)
    if trip_type:
        query = query.filter_by(trip_type=trip_type)
    if duration:
        query = query.filter(Trip.duration_days >= duration)

    trips = query.all()
    countries = [c[0] for c in Trip.query.with_entities(Trip.country).distinct().all()]
    types = [t[0] for t in Trip.query.with_entities(Trip.trip_type).distinct().all()]

    return render_template('trips/list.html', trips=trips, countries=countries, types=types)


@trips_bp.route('/<int:trip_id>')
def trip_detail(trip_id):
    trip = Trip.query.get_or_404(trip_id)
    images = [img for img in trip.images.split(',') if img]
    return render_template('trips/detail.html', trip=trip, images=images)
