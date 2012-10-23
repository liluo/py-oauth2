## Installation

pip
``` bash
pip install py-oauth2
```

easy_install
``` bash
easy_install py-oauth2
```

## Warning

if the py-oauth2 version is less than 0.0.5,pls use `import oauth2` instead.

``` python
from oauth2 import Client
```

else

``` python
from pyoauth2 import Client
```

## Usage Examples

#### Demo for Google

``` python
from pyoauth2 import Client

CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URL = ''
SCOPE = ['https://www.googleapis.com/auth/userinfo.profile', 
          'https://www.googleapis.com/auth/userinfo.email',]
SCOPE = ' '.join(SCOPE)

client = Client(CLIENT_ID, CLIENT_SECRET,
                site='https://www.googleapis.com/oauth2/v1',
                authorize_url='https://accounts.google.com/o/oauth2/auth',
                token_url='https://accounts.google.com/o/oauth2/token')

print '-' * 80
authorize_url = client.auth_code.authorize_url(redirect_uri=REDIRECT_URL, 
                                               scope=SCOPE)
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

```

### Demo for Douban

Get access_token

``` python
from pyoauth2 import Client

KEY = ''
SECRET = ''
CALLBACK = ''

client = Client(KEY, SECRET, 
                site='https://api.douban.com', 
                authorize_url='https://www.douban.com/service/auth2/auth',
                token_url='https://www.douban.com/service/auth2/token')

authorize_url = client.auth_code.authorize_url(redirect_uri=CALLBACK, 
                    scope='shuo_basic_w,douban_basic_common')
# got code
access_token = client.auth_code.get_token(code, redirect_uri=CALLBACK)
```

Get data

``` python
ret = access_token.get('/people/%40me', alt='json')
print ret.parsed
```

Upload image

``` python
ret = access_token.post('/shuo/statuses/', 
                        text='content from py-oauth2', 
                        files={ 'image': open('/path/pic.jpg')})
print ret.parsed
```

#### More:

<https://github.com/liluo/py-oauth2/wiki>

[Demo for Google](https://github.com/liluo/py-oauth2/wiki/Google)

[Demo for Douban](https://github.com/liluo/py-oauth2/wiki/Douban)

[Demo for GitHub](https://github.com/liluo/py-oauth2/wiki/GitHub)

[Demo for Weibo](https://github.com/liluo/py-oauth2/wiki/Weibo)

## License

MIT

## Submitting a Pull Request
* Fork the repository.
* Create a topic branch.
* Implement your feature or bug fix.
* Add, commit, and push your changes.
* Submit a pull request.
