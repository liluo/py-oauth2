from pyoauth2 import Client
from pyoauth2 import AccessToken

KEY = ''
SECRET = ''
CALLBACK = ''

token = ''

client = Client(KEY, SECRET, 
                site='https://api.douban.com', 
                authorize_url='https://www.douban.com/service/auth2/auth',
                token_url='https://www.douban.com/service/auth2/token')

access_token = AccessToken(client, token)

print '-' * 80
ret = access_token.get('/people/%40me', alt='json')
print ret.parsed
