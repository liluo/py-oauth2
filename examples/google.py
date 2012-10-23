from pyoauth2 import Client

CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URL = ''
SCOPE = 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email'

client = Client(CLIENT_ID, CLIENT_SECRET,
                site='https://www.googleapis.com/oauth2/v1',
                authorize_url='https://accounts.google.com/o/oauth2/auth',
                token_url='https://accounts.google.com/o/oauth2/token')

print '-' * 80
authorize_url = client.auth_code.authorize_url(redirect_uri=REDIRECT_URL, scope=SCOPE)
print 'Go to the following link in your browser:'
print authorize_url

code = raw_input('Enter the verification code and hit ENTER when you\'re done:')
code = code.strip()
access_token = client.auth_code.get_token(code, redirect_uri=REDIRECT_URL)
print 'token', access_token.headers

print '-' * 80
print 'get user info' 
ret = access_token.get('/userinfo')
print ret.parsed
