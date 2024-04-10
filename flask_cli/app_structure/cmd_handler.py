import os
from flask_cli.app_template.html import BASE_HTML, DEMO_HTML


APP_SETTINGS = """
import os
import secrets # Secure secret key generation
from flask_migrate import Migrate
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, redirect


# Create a Flask application instance
app = Flask(__name__)


# SECURITY WARNING: keep the secret key used in production secret!
# Use a secure environment variable to store the secret key.
# You can use the 'secrets' module (available in Python 3.6+) to generate a secret key:
SECRET_KEY = 'flask-insecure-c#y(k55srf&7q^i@mi+f*tw_%ll$^w@#cd1=fwa6&8tr^2qwv1'
secret_key = secrets.token_urlsafe(20) # Generate a secure secret key


APP_DATABASE = os.path.join(os.path.dirname(__file__), "database")
DATABASE_PATH = os.path.join(APP_DATABASE, "Database.db")


#App configurations
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Create database and CSRF protection instances
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
migrate = Migrate(app, db) # Database migration with Flask-Migrate


# Session configuration settings
app.config['SESSION_TYPE'] = 'sqlalchemy'  # Use SQLAlchemy backend
app.config['SESSION_SQLALCHEMY'] = db  # Reference SQLAlchemy instance
app.config['SESSION_SQLALCHEMY_TABLE'] = "flask_sessions"  # Use the Session model
app.config['SESSION_PERMANENT'] = False  # Set to True for persistent sessions
app.config['SESSION_USE_SIGNER'] = True  # Use a secret key for signing

Session(app)  # Initialize Flask-Session extension


@app.before_request
def app_middleware():
    #This middleware function performs several actions before each request:

    # URL Canonicalization: Redirects URLs with uppercase letters to lowercase for consistent URL handling.
    # Trailing Slash Removal: Removes trailing slashes from URLs except for the root URL, promoting cleaner URLs.
    # Security Headers: Sets essential security headers to mitigate potential vulnerabilities:
        # Referrer-Policy: Limits referrer information leaks.
        # X-Content-Type-Options: Prevents MIME-sniffing.
        # Content-Security-Policy (Basic implementation): Provides a starting point for restricting resource loading.
    
    # URL Canonicalization: Redirect URLs with uppercase letters to lowercase
    if request.path != request.path.lower():
        return redirect(request.path.lower())

    # Remove trailing slashes except for root URL
    if request.path != '/' and request.path.endswith('/'):
        return redirect(request.path.rstrip('/'))


@app.after_request
def app_security_headers(response):
    #This middleware function sets the X-Frame-Options header to "DENY" to prevent clickjacking attacks.
    
    # Set Referrer-Policy header
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

    # Set X-Content-Type-Options header
    response.headers["X-Content-Type-Options"] = "nosniff"
    
     # Set Content-Security-Policy header
    response.headers["Content-Security-Policy"] = "default-src 'self'"

    # Set Content-Security-Policy header
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self' https://cdn.example.com https://cdnjs.cloudflare.com; "
        "style-src 'self' https://cdn.example.com; "
        "font-src 'self' https://fonts.gstatic.com; "
        "img-src 'self' https://cdn.example.com data;"
    )

    # Set X-Frame-Options header
    response.headers["X-Frame-Options"] = "DENY"

    return response
    
    
from my_demo_app.views.routes import view

        
app.register_blueprint(view, url_prefix="/")
"""


APP_SESSION = \
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Session(db.Model):
    __tablename__ = 'sessions'  # Customize table name if desired

    session_id = db.Column(db.String(255), primary_key=True)
    session_data = db.Column(db.Text)  # Store session data as serialized JSON
    expiration_time = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return f'<Session {self.session_id}>'
        
"""



APP_STARTUP = """
from my_demo_app import db, app


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        db.drop_all()    
    app.run(debug=True, port=5000)
"""


APP_TEMPLATE = """
import secrets
from flask import render_template, Blueprint


view = Blueprint("view", __name__, template_folder="templates", static_url_path="static")


@view.route("/")
def demo_page():
    return render_template("index.html")
"""


APP_STRUCTURE = {
    "templates": {
        "base.html": BASE_HTML, 
        "index.html": DEMO_HTML
        },
    
    "views": {
        "routes.py": APP_TEMPLATE, 
        "__init__.py": ""
        },
    
    "errors": {
        "handlers.py": "",
        "__init__.py": "",
    },
    
    "static": {
        "css": "style.css", 
        "js": "script.js", 
        "images": "flask_cli.png",
        },
    
    "database": {
        "models.py": "", 
        "__init__.py": ""
        },
}


class CmdHandler():

    def init():
        print("Please wait app is setting up virtual environment......")
        os.system("pip install virtualenv && virtualenv env")
        print("Please wait installing, Flask, Flask-SQLAlchemy and Flask-Migrate ")
        os.system("pip install Flask Flask-SQLAlchemy Flask-Migrate")

    def create_flask_app_structure(app_folder_name):
        os.mkdir(app_folder_name)
        with open("app.py", "w") as file:
            file.write(APP_STARTUP)

        with open(f"{app_folder_name}/__init__.py", mode="w") as file:
            file.write(APP_SETTINGS)

        for dir, content in APP_STRUCTURE.items():
            os.mkdir(f"{app_folder_name}/{dir}")

            if dir in ("static"):
                for static_dir, value in content.items():
                    os.makedirs(f"{app_folder_name}/{dir}/{static_dir}")
                    with open(
                        f"{app_folder_name}/{dir}/{static_dir}/{value}", mode="w"
                    ) as file:
                        file.write("")

            if dir in ["templates", "views", "errors", "database"]:
                for temp, value in content.items():
                    with open(f"{app_folder_name}/{dir}/{temp}", mode="w") as file:
                        file.write(value)
