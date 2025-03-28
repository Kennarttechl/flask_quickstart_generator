import os
from .model import USER_MODEL
from colorama import Fore, Style
from .settings import APP_SETTINGS
from .env import ENVIRONMENT_VARIABLE
from .js import LOG_JS, SADASHBOARD_JS, FLASH_DOM_REMOVE
from .css import SADASHBOARD_CSS, LOG_CSS, FLASH_MESSAGE
from .forms import (
    AUTHENTICATION_FORM,
    SADASHBOARD_FORM,
    ACCOUNT_SETTINGS_FORM,
    UPLOAD_FILES_FORM,
    SEARCH_FORM,
)

from .html import (
    BASE_HTML,
    FLASH_CUSTOM_HTML,
    SADASHBOARD_SECURE,
    SADMIN_LOGIN_SECURE,
    DEMO_HTML_TEMPLATES,
    AUTHENTICATION_LOGIN_HTML,
    AUTHENTICATION_REGISTER_HTML,
)

from .routes_ import (
    GITIGNORE,
    APP_STARTUP,
    ACCOUNT_UTILS,
    CACHING_CONSTANT,
    VIEW_TEMPLATE_CODE,
    ADMIN_TEMPLATE_CODE,
    SEARCH_TEMPLATE_CODE,
    SUPER_ADMIN_DASHBOARD_,
    FILES_UPLOAD_TEMPLATE_CODE,
    ERROR_HANDLER_TEMPLATE_CODE,
    AUTHENTICATION_TEMPLATE_CODE,
    ACCOUNT_SETTINGS_TEMPLATE_CODE,
)

APPLICATION_STRUCTURE = {
    "templates": {"base.html": BASE_HTML, "message.html": FLASH_MESSAGE},
    
    "views": {"routes.py": VIEW_TEMPLATE_CODE, "__init__.py": ""},
    
    "errors": {
        "routes.py": ERROR_HANDLER_TEMPLATE_CODE,
        "__init__.py": "",
    },
    
    "authentication": {
        "routes.py": AUTHENTICATION_TEMPLATE_CODE,
        "form.py": AUTHENTICATION_FORM,
        "__init__.py": "",
        
        "templates": {
            "login.html": AUTHENTICATION_LOGIN_HTML,
            "signup.html": AUTHENTICATION_REGISTER_HTML,
        },
    },
    
    "super_admin": {
        "routes.py": SUPER_ADMIN_DASHBOARD_,
        "form.py": SADASHBOARD_FORM,
        "__init__.py": "",
        "templates": {
            "salogin_secure.html": SADMIN_LOGIN_SECURE,
            "sadashboard_secure.html": SADASHBOARD_SECURE,
            "flash_message.html": FLASH_CUSTOM_HTML,
        },
    },
    
    "admin": {"routes.py": ADMIN_TEMPLATE_CODE, "form.py": "", "__init__.py": ""},
    
    "search": {
        "routes.py": SEARCH_TEMPLATE_CODE,
        "form.py": SEARCH_FORM,
        "__init__.py": "",
    },
    
    "static": {
        "css": None, 
        "js": None,
        "fonts": "flask_cli.png",
        "icons": "flask_cli.png",
        "media": "flask_cli.png",
    },

    "database": {"models.py": USER_MODEL, "__init__.py": ""},
    
    "account_settings": {
        "routes.py": ACCOUNT_SETTINGS_TEMPLATE_CODE,
        "form.py": ACCOUNT_SETTINGS_FORM,
        "__init__.py": "",
    },
    
    "media_utils": 
        {"utils.py": ACCOUNT_UTILS, 
         "__init__.py": ""},
        
    "uploads": {
        "routes.py": FILES_UPLOAD_TEMPLATE_CODE,
        "form.py": UPLOAD_FILES_FORM,
        "__init__.py": "",
    },
    
    "caching": {"cache_constant.py": CACHING_CONSTANT, "__init__.py": ""},
    
    "config": {".env": ENVIRONMENT_VARIABLE, ".flaskenv": ""},
}


