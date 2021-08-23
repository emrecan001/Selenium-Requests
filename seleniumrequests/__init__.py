from selenium.webdriver import (
    Firefox as _Firefox, Chrome as _Chrome)

from seleniumrequests.request import RequestsSessionMixin


class Firefox(RequestsSessionMixin, _Firefox):
    pass


class Chrome(RequestsSessionMixin, _Chrome):
    pass
