# 🛡️ Cybersafe – Beginner Cybersecurity Toolkit  

## 📌 Overview  
**Cybersafe** is a beginner-friendly cybersecurity project that brings together simple yet powerful tools for security awareness and testing.  
It’s designed to help students and beginners understand how basic cybersecurity checks work, all in one toolkit.  

## ✨ Features  
- 🔍 **Port Scanner** → Check open ports on a host or IP  
- 🔑 **Password Strength Checker** → Validate password strength using rules  
- 🔐 **Hash Generator & Verifier** → Generate and compare hashes (MD5, SHA256, etc.)  
- 📧 **Email Validator** → Check if an email address format is valid  
- 🌐 **IP Information Lookup** → Get geolocation & ISP details of an IP  
- 📡 **WiFi Network Info** → View saved WiFi profiles (Windows only)  

---

## ⚙️ Installation  

### 1. Clone the repository:  
```bash
   git clone https://github.com/Ninitha-67/Cybersafe.git
   cd Cybersafe
```
### 2.Create a virtual environment (recommended):
```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3.Install dependencies (if any):
```
pip install -r requirements.txt
```
---

## ▶️ Usage
## 1. Run Port Scanner
```
python port_scanner.py
```

Example:

```
Enter target IP or hostnames: localhost
```
### 2. Run Password Strength Checker
```
python password_check.py
```
### 3. Run Hash Generator
```
python hash_tool.py
```
### 4. Run Email Validator
```
python email_validator.py
```
### 5. Run IP Lookup
```
python ip_lookup.py
```
### 6. Run WiFi Info Viewer (Windows only)
```
python wifi_info.py
```
---

## 📂 Project Structure
```
Cybersafe/
│── port_scanner.py        # Scan open ports on target
│── password_check.py      # Password strength validation
│── hash_tool.py           # Hash generator and verifier
│── email_validator.py     # Email address format check
│── ip_lookup.py           # IP address info lookup
│── wifi_info.py           # Show saved WiFi networks
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```
---
## 🛠️ Tech Stack

Python 3 🐍

Socket, hashlib, re, requests libraries

---

## ⚠️ Disclaimer

This project is for educational purposes only.
Do NOT use these scripts on systems or networks without permission.
The author is not responsible for any misuse of this toolkit.

---

## 🤝 Contribution

Pull requests are welcome! Feel free to fork and improve this toolkit.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

Ninitha P

----
