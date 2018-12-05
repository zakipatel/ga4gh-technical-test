
# query the server metadata endpoint
#  The endpoint for the ENA is https://www.ebi.ac.uk/ena/cram/
# and an example sequence ID to use is 3050107579885e1608e6fe50fae3f8d0


import requests
from flask import Flask, flash, redirect, render_template, request, session, abort
import json

app = Flask(__name__)

@app.route("/")
def index():
   return render_template('query_form.html', message='')   # displays the input box for sequence id to the user


@app.route("/query") # /<string:sequence_id>/")
def getSequence():
        user_input = request.args.get('sequence_id')
	r = requests.get("https://www.ebi.ac.uk/ena/cram/sequence/" + user_input + "/metadata")
        if (r.status_code == 200):
                response_data = r.json()
                status = 'success'
                id = response_data["metadata"]["id"]
                md5 = response_data["metadata"]["md5"]
                length = response_data["metadata"]["length"]
                trunc512 = response_data["metadata"]["trunc512"]
                aliases = response_data["metadata"]["aliases"]
                #return_string = "Metadata for Sequence ID: " + id + " ... \n LENGTH is: " + str(length)
                #return return_string
                return render_template('results.html', **locals())
        else:
                message = 'Error Code:  ' + str(r.status_code) + ' \n...  Did not find metadata for input ID'
		return render_template('query_form.html', **locals())

if __name__ == "__main__main":
        app.run()


