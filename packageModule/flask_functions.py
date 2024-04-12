from flask import Flask, request
import json

def app_creation():
    app = Flask(__name__)
    return app

def add_new_employee(companyID):
    data = request.get_json()
    print(json_dump(data))
    return "ok", 200

def update_employee(companyID, employeeId):
    data = request.get_json()
    print(json_dump(data))
    return "ok", 200

def json_dump(data):
    return json.dumps(data, indent=4)