# 🔐 Secure Password Manager (CLI - Local Vault)

A simple interactive command-line password manager written in Python that securely encrypts and stores your credentials using Fernet symmetric encryption.

## 🚀 Features

- 🔐 Master password protected
- 🧠 Credentials stored locally in encrypted `vault.json`
- 🔒 Uses strong AES-128 encryption with Fernet
- 🧪 Interactive CLI for adding, viewing, and listing credentials

## 🛠 Requirements

- Python 3.7+
- `cryptography` library

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/umandalroald/password-manager.git
cd password-manager
```

2. **Set up a virtual environment (recommended)**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

## 🧪 Usage

Run the app:

```bash
python main.py
```

You’ll be prompted to enter your master password. You can then:

- Add new credentials
- View stored credentials
- List all stored sites

## 📁 File Structure

```
password-manager/
├── main.py
├── utils/
│   └── crypto.py
├── vault.json        # Encrypted credentials (ignored by .gitignore)
├── salt.bin          # Salt used for key derivation (ignored)
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚠️ Security Notes

- Do **not** share your `vault.json` or `salt.bin` publicly.
- If you forget your master password, you **cannot** recover encrypted data.
- Store a backup of your `salt.bin` file if you're using across multiple devices.

## 📄 License

MIT License.