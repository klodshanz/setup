###############################################################
# Regular Expressions
###############################################################
import re
haystack = file.read()
needle = '<credentialsId>(.*)</credentialsId>'
ids = [matched.group(1) for matched in re.finditer(needle, haystack)]
   
###############################################################
# Generate Random Strings
###############################################################
import secrets
for x in range(15):
   print(f"random hex string : {secrets.token_hex(16)}")

###############################################################
# Date and Time manipulation
###############################################################
import datetime
today_str = '21-02-2020 10:01'
today = datetime.datetime.strptime(today_str, '%d-%m-%Y %H:%M')
now = datetime.datetime.now()
now_pretty = now.strftime("%d-%m-%Y (%H:%M:%S.%f)")

import time
current_time_millis = int(round(time.time() * 1000))

###############################################################
# JSON
###############################################################
import json
json.dumps(response, indent=4, sort_keys=True)
json.dumps(json.loads(response.text), indent=4, sort_keys=True)

###############################################################
# Decorator
###############################################################
def deco(original_function):
    def wrapper():
        print("Code Executing Before")
        original_function()
        print("Code Executing After")
    return wrapper()

@deco
def foo():
    print("This is a decorated function")

foo()
