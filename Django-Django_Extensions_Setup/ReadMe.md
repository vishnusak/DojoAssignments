# Steps to setup Django Extensions on Windows
### These are the steps to get it working on Windows 10(Should work on 8 and 7 as well).

1. Download and install graphviz on your windows (http://www.graphviz.org).

2. Once that is installed, add the graphviz/bin path to your windows PATH variable (e.g., C:\Program Files (x86)\Graphviz2.38\bin).
  - PATH variable can be modified from system settings >> advanced setting >> environment variables.

3. After updating the PATH variable, logoff and login.

4. Now, activate the virtualenv that you are using for django.

5. Inside that, ```pip install pygraphviz```
  - (if this doesn't work because of not finding compiler dependencies, you can download the compiled wheel from http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygraphviz
  - save it in some location on your drive
  - then do ```pip install <full_path_of_the_downloaded_.whl_file>``` - This should install pygraphviz into your venv).

6. Then do ```pip install pydot``` (dot is the language used to generate the ERD inside graphviz).

7. Finally, ```pip install django-extensions```.
  - Follow the "Installing It" and "Using It" directions from the django-extensions github page (https://github.com/django-extensions/django-extensions)

8. Should be good to go :+1:
