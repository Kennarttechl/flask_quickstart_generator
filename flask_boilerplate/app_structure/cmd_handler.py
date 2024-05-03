import os
from flask_boilerplate.app_template.css import DEMO_CSS
from flask_boilerplate.app_template.html import (
    DEMO_HTML,
    BASE_HTML, 
    FLASH_MESSAGE,
    DEMO_HTML_TEMPLATES
)


APP_SETTINGS = \
"""
import os
import secrets
from flask_babel import Babel
from flask_caching import Cache
from flask_limiter import Limiter
from flask_migrate import Migrate
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, redirect
from flask_assets import Environment, Bundle
from flask_limiter.util import get_remote_address


# Create a Flask application instance
app = Flask(__name__)


# SECURITY WARNING: keep the secret key used in production secret!
# Use a secure environment variable to store the secret key.
# You can use the 'secrets' module (available in Python 3.6+) to generate a secret key:
SECRET_KEY = "flask-insecure-c#y(k55srf&7q^i@mi+f*tw_%ll$^w@#cd1=fwa6&8tr^2qwv1"
secret_key = secrets.token_urlsafe(20)  # Generate a secure secret key


# Define the database path relative to the application directory
APP_DATABASE = os.path.join(os.path.dirname(__file__), "database")
DATABASE_PATH = os.path.join(APP_DATABASE, "Database.db")  # Database name can be change


#Flask-Limiter adds rate limiting to Flask applications (e.g limiting the number of request a client can send).
limiter = Limiter(
    app=app,
    headers_enabled=True,
    storage_uri="memory://",
    key_func=get_remote_address,
    default_limits=["3000 per hour"],
)


# Configure Flask application settings
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["BABEL_DEFAULT_LOCALE"] = "en_US"
app.config["BABEL_DEFAULT_TIMEZONE"] = "UTC"


# Configure Flask-Caching
app.config["CACHE_TYPE"] = "simple"  # You can use 'simple', 'redis', 'memcached'
app.config["CACHE_DEFAULT_TIMEOUT"] = (
    300  # Cache timeout in seconds (e.g., 300 seconds = 5 minutes)
)


# Initialize database, babel, cache, CSRF protection, and migration management instances
babel = Babel(app)
cache = Cache(app)
cache.init_app(app)
db = SQLAlchemy(app)
csrf = CSRFProtect(app)  # Protect against Cross-Site Request Forgery (CSRF) attacks
migrate = Migrate(app, db)  # Database migration with Flask-Migrate


# Configure Flask-Session for database-backed sessions
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_TYPE"] = "sqlalchemy"  # Use SQLAlchemy backend
app.config["SESSION_SQLALCHEMY"] = db  # Reference SQLAlchemy instance
app.config["SESSION_SQLALCHEMY_TABLE"] = "flask_sessions"  # Use the Session model
app.config["SESSION_PERMANENT"] = False  # Set to True for persistent sessions
app.config["SESSION_USE_SIGNER"] = True  # Use a secret key for signing

Session(app)  # Initialize Flask-Session extension


# Flask_Asset for minifying js & css code for faster page loading
assets = Environment(app)


# Creating an instance of the Bundle
js = Bundle(
    # filters="",
    # output="",
)


bootjs = Bundle(
    # filters="jsmin",
    # output="gen/packed.js",
)


css = Bundle(
    "css/base_main.css",
    filters="cssmin",
    output="gen/packed.css",
)


# Flask asset registration
assets.register("main_js", js)
assets.register("base_main_", css)
assets.register("bootstrap_js", bootjs)


@app.before_request
def app_middleware():
    # This middleware function performs several actions before each request:

    # URL Canonicalization: Redirects URLs with uppercase letters to lowercase for consistent URL handling.

    # Trailing Slash Removal: Removes trailing slashes from URLs except for the root URL, promoting cleaner URLs.

    # URL Canonicalization: Redirect URLs with uppercase letters to lowercase
    if request.path != request.path.lower():
        return redirect(request.path.lower())

    # Remove trailing slashes except for root URL
    if request.path != "/" and request.path.endswith("/"):
        return redirect(request.path.rstrip("/"))


@app.after_request
def app_security_headers_middleware(response):
    #This middleware function sets the X-Frame-Options header to "DENY" to prevent clickjacking attacks.
    
    # Security Headers: Sets essential security headers to mitigate potential vulnerabilities:
    
    # Referrer-Policy: Limits referrer information leaks.
    
    # X-Content-Type-Options: Prevents MIME-sniffing.
    
    # Content-Security-Policy (Basic implementation): Provides a starting point for restricting resource loading.
    
    '''Content-Security-Policy (CSP) Header
    The Content-Security-Policy (CSP) header is a security feature that helps prevent various types of attacks, such as Cross-Site Scripting (XSS) and data injection attacks. It allows web developers to control which resources (e.g., scripts, stylesheets, fonts, images) the browser is allowed to load for a specific web page.'''
    
    # X-Frame-Options: # Prevent clickjacking
    
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin" 
    # You can set response.headers to "no-referrer" to prevent any information leaking from your site.

    response.headers["X-Content-Type-Options"] = "nosniff"

    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self' https://cdn.example.com https://cdnjs.cloudflare.com; "
        "style-src 'self' https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css; "
        "font-src 'self' https://fonts.gstatic.com; "
        "img-src 'self' https://cdn.example.com data;"
        
        #Example of adding 1 or more links to => "style-src 'self' https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css https://example.com/other.css static/css/;" 
    )

    response.headers["X-Frame-Options"] = "DENY" # Prevent clickjacking
    
    # When executed the code below in a browser's console, it attempts to create an iframe pointing to http://127.0.0.1:5000/. However, because you've set the X-Frame-Options header to DENY, the browser will refuse to load your web page within an iframe, regardless of where it's hosted.
    
    ''' var iframe = document.createElement('iframe');
    iframe.src = 'http://127.0.0.1:5000/';
    document.body.appendChild(iframe); '''

    return response
    
    
    
# Import and register blueprint containing application routes
from my_demo_app.views.routes import view
from my_demo_app.search.routes import search_
from my_demo_app.errors.routes import errors_
from my_demo_app.admin.routes import admin_controller
from my_demo_app.authentication.routes import authent_
from my_demo_app.password_reset.routes import reset_pswd


app.register_blueprint(view, url_prefix="/")
app.register_blueprint(search_, url_prefix="/")
app.register_blueprint(errors_, url_prefix="/")
app.register_blueprint(authent_, url_prefix="/")
app.register_blueprint(reset_pswd, url_prefix="/")
app.register_blueprint(admin_controller, url_prefix="/")
"""


