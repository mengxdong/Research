import hashlib
from urllib.parse import urlencode

from django import template
from django.conf import settings

register = template.Library()


@register.filter
def gravatar(user):
    email = user.email.lower().encode('utf-8')
    default = 'mm'
    size = 256
    url = 'https://gravatar.cn/avatar/{md5}?{params}'.format(
        md5=hashlib.md5(email).hexdigest(),
        params=urlencode({'d': default, 's': str(size)})
    )

    print(url)
    #return url
    #return "https://gravatar.cn/avatar/205e460b479e2e5b48aec07710c08d50?f=y"
    return "https://gravatar.cn/avatar/205e460b479e2e5b48aec07710c08d50?r=pg"