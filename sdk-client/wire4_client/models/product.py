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

class Product(object):
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
        'amount': 'float',
        'billing_period': 'str',
        'frequency': 'int',
        'name': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'billing_period': 'billing_period',
        'frequency': 'frequency',
        'name': 'name'
    }

    def __init__(self, amount=None, billing_period=None, frequency=None, name=None):  # noqa: E501
        """Product - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._billing_period = None
        self._frequency = None
        self._name = None
        self.discriminator = None
        self.amount = amount
        self.billing_period = billing_period
        self.frequency = frequency
        self.name = name

    @property
    def amount(self):
        """Gets the amount of this Product.  # noqa: E501

        Monto del calgo que se aplicará de forma periodica  # noqa: E501

        :return: The amount of this Product.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Product.

        Monto del calgo que se aplicará de forma periodica  # noqa: E501

        :param amount: The amount of this Product.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def billing_period(self):
        """Gets the billing_period of this Product.  # noqa: E501

        Periodo en el cual se aplicará el cargo, si no se especifica la propiedad frequency por defecto sera la unidad  # noqa: E501

        :return: The billing_period of this Product.  # noqa: E501
        :rtype: str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this Product.

        Periodo en el cual se aplicará el cargo, si no se especifica la propiedad frequency por defecto sera la unidad  # noqa: E501

        :param billing_period: The billing_period of this Product.  # noqa: E501
        :type: str
        """
        if billing_period is None:
            raise ValueError("Invalid value for `billing_period`, must not be `None`")  # noqa: E501
        allowed_values = ["WEEKLY", "MONTHLY", "YEARLY"]  # noqa: E501
        if billing_period not in allowed_values:
            raise ValueError(
                "Invalid value for `billing_period` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_period, allowed_values)
            )

        self._billing_period = billing_period

    @property
    def frequency(self):
        """Gets the frequency of this Product.  # noqa: E501

        La frecuencia en la que se aplicará el cargo, trabaja en conjunto con la propiedad billingPeriod  # noqa: E501

        :return: The frequency of this Product.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this Product.

        La frecuencia en la que se aplicará el cargo, trabaja en conjunto con la propiedad billingPeriod  # noqa: E501

        :param frequency: The frequency of this Product.  # noqa: E501
        :type: int
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501

        self._frequency = frequency

    @property
    def name(self):
        """Gets the name of this Product.  # noqa: E501

        Nombre del producto sobre el cual se aplicará el cobro recurrente  # noqa: E501

        :return: The name of this Product.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Product.

        Nombre del producto sobre el cual se aplicará el cobro recurrente  # noqa: E501

        :param name: The name of this Product.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(Product, dict):
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
        if not isinstance(other, Product):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
