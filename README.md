## READ ME

### This repository contains a python3 client that allows a user to query the ENA metadata endpoint given a sequence ID

- The endpoint for the ENA is https://www.ebi.ac.uk/ena/cram/
- The ENA CRAM archive is a refget API server instance. 

### There are 2 branches in this repository:

#### command-line-client : contains a basic python client that a user can run from the command-line

`$git clone this_repository`

`$cd this_repository`

`$git checkout command-line-client`

`$python client.py <sequence_id> # eg. 3050107579885e1608e6fe50fae3f8d0 or 6681ac2f62509cfc220d78751b8dc524` 


#### flask-miniapp-client : contains a simple web app with a form that user can run from a browser

`$git checkout flask-miniapp-client`

`$pip install requirements`

`$export FLASK_APP=miniapp.py`

`$flask run`

For more details on how to use each client, please see the README for the respective branch
