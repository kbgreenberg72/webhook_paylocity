import requests

#Default testing data used in the example from paylocity.
new_hire_data = {
    "companyId": "C01",
    "companyName": "Garner Group",
    "employeeAddressLine1": "1060 W Addison St",
    "employeeAddressLine2": "",
    "employeeBadgeClockNumber": "4321"
    "employeeCity": "Chicago",
    "employeeCostCenter1": "11 - Software Development",
    "employeeCostCenter2": "22 - Director 2",
    "employeeCostCenter3": "33 - Team 3",
    "employeeEEOClass": "Software Developer II",
    "employeeFirstName": "Jane",
    "employeeGender": "Female",
    "employeeHireDate": "2015-10-14T00:00:00Z",
    "employeeId": "12345",
    "employeeJobTitle": "Software Developer",
    "employeeLastName": "Doe",
    "employeeMaritalStatus": "Single",
    "employeeMiddleInitial": "R",
    "employeePayFrequency": "B",
    "employeePayType": "Salary",
    "employeePosition": "?",
    "employeeState": "IL",
    "employeeSupervisor": "",
    "employeeSupervisorId": "15",
    "employeeType": "Regular Full Time",
    "employeeWorkEMailAddress": "jdoe@work.com",
    "employeeWorkPhone": "(800) 555-1212",
    "employeeZip": "60613",
    "employeeTaxForm": "W2"
}

#Default testing data used in the example from paylocity
""" You still need to add an get action if you get this to pull the data on the employee.

The following item changes will cause this event to activate
LastName
AddressLine1
EmpStatus
CostCenter1
Phone1
PrimaryPayRate
FirstName
AddressLine2
HireDate
CostCenter2
Phone1Ext
BaseRate
MiddleName
City
TermDate
CostCenter3
Phone2
DefaultHours
Ssn
State
TermReason
EmpType
Phone2Ext
PayFrequency
BirthDate
Zip
RehireDate
Title
Phone3
PayType
Sex
PersonalMobilePhone
EeoClass
Phone3Ext
PrimaryPayRateEffectiveDate
Ethnicity
PersonalEmail
PayGroup
EmailAddress
Salary
MaritalStatus
"""
employee_change_data = {
    "companyId": "C01",
    "employeeId": "12345"
}

#Default testing data used in the example from paylocity.
employee_term_data = {
    "companyId": "C01",
    "employeeCostCenter1": "11 - Software Development",
    "employeeCostCenter2": "22 - Director 2",
    "employeeCostCenter3": "33 - Team 3",
    "employeeFirstName": "Jane",
    "employeeId": "12345",
    "employeeLastName": "Doe",
    "employeeMiddleInitial": "R",
    "employeeWorkEMailAddress": "jdoe@work.com",
    "employeeTerminationDate": "2015-09-30T00:00:00Z",
    
}




url = "http://127.0.0.1:5000/Post/v2/companies/1/employees"

response = requests.post(url, json=new_hire_data)

print(f"Status Code: {response.status_code}")
print(f"Response Test: {response.text}")