py-oauth2
=========

#### A Python wrapper for the OAuth 2.0 specification

## Installation

``` bash
easy_install py-oauth2
```

## Usage Examples

Get access_token

``` python
from oauth2 import Client

KEY = ''
SECRET = ''
CALLBACK = ''

client = Client(KEY, SECRET, 
                site='https://api.douban.com', 
                authorize_url='https://www.douban.com/service/auth2/auth',
                token_url='https://www.douban.com/service/auth2/token')

authorize_url = client.auth_code.authorize_url(redirect_uri=CALLBACK, scope='shuo_basic_w,douban_basic_common')

......

access_token = client.auth_code.get_token(code, redirect_uri=CALLBACK)
```

Get data

``` python
ret = access_token.get('/people/%40me', alt='json')
print ret.parsed
```

Upload image

``` python
ret = access_token.post('/shuo/statuses/', text='content from py-oauth2', files={ 'image': open('/path/pic.jpg')})
print ret.parsed
```

More:
<https://github.com/liluo/py-oauth2/wiki>

## License

MIT

## Submitting a Pull Request
* Fork the repository.
* Create a topic branch.
* Implement your feature or bug fix.
* Add, commit, and push your changes.
* Submit a pull request.
