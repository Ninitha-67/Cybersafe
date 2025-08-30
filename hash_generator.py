import hashlib

def generate_hashes(text):
    print(f"\nOriginal Text: {text}")
    print("MD5    :", hashlib.md5(text.encode()).hexdigest())
    print("SHA1   :", hashlib.sha1(text.encode()).hexdigest())
    print("SHA256  :", hashlib.sha256(text.encode()).hexdigest()) 

if __name__ == "__main__":
    print("Script started")
    user_input = input("Enter text to hash: ")
    generate_hashes(user_input)