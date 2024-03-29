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

class GetDepositants(object):
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
        'depositants': 'list[Depositant]'
    }

    attribute_map = {
        'depositants': 'depositants'
    }

    def __init__(self, depositants=None):  # noqa: E501
        """GetDepositants - a model defined in Swagger"""  # noqa: E501
        self._depositants = None
        self.discriminator = None
        self.depositants = depositants

    @property
    def depositants(self):
        """Gets the depositants of this GetDepositants.  # noqa: E501

        Es la lista que contiene cada depositante encontrad.o  # noqa: E501

        :return: The depositants of this GetDepositants.  # noqa: E501
        :rtype: list[Depositant]
        """
        return self._depositants

    @depositants.setter
    def depositants(self, depositants):
        """Sets the depositants of this GetDepositants.

        Es la lista que contiene cada depositante encontrad.o  # noqa: E501

        :param depositants: The depositants of this GetDepositants.  # noqa: E501
        :type: list[Depositant]
        """
        if depositants is None:
            raise ValueError("Invalid value for `depositants`, must not be `None`")  # noqa: E501

        self._depositants = depositants

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
        if issubclass(GetDepositants, dict):
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
        if not isinstance(other, GetDepositants):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
