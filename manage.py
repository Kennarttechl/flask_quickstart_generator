import sys
from flask_cli.app_structure.cmd_handler import CmdHandler


docs = \
""" 
flask-cli:
    Flask-CLI is a command-line interface (CLI) tool built using Python and the Flask framework. It aims to provide developers with a convenient way to generate Flask boilerplate code for creating new Flask applications. Flask-CLI simplifies the process of creating new Flask projects, enabling developers to focus on building application logic rather than spending time on repetitive setup tasks.

    commands for creating the project folder:
        * python manage.py create-app [project/app name]

    commands for creating virtualenv venv:
        * python manage.py create-app -i my_demo_app
        * python manage.py create-app --init my_demo_app
"""

def main():
    command = sys.argv[1].strip() if len(sys.argv) > 1 else ""
    argument = sys.argv[2].strip() if len(sys.argv) > 2 else ""

    if command == "create-app" and argument != "":
        CmdHandler.create_flask_app_structure(argument)
        print("Project created sucessfully)")

    elif command in ["--init", "-i"]:
        CmdHandler.init()
        print("Virtualenv created sucessfully")

    else:
        exit(docs)


if __name__ == "__main__":
    main()