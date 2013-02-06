from pyoauth2 import Client

CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URL = ''

client = Client(CLIENT_ID, CLIENT_SECRET, 
                site='https://api.instagram.com',
                authorize_url='/oauth/authorize',
                token_url='/oauth/access_token')

authorize_url = client.auth_code.authorize_url(redirect_uri=REDIRECT_URL)

print 'Go to the following link in your browser:'
print authorize_url
print '-' * 80

code = raw_input('Enter the verification code and hit ENTER when you\'re done:')
code = code.strip()
access_token = client.auth_code.get_token(code, redirect_uri=REDIRECT_URL)

print 'token', access_token.headers
print 'params', access_token.params
