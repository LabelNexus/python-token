from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, BadSignature
from flask import request
from lumavate_exceptions import AuthorizationException
import os
import uuid

# Attempt to import pyro - tolerate the miss if it's not in the pythonpath
try:
  import pyro
except:
  pyro = None

def _get_serializer():
  # Load the private key - if pyro is loaded, make sure to use get_setting.
  # Otherwise os.genenv is the best place.
  private_key = os.getenv('PRIVATE_KEY')
  if pyro:
    private_key = pyro.get_setting('PRIVATE_KEY')
  return TimedJSONWebSignatureSerializer(private_key)

class AuthToken:
  @staticmethod
  def from_cookie():
    pwa_jwt = request.cookies.get('pwa_jwt')
    if not pwa_jwt:
      return None

    token = AuthToken.from_token(pwa_jwt)

    return token

  @staticmethod
  def from_token(token):
    t = AuthToken()
    t.read_token(token)
    return t

  def __init__(self):
    self._data = {
      'salt': str(uuid.uuid4())[:8]
    }
    self.lang = 'en-us'
    self.default_lang = 'en-us'
    self.is_browser_supported = True

  def get_token(self):
    return _get_serializer().dumps(self._data).decode('utf-8')

  def read_token(self, token):
    if token.startswith('Bearer '):
      token = token.replace('Bearer ', '')
    try:
      self._data = _get_serializer().loads(token)
    except SignatureExpired:
      raise AuthorizationException('Token expired')
    except BadSignature as e:
      raise AuthorizationException('Invalid token')

  @property
  def session(self):
    return self._data.get('session')

  @session.setter
  def session(self, value):
    self._data['session'] = value

  @property
  def namespace(self):
    return self._data.get('namespace')

  @namespace.setter
  def namespace(self, value):
    self._data['namespace'] = value

  @property
  def code(self):
    return self._data.get('code')

  @code.setter
  def code(self, value):
    self._data['code'] = value

  @property
  def scope(self):
    return self._data.get('scope')

  @scope.setter
  def scope(self, value):
    self._data['scope'] = value

  @property
  def company_id(self):
    if 'orgId' in self._data:
      return self._data.get('orgId')

    return self._data.get('companyId')

  @company_id.setter
  def company_id(self, value):
    self._data['orgId'] = value
    self._data['companyId'] = value

  @property
  def is_test_company(self):
    return self._data.get('isTestCompany')

  @is_test_company.setter
  def is_test_company(self, value):
    self._data['isTestCompany'] = value

  @property
  def org_type(self):
    return self._data.get('orgType')

  @org_type.setter
  def org_type(self, value):
    self._data['orgType'] = value

  @property
  def version(self):
    return self._data.get('version')

  @version.setter
  def version(self, value):
    self._data['version'] = value

  @property
  def site_id(self):
    return self._data.get('siteId')

  @site_id.setter
  def site_id(self, value):
    self._data['siteId'] = value

  @property
  def domain_id(self):
    return self._data.get('domainId')

  @domain_id.setter
  def domain_id(self, value):
    self._data['domainId'] = value

  @property
  def activation_id(self):
    return self._data.get('activationId')

  @activation_id.setter
  def activation_id(self, value):
    self._data['activationId'] = value

  @property
  def home_url(self):
    return self._data.get('homeUrl')

  @home_url.setter
  def home_url(self, value):
    self._data['homeUrl'] = value

  @property
  def auth_url(self):
    return self._data.get('authUrl')

  @auth_url.setter
  def auth_url(self, value):
    self._data['authUrl'] = value

  @property
  def sw_url(self):
    return self._data.get('swUrl')

  @sw_url.setter
  def sw_url(self, value):
    self._data['swUrl'] = value

  @property
  def lang(self):
    return self._data.get('lang')

  @lang.setter
  def lang(self, value):
    self._data['lang'] = value

  @property
  def default_lang(self):
    return self._data.get('defaultLang')

  @default_lang.setter
  def default_lang(self, value):
    self._data['defaultLang'] = value

  @property
  def query_string(self):
    return self._data.get('queryString')

  @query_string.setter
  def query_string(self, value):
    self._data['queryString'] = value

  @property
  def is_browser_supported(self):
    return self._data.get('isBrowserSupported')

  @is_browser_supported.setter
  def is_browser_supported(self, value):
    self._data['isBrowserSupported'] = value

  @property
  def user(self):
    return self._data.get('user')

  @user.setter
  def user(self, value):
    self._data['user'] = value

  @property
  def role(self):
    return self._data.get('role')

  @role.setter
  def role(self, value):
    self._data['role'] = value

  @property
  def container_version_id(self):
    return self._data.get('containerVersionId')

  @container_version_id.setter
  def container_version_id(self, value):
    self._data['containerVersionId'] = value
