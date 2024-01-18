from flask import Flask, jsonify, request
import time
import random


app = Flask(__name__)

@app.route('/extract-act-frame', methods=['POST'])
def data_process():
    
    validate_request(request)
    response = {
        "Action": "grant",
        "Actor": "Minister of Justice and Security",
        "Object": "application to provide a temporary regular residence permit",
        "Recipient": "alien",
        "Preconditions": [
            {
                "AND": [
                    {"condition": "regular residence permit is granted from the day on which the alien has demonstrated that he meets all conditions"},
                    {"NOT": "residence permit granted earlier than from the day on which the application was received"},
                    {"NOT": "alien has a travel ban or has been signaled for the purpose of refusing entry"},
                    {"NOT": "alien has pronouncement of undesirability"}
                ]
            }
        ],
        "Creating_postcondition": [
            "decision to grant an application to provide a temporary regular residence permit",
            "granting a temporary regular residence permit under restrictions",
            "determine the period of validity of the regular residence permit",
            "provide the alien with a document proving lawful residence"
        ],
        "Terminating_postcondition": [
            "application to provide a temporary regular residence permit"
        ],
        "References_to_sources": [
            "Art. 14 (1) Aliens Act, main clause and under (a)"
        ]
    }
    # wait for 5 - 10 seconds to mimic processing time
    return jsonify(response)

def validate_request(request):
     # Check if the request data is JSON
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    # Get JSON data from request
    data = request.get_json()

    # Check if the JSON data contains only one key and the value is a string
    if len(data) == 1 and isinstance(list(data.values())[0], str):
        # if key is debug, wait for 5 - 10 seconds
        if "debug" in data.keys():
            if data["debug"] == "true":
                return
        else:
            time.sleep(random.randint(5, 10))
            return
    else:
        return jsonify({"error": "Request JSON must contain exactly one key with a string value"}), 400


if __name__ == '__main__':
    app.run(debug=True)
