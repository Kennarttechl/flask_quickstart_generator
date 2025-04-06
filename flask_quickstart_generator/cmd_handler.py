import os
from .model import USER_MODEL
from colorama import Fore, Style
from .settings import APP_SETTINGS
from .env import ENVIRONMENT_VARIABLE
from .js import (
    LOG_JS,
    PROFILE_AC,
    ERROR_PAGES,
    TOO_MANY_JS,
    NOT_FOUND_JS,
    MAINTAINANCE_JS,
    SADASHBOARD_JS,
    FLASH_DOM_REMOVE,
)
from .css import (
    LOG_CSS,
    VIEW_CSS,
    FORBIDDEN,
    NOT_FOUND,
    BASE_FOOTER,
    BAD_REQUESTS,
    UNAUTHORIZED,
    MAINTAINANCE,
    FLASH_MESSAGE,
    SADASHBOARD_CSS,
    INTERNAL_SERVER,
    CONTENT_TOO_LARGE,
    TOO_MANAY_REQUEST,
    ACCOUNT_CSS_PROFILE,
)
from .forms import (
    SEARCH_FORM,
    SADASHBOARD_FORM,
    UPLOAD_FILES_FORM,
    AUTHENTICATION_FORM,
    ACCOUNT_SETTINGS_FORM,
)

from .html import (
    BASE_HTML,
    VIEW_HTML,
    USER_ROLE_HTML,
    FORBIDDEN_HTML,
    NOT_FOUND_HTML,
    UNAUTHORIZED_HTML,
    BAD_REQUESTS_HTML,
    MAINTAINANCE_HTML,
    FLASH_CUSTOM_HTML,
    SADASHBOARD_SECURE,
    SADMIN_LOGIN_SECURE,
    DEMO_HTML_TEMPLATES,
    PROFILE_UPDATE_HTML,
    INTERNAL_SERVER_HTML,
    CONTENT_TOO_LARGE_HTML,
    TOO_MANAY_REQUEST_HTML,
    ACCOUNT_SETTING_FORM_HTML,
    AUTHENTICATION_LOGIN_HTML,
    AUTHENTICATION_REGISTER_HTML,
)

