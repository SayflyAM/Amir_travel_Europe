from flask import Flask, send_from_directory
from extensions import db, babel
import os
from dotenv import load_dotenv



def create_app():
    # Load environment variables
    load_dotenv()

    app = Flask(__name__, static_folder='static', template_folder='templates')

    # Basic config
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['BABEL_DEFAULT_LOCALE'] = 'ar'

    # Init extensions
    db.init_app(app)
    babel.init_app(app)

    # Register blueprints
    from blueprints.home.views import home_bp
    from blueprints.trips.views import trips_bp
    from blueprints.driver.views import driver_bp
    from blueprints.about.views import about_bp
    from blueprints.contact.views import contact_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(trips_bp, url_prefix='/trips')
    app.register_blueprint(driver_bp, url_prefix='/driver')
    app.register_blueprint(about_bp, url_prefix='/about')
    app.register_blueprint(contact_bp, url_prefix='/contact')
    # Removed blog and reviews features per request

    # Create DB if not exists
    with app.app_context():
        from models import Trip  # noqa: F401
        db.create_all()

    # SEO files
    @app.get('/robots.txt')
    def robots():
        return send_from_directory(app.static_folder, 'robots.txt', mimetype='text/plain')

    @app.get('/sitemap.xml')
    def sitemap():
        return send_from_directory(app.static_folder, 'sitemap.xml', mimetype='application/xml')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
