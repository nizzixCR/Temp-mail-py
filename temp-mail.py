import nizzix.temp_mail
import nizzix.temp_org
import time  

def create_temp_email():
    temp_email = nizzix.temp_org.TempMail()
    email_address = temp_email.get_new_email()
    print(f"Votre adresse email temporaire est : {email_address}")
    
    return temp_email, email_address  

def check_messages(temp_email, email_address):
    while True:
        messages = temp_email.get_mails()
        print(messages)
        
        time.sleep(5)

def main():
    temp_email, email_address = create_temp_email()
    check_messages(temp_email, email_address)

if __name__ == "__main__":
    main()