from .routes_ import (
    GITIGNORE,
    APP_STARTUP,
    ANSI_COLORS_,
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
        "fonts": None,
        "icons": "flask_cli.png",
        "media": "default.jpg",
    },
    "database": {"models.py": USER_MODEL, "__init__.py": ""},
    "account_settings": {
        "routes.py": ACCOUNT_SETTINGS_TEMPLATE_CODE,
        "form.py": ACCOUNT_SETTINGS_FORM,
        "__init__.py": "",
    },
    "media_utils": {"utils.py": ACCOUNT_UTILS, "__init__.py": ""},
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
            f"{Fore.YELLOW}Please wait installing collected packages: Flask, python-dotenv, Flask-Session, Flask-Limiter, flask-babel, Flask-Caching, Flask-SQLAlchemy, psycopg2, Flask-Migrate, Flask-WTF, WTForms, waitress, pillow, Flask-Bcrypt, Flask-Login {Style.RESET_ALL}"
        )

        os.system(
            "pip install Flask flask-babel python-dotenv Flask-Bcrypt waitress Flask-Caching Flask-Limiter Flask-Login Flask-Migrate Flask-Session Flask-SQLAlchemy Flask-WTF WTForms psycopg2 pillow Flask-Login"
        )

        print(
            f"{Fore.GREEN}These packages are installed globally on your computer. To use them, activate your virtual environment and reinstall them inside.{Style.RESET_ALL}"
        )

        print("")

        print(
            f"{Fore.RED}To activate the virtual environment, navigate into the 'venv' directory and run 'Scripts/activate' on Windows or 'source bin/activate' on Unix-based systems.{Style.RESET_ALL}"
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
                CmdHandler.create_file(
                    "wsgi.py", APP_STARTUP.replace("my_demo_app", app_folder_name)
                )
                CmdHandler.create_file(
                    os.path.join(app_folder_name, "__init__.py"),
                    APP_SETTINGS.replace("my_demo_app", app_folder_name),
                )
                CmdHandler.create_file(
                    os.path.join(app_folder_name, ".gitignore"), GITIGNORE
                )
                CmdHandler.create_file(
                    os.path.join(app_folder_name, "ansi_.py"), ANSI_COLORS_
                )

                for dir_name, content in APPLICATION_STRUCTURE.items():
                    os.makedirs(os.path.join(app_folder_name, dir_name), exist_ok=True)

                    # Create templates for specific directories
                    if dir_name in [
                        "uploads",
                        "errors",
                        "views",
                        "admin",
                        "search",
                        "super_admin",
                        "authentication",
                        "account_settings",
                    ]:
                        template_folder = os.path.join(
                            app_folder_name, dir_name, "templates"
                        )
                        os.makedirs(template_folder, exist_ok=True)

                        if dir_name == "errors":
                            CmdHandler.create_error_templates(template_folder)
                        elif dir_name == "authentication":
                            CmdHandler.create_auth_templates(
                                template_folder, content["templates"]
                            )
                        elif dir_name == "super_admin":
                            CmdHandler.create_super_admin_templates(
                                template_folder, content["templates"]
                            )
                        else:
                            CmdHandler.create_templates_for_directories(
                                template_folder, dir_name
                            )

                    # Create base template for the "templates" folder
                    if dir_name == "templates":
                        CmdHandler.create_templates_base(
                            os.path.join(app_folder_name, "templates")
                        )

                    # Handle static files
                    if dir_name == "static":
                        CmdHandler.create_static_files(
                            app_folder_name, dir_name, content
                        )

                        # Call to create CSS files within the static/css folder
                        CmdHandler.create_css_files(app_folder_name)

                    # Write other files in the directory
                    if dir_name in [
                        "views",
                        "admin",
                        "errors",
                        "config",
                        "search",
                        "caching",
                        "uploads",
                        "database",
                        "super_admin",
                        "media_utils",
                        "authentication",
                        "account_settings",
                    ]:
                        for filename, file_content in content.items():
                            if filename != "templates":
                                CmdHandler.create_file(
                                    os.path.join(app_folder_name, dir_name, filename),
                                    file_content.replace(
                                        "my_demo_app", app_folder_name
                                    ),
                                )

            else:
                print(
                    f"{Fore.YELLOW} The Folder {app_folder_name} already exists. {Style.RESET_ALL}"
                )
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
        with open(file_path, "w") as file:
            file.write(content)

    @staticmethod
    def create_css_files(app_folder_name):
        """Create CSS files like sadashboard.css, log.css, flash.css."""
        css_dir = os.path.join(app_folder_name, "static", "css")
        os.makedirs(css_dir, exist_ok=True)  # Ensure the css directory is created

        # Write each CSS constant to its respective file
        css_files = {
            "403.css": FORBIDDEN,
            "404.css": NOT_FOUND,
            "503.css": MAINTAINANCE,
            "400.css": BAD_REQUESTS,
            "401.css": UNAUTHORIZED,
            "500.css": INTERNAL_SERVER,
            "413.css": CONTENT_TOO_LARGE,
            "429.css": TOO_MANAY_REQUEST,
            "log.css": LOG_CSS,
            "view.css": VIEW_CSS,
            "footer.css": BASE_FOOTER,
            "flash.css": FLASH_MESSAGE,
            "sadashboard.css": SADASHBOARD_CSS,
            "account.css": ACCOUNT_CSS_PROFILE,
        }

        for filename, css_content in css_files.items():
            file_path = os.path.join(css_dir, filename)
            CmdHandler.create_file(file_path, css_content)

    @staticmethod
    def create_error_templates(template_folder):
        error_files_content = {
            "bad_request.html": BAD_REQUESTS_HTML,
            "forbidden.html": FORBIDDEN_HTML,
            "not_found.html": NOT_FOUND_HTML,
            "maintenance.html": MAINTAINANCE_HTML,
            "payload_data.html": CONTENT_TOO_LARGE_HTML,
            "invalid_path.html": "",
            "internal_server.html": INTERNAL_SERVER_HTML,
            "too_many_requests.html": TOO_MANAY_REQUEST_HTML,
            "unauthorized.html": UNAUTHORIZED_HTML,
        }
        # Loop through the error files and create each with the corresponding content
        for error_file, html_content in error_files_content.items():
            file_path = os.path.join(template_folder, error_file)
            CmdHandler.create_file(file_path, html_content)

    @staticmethod
    def create_auth_templates(template_folder, auth_templates):
        """Create authentication templates like login and signup."""
        for filename, html_content in auth_templates.items():
            file_path = os.path.join(template_folder, filename)
            CmdHandler.create_file(file_path, html_content)

    @staticmethod
    def create_super_admin_templates(template_folder, super_admin_templates):
        """Create super admin templates using SADMIN_LOGIN_SECURE and SADASHBOARD_SECURE."""
        CmdHandler.create_file(
            os.path.join(template_folder, "salogin_secure.html"), SADMIN_LOGIN_SECURE
        )
        CmdHandler.create_file(
            os.path.join(template_folder, "sadashboard_secure.html"), SADASHBOARD_SECURE
        )
        CmdHandler.create_file(
            os.path.join(template_folder, "flash_message.html"), FLASH_CUSTOM_HTML
        )
        CmdHandler.create_file(
            os.path.join(template_folder, "flash_message.html"), FLASH_CUSTOM_HTML
        )
        CmdHandler.create_file(
            os.path.join(template_folder, "account_edit_data.html"), PROFILE_UPDATE_HTML
        )
        CmdHandler.create_file(
            os.path.join(template_folder, "user_role.html"), USER_ROLE_HTML
        )
    
    @staticmethod
    def create_templates_for_directories(template_folder, dir_name):
        """Create general templates for directories like views, admin, search."""
        template_filenames = {
            "views": "index.html",
            "admin": "controller.html",
            "search": "item_search.html",
            "uploads": "file_upload.html",
            "account_settings": "update_account.html",  # Fix incorrect variable reference
        }

        file_name = template_filenames.get(dir_name, None)

        if file_name:
            if dir_name == "views":
                content = VIEW_HTML  # Use VIEW_HTML for index.html
            elif dir_name == "account_settings":
                content = ACCOUNT_SETTING_FORM_HTML
            else:
                content = DEMO_HTML_TEMPLATES  # Keep default content for other templates
            
            CmdHandler.create_file(os.path.join(template_folder, file_name), content)


    # @staticmethod
    # def create_templates_for_directories(template_folder, dir_name):
    #     """Create general templates for directories like views, admin, search."""
    #     template_filenames = {
    #         "views": "index.html",
    #         "admin": "controller.html",
    #         "search": "item_search.html",
    #         "uploads": "file_upload.html",
    #         "account_settings": "update_account.html",  # Fix incorrect variable reference
    #     }

    #     file_name = template_filenames.get(dir_name, None)

    #     if file_name:
    #         content = (
    #             ACCOUNT_SETTING_FORM_HTML
    #             if dir_name == "account_settings"
    #             else DEMO_HTML_TEMPLATES
    #         )
    #         CmdHandler.create_file(os.path.join(template_folder, file_name), content)

    @staticmethod
    def create_static_files(app_folder_name, static_dir, content):
        """Create static files like CSS, JS, fonts, etc."""
        for static_subdir, value in content.items():
            static_subdir_path = os.path.join(
                app_folder_name, static_dir, static_subdir
            )
            os.makedirs(
                static_subdir_path, exist_ok=True
            )  # Ensure the static subdirectories are created

            # Handle JavaScript files specifically in the js folder
            if static_subdir == "js":
                js_files = {
                    "log.js": LOG_JS,
                    "account.js": PROFILE_AC,
                    "too_many.js": TOO_MANY_JS,
                    "notfound.js": NOT_FOUND_JS,
                    "dashboard.js": SADASHBOARD_JS,
                    "error_pages_all.js": ERROR_PAGES,
                    "maintainance.js": MAINTAINANCE_JS,
                    "flash_remove_dom.js": FLASH_DOM_REMOVE,
                }

                for filename, js_content in js_files.items():
                    js_file_path = os.path.join(static_subdir_path, filename)
                    CmdHandler.create_file(js_file_path, js_content)
                    
            # Handle font files in static/fonts directory
            if static_subdir == "fonts":
                font_files = [
                    "EBGaramond-Medium.woff",
                    "EBGaramond-Medium.woff2",
                ]
                for font_file in font_files:
                    font_file_path = os.path.join(static_subdir_path, font_file)
                    CmdHandler.create_file(font_file_path, "") #Creates an empty file for now
                    
             # Only create files if 'value' is not empty (avoid creating empty files)
            if value and static_subdir not in ["js", "fonts"]:  # We handle JS and fonts separately
                static_file_path = os.path.join(static_subdir_path, value)
                CmdHandler.create_file(static_file_path, "")  # Create empty files for now

            # # Only create files if 'value' is not empty (avoid creating empty files)
            # if value and static_subdir != "js":  # We handle JS separately, so skip here
            #     static_file_path = os.path.join(static_subdir_path, value)
            #     CmdHandler.create_file(
            #         static_file_path, ""
            #     )  # Create empty files for now
