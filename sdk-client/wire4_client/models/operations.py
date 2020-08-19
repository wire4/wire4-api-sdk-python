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
from wire4_client.models.compay import Compay  # noqa: F401,E501
from wire4_client.models.payment import Payment  # noqa: F401,E501
from wire4_client.models.sales_point import SalesPoint  # noqa: F401,E501


class Operations(object):
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
        'company': 'Compay',
        'description': 'str',
        'due_date': 'datetime',
        'order_id': 'str',
        'payment': 'Payment',
        'phone_number': 'str',
        'sales_point': 'SalesPoint',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'company': 'company',
        'description': 'description',
        'due_date': 'due_date',
        'order_id': 'order_id',
        'payment': 'payment',
        'phone_number': 'phone_number',
        'sales_point': 'sales_point',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, amount=None, company=None, description=None, due_date=None, order_id=None, payment=None, phone_number=None, sales_point=None, status=None, type=None):  # noqa: E501
        """Operations - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._company = None
        self._description = None
        self._due_date = None
        self._order_id = None
        self._payment = None
        self._phone_number = None
        self._sales_point = None
        self._status = None
        self._type = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if company is not None:
            self.company = company
        if description is not None:
            self.description = description
        if due_date is not None:
            self.due_date = due_date
        if order_id is not None:
            self.order_id = order_id
        if payment is not None:
            self.payment = payment
        if phone_number is not None:
            self.phone_number = phone_number
        if sales_point is not None:
            self.sales_point = sales_point
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def amount(self):
        """Gets the amount of this Operations.  # noqa: E501

        Monto de la petición  # noqa: E501

        :return: The amount of this Operations.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Operations.

        Monto de la petición  # noqa: E501

        :param amount: The amount of this Operations.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def company(self):
        """Gets the company of this Operations.  # noqa: E501


        :return: The company of this Operations.  # noqa: E501
        :rtype: Compay
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Operations.


        :param company: The company of this Operations.  # noqa: E501
        :type: Compay
        """

        self._company = company

    @property
    def description(self):
        """Gets the description of this Operations.  # noqa: E501

        Descripción de la petición  # noqa: E501

        :return: The description of this Operations.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Operations.

        Descripción de la petición  # noqa: E501

        :param description: The description of this Operations.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def due_date(self):
        """Gets the due_date of this Operations.  # noqa: E501

        Fecha de vencimiento de la petición  # noqa: E501

        :return: The due_date of this Operations.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Operations.

        Fecha de vencimiento de la petición  # noqa: E501

        :param due_date: The due_date of this Operations.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def order_id(self):
        """Gets the order_id of this Operations.  # noqa: E501

        Order id de la petición  # noqa: E501

        :return: The order_id of this Operations.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Operations.

        Order id de la petición  # noqa: E501

        :param order_id: The order_id of this Operations.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def payment(self):
        """Gets the payment of this Operations.  # noqa: E501


        :return: The payment of this Operations.  # noqa: E501
        :rtype: Payment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this Operations.


        :param payment: The payment of this Operations.  # noqa: E501
        :type: Payment
        """

        self._payment = payment

    @property
    def phone_number(self):
        """Gets the phone_number of this Operations.  # noqa: E501

        Numero de telefono  # noqa: E501

        :return: The phone_number of this Operations.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Operations.

        Numero de telefono  # noqa: E501

        :param phone_number: The phone_number of this Operations.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def sales_point(self):
        """Gets the sales_point of this Operations.  # noqa: E501


        :return: The sales_point of this Operations.  # noqa: E501
        :rtype: SalesPoint
        """
        return self._sales_point

    @sales_point.setter
    def sales_point(self, sales_point):
        """Sets the sales_point of this Operations.


        :param sales_point: The sales_point of this Operations.  # noqa: E501
        :type: SalesPoint
        """

        self._sales_point = sales_point

    @property
    def status(self):
        """Gets the status of this Operations.  # noqa: E501

        Estatus de la petición  # noqa: E501

        :return: The status of this Operations.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Operations.

        Estatus de la petición  # noqa: E501

        :param status: The status of this Operations.  # noqa: E501
        :type: str
        """
        allowed_values = ["RECEIVED", "COMPLETED", "CANCELLED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def type(self):
        """Gets the type of this Operations.  # noqa: E501

        Tipo de petición de cobro  # noqa: E501

        :return: The type of this Operations.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Operations.

        Tipo de petición de cobro  # noqa: E501

        :param type: The type of this Operations.  # noqa: E501
        :type: str
        """
        allowed_values = ["PUSH_NOTIFICATION", "QR_CODE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(Operations, dict):
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
        if not isinstance(other, Operations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
