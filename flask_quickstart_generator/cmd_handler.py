import os
from .css import DEMO_CSS, REGISTER_LOGIN_CSS, BASE_CSS
from .model import USER_MODEL
from .settings import APP_SETTINGS
from .html import (
    BASE_HTML,
    FLASH_MESSAGE,
    DEMO_HTML_TEMPLATES,
    AUTHENTICATION_LOGIN_HTML,
    AUTHENTICATION_REGISTER_HTML
)

from .routes_ import (
    GITIGNORE,
    APP_STARTUP,
    SEARCH_FORM,
    ACCOUNT_UTILS,
    CACHING_CONSTANT,
    UPLOAD_FILES_FORM,
    VIEW_TEMPLATE_CODE,
    AUTHENTICATION_FORM,
    ADMIN_TEMPLATE_CODE,
    SEARCH_TEMPLATE_CODE, 
    ACCOUNT_SETTINGS_FORM,
    FILES_UPLOAD_TEMPLATE_CODE,
    ERROR_HANDLER_TEMPLATE_CODE,
    AUTHENTICATION_TEMPLATE_CODE,
    ACCOUNT_SETTINGS_TEMPLATE_CODE,
)


# ANSI escape color code for displaying or printing sucessful message
GREEN = "\033[92m"
RESET = "\033[0m"


# ANSI escape color code for displaying or printing sucessful message
YELLOW = "\033[33m"
RESET = "\033[0m"


PINK = "\033[95m"
RESET = "\033[0m"


