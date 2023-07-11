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

class SalesPointRespose(object):
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
        'sales_point_id': 'str',
        'user_key': 'str',
        'user_secret': 'str',
        'webhook': 'Webhook'
    }

    attribute_map = {
        'sales_point_id': 'sales_point_id',
        'user_key': 'user_key',
        'user_secret': 'user_secret',
        'webhook': 'webhook'
    }

    def __init__(self, sales_point_id=None, user_key=None, user_secret=None, webhook=None):  # noqa: E501
        """SalesPointRespose - a model defined in Swagger"""  # noqa: E501
        self._sales_point_id = None
        self._user_key = None
        self._user_secret = None
        self._webhook = None
        self.discriminator = None
        if sales_point_id is not None:
            self.sales_point_id = sales_point_id
        if user_key is not None:
            self.user_key = user_key
        if user_secret is not None:
            self.user_secret = user_secret
        if webhook is not None:
            self.webhook = webhook

    @property
    def sales_point_id(self):
        """Gets the sales_point_id of this SalesPointRespose.  # noqa: E501

        Es el identificador del punto de venta.  # noqa: E501

        :return: The sales_point_id of this SalesPointRespose.  # noqa: E501
        :rtype: str
        """
        return self._sales_point_id

    @sales_point_id.setter
    def sales_point_id(self, sales_point_id):
        """Sets the sales_point_id of this SalesPointRespose.

        Es el identificador del punto de venta.  # noqa: E501

        :param sales_point_id: The sales_point_id of this SalesPointRespose.  # noqa: E501
        :type: str
        """

        self._sales_point_id = sales_point_id

    @property
    def user_key(self):
        """Gets the user_key of this SalesPointRespose.  # noqa: E501

        Es la llave de usuario para el API Wire4. Sólo para el uso de CODI®.  # noqa: E501

        :return: The user_key of this SalesPointRespose.  # noqa: E501
        :rtype: str
        """
        return self._user_key

    @user_key.setter
    def user_key(self, user_key):
        """Sets the user_key of this SalesPointRespose.

        Es la llave de usuario para el API Wire4. Sólo para el uso de CODI®.  # noqa: E501

        :param user_key: The user_key of this SalesPointRespose.  # noqa: E501
        :type: str
        """

        self._user_key = user_key

    @property
    def user_secret(self):
        """Gets the user_secret of this SalesPointRespose.  # noqa: E501

        Es la contraseña para el API Wire4. Sólo para el uso de CODI®.  # noqa: E501

        :return: The user_secret of this SalesPointRespose.  # noqa: E501
        :rtype: str
        """
        return self._user_secret

    @user_secret.setter
    def user_secret(self, user_secret):
        """Sets the user_secret of this SalesPointRespose.

        Es la contraseña para el API Wire4. Sólo para el uso de CODI®.  # noqa: E501

        :param user_secret: The user_secret of this SalesPointRespose.  # noqa: E501
        :type: str
        """

        self._user_secret = user_secret

    @property
    def webhook(self):
        """Gets the webhook of this SalesPointRespose.  # noqa: E501


        :return: The webhook of this SalesPointRespose.  # noqa: E501
        :rtype: Webhook
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this SalesPointRespose.


        :param webhook: The webhook of this SalesPointRespose.  # noqa: E501
        :type: Webhook
        """

        self._webhook = webhook

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
        if issubclass(SalesPointRespose, dict):
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
        if not isinstance(other, SalesPointRespose):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
