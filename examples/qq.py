from pyoauth2 import Client

KEY = ''
SECRET = ''
CALLBACK = ''

client = Client(KEY, SECRET, 
                site='https://graph.qq.com', 
                authorize_url='https://graph.qq.com/oauth2.0/authorize',
                token_url='https://graph.qq.com/oauth2.0/token')

print '-' * 80
authorize_url = client.auth_code.authorize_url(redirect_uri=CALLBACK, 
                    scope='get_user_info,list_album,upload_pic,do_like')
print 'Go to the following link in your browser:'
print authorize_url
print '-' * 80

code = raw_input('Enter the verification code and hit ENTER when you\'re done:')
code = code.strip()
access_token = client.auth_code.get_token(code, redirect_uri=CALLBACK, parse='query')

print 'token', access_token.headers
print access_token.expires_at
