from flask import Flask, request

app = Flask(__name__)

@app.route(f"/Post/v2/companies/{companyID}/employees", methods=['Post'])
def add_new_employee():
    data = request.get_json()
    print(data)
    return "ok", 200

@app.route(f"/Post/v2/companies/{companyID}/employees/{employeeId}", methods=['Post'])
def update_employee():
    data = request.get_json()
    print(data)
    return "ok", 200


def main():
    app.run(port=5000)
    
    

if __name__ == '__main__':
    main()