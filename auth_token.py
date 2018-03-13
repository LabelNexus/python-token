from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, BadSignature
from lumavate_exceptions import AuthorizationException
import os

def _get_serializer():
  return TimedJSONWebSignatureSerializer(os.environ['PRIVATE_KEY'])

class AuthToken:
  @staticmethod
  def from_token(token):
    t = AuthToken()
    t.read_token(token)
    return t

  def __init__(self):
    self._data = {}
    self.lang = 'en-us'
    self.default_lang = 'en-us'

  def get_token(self):
    return _get_serializer().dumps(self._data).decode('utf-8')

  def read_token(self, token):
    try:
      self._data = _get_serializer().loads(token)
    except SignatureExpired:
      raise AuthorizationException('Token expired')
    except BadSignature:
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
  def scope(self):
    return self._data.get('scope')

  @scope.setter
  def scope(self, value):
    self._data['scope'] = value

  @property
  def company_id(self):
    return self._data.get('companyId')

  @company_id.setter
  def company_id(self, value):
    self._data['companyId'] = value

  @property
  def version(self):
    return self._data.get('version')

  @version.setter
  def version(self, value):
    self._data['version'] = value

  @property
  def template_id(self):
    return self._data.get('templateId')

  @template_id.setter
  def template_id(self, value):
    self._data['templateId'] = value

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
  def subscriber_id(self):
    return self._data.get('subscriberId')

  @subscriber_id.setter
  def subscriber_id(self, value):
    self._data['subscriberId'] = value

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
  def pre_cache_data_routes(self):
    return self._data.get('preCacheDataRoutes')

  @pre_cache_data_routes.setter
  def pre_cache_data_routes(self, value):
    self._data['preCacheDataRoutes'] = value

  @property
  def theme_color(self):
    return self._data.get('themeColor')

  @theme_color.setter
  def theme_color(self, value):
    self._data['themeColor'] = value

  @property
  def display_name(self):
    return self._data.get('displayName')

  @display_name.setter
  def display_name(self, value):
    self._data['displayName'] = value

  @property
  def query_string(self):
    return self._data.get('queryString')

  @query_string.setter
  def query_string(self, value):
    self._data['queryString'] = value