class CmdHandler:
    def init():
        print(
            f"{Fore.GREEN}Please wait, app is setting up virtual environment....{Style.RESET_ALL}"
        )

        os.system("pip install virtualenv")

        os.system("python -m venv venv")

        print(
            f"{Fore.GREEN}***** Successfully created virtual environment *****{Style.RESET_ALL}"
        )

        print("")

        print(
            f"{Fore.YELLOW}Please wait installing collected packages: Flask, Flask-Session, Flask-Limiter, flask-babel, Flask-Caching, Flask-SQLAlchemy, psycopg2, Flask-Migrate, Flask-WTF, WTForms, Flask-Minify, pillow, Flask-Bcrypt, Flask-Login{Style.RESET_ALL}"
        )

        os.system(
            "pip install Flask flask-babel Flask-Bcrypt Flask-Caching Flask-Limiter Flask-Login Flask-Migrate Flask-Session Flask-SQLAlchemy Flask-WTF WTForms psycopg2 Flask-Minify pillow Flask-Login"
        )

        print(
            f"{Fore.GREEN}These packages are installed globally on your computer. To use them, activate your virtual environment and reinstall them inside.{Style.RESET_ALL}"
        )

        print("")

        print(
            f"{Fore.PINK}To activate the virtual environment, navigate into the 'venv' directory and run 'Scripts/activate' on Windows or 'source bin/activate' on Unix-based systems.{Style.RESET_ALL}"
        )
        print("")

        print(f"{Fore.GREEN}***** Project created successfully *****{Style.RESET_ALL}")

        print("")

    @staticmethod
    def generate_flask_app_folder(app_folder_name):
        try:
            if not os.path.exists(app_folder_name):
                os.mkdir(app_folder_name)

                # Create initial files: wsgi.py, __init__.py, .gitignore
                CmdHandler.create_file("wsgi.py", APP_STARTUP.replace("my_demo_app", app_folder_name))
                CmdHandler.create_file(os.path.join(app_folder_name, "__init__.py"),
                                       APP_SETTINGS.replace("my_demo_app", app_folder_name))
                CmdHandler.create_file(os.path.join(app_folder_name, ".gitignore"), GITIGNORE)

                for dir_name, content in APPLICATION_STRUCTURE.items():
                    os.makedirs(os.path.join(app_folder_name, dir_name), exist_ok=True)

                    # Create templates for specific directories
                    if dir_name in ["uploads", "errors", "views", "admin", "search", "super_admin", "authentication", "account_settings"]:
                        template_folder = os.path.join(app_folder_name, dir_name, "templates")
                        os.makedirs(template_folder, exist_ok=True)

                        if dir_name == "errors":
                            CmdHandler.create_error_templates(template_folder)
                        elif dir_name == "authentication":
                            CmdHandler.create_auth_templates(template_folder, content["templates"])
                        elif dir_name == "super_admin":
                            CmdHandler.create_super_admin_templates(template_folder, content["templates"])
                        else:
                            CmdHandler.create_templates_for_directories(template_folder, dir_name)

                    # Create base template for the "templates" folder
                    if dir_name == "templates":
                        CmdHandler.create_templates_base(os.path.join(app_folder_name, "templates"))

                    # Handle static files
                    if dir_name == "static":
                        CmdHandler.create_static_files(app_folder_name, dir_name, content)

                        # Call to create CSS files within the static/css folder
                        CmdHandler.create_css_files(app_folder_name)

                    # Write other files in the directory
                    if dir_name in ["views", "admin", "errors", "config", "search", "caching", "uploads", "database", "super_admin", "media_utils", "authentication", "account_settings"]:
                        for filename, file_content in content.items():
                            if filename != "templates":
                                CmdHandler.create_file(os.path.join(app_folder_name, dir_name, filename),
                                                       file_content.replace("my_demo_app", app_folder_name))

            else:
                print(f"{Fore.YELLOW} The Folder {app_folder_name} already exists. {Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED} Error: {e}{Style.RESET_ALL}")

    @staticmethod
    def create_templates_base(template_folder):
        """Creates a base HTML file in the 'templates' directory."""
        base_html_path = os.path.join(template_folder, "base.html")
        CmdHandler.create_file(base_html_path, BASE_HTML)

    @staticmethod
    def create_file(file_path, content):
        """Helper function to create a file with given content."""
        with open(file_path, 'w') as file:
            file.write(content)

    @staticmethod
    def create_css_files(app_folder_name):
        """Create CSS files like sadashboard.css, log.css, flash.css."""
        css_dir = os.path.join(app_folder_name, 'static', 'css')
        os.makedirs(css_dir, exist_ok=True)  # Ensure the css directory is created

        # Write each CSS constant to its respective file
        css_files = {
            'sadashboard.css': SADASHBOARD_CSS,
            'log.css': LOG_CSS,
            'flash.css': FLASH_MESSAGE,
        }

        for filename, css_content in css_files.items():
            file_path = os.path.join(css_dir, filename)
            CmdHandler.create_file(file_path, css_content)

    @staticmethod
    def create_error_templates(template_folder):
        """Create error template files."""
        error_files = [
            "forbidden.html", "not_found.html", "maintenance.html",
            "payload_data.html", "invalid_path.html", "internal_server.html", "too_many_requests.html"
        ]
        for error_file in error_files:
            file_path = os.path.join(template_folder, error_file)
            CmdHandler.create_file(file_path, f"<!-- This is the {error_file} template -->\n{DEMO_HTML_TEMPLATES}")

    @staticmethod
    def create_auth_templates(template_folder, auth_templates):
        """Create authentication templates like login and signup."""
        for filename, html_content in auth_templates.items():
            file_path = os.path.join(template_folder, filename)
            CmdHandler.create_file(file_path, html_content)

    @staticmethod
    def create_super_admin_templates(template_folder, super_admin_templates):
        """Create super admin templates using SADMIN_LOGIN_SECURE and SADASHBOARD_SECURE."""
        CmdHandler.create_file(os.path.join(template_folder, "salogin_secure.html"), SADMIN_LOGIN_SECURE)
        CmdHandler.create_file(os.path.join(template_folder, "sadashboard_secure.html"), SADASHBOARD_SECURE)
        CmdHandler.create_file(os.path.join(template_folder, "flash_message.html"), FLASH_CUSTOM_HTML)

    @staticmethod
    def create_templates_for_directories(template_folder, dir_name):
        """Create general templates for directories like views, admin, search."""
        template_filenames = {
            "views": "index.html",
            "admin": "controller.html",
            "search": "item_search.html",
            "uploads": "file_upload.html",
            "account_settings": ["reset_pswd.html", "update_account.html"],
        }

        file_names = template_filenames.get(dir_name, None)
        if isinstance(file_names, list):
            for file_name in file_names:
                CmdHandler.create_file(os.path.join(template_folder, file_name), DEMO_HTML_TEMPLATES)
        else:
            CmdHandler.create_file(os.path.join(template_folder, file_names), DEMO_HTML_TEMPLATES)

    @staticmethod
    def create_static_files(app_folder_name, static_dir, content):
        """Create static files like CSS, JS, fonts, etc."""
        for static_subdir, value in content.items():
            static_subdir_path = os.path.join(app_folder_name, static_dir, static_subdir)
            os.makedirs(static_subdir_path, exist_ok=True)  # Ensure the static subdirectories are created

            # Handle JavaScript files specifically in the js folder
            if static_subdir == 'js':
                js_files = {
                    'log.js': LOG_JS,
                    "flash_remove_dom.js": FLASH_DOM_REMOVE,
                    'dashboard.js': SADASHBOARD_JS  
                }

                for filename, js_content in js_files.items():
                    js_file_path = os.path.join(static_subdir_path, filename)
                    CmdHandler.create_file(js_file_path, js_content)

            # Only create files if 'value' is not empty (avoid creating empty files)
            if value and static_subdir != 'js':  # We handle JS separately, so skip here
                static_file_path = os.path.join(static_subdir_path, value)
                CmdHandler.create_file(static_file_path, "")  # Create empty files for now  
