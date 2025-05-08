import bcrypt
import pwinput
import os

DB_FILE = "db.txt"

def load_users():
    users = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            for line in f:
                username, hashed = line.strip().split(" ", 1)
                users[username] = hashed.encode('utf-8')
    return users

def save_user(username, hashed_password):
    with open(DB_FILE, "a") as f:
        f.write(f"{username} {hashed_password.decode('utf-8')}\n")

def create_account():
    users = load_users()
    username = input("Please enter the user name: ").strip()
    if username in users:
        print("Username already exists.")
        return
    password = pwinput.pwinput("Please enter the password: ")
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    save_user(username, hashed)
    print("Your account was successfully created!")

def login():
    users = load_users()
    username = input("Please enter your registered user name: ").strip()
    if username not in users:
        print("Access denied")
        return
    password = pwinput.pwinput("Please enter your password: ")
    if bcrypt.checkpw(password.encode('utf-8'), users[username]):
        print(f"Welcome {username}")
    else:
        print("Access denied")

def main():
    print("Choose (1) to create an account; (2) To login into an existing account:")
    choice = input().strip()
    if choice == "1":
        create_account()
    elif choice == "2":
        login()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
