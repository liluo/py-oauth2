from pyoauth2 import Client

KEY = ''
SECRET = ''
CALLBACK = ''

client = Client(KEY, SECRET,
                site='https://api.github.com',
                authorize_url='https://github.com/login/oauth/authorize',
                token_url='https://github.com/login/oauth/access_token')

print '-' * 80
authorize_url = client.auth_code.authorize_url(redirect_uri=CALLBACK, scope='user,public_repo')
print 'Go to the following link in your browser:'
print authorize_url
print '-' * 80

code = raw_input('Enter the verification code and hit ENTER when you\'re done:')
code = code.strip()
access_token = client.auth_code.get_token(code, redirect_uri=CALLBACK, parse='query')
print 'token', access_token.headers

print '-' * 80
print 'get user info'
ret = access_token.get('/user')
print ret.parsed

print '-' * 80
print 'create a repos'
ret = access_token.post('/user/repos', name='test_repo', headers={'content-type': 'application/json'})
print ret.parsed
