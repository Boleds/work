import time as sleper
from datetime import datetime
try:
    import requests, os
except ModuleNotFoundError:
    os.system("pip install requests")
import sys

def banner():
 print("""
╦╔═╗  ╔╦╗╔═╗╔═╗╦  ╔═╗
║║ ╦   ║ ║ ║║ ║║  ╚═╗
╩╚═╝   ╩ ╚═╝╚═╝╩═╝╚═╝
                          
IG TOOLS v0.1
----------------------------------------
Gunakan TOOL Dengan Bijak
----------------------------------------
""")
time = int(datetime.now().timestamp())
csrftoken_url = 'https://i.instagram.com/api/v1/public/landing_info/'
csrftoken_headers  = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105 Version/11.1.1 Safari/605.1.15',
    'X-IG-App-ID':'936619743392459',
}
csrftoken_r = requests.get(csrftoken_url,headers=csrftoken_headers).cookies

mid = csrftoken_r['mid']
ig_did = csrftoken_r['ig_did']
csrftoken = csrftoken_r['csrftoken']
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'X-IG-App-ID':'936619743392459',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':f'csrftoken={csrftoken}; ig_did={ig_did}; ig_nrcb=1; mid={mid}',
    'X-CSRFToken':f'{csrftoken}'
}
banner()
username = input('Masukan username : ')
password = input('Masukan password : ')
url = 'https://www.instagram.com/accounts/login/ajax/'
data = f'enc_password=#PWD_INSTAGRAM_BROWSER:0:{time}:{password}&username={username}&queryParams=%7B%7D&optIntoOneTap=false&stopDeletionNonce=&trustedDeviceRecords=%7B%7D'
print('Checking For Login...')
login = requests.post(url,headers=headers,data=data)
if '"authenticated":true,' in login.text:
    sessionid = login.cookies['sessionid']
    csrftoken = login.cookies['csrftoken']
    ds_user_id = login.cookies['ds_user_id']
    rur = login.cookies['rur']
    with open('data/sessionid.txt','a') as f:
        f.write(f'{sessionid}')
    with open('data/csrftoken.txt','a') as f:
        f.write(f'{csrftoken}')
    with open('data/ds_user_id.txt','a') as f:
        f.write(f'{ds_user_id}')
    with open('data/accounts.txt','a') as f:
        f.write(f'{rur}')
    print('login success')
    def clear():
        if "linux" in sys.platform.lower():os.system('clear')
        elif "win" in sys.platform.lower():os.system('cls')
    
    def Unfollow1():
        Total = 0
        Unfollowed = 0
        print('Masukan jumlah unfollow ?')
        count = input('count : ')
        url = f'https://i.instagram.com/api/v1/friendships/{ds_user_id}/follower/?count={count}'
        headers = {
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'X-IG-App-ID':'1217981644879628',
            'Cookie':f'csrftoken={csrftoken}; ds_user_id={ds_user_id}; rur="{rur}"; datr=-rVQY9YiK4ZoYN0PJg0eQIpE; dpr=3; sessionid={sessionid}; shbid="699\05455340585566\0541697769850:01f7b7f145f2538bfb0219970bbb24ae1d9dfb7ca6ef8652b490b71a1e054ae68bf84213"; shbts="1666233850\05455340585566\0541697769850:01f7691e397f9d4a4e64283b0ce19b37bcb109e8e878ff5c557b3b43e266e793e497638d"; ig_did={ig_did}; ig_nrcb=1; mid={mid}',
            'X-CSRFToken':f'{csrftoken}'
        }
        r = requests.get(url,headers=headers).json()
        print(r)
        for users in r['users']:
            Total = Total +1
            id = users['pk']
            username = users['username']
            url = f'https://i.instagram.com/api/v1/web/friendships/{id}/remove_follower/'
            unfollow = requests.post(url,headers=headers)
            print(unfollow.text)
            if '{"status":"ok"}' in unfollow.text:
                Unfollowed = Unfollowed + 1
                print(f'Unfollowed : {username}')
            else:
                print(unfollow.text)
            sleper.sleep(3)
                
            print(f'\rTotal : {count} | Unfollowed :{Unfollowed}',end='')


    def Unfollow2():
        Total = 0
        Unfollowed = 0
        print('Masukan jumlah unfollow ?')
        count = input('count : ')
        url = f'https://i.instagram.com/api/v1/friendships/{ds_user_id}/following/?count={count}'
        headers = {
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'X-IG-App-ID':'1217981644879628',
            'Cookie':f'csrftoken={csrftoken}; ds_user_id={ds_user_id}; rur="{rur}"; datr=-rVQY9YiK4ZoYN0PJg0eQIpE; dpr=3; sessionid={sessionid}; shbid="699\05455340585566\0541697769850:01f7b7f145f2538bfb0219970bbb24ae1d9dfb7ca6ef8652b490b71a1e054ae68bf84213"; shbts="1666233850\05455340585566\0541697769850:01f7691e397f9d4a4e64283b0ce19b37bcb109e8e878ff5c557b3b43e266e793e497638d"; ig_did={ig_did}; ig_nrcb=1; mid={mid}',
            'X-CSRFToken':f'{csrftoken}'
        }
        r = requests.get(url,headers=headers).json()
        for users in r['users']:
            Total = Total +1
            id = users['pk']
            username = users['username']
            url = f'https://i.instagram.com/api/v1/web/friendships/{id}/unfollow/'
            unfollow = requests.post(url,headers=headers)
            if '{"status":"ok"}' in unfollow.text:
                Unfollowed = Unfollowed + 1
                print(f'Unfollowed : {username}')
            else:
                print(unfollow.text)
            sleper.sleep(3)
                
            print(f'\rTotal : {count} | Unfollowed :{Unfollowed}',end='')

    #Deleted Chats
    def DeleteChats():
        url = f'https://i.instagram.com/api/v1/direct_v2/inbox/?persistentBadging=true&folder=&limit=20&thread_message_limit=10'
        headers = {
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'X-IG-App-ID':'1217981644879628',
            'Cookie':f'csrftoken={csrftoken}; ds_user_id={ds_user_id}; rur="{rur}"; datr=-rVQY9YiK4ZoYN0PJg0eQIpE; dpr=3; sessionid={sessionid}; shbid="699\05455340585566\0541697769850:01f7b7f145f2538bfb0219970bbb24ae1d9dfb7ca6ef8652b490b71a1e054ae68bf84213"; shbts="1666233850\05455340585566\0541697769850:01f7691e397f9d4a4e64283b0ce19b37bcb109e8e878ff5c557b3b43e266e793e497638d"; ig_did={ig_did}; ig_nrcb=1; mid={mid}',
            'X-CSRFToken':f'{csrftoken}'
        }
        r = requests.get(url,headers=headers).json()
        Total = 0
        Deleted = 0
        UnDeleted = 0
        for info in r['inbox']['threads']:
            thread = info['thread_id']
            url = f'https://i.instagram.com/api/v1/direct_v2/threads/{thread}/hide/'
            Delete = requests.post(url,headers=headers)
            
            if '{"status":"ok","status_code":"200"}' in Delete.text:
                Deleted = Deleted + 1
                
            else:
                UnDeleted = UnDeleted +1
            print(f'\rDeleted {Deleted} | UnDeleted {UnDeleted}',end='')
    def DeletePosts():
        Deleted = 0
        headers = {
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'X-IG-App-ID':'1217981644879628',
            'Cookie':f'csrftoken={csrftoken}; ds_user_id={ds_user_id}; rur="{rur}"; datr=-rVQY9YiK4ZoYN0PJg0eQIpE; dpr=3; sessionid={sessionid}; shbid="699\05455340585566\0541697769850:01f7b7f145f2538bfb0219970bbb24ae1d9dfb7ca6ef8652b490b71a1e054ae68bf84213"; shbts="1666233850\05455340585566\0541697769850:01f7691e397f9d4a4e64283b0ce19b37bcb109e8e878ff5c557b3b43e266e793e497638d"; ig_did={ig_did}; ig_nrcb=1; mid={mid}',
            'X-CSRFToken':f'{csrftoken}',
            'Content-Type':'application/x-www-form-urlencoded'
        }
        url = f'https://i.instagram.com/api/v1/feed/user/{username}/username/?count=12'
        r = requests.get(url,headers=headers).json()
        for data in r['items']:
            Deleted = Deleted + 1
            pk = data['pk']
            url = f'https://i.instagram.com/api/v1/web/create/{pk}/delete/'
            r = requests.post(url,headers=headers)
            if 'did_delete":true' in r.text:
                print(f'Deleting.. {Deleted}',end='')
    def menu():
        clear()
        banner()
        print('-'*40)
        print(f'[1]Unfollow-Follower(error/sedang perbaikan)\n[2]Unfollow-Following\n[3]Delete Chats\n[4]Delete All Posts\n[x]Exit')
        print('-'*40)
    while True:
        print('\n')
        menu()
        mood = input('Pilih : ')
        if mood == '1':
            Unfollow1()
        elif mood == '2':
            Unfollow2()
        elif mood == '3':
            DeleteChats()
        elif mood == '4':
            DeletePosts()
        else:
            break
    
elif '"authenticated":false,' in login.text:
    print('faild to login')
elif 'checkpoint_required' in login.text:
    print('Your Account Secure or suspended')
else:
    print(login.text)

if __name__ == '__main__':
     menu()
