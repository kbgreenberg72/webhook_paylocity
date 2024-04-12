# webhook_paylocity
## This is for api request events from paylocity

### Main.py
##### This is the main program that has function calls while the server is running. The functions will eventually go into a module and will be called seperately.
- Stage One: Create a working Webhook Receiver server code.
- Move functions into a module keeping all code in function calls.
- Create a non-proprietary version with no information on our systems.
- All other code will not be published to the public repo.

### packageModule
##### Used to store action functions that are simply called within each other or via the main functions routes. We do not want a hard to read main function and this allows us to keep the program clean.

#### flask_functions.py
##### Used for flask related functions. These handle the json api requests from Paylocity as well as flask related activities. Most of the json manipulation will also occur in these functions.

### test_request.py
##### This is the main program for testing code throughout the deployment of this project.
- Change the json data to match paylocity's layout which is public knowledge on their developer.paylocity.com website.
- Use this for testing code throughout the process.