APPLICATION_STRUCTURE = {
    "templates": {
        "base.html": BASE_HTML,
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

    "authentication": {
        "routes.py": AUTHENTICATION_TEMPLATE_CODE,
        "form.py": AUTHENTICATION_FORM,
        "__init__.py": "",
        "templates": {
            "login.html": "",
            "signup.html": AUTHENTICATION_REGISTER_HTML,
        },
    },

    "search": {
        "routes.py": SEARCH_TEMPLATE_CODE,
        "form.py": SEARCH_FORM,
        "__init__.py": ""
    },

    "admin": {
        "routes.py": ADMIN_TEMPLATE_CODE,
        "form.py": "",
        "__init__.py": ""
    },

    "static": {
        "css": "base_main.css", 
        "js": "script.js", 
        "fonts": "flask_cli.png",
        "icons": "flask_cli.png",
        "media": "flask_cli.png",
        },

    "database": {
        "models.py": USER_MODEL,
        "__init__.py": ""
    },

    "account_settings": {
        "routes.py": ACCOUNT_SETTINGS_TEMPLATE_CODE,
        "form.py": ACCOUNT_SETTINGS_FORM,
        "__init__.py": ""
    },

    "media_utils": {
        "utils.py": ACCOUNT_UTILS,
        "routes.py": "",
        "__init__.py": ""
    },

    "uploads": {
        "routes.py": FILES_UPLOAD_TEMPLATE_CODE,
        "form.py": UPLOAD_FILES_FORM,
        "__init__.py": ""
    },

    "caching": {
        "cache_constant.py": CACHING_CONSTANT,
        "__init__.py": ""
    },

    "config": {
        ".env": "",
        ".flaskenv": ""
    }
}


class CmdHandler:

    def init():
        print(f"{GREEN}Please wait, app is setting up virtual environment....{RESET}")

        os.system("pip install virtualenv")

        os.system("python -m venv venv")

        print(f"{GREEN}***** Successfully created virtual environment *****{RESET}")

        print("")

        print(
            f"{YELLOW}Please wait installing collected packages: Flask, Flask-Session, Flask-Limiter, flask-babel, Flask-Caching, Flask-SQLAlchemy, psycopg2, Flask-Migrate, Flask-WTF, WTForms, Flask-Minify, pillow, Flask-Bcrypt, Flask-Login{RESET}"
        )

        os.system(
            "pip install Flask Flask-Assets flask-babel Flask-Bcrypt Flask-Caching Flask-Limiter Flask-Login Flask-Migrate Flask-Session Flask-SQLAlchemy Flask-WTF WTForms psycopg2 Flask-Minify pillow Flask-Login"
        )

        print(
            f"{GREEN}These packages are installed globally on your computer. To use them, activate your virtual environment and reinstall them inside.{RESET}"
        )

        print("")

        print(
            f"{PINK}To activate the virtual environment, navigate into the 'venv' directory and run 'Scripts/activate' on Windows or 'source bin/activate' on Unix-based systems.{RESET}"
        )
        print("")
        
        print(f"{GREEN}***** Project created successfully *****{RESET}")

        print("")

    def generate_flask_app_folder(app_folder_name):
        try:
            if not os.path.exists(app_folder_name):
                os.mkdir(app_folder_name)
                with open(file="wsgi.py", mode="w") as file:
                    file.write(APP_STARTUP.replace("my_demo_app", app_folder_name))

                with open(
                    file=os.path.join(app_folder_name, "__init__.py"), mode="w"
                ) as file:
                    file.write(APP_SETTINGS.replace("my_demo_app", app_folder_name))

                with open(
                    file=os.path.join(app_folder_name, ".gitignore"), mode="w"
                ) as file:
                    file.write(GITIGNORE)

                for dir, content in APPLICATION_STRUCTURE.items():
                    os.mkdir(os.path.join(app_folder_name, dir))

                    if dir in [
                        "uploads",
                        "errors",
                        "views",
                        "admin",
                        "search",
                        "authentication",
                        "account_settings",
                    ]:
                        template_folder = os.path.join(
                            app_folder_name, dir, "templates"
                        )
                        os.mkdir(template_folder)

                        if dir == "errors":
                            error_files = [
                                "forbidden.html",
                                "not_found.html",
                                "maintenance.html",
                                "payload_data.html",
                                "invalid_path.html",
                                "internal_server.html",
                                "too_many_requests.html",
                            ]
                            for error_file in error_files:
                                file_path = os.path.join(template_folder, error_file)
                                with open(file=file_path, mode="w") as file:
                                    file.write(
                                        f"<!-- This is the {error_file} template -->\n{DEMO_HTML_TEMPLATES}"
                                    )

                        elif dir == "authentication":
                            for filename, html_content in content["templates"].items():
                                file_path = os.path.join(template_folder, filename)
                                with open(file=file_path, mode="w") as file:
                                    file.write(html_content)

                        else:
                            template_filenames = {
                                "views": "index.html",
                                "admin": "controller.html",
                                "search": "item_search.html",
                                "uploads": "file_upload.html",
                                "account_settings": [
                                    "reset_pswd.html",
                                    "update_account.html",
                                ],
                            }

                            file_name = template_filenames.get(dir, None)
                            if isinstance(file_name, list):
                                for name in file_name:
                                    file_path = os.path.join(template_folder, name)
                                    with open(file=file_path, mode="w") as file:
                                        file.write(
                                            f"<!-- This is the {name} template -->\n{DEMO_HTML_TEMPLATES}"
                                        )
                            else:
                                file_path = os.path.join(template_folder, file_name)
                                with open(file=file_path, mode="w") as file:
                                    file.write(
                                        f"<!-- This is the {file_name} template -->\n{DEMO_HTML_TEMPLATES}"
                                    )

                    if dir == "static":
                        for static_dir, value in content.items():
                            os.makedirs(os.path.join(app_folder_name, dir, static_dir))
                            with open(
                                file=os.path.join(
                                    app_folder_name, dir, static_dir, value
                                ),
                                mode="w",
                            ) as file:
                                file.write(DEMO_CSS)

                    if dir in [
                        "views",
                        "admin",
                        "errors",
                        "config",
                        "search",
                        "caching",
                        "uploads",
                        "database",
                        "templates",
                        "media_utils",
                        "authentication",
                        "account_settings",
                    ]:
                        for temp, value in content.items():
                            if temp != "templates":
                                with open(
                                    file=os.path.join(app_folder_name, dir, temp), mode="w"
                                ) as file:
                                    file.write(
                                        value.replace("my_demo_app", app_folder_name)
                                    )
            else:
                print(f"{YELLOW} The Folder {app_folder_name} already exists. {RESET}")
        except FileExistsError as e:
            print(f"{YELLOW} Error: {e}{RESET}")





