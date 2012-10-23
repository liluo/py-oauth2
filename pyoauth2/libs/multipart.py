import codecs
import mimetypes
from uuid import uuid4
from io import BytesIO

CRLF = '\r\n'
writer = codecs.lookup('utf-8')[3]

def guess_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/sctet-stream'

def iter_fields(fields):
    if isinstance(fields, dict):
        fields = fields.iteritems()
    return ((k, v) for k, v in fields)

def build_multipart(fields, boundary=None):
    body = BytesIO()
    boundary = boundary or uuid4().hex

    for field_name, value in iter_fields(fields):
        body.write('--%s%s'%(boundary, CRLF))

        if isinstance(value, tuple):
            file_name, data = value
            writer(body).write('Content-Disposition: form-data; name="%s"; '
                              'filename="%s"%s'%(field_name, file_name, CRLF))
            body.write('Content-Type: %s%s'%(guess_type(file_name), CRLF*2))
        else:
            data = value
            writer(body).write('Content-Disposition: form-data; name="%s"%s'
                               %(field_name, CRLF))
            body.write('Content-Type: text/plain%s'%(CRLF*2))

        if isinstance(data, int):
            data = str(data)

        if isinstance(data, unicode):
            writer(body).write(data)
        else:
            body.write(data)

        body.write(CRLF)

    body.write('--%s--%s'%(boundary, CRLF))
    content_type = 'multipart/form-data; boundary=%s' % boundary
    return body.getvalue(), content_type
