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

class PaymentRequestCodiResponseDTO(object):
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
        'barcode_base64': 'str',
        'barcode_url': 'str',
        'concept': 'str',
        'creation_date': 'datetime',
        'due_date': 'datetime',
        'operations': 'list[CodiOperationResponseDTO]',
        'order_id': 'str',
        'phone_number': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'barcode_base64': 'barcode_base64',
        'barcode_url': 'barcode_url',
        'concept': 'concept',
        'creation_date': 'creation_date',
        'due_date': 'due_date',
        'operations': 'operations',
        'order_id': 'order_id',
        'phone_number': 'phone_number',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, amount=None, barcode_base64=None, barcode_url=None, concept=None, creation_date=None, due_date=None, operations=None, order_id=None, phone_number=None, status=None, type=None):  # noqa: E501
        """PaymentRequestCodiResponseDTO - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._barcode_base64 = None
        self._barcode_url = None
        self._concept = None
        self._creation_date = None
        self._due_date = None
        self._operations = None
        self._order_id = None
        self._phone_number = None
        self._status = None
        self._type = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if barcode_base64 is not None:
            self.barcode_base64 = barcode_base64
        if barcode_url is not None:
            self.barcode_url = barcode_url
        if concept is not None:
            self.concept = concept
        if creation_date is not None:
            self.creation_date = creation_date
        if due_date is not None:
            self.due_date = due_date
        if operations is not None:
            self.operations = operations
        if order_id is not None:
            self.order_id = order_id
        if phone_number is not None:
            self.phone_number = phone_number
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def amount(self):
        """Gets the amount of this PaymentRequestCodiResponseDTO.  # noqa: E501

        Es el Monto del pago. Ejemplo 1000.00  # noqa: E501

        :return: The amount of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentRequestCodiResponseDTO.

        Es el Monto del pago. Ejemplo 1000.00  # noqa: E501

        :param amount: The amount of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def barcode_base64(self):
        """Gets the barcode_base64 of this PaymentRequestCodiResponseDTO.  # noqa: E501

        Es la imagen QR en formato Base64 para el CODI®.  # noqa: E501

        :return: The barcode_base64 of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._barcode_base64

    @barcode_base64.setter
    def barcode_base64(self, barcode_base64):
        """Sets the barcode_base64 of this PaymentRequestCodiResponseDTO.

        Es la imagen QR en formato Base64 para el CODI®.  # noqa: E501

        :param barcode_base64: The barcode_base64 of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :type: str
        """

        self._barcode_base64 = barcode_base64

    @property
    def barcode_url(self):
        """Gets the barcode_url of this PaymentRequestCodiResponseDTO.  # noqa: E501

        Es la dirección URL de la imagen QR para el CODI®.  # noqa: E501

        :return: The barcode_url of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._barcode_url

    @barcode_url.setter
    def barcode_url(self, barcode_url):
        """Sets the barcode_url of this PaymentRequestCodiResponseDTO.

        Es la dirección URL de la imagen QR para el CODI®.  # noqa: E501

        :param barcode_url: The barcode_url of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :type: str
        """

        self._barcode_url = barcode_url

    @property
    def concept(self):
        """Gets the concept of this PaymentRequestCodiResponseDTO.  # noqa: E501

        Es el concepto de pago.  # noqa: E501

        :return: The concept of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._concept

    @concept.setter
    def concept(self, concept):
        """Sets the concept of this PaymentRequestCodiResponseDTO.

        Es el concepto de pago.  # noqa: E501

        :param concept: The concept of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :type: str
        """

        self._concept = concept

    @property
    def creation_date(self):
        """Gets the creation_date of this PaymentRequestCodiResponseDTO.  # noqa: E501

        Es la fecha de creación. Ésta fecha viene en formato ISO 8601 con zona horaria, ejemplo: <strong>2020-10-27T11:03:15.000-06:00</strong>.  # noqa: E501

        :return: The creation_date of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this PaymentRequestCodiResponseDTO.

        Es la fecha de creación. Ésta fecha viene en formato ISO 8601 con zona horaria, ejemplo: <strong>2020-10-27T11:03:15.000-06:00</strong>.  # noqa: E501

        :param creation_date: The creation_date of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def due_date(self):
        """Gets the due_date of this PaymentRequestCodiResponseDTO.  # noqa: E501

        Es la fecha de vencimiento. Ésta fecha viene en formato ISO 8601 con zona horaria, ejemplo: <strong>2020-10-27T11:03:15.000-06:00</strong>.  # noqa: E501

        :return: The due_date of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this PaymentRequestCodiResponseDTO.

        Es la fecha de vencimiento. Ésta fecha viene en formato ISO 8601 con zona horaria, ejemplo: <strong>2020-10-27T11:03:15.000-06:00</strong>.  # noqa: E501

        :param due_date: The due_date of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def operations(self):
        """Gets the operations of this PaymentRequestCodiResponseDTO.  # noqa: E501

        Es el listado de pagos realizados sobre la petición.  # noqa: E501

        :return: The operations of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :rtype: list[CodiOperationResponseDTO]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this PaymentRequestCodiResponseDTO.

        Es el listado de pagos realizados sobre la petición.  # noqa: E501

        :param operations: The operations of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :type: list[CodiOperationResponseDTO]
        """

        self._operations = operations

    @property
    def order_id(self):
        """Gets the order_id of this PaymentRequestCodiResponseDTO.  # noqa: E501

        Es el orderId asignado a la solicitud.  # noqa: E501

        :return: The order_id of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PaymentRequestCodiResponseDTO.

        Es el orderId asignado a la solicitud.  # noqa: E501

        :param order_id: The order_id of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def phone_number(self):
        """Gets the phone_number of this PaymentRequestCodiResponseDTO.  # noqa: E501

        Es el número de teléfono.  # noqa: E501

        :return: The phone_number of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this PaymentRequestCodiResponseDTO.

        Es el número de teléfono.  # noqa: E501

        :param phone_number: The phone_number of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def status(self):
        """Gets the status of this PaymentRequestCodiResponseDTO.  # noqa: E501

        Es el estado (estatus) de la orden de pago. Los valores pueden ser: <b>RECEIVED, COMPLETED Y CANCELLED</b>  # noqa: E501

        :return: The status of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentRequestCodiResponseDTO.

        Es el estado (estatus) de la orden de pago. Los valores pueden ser: <b>RECEIVED, COMPLETED Y CANCELLED</b>  # noqa: E501

        :param status: The status of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this PaymentRequestCodiResponseDTO.  # noqa: E501

        Es el tipo de petición. Los valores pueden ser: <b>QR_CODE o PUSH_NOTIFICATION</b>  # noqa: E501

        :return: The type of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PaymentRequestCodiResponseDTO.

        Es el tipo de petición. Los valores pueden ser: <b>QR_CODE o PUSH_NOTIFICATION</b>  # noqa: E501

        :param type: The type of this PaymentRequestCodiResponseDTO.  # noqa: E501
        :type: str
        """

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
        if issubclass(PaymentRequestCodiResponseDTO, dict):
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
        if not isinstance(other, PaymentRequestCodiResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
