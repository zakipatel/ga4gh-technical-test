import sys
import requests

def main():
        if len(sys.argv) < 2:
            print("Please input an ID. For eg. use 3050107579885e1608e6fe50fae3f8d0")
        else:
                arg = sys.argv[1]
                r = requests.get("https://www.ebi.ac.uk/ena/cram/sequence/" + arg + "/metadata")
                if r.status_code == 200:
                        print('Success, status code is: ' + str(r.status_code))
                        response = r.json()
                        metadataString = "METADATA FOR INPUT : " + arg
                        id = "ID: " + response["metadata"]["id"]
                        length = "LENGTH: " + str(response["metadata"]["length"])
                        return_string = metadataString + ' ..... \n' +  '... ' +  id +  '\n... '  + length
                        print(return_string)
                else:
                        print('Error: ' + str(r.status_code))

if __name__ == "__main__":
    main()






