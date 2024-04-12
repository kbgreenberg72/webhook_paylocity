from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/Post/v2/companies/<companyID>/employees", methods=['POST'])
def add_new_employee(companyID):
    data = request.get_json()
    print(json_dump(data))
    return "ok", 200

@app.route("/Post/v2/companies/<companyID>/employees/<employeeId>", methods=['POST'])
def update_employee(companyID, employeeId):
    data = request.get_json()
    print(json_dump(data))
    return "ok", 200

def json_dump(data):
    return json.dumps(data, indent=4)


def main():
    app.run(port=5000, debug=True)
    
    

if __name__ == '__main__':
    main()