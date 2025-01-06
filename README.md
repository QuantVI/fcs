# fcs
## A repo for codespaces
- hence FCS = For Code Spaces

## Purpose(s)
1. "Host" the capstone projects for back-end development from Coursera.
1. Enable coding on-the-go by having an in-browser _environment_ that can be use on a failry modern tablet pc.
1. Since the codespace is in-browser, it is essentially "multi-device" meaning I can work form any any device and not have authentication conflicts, etc.

Both the Meta&trade; and IBM&trade; back-end development certificates have a capstone project.

In the IBM&trade; certificate path, your app with have this architecture:
![IBM website build](backend_capstone_architecture.png)
###### See - https://www.coursera.org/learn/backend-development-capstone-project/supplement/1PoJi/project-tasks-overview

----

## Installation Notes
- For reference: IBM Capstone - Module 1 - Intro fo Flask
- `python3 -m venv SomeEnvironmentName`
  - a folder in the current directory bearing the env name is made
    - it contains _bin, include, lib, lib64, pyvenv.cfg_
  - you can acivate this and install Flask or Django in the activated env
    - `source SomeEnvironmentName/bin/activate`
        - `pip freeze` on this will show nothing. You have no non-standard, "external" modules installed
    - `pip install Flask` or `pip install Flask==2.2.2` for example when a specific version is needed.
        - Might need to use `pip3`
        - `pip freeze` can show for example
            + asgiref==3.8.1  
            Django==5.1.4  
            sqlparse==0.5.3

## Django Project Setup/Run 
- For reference see : Facebook Capstone - Module 1 - Setting up the Project
1. Create a virtual environment, such as for "Little Lemon" example.
1. Activate the virtual environment
    - Python recommends using __separate virtual environments__ for each Django __application__  
  so that the dependencies do not conflict
1. Install Django with pip
    - The command line utility `django-admin` will be available in the scripts directory.
1. Add an "app" to Django (aka Create a Django project)
    - `django-admin startproject bigorange`  
    Note that _little lemon_ is the intended name for a NEW project that doesn't  
    exist yet. Also, the name doesn't need to be the same as the virtual environment.  
    This sort of "name overloading" is annoying and confusing.  
    Furthermore __startproject__ really means _create a new project and folders with this name..._.
1. Run the command to start the development server
    - Step inside the project directory first
    - `python manage.py runserver`
    - you should see the dev server running by loadin the localhost url in our web browser
1. Create (another) "app" inside the project using the __startapp__ command
    - Thus `startapp` really means "__create__ a new app"
    - `python3 manage.py startapp reservation`
    - Be sure to add this app to the `settings.py` file in the `installed_apps` list

### Folder Structure
- anEnv : folder made by using this name for virtual env : `python -m venv anEnv`
  - bin, include, lib, lib64, pyenv.cfg : folders and config file inside __anEnv__ when it's created
- after activating `anEnv` you run pip
- `pip install django` : wil put Djano 5.1.4 (or latest) into your lib64/python3.12/site-packages folder
  - asfiref 3.8.1 and sqlparse 0.5.3 are also installed
  - The show up with `Django==5.1.4` when you run `pip freeze`
- with anEnv still activated
  - `django-admin` command can be called from anywhere, even the root "fcs" folder
  - `django-admin startproject littlelemon`
  - if called in `workspaces/fcs` then a folder is made there.
  - This is why it's good to create a **"Project Folder"** beuuase  
  otherwise `anEnv` and `littlelemon` are in the `fcs` parent folder,  
  but we do not know that `anEnv` was the virtual environment specifically  
  made for the `littlelemon` Django project.

#### Example
- `proj_lemon` folder
  - `env_lemon` virtual env folder from `venv` command
  - `littlelemon` django project folder from `startproject` command
    - `cd` into this folder to run `python manage.py runserver`  
    This boots/launches the website, view in-browser at localhost : 8000  
    Quit with CTRl+C.
- Your (new) django **project** needs its first **app*
  - `python manage.py startapp reservation`  
  Where *startapp* really means "create", will create a reservation app  
  in your littlelemon project. This *app* must be added to `settings.py`
  - Notice that since this command uses `manage,py` it is in the **outer**  
  **PROJECT** folder, not the inner folder of the same name
  - proj_lemon $\leftarrow$ directory from `mkdir` to hold env and django full-design
    - littlelemon $\leftarrow$ Project Folder (from `startproject`)
      - littlelemon $\leftarrow$ *inner* folder auto-created with the same name
      - manage.py
      - db.sqlite3
    - env_lemon $\leftarrow$ the virtual_env that Django Python module is installed in


