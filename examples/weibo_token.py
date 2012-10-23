from pyoauth2 import Client
from pyoauth2 import AccessToken

KEY = ''
SECRET = ''
CALLBACK = ''

client = Client(KEY, SECRET, site='https://api.weibo.com', 
                authorize_url='/oauth2/authorize',
                token_url='/oauth2/access_token')

code = raw_input('Enter the verification code and hit ENTER when you\'re done:')
client.auth_code.get_token(code, redirect_uri=CALLBACK)
access_token = AccessToken(client, code)

print access_token.get('/2/statuses/public_timeline.json', access_token=access_token.token).parsed
