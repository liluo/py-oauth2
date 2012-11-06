from pyoauth2 import Client
from pyoauth2 import AccessToken

KEY = ''
SECRET = ''
CALLBACK = ''

user_email = ''
user_password = ''

client = Client(KEY, SECRET, 
                site='https://api.douban.com', 
                authorize_url='https://www.douban.com/service/auth2/auth',
                token_url='https://www.douban.com/service/auth2/token')

access_token = client.password.get_token(user_email, user_password)

print '-' * 80
ret = access_token.get('/v2/user/~me')
print ret.parsed