APP_SESSION = \
"""
from my_demo_app import db





class Session(db.Model):
    __tablename__ = 'sessions'  # Customize table name if desired

    session_id = db.Column(db.String(255), primary_key=True, unique=True)
    session_data = db.Column(db.Text)  # Store session data as serialized JSON
    expiration_time = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return f"Session('{self.session_id}')"
"""


APP_STARTUP = \
"""
from my_demo_app import db, app



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # db.drop_all()    
    app.run(debug=True, port=5000)
"""


VIEW_TEMPLATE_CODE = \
"""
from flask import render_template, Blueprint




view = Blueprint("view", __name__, template_folder="templates", 
static_folder="static")


@view.route("/")
def home_page():
    return render_template("index.html")
"""


SEARCH_TEMPLATE_CODE = \
"""
from my_demo_app import limiter
from flask import render_template, Blueprint



search_ = Blueprint("search_", __name__, template_folder="templates", 
static_folder="static")


@search_.route("/")
@limiter.limit("4 per minute")
def search_item():
    return render_template("item_search.html")
"""


ERROR_HANDLER_TEMPLATE_CODE = \
"""
from http import HTTPStatus
from flask import render_template, Blueprint, flash



errors_ = Blueprint("errors_", __name__, template_folder="templates", static_folder="static")


@errors_.app_errorhandler(403)
def error_403(error):
    return render_template("error_403.html"), HTTPStatus.FORBIDDEN


@errors_.app_errorhandler(404)
def error_404(error):
    return render_template("error_404.html"), HTTPStatus.NOT_FOUND


@errors_.app_errorhandler(429)
def error_429(error):
    flash(message="Your request is too much, try again in a few minute", category="error")
    return render_template("error_429.html"), HTTPStatus.TOO_MANY_REQUESTS
    

@errors_.app_errorhandler(500)
def error_500(error):
    return render_template("error_500.html"), HTTPStatus.INTERNAL_SERVER_ERROR
    
"""


AUTHENTICATION_TEMPLATE_CODE = \
"""
from my_demo_app import app, limiter
from flask import render_template, Blueprint



authent_ = Blueprint("authent_", __name__, template_folder="templates", static_folder="static")


@authent_.route("/")
@limiter.limit("5 per minute")
def secure_register():
    return render_template("register.html")

    
@authent_.route("/")
@limiter.limit("5 per minute")
def secure_login():
    return render_template("login.html")
"""


RESET_PASSWORD_TEMPLATE_CODE = \
"""
from flask import render_template, Blueprint




reset_pswd = Blueprint("reset_pswd", __name__, template_folder="templates", static_folder="static")


@reset_pswd.route("/")
def secure_password():
    return render_template("reset_pswd.html")
"""


ADMIN_TEMPLATE_CODE = \
"""
from flask import render_template, Blueprint




admin_controller = Blueprint("admin_controller", __name__, template_folder="templates", static_folder="static")


@admin_controller.route("/")
def controller():
    return render_template("controller.html")
"""


GITIGNORE = \
"""
*.db
venv/
config/.venv
__pycache__
/__pycache__
**/*/__pycache__
"""


