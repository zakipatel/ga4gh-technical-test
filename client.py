import sys
import requests

def main():
	try:
		print("---"*50)
		if len(sys.argv) < 2:
			print("Please input an argument specifying the sequence ID. For eg. python client.py 3050107579885e1608e6fe50fae3f8d0")
		else:
			arg = sys.argv[1]
			print(".....Getting metadata for input sequence id : " + str(arg) + " from https://www.ebi.ac.uk/ena/cram")
			try:
				r = requests.get("https://www.ebi.ac.uk/ena/cram/sequence/" + arg + "/metadata")
				r.raise_for_status()
				#if r.status_code == 200:
				print('.....Success, status code is: ' + str(r.status_code))
				print('**'*10 + '  METADATA  ' + '**'*10)
				response = r.json()
				id = "ID: " + response["metadata"]["id"]
				length = "LENGTH....... " + str(response["metadata"]["length"])
				md5 = "MD5..........  " + str(response["metadata"]["md5"]) 
				trunc512 = "TRUNC512..........  " + str(response["metadata"]["trunc512"]) 
				aliases = "ALIASES..........  " + str(response["metadata"]["aliases"])
				return_string = '... ' +  id +  '\n... '  + length + '\n... ' + trunc512 + '\n... ' + aliases
				if len(sys.argv) == 3 and sys.argv[2] == 'json':
					print(r.text)								
					print('*'*52)
				else:
					print(return_string)
					print('*'*52)
			except requests.exceptions.HTTPError as errh:
				print (".....ERROR: Sorry, the API  did not return any metadata record for the input sequence ID " + arg + ".The EBI ENA CRAM API returned the following error message:\n .......",errh)
			except requests.exceptions.ConnectionError as errc:
				print ("Error Connecting:",errc)
			except requests.exceptions.Timeout as errt:
				print ("Timeout Error:",errt)
			except requests.exceptions.RequestException as err:
				print ("OOps: Something Else",err)
		print("---"*50)
	except:
		print("An error occured") #should I also sys.exit(1) after this?

if __name__ == "__main__":
	try:
		main()
	except exceptions as eer:
		print(eer)




