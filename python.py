# Generate Random Strings
import secrets
for x in range(15):
   print(f"random hex string : {secrets.token_hex(16)}")

# Date and Time manipulation
import datetime
today_str = '21-02-2020 10:01'
today = datetime.strptime(today_str, '%d-%m-%Y %H:%M')

