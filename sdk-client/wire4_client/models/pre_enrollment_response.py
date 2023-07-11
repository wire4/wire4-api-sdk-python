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

class PreEnrollmentResponse(object):
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
        'subscription_id': 'str',
        'url': 'str'
    }

    attribute_map = {
        'subscription_id': 'subscription_id',
        'url': 'url'
    }

    def __init__(self, subscription_id=None, url=None):  # noqa: E501
        """PreEnrollmentResponse - a model defined in Swagger"""  # noqa: E501
        self._subscription_id = None
        self._url = None
        self.discriminator = None
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if url is not None:
            self.url = url

    @property
    def subscription_id(self):
        """Gets the subscription_id of this PreEnrollmentResponse.  # noqa: E501

        Es el identificador público generado para la suscripción.  # noqa: E501

        :return: The subscription_id of this PreEnrollmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this PreEnrollmentResponse.

        Es el identificador público generado para la suscripción.  # noqa: E501

        :param subscription_id: The subscription_id of this PreEnrollmentResponse.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def url(self):
        """Gets the url of this PreEnrollmentResponse.  # noqa: E501

        Es la dirección URL del centro de autorizción para confirmación del alta de la suscripción.  # noqa: E501

        :return: The url of this PreEnrollmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PreEnrollmentResponse.

        Es la dirección URL del centro de autorizción para confirmación del alta de la suscripción.  # noqa: E501

        :param url: The url of this PreEnrollmentResponse.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(PreEnrollmentResponse, dict):
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
        if not isinstance(other, PreEnrollmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
