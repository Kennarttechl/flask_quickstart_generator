import sys
from colorama import Fore, Style
from .cmd_handler import CmdHandler


docs = """ 
Flask Quickstart Generator:
    The Flask Quickstart Generator is a command-line tool (CLI) built with Python and the Flask framework. It provides developers with a convenient way to generate the folder structure and code for new Flask applications. This simplifies the process of starting new projects, allowing developers to focus on building application logic instead of skipping the boilerplate setup.
    
    ***** User Commands: To Get Started Quickly *****

    command for creating the project folder structure `Only`:
        flask-manage create-app my_demo_app

    command for creating virtualenv venv `Only`:
        flask-manage -v  
        
    commands for creating Both (Virtual Environment & App or Project) :
        flask-manage -v create-app my_demo_app
        
    ==== Note =====
    You can change `my_demo_app` to any name of your choice
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
        # print(f"{GREEN}Virtual environment created successfully{RESET}")

    elif command == "create-app" and argument != "":
        CmdHandler.generate_flask_app_folder(argument)
        print(f"{Fore.GREEN}***** Project created successfully *****{Style.RESET_ALL}")

    else:
        sys.exit(f"{Fore.YELLOW}{docs}{Style.RESET_ALL}")
        
if __name__ == "__main__":
    main()
