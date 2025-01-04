# fcs
## A repo for codespaces
- hence FCS = For Code Spaces

## Purpose(s)
1. "Host" the capstone projects for back-end development from Coursera.
1. Enable coding on-the-go by having an in-browser _environment_ that can be use on a failry modern tablet pc.
1. Since the codespace is in-browser, it is essentially "multi-device" meaning I can work form any any device and not have authentication conflicts, etc.


## Installation Notes
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
        Both the Meta&trade; and IBM&trade; back-end development certificates have a capstone project.

In the IBM&trade; certificate path, your app with have this architecture:
![IBM website build](backend_capstone_architecture.png)
###### See - https://www.coursera.org/learn/backend-development-capstone-project/supplement/1PoJi/project-tasks-overview
