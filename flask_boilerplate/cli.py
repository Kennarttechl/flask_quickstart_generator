import sys
from .cmd_handler import CmdHandler


# ANSI escape color code for displaying or printing sucessful message
GREEN = "\033[92m"
RESET = "\033[0m"


# ANSI escape color code for displaying or printing the docs
YELLOW = "\033[33m"
RESET = "\033[0m"


docs = """ 
flask-boilerplate generator:
    The Flask Boilerplate Generator is a command-line tool (CLI) built with Python and the Flask framework. It provides developers with a convenient way to generate the folder structure and code for new Flask applications. This simplifies the process of starting new projects, allowing developers to focus on building application logic instead of skipping the boilerplate setup.
    
    command for creating the project folder:
        * flask-manage create-app [project/app name]

    command for creating `Only` virtualenv venv:
        * flask-manage -v  
        
    commands for creating `Both` virtual environment & app (app folder):
        * flask-manage -v create-app my_demo_app
"""


def main():
    """This function is the entry point for the script's execution."""

    command = sys.argv[1].strip() if len(sys.argv) > 1 else ""
    argument = sys.argv[2].strip() if len(sys.argv) > 2 else ""
    project_name = sys.argv[3].strip() if len(sys.argv) > 3 else ""

    if command == "-v" and argument == "create-app" and project_name != "":
        CmdHandler.init()
        CmdHandler.generate_flask_app_folder(project_name)

    elif command == "-v" and argument == "":
        CmdHandler.init()
        print(f"{GREEN}Virtual environment created successfully{RESET}")

    elif command == "create-app" and argument != "":
        CmdHandler.generate_flask_app_folder(argument)
        print(f"{GREEN}Project created successfully{RESET}")

    else:
        sys.exit(f"{YELLOW}{docs}{RESET}")


if __name__ == "__main__":
    main()
