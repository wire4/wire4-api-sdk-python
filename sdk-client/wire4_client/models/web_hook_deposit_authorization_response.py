# coding: utf-8

"""
    Wire4RestAPI

    Referencia de la API de Wire4  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WebHookDepositAuthorizationResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'events': 'list[str]',
        'name': 'str',
        'secret': 'str',
        'status': 'str',
        'url': 'str',
        'wh_uuid': 'str'
    }

    attribute_map = {
        'events': 'events',
        'name': 'name',
        'secret': 'secret',
        'status': 'status',
        'url': 'url',
        'wh_uuid': 'wh_uuid'
    }

    def __init__(self, events=None, name=None, secret=None, status=None, url=None, wh_uuid=None):  # noqa: E501
        """WebHookDepositAuthorizationResponse - a model defined in Swagger"""  # noqa: E501
        self._events = None
        self._name = None
        self._secret = None
        self._status = None
        self._url = None
        self._wh_uuid = None
        self.discriminator = None
        if events is not None:
            self.events = events
        if name is not None:
            self.name = name
        if secret is not None:
            self.secret = secret
        if status is not None:
            self.status = status
        if url is not None:
            self.url = url
        if wh_uuid is not None:
            self.wh_uuid = wh_uuid

    @property
    def events(self):
        """Gets the events of this WebHookDepositAuthorizationResponse.  # noqa: E501

        Tipo de evento manejado por el webhook, para mas referencia sobre los tipos de eventos soportados, revise la siguiente liga: <a href=\"https://developers.wire4.mx/#section/Eventos\">https://developers.wire4.mx/#section/Eventos.</a>  # noqa: E501

        :return: The events of this WebHookDepositAuthorizationResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this WebHookDepositAuthorizationResponse.

        Tipo de evento manejado por el webhook, para mas referencia sobre los tipos de eventos soportados, revise la siguiente liga: <a href=\"https://developers.wire4.mx/#section/Eventos\">https://developers.wire4.mx/#section/Eventos.</a>  # noqa: E501

        :param events: The events of this WebHookDepositAuthorizationResponse.  # noqa: E501
        :type: list[str]
        """

        self._events = events

    @property
    def name(self):
        """Gets the name of this WebHookDepositAuthorizationResponse.  # noqa: E501

        Es el nombre del webhook.  # noqa: E501

        :return: The name of this WebHookDepositAuthorizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebHookDepositAuthorizationResponse.

        Es el nombre del webhook.  # noqa: E501

        :param name: The name of this WebHookDepositAuthorizationResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def secret(self):
        """Gets the secret of this WebHookDepositAuthorizationResponse.  # noqa: E501

        Es la llave con la cuál se debe de identificar que el webhook fue enviado por Wire4. Para mayor información revisar la guía de notificaciones en la sección de  <a href=\"https://wire4.mx/#/guides/notificaciones\">\"Comprobación de firmas de Webhook\".</a>  # noqa: E501

        :return: The secret of this WebHookDepositAuthorizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this WebHookDepositAuthorizationResponse.

        Es la llave con la cuál se debe de identificar que el webhook fue enviado por Wire4. Para mayor información revisar la guía de notificaciones en la sección de  <a href=\"https://wire4.mx/#/guides/notificaciones\">\"Comprobación de firmas de Webhook\".</a>  # noqa: E501

        :param secret: The secret of this WebHookDepositAuthorizationResponse.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def status(self):
        """Gets the status of this WebHookDepositAuthorizationResponse.  # noqa: E501

        Es el estado (estatus) en el que se encuentra el webhook.  # noqa: E501

        :return: The status of this WebHookDepositAuthorizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebHookDepositAuthorizationResponse.

        Es el estado (estatus) en el que se encuentra el webhook.  # noqa: E501

        :param status: The status of this WebHookDepositAuthorizationResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def url(self):
        """Gets the url of this WebHookDepositAuthorizationResponse.  # noqa: E501

        Es la dirección URL a la cuál Wire4 enviará las notificaciones cuando un evento ocurra.  # noqa: E501

        :return: The url of this WebHookDepositAuthorizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebHookDepositAuthorizationResponse.

        Es la dirección URL a la cuál Wire4 enviará las notificaciones cuando un evento ocurra.  # noqa: E501

        :param url: The url of this WebHookDepositAuthorizationResponse.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def wh_uuid(self):
        """Gets the wh_uuid of this WebHookDepositAuthorizationResponse.  # noqa: E501

         Es el identificador del webhook.  # noqa: E501

        :return: The wh_uuid of this WebHookDepositAuthorizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._wh_uuid

    @wh_uuid.setter
    def wh_uuid(self, wh_uuid):
        """Sets the wh_uuid of this WebHookDepositAuthorizationResponse.

         Es el identificador del webhook.  # noqa: E501

        :param wh_uuid: The wh_uuid of this WebHookDepositAuthorizationResponse.  # noqa: E501
        :type: str
        """

        self._wh_uuid = wh_uuid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WebHookDepositAuthorizationResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebHookDepositAuthorizationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
