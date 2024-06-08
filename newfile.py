import requests
import random
import os
from user_agent import generate_user_agent
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
#os.system('pip install telebot')
#os.system('pip install random')
#os.system('pip install requests')
#os.system('clear')
token1 = '7494457262:AAE6CVZx9z7UCHR0IuCaLlodadu-pfAGTQ8'

id1 = '1761998181'

token = input('your token : ')
ID = input('your id : ')
os.system('clear')   
def check():
    while True:
              ss = '1234567890qwertyuiipoasdfghjklmnbvcxz'
              bb='ss','rr','bb','oo','jj','gg','aa','cc','dd','ee','ff','hh','ii','kk','ll','mm','nn','pp','qq','tt','uu','vv','ww','xx','yy','zz'
              
              mm = '_','.'
              soha = ''.join((random.choice(ss)) for i in (range(2)))
              
              soha2 = ''.join((random.choice(ss)) for i in (range(2)))
              soha3 = ''.join((random.choice(mm)) for i in (range(1)))
              
              
             # user1 = soha2+ '_' +soha
              user = soha +soha3 +soha2
            #  user=random.choice(user1+user2)
 

              cookies = {
    'ps_n': '1',
    'ps_l': '1',
    'mid': 'ZlCmcwABAAGZbfEkot8TcDlF4r7u',
    'ig_did': '34018F83-DC5F-4E66-850B-8B6F8B10287D',
    'datr': 'c6ZQZhuPD68iCVXAi19YL9Jr',
    'ig_nrcb': '1',
    'dpr': '2.3014395236968994',
    'shbid': '"10379\\05461313259630\\0541749255115:01f7cd06c7341a2f8c77c0209f8914255498828f4e4068382271d0d781376f84ea9a2af4"',
    'shbts': '"1717719115\\05461313259630\\0541749255115:01f77b31e42965fb3b25fb9315400ac6852859a0e463138e5b247deadda47695ab4b7f52"',
    'rur': '"ODN\\05461313259630\\0541749256287:01f7a7eaee7cfa2d34039fd7a1564b086b979f2d4fbea77164cc4639eb76ba60ece77c92"',
    'csrftoken': 'PKyWu9OEzglkPKlD2vfITIIui5rKnGcF',
    'wd': '313x632',
}
              headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'ar-LY,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'ps_n=1; ps_l=1; mid=ZlCmcwABAAGZbfEkot8TcDlF4r7u; ig_did=34018F83-DC5F-4E66-850B-8B6F8B10287D; datr=c6ZQZhuPD68iCVXAi19YL9Jr; ig_nrcb=1; dpr=2.3014395236968994; shbid="10379\\05461313259630\\0541749255115:01f7cd06c7341a2f8c77c0209f8914255498828f4e4068382271d0d781376f84ea9a2af4"; shbts="1717719115\\05461313259630\\0541749255115:01f77b31e42965fb3b25fb9315400ac6852859a0e463138e5b247deadda47695ab4b7f52"; rur="ODN\\05461313259630\\0541749256287:01f7a7eaee7cfa2d34039fd7a1564b086b979f2d4fbea77164cc4639eb76ba60ece77c92"; csrftoken=PKyWu9OEzglkPKlD2vfITIIui5rKnGcF; wd=313x632',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/signup/username/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X688B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': str(generate_user_agent()),
    'x-asbd-id': '129477',
    'x-csrftoken': 'PKyWu9OEzglkPKlD2vfITIIui5rKnGcF',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': 'hmac.AR35_mqB9N606TsZqcB1ItjErWEtT8LUyXtAv8UIoWnMQoyG',
    'x-instagram-ajax': '1014040072',
    'x-requested-with': 'XMLHttpRequest'
}
              data = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1717720514:AetQAOhb1pmX4lvDJhGZYy68ENeUHMh5xy2qbcA/o8GfMrQ9JqHJoj0EC11iCf+adseX/An4fpdCHOsLce/4LxVA85U1k2KWhRWi4M3zI2zcexn07UM3hatp7kWhyprNTxjJ8Pd2nmnhQ0YKenI=',
    'day': '15',
    'email': '',
    'first_name': 'lbwzydy6094',
    'month': '8',
    'username': user,
    'year': '1962',
    'client_id': 'e9q5x0134yvkixotpu61dj5enb1s8yp889i09xu14i68l81gisdbr',
    'seamless_login_enabled': '1',
    'tos_version': 'row',
    'force_sign_up_code': 'NtmTCp76',
}

              response = requests.post(
    'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
    cookies=cookies,
    headers=headers,
    data=data,
).text

     
              if 'code": "username_is_taken' not in response:
               print(f'{F}GOOD USER : {user}')
               ff = f'''
        ࿕┈┉━ ᯓ 𓆩🫶🏻𝙷𝙸𝚃🫶🏻 𓆪 ᯓ ━┅┄࿕
        「❃」𝗨𝗘𝗦𝗥 ✓👉     {user}
        ࿕┈┉━ ᯓ 𓆩 🫶🏻𝙷𝙸𝚃🫶🏻 𓆪 ᯓ ━┅┄࿕
        ⊊𝗕𝗬⊋ @BYPASS_vip'''

               requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}')
               requests.post(f'https://api.telegram.org/bot{token1}/sendMessage?chat_id={id1}&text={ff}')
                
              else:
                
                print(f'{Z}BAD USER : {user}')
check()