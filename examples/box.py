from pyoauth2 import Client

KEY = ''
SECRET = ''
CALLBACK = ''

client = Client(KEY, SECRET, 
                site='https://api.box.com/2.0', 
                authorize_url='https://api.box.com/oauth2/authorize',
                token_url='https://api.box.com/oauth2/token')

print '-' * 80
authorize_url = client.auth_code.authorize_url(redirect_uri=CALLBACK)
print 'Go to the following link in your browser:'
print authorize_url
print '-' * 80

code = raw_input('Enter the verification code and hit ENTER when you\'re done:')
code = code.strip()
access_token = client.auth_code.get_token(code, redirect_uri=CALLBACK)
print 'token', access_token.headers

print '-' * 80
ret = access_token.get('/folders/0')
print ret.parsed
