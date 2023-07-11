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

class UpdateConfigurationsRequestDTO(object):
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
        'configurations': 'list[ConfigurationsLimits]'
    }

    attribute_map = {
        'configurations': 'configurations'
    }

    def __init__(self, configurations=None):  # noqa: E501
        """UpdateConfigurationsRequestDTO - a model defined in Swagger"""  # noqa: E501
        self._configurations = None
        self.discriminator = None
        self.configurations = configurations

    @property
    def configurations(self):
        """Gets the configurations of this UpdateConfigurationsRequestDTO.  # noqa: E501

        Listado de configuraciones para actualizar  # noqa: E501

        :return: The configurations of this UpdateConfigurationsRequestDTO.  # noqa: E501
        :rtype: list[ConfigurationsLimits]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """Sets the configurations of this UpdateConfigurationsRequestDTO.

        Listado de configuraciones para actualizar  # noqa: E501

        :param configurations: The configurations of this UpdateConfigurationsRequestDTO.  # noqa: E501
        :type: list[ConfigurationsLimits]
        """
        if configurations is None:
            raise ValueError("Invalid value for `configurations`, must not be `None`")  # noqa: E501

        self._configurations = configurations

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
        if issubclass(UpdateConfigurationsRequestDTO, dict):
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
        if not isinstance(other, UpdateConfigurationsRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
