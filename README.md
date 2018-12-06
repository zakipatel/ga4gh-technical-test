### READ ME

This repository contains a python3 client that allows a user to query the ENA metadata endpoint for given a reference sequence ID. The ENA CRAM archive is a refget API server instance. The endpoint for the ENA is https://www.ebi.ac.uk/ena/cram/- 

There are 2 branches in this repository:

##### 1. command-line-client : contains a basic python client that a user can run from the command-line

To use this client, check out this branch:

`$git clone this_repository`

`$cd this_repository`

`$git checkout command-line-client`

And then run the following commands:

`$python client.py <sequence_id> # eg. 3050107579885e1608e6fe50fae3f8d0 or 6681ac2f62509cfc220d78751b8dc524` 


##### 2. flask-miniapp-client : contains a simple web app with a form that user can run from a browser

To use this client, check out this branch:

`$git checkout flask-miniapp-client`

And then run the following commands:

`$pip install requirements`

`$export FLASK_APP=miniapp.py`

`$flask run`

For more details on how to use each client, please see the README for the respective branch
