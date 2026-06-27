# PRIVATE, PUBLIC ATTRIBUTES
from datetime import datetime
class Account:
    @staticmethod
    def create_account():
        try: 
            name = input("Enter Your Name: ").strip().title()
            email = input("Enter Your Email: ").lower()
            dob = input("Enter Your Date of Birth: ")
            __passwd = input("Enter Your Password: ")
            __confirm_passwd = input("Enter Again Password: ")
            if __passwd != __confirm_passwd:
                print("Password not match!")
            
            user_data = {
                "Account Creation Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": name,
                "Email": email,
                "Date of Birth": dob,
                "Password" : __passwd
            }
            
            print({k: v for k, v in user_data.items() if k != "Password"})
        except Exception as e:
            print(e)

user1 = Account()
user1.create_account()
