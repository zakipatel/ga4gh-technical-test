# literate-waffle


###First, make sure you are using  python3

$python --version

To make python3 the default, set alias python='python3' in bash profile


###Next, install the dependencies i.e. requests, flask
$pip install requirements

###Followed by: 
$export FLASK_APP=miniapp.py


###And then: 
$flask run 

Go to http://127.0.0.1:5000 
Enter a sequence ID, run the query, view the meta-data. 
For example,use :  3050107579885e1608e6fe50fae3f8d0 OR 6681ac2f62509cfc220d78751b8dc524



###If you are using a virtual environment, follow steps below: 

For details, see: https://docs.python-guide.org/dev/virtualenvs/#virtualenvironments-ref

####
$ pip install virtualenv
$ virtualenv --version
Tested on 16.0.6

####
$git clone the_repository
$cd into the cloned repo
$ virtualenv venv
will create a venv folder

#### Next, activate the venv
$source venv/bin/activate

### Then:
(venv)$pip install requirements
(venv)$export FLASK_APP=hello.py
(venv)$flask run 

Go to 127.0.0.1:5000 will load up a form 
Enter a sequence ID, run the query, view the meta-data. 


