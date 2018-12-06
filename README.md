#### READ ME - Flask MiniApp Client 

Check version of Python
`$python --version`

Next, install the dependencies i.e. requests, flask
`$pip install requirements`

Set the following: 
`$export FLASK_APP=miniapp.py`

Next:   
`$flask run`   # https://pythonspot.com/flask-web-app-with-python/

Now, open a browser
- Go to http://127.0.0.1:5000 . This should display a form with one input field
- Enter a sequence ID, run the query, view the response meta-data or error message
- For example,use reference sequence ID 3050107579885e1608e6fe50fae3f8d0 OR 6681ac2f62509cfc220d78751b8dc524

<hr> 

If you are using a virtual environment, follow steps below: 

`$ pip install virtualenv`

`$ virtualenv --version`

`$git clone the_repository`

`$cd into the cloned repo`

Initialize a venv for the project
`$ virtualenv venv`    

Activate the venv
`$source venv/bin/activate`   

Then install dependencies, specify the flask app entry point and run the app 
`(venv)$pip install requirements`

`(venv)$export FLASK_APP=miniapp.py`

`(venv)$flask run` 

Now, open a browser
- Go to http://127.0.0.1:5000 
- Enter a sequence ID, run the query, view the response meta-data or error message
- For example,use reference sequence ID 3050107579885e1608e6fe50fae3f8d0 OR 6681ac2f62509cfc220d78751b8dc524

