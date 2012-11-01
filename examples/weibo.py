from pyoauth2 import Client

KEY = ''
SECRET = ''
CALLBACK = ''

client = Client(KEY, SECRET, 
                site='https://api.weibo.com', 
                authorize_url='/oauth2/authorize',
                token_url='/oauth2/access_token')

print '-' * 80
authorize_url = client.auth_code.authorize_url(redirect_uri=CALLBACK)
print 'Go to the following link in your browser:'
print authorize_url

code = raw_input('Enter the verification code and hit ENTER when you\'re done:')
code = code.strip()
access_token = client.auth_code.get_token(code, redirect_uri=CALLBACK, header_format='OAuth2 %s')
print 'token', access_token.headers

ret = access_token.get('/2/statuses/public_timeline.json')
print '-' * 80
print 'get public timeline' 
print ret.body

print '-' * 80
print 'post miniblog...'
ret = access_token.post('/2/statuses/update.json', status='now')
print ret.body
