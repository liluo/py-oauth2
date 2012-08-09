from oauth2 import Client
from oauth2 import AccessToken

KEY = ''
SECRET = ''
CALLBACK = ''

client = Client(KEY, SECRET, 
                site='https://api.douban.com', 
                authorize_url='https://www.douban.com/service/auth2/auth',
                token_url='https://www.douban.com/service/auth2/token')

code = raw_input('Enter the verification code and hit ENTER when you\'re done:')
client.auth_code.get_token(code, redirect_uri=CALLBACK)
access_token = AccessToken(client, code)
print '-' * 80
print 'access token'
print access_token.headers

print '-' * 80
ret = access_token.get('/people/%40me', alt='json')
print ret.parsed
