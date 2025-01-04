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
    - `pip install Flask` or `pip install Flas==2.2.2` for example when a specific version is needed.
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
    - `django-admin startproject littlelemon`  
    Note that _littlelemon_ is the intended name for a NEW projec that doesn't  
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
