import json

def main():
    num_accounts = int(input("Inserisci il numero di account: "))
    accounts = []

    for i in range(num_accounts):
        print(f"Inserisci le credenziali per l'account {i + 1}:")
        host = input("Host: ")
        port = input("Porta: ")
        user = input("Utente: ")
        password = input("Password: ")

        account = {
            "HOST": host,
            "PORT": port,
            "USER": user,
            "PASS": password
        }
        accounts.append(account)

    with open('accounts.json', 'w') as f:
        json.dump(accounts, f, indent=4)

    print("Il file accounts.json è stato creato con successo.")

if __name__ == "__main__":
    main()
