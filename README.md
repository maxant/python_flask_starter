# what is this?

a demo project with bare basics (python, flask for web, jinja2 for templating, pymysql for database access)

# installation

this project uses python3, which was installed first.

used pycharm to create a new project with a new virtual env (venv). it uses the above python installation.

# create the database:

see `createDatabaseAndTables.sql`

# development

install dependencies from the requirements file:

    pip install -r requirements.txt 

adding more requirements:

    pip install PyMySQL && pip freeze > requirements.txt

run the web application. we have options: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

1) run main directly, thanks to the main method in it:


    python3 main.py 

2) run flask as a module which requires the environment variable to know where to load routes, etc. from:


    export FLASK_APP=main
    python3 -m flask run

3) gunicorn (which relies on wsgi.py)


    sudo apt install gunicorn
    gunicorn --bind 0.0.0.0:5000 wsgi:app

or with more workers and a unix socket created within the folder and set an umask value of 007 so that the socket 
file is created to give access to the owner and group, while restricting other access:

    gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app

# debugging

debug in pycharm using the main function of main.py

    export FLASK_ENV=development

will cause reloading and an interactive debugger in the browser. NOTE - the above can be added to the run config so
that it works together with the debugger.

or we can set it here:

    app.run(host='0.0.0.0', port=8080, debug=True)


# Python Reference

- https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3
  - `*args` is a variable length list of args, like `Object... a` in java
  - `**kwargs` pass a keyworded, variable-length argument dictionary to a function. 
    - `print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)`
    - prints: `{'kwargs_3': True, 'kwargs_2': 4.5, 'kwargs_1': 'Shark'}` if the function does `print(kwargs)`
    - you can do this too: `for key, value in kwargs.items():`

# TODO 

- pymysql tutorial
- python and json: see https://flask.palletsprojects.com/en/2.1.x/quickstart/#debug-mode => there's a section on json
- SQLAlchemy and Alembic is cool for Python.
  - But what about yoyo ? https://pypi.org/project/yoyo-migrations/
- myapp = Flask(__name__, template_folder="templates")
  - static_url_path=''
  - static_folder='../web')
- @app.route('/users/<id>', methods=['GET'])
- app.run(host='0.0.0.0', port=8080, debug=True)
- try:  except (environs.EnvError, NameError): raise EnvVariablesException("Error with a env name variable")
- validation?
