import json
import os
import getpass
from utils.crypto import generate_salt, generate_key, encrypt_data, decrypt_data

VAULT_FILE = 'vault.json'
SALT_FILE = 'salt.bin'

def load_salt():
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, 'rb') as f:
            return f.read()
    else:
        salt = generate_salt()
        with open(SALT_FILE, 'wb') as f:
            f.write(salt)
        return salt

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return {}
    with open(VAULT_FILE, 'r') as f:
        return json.load(f)

def save_vault(vault):
    with open(VAULT_FILE, 'w') as f:
        json.dump(vault, f)

def add_credential(vault, key):
    site = input("Enter site name: ").strip()
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password (hidden): ").strip()

    entry = {
        "username": encrypt_data(username, key).decode(),
        "password": encrypt_data(password, key).decode()
    }
    vault[site] = entry
    save_vault(vault)
    print(f"✅ Credential for '{site}' saved!")

def view_credential(vault, key):
    site = input("Enter site name to retrieve: ").strip()
    if site in vault:
        entry = vault[site]
        try:
            username = decrypt_data(entry["username"].encode(), key)
            password = decrypt_data(entry["password"].encode(), key)
            print(f"\n🔐 {site} Credentials:")
            print(f"Username: {username}")
            print(f"Password: {password}")
        except Exception:
            print("❌ Incorrect master password or corrupted data.")
    else:
        print("⚠️ Site not found in vault.")

def list_sites(vault):
    print("\n📁 Stored Sites:")
    for site in vault.keys():
        print(f"- {site}")
    print()

def main():
    print("🔐 Welcome to Your Secure Password Manager")

    master_password = getpass.getpass("Enter your master password: ").strip()
    salt = load_salt()
    key = generate_key(master_password, salt)

    vault = load_vault()

    while True:
        print("\n📋 Options:")
        print("[1] Add new credential")
        print("[2] View credential")
        print("[3] List stored sites")
        print("[4] Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_credential(vault, key)
        elif choice == "2":
            view_credential(vault, key)
        elif choice == "3":
            list_sites(vault)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
