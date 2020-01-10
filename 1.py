import random
import pycurl
import smtplib, ssl
from io import BytesIO
import pyfiglet
import terminal_banner
a=pyfiglet.figlet_format("BORING")
b=terminal_banner.Banner(a)
print(b)



print("Select one of the options: \n")
list1={"1":"1.Birthday","2":"2.Good Night","3":"3.Anniversery","4":"4.Good Morning","5":"5.Weather"}
for key,value in list1.items():
    print(value)

print("\nenter one of the hai!!")
users=str(input("\nWhat is your choice :\n"))
if users==str("birthday") or users=="1" or users==str("Birthday") or users==str("bornday"):
    a=random.choice(list(open('birthday.txt')))
    print(terminal_banner.Banner(a))
    

    #send via email
    print("If You want to send is as email then type 'Y' for yes and 'N' for no" )
    email=input()
    if email=="yes"or email=='y' or email=='Y'or email=='Yes' or email=='YES':

        smtp_server = "smtp.gmail.com"
        port = 587  # For starttls
        sender_email =input("Sender email: ")
        receiver_email=input("Receiver email: ")
        password = input("Type sender password and press enter: ")

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            with smtplib.SMTP(smtp_server, port,) as server:
                server.ehlo() # Can be omitted
                server.starttls(context=context) # Secure the connection
                server.ehlo() # Can be omitted
                server.login(sender_email, password)
                print("Login success!!")
                server.sendmail(sender_email,receiver_email,a)
                print("Email has been recieved by receiver.")
                # TODO: Send email here
        except Exception as e:
            print("Login failed. Something went wrong!!!")

    else :
        print("Opps!!It seems you don't wanna send it.")
        
    





#Goodnight part

if users=="goodnight"or users=="2"or users=="w" or users=="GoodNight" or users=="Gn" or users=="gn" or users=="Goodnight":
    b=(random.choice(list(open('goodnight.txt'))))
    print(terminal_banner.Banner(b))


   #send via email
    print("If You want to send is as email then type 'Y' for yes and 'N' for no" )
    email=input()
    if email=="yes"or email=='y' or email=='Y'or email=='Yes' or email=='YES':

        smtp_server = "smtp.gmail.com"
        port = 587  # For starttls
        sender_email =input("Sender email: ")
        receiver_email=input("Receiver email: ")
        password = input("Type sender password and press enter: ")

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
          with smtplib.SMTP(smtp_server, port,) as server:
                server.ehlo() # Can be omitted
                server.starttls(context=context) # Secure the connection
                server.ehlo() # Can be omitted
                server.login(sender_email, password)
                print("Login success!!")
                server.sendmail(sender_email,receiver_email,b)
                print("Email has been recieved by receiver.")
                # TODO: Send email here
        except Exception as e:
            print("Login failed. Something went wrong!!!")

    else :
        print("Opps!!It seems you don't wanna send it.")

      


#Anniversay Part
if users=="anniversary" or users=="3" or users=="Anniversary" or users=="ANNIVERSARY":
    c=(random.choice(list(open('anniversary.txt'))))
    print(terminal_banner.Banner(c))

   #send via email
    print("If You want to send is as email then type 'Y' for yes and 'N' for no" )
    email=input()
    if email=="yes"or email=='y' or email=='Y'or email=='Yes' or email=='YES':

        smtp_server = "smtp.gmail.com"
        port = 587  # For starttls
        sender_email =input("Sender email: ")
        receiver_email=input("Receiver email: ")
        password = input("Type sender password and press enter: ")

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
          with smtplib.SMTP(smtp_server, port,) as server:
                server.ehlo() # Can be omitted
                server.starttls(context=context) # Secure the connection
                server.ehlo() # Can be omitted
                server.login(sender_email, password)
                print("Login success!!")
                server.sendmail(sender_email,receiver_email,c)
                print("Email has been recieved by receiver.")
                # TODO: Send email here
        except Exception as e:
            print("Login failed. Something went wrong!!!")

    else :
        print("Opps!!It seems you don't wanna send it.")










#Good morning part
if users=="goodmorning" or users=="4" or users=="Goodmorning" or users=="GM" or users=="gm" or users=="Gm" or users=="GOODMORNING" or users=="good morning":
    d=(random.choice(list(open('goodmorning.txt'))))
    print(terminal_banner.Banner(d))



   #send via email
    print("If You want to send is as email then type 'Y' for yes and 'N' for no" )
    email=input()
    if email=="yes"or email=='y' or email=='Y'or email=='Yes' or email=='YES':

        smtp_server = "smtp.gmail.com"
        port = 587  # For starttls
        sender_email =input("Sender email: ")
        receiver_email=input("Receiver email: ")
        password = input("Type Sender password and press enter: ")

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
          with smtplib.SMTP(smtp_server, port,) as server:
                server.ehlo() # Can be omitted
                server.starttls(context=context) # Secure the connection
                server.ehlo() # Can be omitted
                server.login(sender_email, password)
                print("Login success!!")
                server.sendmail(sender_email,receiver_email,d)
                print("Email has been recieved by receiver.")
                # TODO: Send email here
        except Exception as e:
            print("Login failed. Something went wrong!!!")

    else :
        print("Opps!!It seems you don't wanna send it.")











#weather part
if users=="weather" or users=="5" or users=="Weather" :
  
    b_obj = BytesIO() 
    crl = pycurl.Curl() 

    print("what is your country?\n")
    user=input()   
    # Set URL value
    crl.setopt(crl.URL, 'https://wttr.in/' + user)

    # Write bytes that are utf-8 encoded
    crl.setopt(crl.WRITEDATA, b_obj)

    # Perform a file transfer 
    crl.perform() 

    # End curl session
    crl.close()

    # Get the content stored in the BytesIO object (in byte characters) 
    get_body = b_obj.getvalue()

    # Decode the bytes stored in get_body to HTML and print the result 
    print('Output of GET request:\n%s' % get_body.decode('utf8')) 
