from flask import Flask, request

app = Flask(__name__)

@app.route("/Post/v2/companies/<companyID>/employees", methods=['POST'])
def add_new_employee(companyID):
    data = request.get_json()
    print(data)
    return "ok", 200

@app.route("/Post/v2/companies/<companyID>/employees/<employeeId>", methods=['Post'])
def update_employee(companyID, employeeId):
    data = request.get_json()
    print(data)
    return "ok", 200


def main():
    app.run(port=5000, debug=True)
    
    

if __name__ == '__main__':
    main()