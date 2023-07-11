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

class ContractDetailRequest(object):
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
        'contract': 'str',
        'password': 'str',
        'token_code': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'contract': 'contract',
        'password': 'password',
        'token_code': 'token_code',
        'user_name': 'user_name'
    }

    def __init__(self, contract=None, password=None, token_code=None, user_name=None):  # noqa: E501
        """ContractDetailRequest - a model defined in Swagger"""  # noqa: E501
        self._contract = None
        self._password = None
        self._token_code = None
        self._user_name = None
        self.discriminator = None
        if contract is not None:
            self.contract = contract
        if password is not None:
            self.password = password
        if token_code is not None:
            self.token_code = token_code
        if user_name is not None:
            self.user_name = user_name

    @property
    def contract(self):
        """Gets the contract of this ContractDetailRequest.  # noqa: E501

        El contrato a consultar la información  # noqa: E501

        :return: The contract of this ContractDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this ContractDetailRequest.

        El contrato a consultar la información  # noqa: E501

        :param contract: The contract of this ContractDetailRequest.  # noqa: E501
        :type: str
        """

        self._contract = contract

    @property
    def password(self):
        """Gets the password of this ContractDetailRequest.  # noqa: E501

        La contraseña del usuario  # noqa: E501

        :return: The password of this ContractDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ContractDetailRequest.

        La contraseña del usuario  # noqa: E501

        :param password: The password of this ContractDetailRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def token_code(self):
        """Gets the token_code of this ContractDetailRequest.  # noqa: E501

        La contraseña del usuario  # noqa: E501

        :return: The token_code of this ContractDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._token_code

    @token_code.setter
    def token_code(self, token_code):
        """Sets the token_code of this ContractDetailRequest.

        La contraseña del usuario  # noqa: E501

        :param token_code: The token_code of this ContractDetailRequest.  # noqa: E501
        :type: str
        """

        self._token_code = token_code

    @property
    def user_name(self):
        """Gets the user_name of this ContractDetailRequest.  # noqa: E501

        El nombre del usuario  # noqa: E501

        :return: The user_name of this ContractDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ContractDetailRequest.

        El nombre del usuario  # noqa: E501

        :param user_name: The user_name of this ContractDetailRequest.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(ContractDetailRequest, dict):
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
        if not isinstance(other, ContractDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
