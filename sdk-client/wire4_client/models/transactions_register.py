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

class TransactionsRegister(object):
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
        'cancel_return_url': 'str',
        'return_url': 'str',
        'spei': 'list[TransactionSpeiSpid]',
        'spid': 'list[TransactionSpeiSpid]'
    }

    attribute_map = {
        'cancel_return_url': 'cancel_return_url',
        'return_url': 'return_url',
        'spei': 'spei',
        'spid': 'spid'
    }

    def __init__(self, cancel_return_url=None, return_url=None, spei=None, spid=None):  # noqa: E501
        """TransactionsRegister - a model defined in Swagger"""  # noqa: E501
        self._cancel_return_url = None
        self._return_url = None
        self._spei = None
        self._spid = None
        self.discriminator = None
        self.cancel_return_url = cancel_return_url
        self.return_url = return_url
        if spei is not None:
            self.spei = spei
        if spid is not None:
            self.spid = spid

    @property
    def cancel_return_url(self):
        """Gets the cancel_return_url of this TransactionsRegister.  # noqa: E501

        Es la dirección URL a la que se redirigirá en caso de que el usario cancele el registro.  # noqa: E501

        :return: The cancel_return_url of this TransactionsRegister.  # noqa: E501
        :rtype: str
        """
        return self._cancel_return_url

    @cancel_return_url.setter
    def cancel_return_url(self, cancel_return_url):
        """Sets the cancel_return_url of this TransactionsRegister.

        Es la dirección URL a la que se redirigirá en caso de que el usario cancele el registro.  # noqa: E501

        :param cancel_return_url: The cancel_return_url of this TransactionsRegister.  # noqa: E501
        :type: str
        """
        if cancel_return_url is None:
            raise ValueError("Invalid value for `cancel_return_url`, must not be `None`")  # noqa: E501

        self._cancel_return_url = cancel_return_url

    @property
    def return_url(self):
        """Gets the return_url of this TransactionsRegister.  # noqa: E501

        Es la dirección URL a la que se redirigirá en caso de éxito.  # noqa: E501

        :return: The return_url of this TransactionsRegister.  # noqa: E501
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this TransactionsRegister.

        Es la dirección URL a la que se redirigirá en caso de éxito.  # noqa: E501

        :param return_url: The return_url of this TransactionsRegister.  # noqa: E501
        :type: str
        """
        if return_url is None:
            raise ValueError("Invalid value for `return_url`, must not be `None`")  # noqa: E501

        self._return_url = return_url

    @property
    def spei(self):
        """Gets the spei of this TransactionsRegister.  # noqa: E501

        Lista de transacciones SPEI  # noqa: E501

        :return: The spei of this TransactionsRegister.  # noqa: E501
        :rtype: list[TransactionSpeiSpid]
        """
        return self._spei

    @spei.setter
    def spei(self, spei):
        """Sets the spei of this TransactionsRegister.

        Lista de transacciones SPEI  # noqa: E501

        :param spei: The spei of this TransactionsRegister.  # noqa: E501
        :type: list[TransactionSpeiSpid]
        """

        self._spei = spei

    @property
    def spid(self):
        """Gets the spid of this TransactionsRegister.  # noqa: E501

        Lista de transacciones SPID  # noqa: E501

        :return: The spid of this TransactionsRegister.  # noqa: E501
        :rtype: list[TransactionSpeiSpid]
        """
        return self._spid

    @spid.setter
    def spid(self, spid):
        """Sets the spid of this TransactionsRegister.

        Lista de transacciones SPID  # noqa: E501

        :param spid: The spid of this TransactionsRegister.  # noqa: E501
        :type: list[TransactionSpeiSpid]
        """

        self._spid = spid

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
        if issubclass(TransactionsRegister, dict):
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
        if not isinstance(other, TransactionsRegister):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
