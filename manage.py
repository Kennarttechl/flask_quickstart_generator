import sys
# from colorama import Fore, Style
from flask_cli.app_structure.cmd_handler import CmdHandler


# ANSI escape color code for displaying or printing sucessful message
GREEN = '\033[92m'
RESET = '\033[0m'


# ANSI escape color code for displaying or printing the docs
YELLOW = "\033[33m"
RESET = "\033[0m"


# Define colors for messages
# success_color = Fore.GREEN


docs = \
""" 
flask-cli:
    Flask-CLI is a command-line interface (CLI) tool built using Python and the Flask framework. It aims to provide developers with a convenient way to generate Flask boilerplate code for creating new Flask applications. Flask-CLI simplifies the process of creating new Flask projects, enabling developers to focus on building application logic rather than spending time on repetitive setup tasks.

    
    command for creating the project folder:
        * python manage.py create-app [project/app name]
          example =>  python manage.py create-app my_demo_app

    commands for creating virtualenv venv:
        * python manage.py -i create-app 
        * python manage.py --init create-app  
"""

def main():
    command = sys.argv[1].strip() if len(sys.argv) > 1 else ""
    argument = sys.argv[2].strip() if len(sys.argv) > 2 else ""

    if command == "create-app" and argument != "":
        CmdHandler.create_flask_app_structure(argument)
        print(f"{GREEN}Project created sucessfully{RESET}")
        # print(success_color + "Project created successfully!" + Style.RESET_ALL)

    elif command in ["--init", "-i"]:
        CmdHandler.init()
        print(f"{GREEN}Sucessfully create virtualenv env{RESET}")

    else:
        exit(f"{YELLOW}{docs}{RESET}")


if __name__ == "__main__":
    main()