APP_STRUCTURE = {
    "templates": {
        "base.html": BASE_HTML, 
        "index.html": DEMO_HTML,
        "message.html": FLASH_MESSAGE
        },
    
    "views": {
        "routes.py": VIEW_TEMPLATE_CODE, 
        "__init__.py": ""
        },
    
    "errors": {
        "routes.py": ERROR_HANDLER_TEMPLATE_CODE,
        "__init__.py": "",
    },
    
    "authentication":{
      "routes.py": AUTHENTICATION_TEMPLATE_CODE,
      "form.py": "",
      "__init__.py": ""  
    },
    
    "password_reset":{
      "routes.py": RESET_PASSWORD_TEMPLATE_CODE,
      "form.py": "",
      "__init__.py": ""  
    },
    
    "search":{
      "routes.py": SEARCH_TEMPLATE_CODE,
      "form.py": "",
      "__init__.py": ""  
    },
    
    "admin":{
      "routes.py": ADMIN_TEMPLATE_CODE,
      "form.py": "",
      "__init__.py": ""  
    },

    "static": {
        "css": "base_main.css", 
        "js": "script.js", 
        "media": "flask_cli.png",
        },
    
    "database": {
        "models.py": APP_SESSION, 
        "__init__.py": ""
        },
    
    "config":{
        ".env": "",
        ".flaskenv": ""
    }
}


# ANSI escape color code for displaying or printing sucessful message
GREEN = '\033[92m'
RESET = '\033[0m'


#ANSI escape color code for displaying or printing sucessful message
YELLOW = "\033[33m"
RESET = "\033[0m" 


class CmdHandler():
    
    def init():
        print(f"{GREEN}Please wait, app is setting up virtual environment......{RESET}")
        
        os.system("pip install virtualenv")
        
        os.system("python -m venv venv")
        
        print(f"{GREEN}Successfully created virtual environment{RESET}")
        
        print("")

        print(f"{YELLOW}Please wait installing, Flask, Flask-Session, Flask-Limiter, flask-babel, Flask-Caching, Flask-Assets, Flask-SQLAlchemy and Flask-Migrate{RESET}")
        
        os.system("pip install Flask Flask-Session flask-babel Flask-Limiter Flask-Caching Flask-Assets Flask-SQLAlchemy Flask-Migrate")
        
        print(f"{GREEN}These packages are installed globally on your computer. To use them, activate your virtual environment and reinstall them inside.{RESET}")
        
        print("")

        print(f"{YELLOW}To activate the virtual environment, navigate into the 'venv' directory and run 'Scripts/activate' on Windows or 'source bin/activate' on Unix-based systems.{RESET}")

        print("")
    
    def create_flask_app_folder(app_folder_name):
        try:
            if not os.path.exists(app_folder_name):
                os.mkdir(app_folder_name)
                with open(file="app.py", mode="w") as file:
                    file.write(APP_STARTUP.replace("my_demo_app",  app_folder_name))

                with open(file=os.path.join(app_folder_name, "__init__.py"), mode="w") as file:
                    file.write(APP_SETTINGS.replace("my_demo_app", app_folder_name))
                
                with open(file=os.path.join(app_folder_name, ".gitignore"), mode="w") as file:
                    file.write(GITIGNORE)
                                          
                for dir, content in APP_STRUCTURE.items():
                    os.mkdir(os.path.join(app_folder_name, dir))
                    
                    if dir in ["errors", "views", "authentication", "admin", "search", "password_reset"]:
                        template_folder = os.path.join(app_folder_name, dir, "templates")
                        os.mkdir(template_folder)
                        
                        if dir == "errors":
                            error_files = ["error_403.html", "error_404.html", "error_500.html", "error_429.html"]
                            for error_file in error_files:
                                file_path = os.path.join(template_folder, error_file)
                                with open(file=file_path, mode="w") as file:
                                    file.write(f"<!-- This is the {error_file} template -->\n{DEMO_HTML_TEMPLATES}")
                        else:
                            template_filenames = {
                                "views": "index.html",
                                "admin": "controller.html",
                                "search": "item_search.html",
                                "authentication": "login.html",
                                "authentication": "register.html",
                                "password_reset": "reset_pswd.html"
                            }
                            
                            file_name = template_filenames.get(dir, None)
                            if file_name:
                                file_path = os.path.join(template_folder, file_name)
                                with open(file=file_path, mode="w") as file:
                                    file.write(f"<!-- This is the {file_name} template -->\n{DEMO_HTML_TEMPLATES}")
                            
                            
                    if dir == "static":
                        for static_dir, value in content.items():
                            os.makedirs(os.path.join(app_folder_name, dir, static_dir))
                            with open(file=
                                os.path.join(app_folder_name, dir, static_dir, value), mode="w") as file:
                                file.write(DEMO_CSS)

                                
                    if dir in ["templates", "views", "errors", "authentication", "database", "config", "admin", "search", "password_reset"]:
                        for temp, value in content.items():
                            with open(file=os.path.join(app_folder_name, dir, temp), mode="w") as file:
                                file.write(value.replace("my_demo_app", app_folder_name))
            else:
                print(f"{YELLOW} The Folder {app_folder_name} already exists. {RESET}")
        except FileExistsError as e:
            print(f"{YELLOW} Error: {e}{RESET}")  
