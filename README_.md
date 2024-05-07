# flask_boilerplate_generator

The project generates boilerplate code for Flask applications.


# This project uses os and sys modules

`os module is purposely use in this project for some reasons`


**1. File and Directory Management:**
1. Create, delete, rename, move, and check the existence of files and directories.
2. Get file/directory attributes (size, creation time, etc.).
3. List directory contents.
4. Change the current working directory.


**2. process management.**
1. Execute system commands and capture their output.
2. Get information about running processes.


**3. Environment Variables:**
1. Get, set, and delete environment variables


**4. Path Manipulation:**
1. Join path components to create valid file paths across different operating systems.
2. Split paths into components.
3. Expand user's home directory in paths


*Functions:*
1. os.getcwd(): Get the current working directory.
2. os.listdir(path): List files and directories in a directory.
3. os.mkdir(path): Create a directory.
4. os.makedirs(path, exist_ok=True): Create directories recursively, ignoring errors if they already exist (optional exist_ok argument).
5. os.remove(path): Delete a file.
6. os.rmdir(path): Delete an empty directory.
7. os.path.join(path1, path2, ...): Join path components into a valid path.
8. os.path.exists(path): Check if a file or directory exists.
9. os.system(command): Execute a system command and wait for its completion.
10. os.environ: A dictionary containing the environment variables.


`sys moduel is purposely use for some reasons`

**Functions:**
1. sys.argv: A list containing the command-line arguments passed to the Python script when it's executed. The first element (sys.argv[0]) is always the script name itself, and subsequent elements are the arguments provided.

1. 1 In Python, argv is a built-in list variable that represents the arguments passed to a script when it's executed from the command line.

2. 2 Use sys.argv when your script needs to process command-line arguments (arguments passed when running the script).

2. sys.exit(exit_code=0): Exits the Python script with an optional exit code. The exit code can be used to indicate success (0) or an error condition (a non-zero value).

3. sys.getsizeof(object): Returns the approximate memory size, in bytes, of an object. This can be helpful for debugging memory usage.

4. sys.stdin: A standard input stream object, usually referring to the console from which the user can provide input.

5. sys.stdout: A standard output stream object, usually referring to the console where the program's output is displayed.

6. sys.stderr: A standard error stream object, usually referring to the console where error messages are displayed.

7. sys.version: A string containing the Python interpreter version information.


# Attributes:
1. sys.platform: A string indicating the operating system platform the script is running on (e.g., 'win32', 'linux', 'darwin').

2. sys.path: A list containing the search path for modules. This list determines where Python looks for modules when you use the import statement. You can modify sys.path to add custom directories containing modules.

3. sys.maxsize: The largest integer value a variable of data type Py_ssize_t can hold. This can be useful for understanding the limits of integer calculations.

4. sys.executable: The absolute path to the Python interpreter binary that executed the current script.




<!-- pip install flask_cli-0.1.0.tar.gz
pip install flask_cli-0.1.0-py3-none-any.whl
python setup.py sdist bdist_wheel
pip install .


