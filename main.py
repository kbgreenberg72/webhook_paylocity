from packageModule import flask_functions

#App creation
app = flask_functions.app_creation()

#Routes
@app.route("/Post/v2/companies/<companyID>/employees", methods=['POST'])
def route_new_employee(companyID):
    return flask_functions.add_new_employee(companyID)

@app.route("/Post/v2/companies/<companyID>/employees/<employeeId>", methods=['POST'])
def route_update_employee(companyID, employeeId):
    return flask_functions.update_employee(companyID, employeeId)

#Main Function
def main():
    app.run(port=5000, debug=True)

#Only runs if this file is the main file
if __name__ == '__main__':
    main()