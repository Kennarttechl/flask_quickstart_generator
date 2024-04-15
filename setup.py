from setuptools import setup, find_packages



setup(
    name="flask_command_line",  # Keep the project name the same for installation
    version="0.1.0",
    packages=find_packages(include=["flask_comand_line*"]),  # Adjust the pattern
    scripts=["manage.py"],
    install_requires=[
        "Flask",
        "Flask-Session",  # Add required dependencies from B
        "Flask-SQLAlchemy",
        "Flask-Migrate",
    ],
    entry_points={
        "console_scripts": [
            "flask_command_line=flask_comand_line.main:main"  # Update the entry point
        ]
    },
)

