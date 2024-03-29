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

class MessageDepositReceived(object):
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
        'beneficiary_account': 'str',
        'beneficiary_name': 'str',
        'beneficiary_rfc': 'str',
        'cep': 'MessageCEP',
        'clave_rastreo': 'str',
        'confirm_date': 'datetime',
        'currency_code': 'str',
        'deposit_date': 'datetime',
        'depositant': 'str',
        'depositant_alias': 'str',
        'depositant_clabe': 'str',
        'depositant_email': 'str',
        'depositant_rfc': 'str',
        'description': 'str',
        'monex_description': 'str',
        'monex_transaction_id': 'str',
        'reference': 'str',
        'sender_account': 'str',
        'sender_bank': 'MessageInstitution',
        'sender_name': 'str',
        'sender_rfc': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'beneficiary_account': 'beneficiary_account',
        'beneficiary_name': 'beneficiary_name',
        'beneficiary_rfc': 'beneficiary_rfc',
        'cep': 'cep',
        'clave_rastreo': 'clave_rastreo',
        'confirm_date': 'confirm_date',
        'currency_code': 'currency_code',
        'deposit_date': 'deposit_date',
        'depositant': 'depositant',
        'depositant_alias': 'depositant_alias',
        'depositant_clabe': 'depositant_clabe',
        'depositant_email': 'depositant_email',
        'depositant_rfc': 'depositant_rfc',
        'description': 'description',
        'monex_description': 'monex_description',
        'monex_transaction_id': 'monex_transaction_id',
        'reference': 'reference',
        'sender_account': 'sender_account',
        'sender_bank': 'sender_bank',
        'sender_name': 'sender_name',
        'sender_rfc': 'sender_rfc'
    }

    def __init__(self, amount=None, beneficiary_account=None, beneficiary_name=None, beneficiary_rfc=None, cep=None, clave_rastreo=None, confirm_date=None, currency_code=None, deposit_date=None, depositant=None, depositant_alias=None, depositant_clabe=None, depositant_email=None, depositant_rfc=None, description=None, monex_description=None, monex_transaction_id=None, reference=None, sender_account=None, sender_bank=None, sender_name=None, sender_rfc=None):  # noqa: E501
        """MessageDepositReceived - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._beneficiary_account = None
        self._beneficiary_name = None
        self._beneficiary_rfc = None
        self._cep = None
        self._clave_rastreo = None
        self._confirm_date = None
        self._currency_code = None
        self._deposit_date = None
        self._depositant = None
        self._depositant_alias = None
        self._depositant_clabe = None
        self._depositant_email = None
        self._depositant_rfc = None
        self._description = None
        self._monex_description = None
        self._monex_transaction_id = None
        self._reference = None
        self._sender_account = None
        self._sender_bank = None
        self._sender_name = None
        self._sender_rfc = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if beneficiary_account is not None:
            self.beneficiary_account = beneficiary_account
        if beneficiary_name is not None:
            self.beneficiary_name = beneficiary_name
        if beneficiary_rfc is not None:
            self.beneficiary_rfc = beneficiary_rfc
        if cep is not None:
            self.cep = cep
        if clave_rastreo is not None:
            self.clave_rastreo = clave_rastreo
        if confirm_date is not None:
            self.confirm_date = confirm_date
        if currency_code is not None:
            self.currency_code = currency_code
        if deposit_date is not None:
            self.deposit_date = deposit_date
        if depositant is not None:
            self.depositant = depositant
        if depositant_alias is not None:
            self.depositant_alias = depositant_alias
        if depositant_clabe is not None:
            self.depositant_clabe = depositant_clabe
        if depositant_email is not None:
            self.depositant_email = depositant_email
        if depositant_rfc is not None:
            self.depositant_rfc = depositant_rfc
        if description is not None:
            self.description = description
        if monex_description is not None:
            self.monex_description = monex_description
        if monex_transaction_id is not None:
            self.monex_transaction_id = monex_transaction_id
        if reference is not None:
            self.reference = reference
        if sender_account is not None:
            self.sender_account = sender_account
        if sender_bank is not None:
            self.sender_bank = sender_bank
        if sender_name is not None:
            self.sender_name = sender_name
        if sender_rfc is not None:
            self.sender_rfc = sender_rfc

    @property
    def amount(self):
        """Gets the amount of this MessageDepositReceived.  # noqa: E501

        Es el monto de la transferencia.  # noqa: E501

        :return: The amount of this MessageDepositReceived.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this MessageDepositReceived.

        Es el monto de la transferencia.  # noqa: E501

        :param amount: The amount of this MessageDepositReceived.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def beneficiary_account(self):
        """Gets the beneficiary_account of this MessageDepositReceived.  # noqa: E501

        Es la cuenta del beneficiario.  # noqa: E501

        :return: The beneficiary_account of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_account

    @beneficiary_account.setter
    def beneficiary_account(self, beneficiary_account):
        """Sets the beneficiary_account of this MessageDepositReceived.

        Es la cuenta del beneficiario.  # noqa: E501

        :param beneficiary_account: The beneficiary_account of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._beneficiary_account = beneficiary_account

    @property
    def beneficiary_name(self):
        """Gets the beneficiary_name of this MessageDepositReceived.  # noqa: E501

        Es el nombre del beneficiario.  # noqa: E501

        :return: The beneficiary_name of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_name

    @beneficiary_name.setter
    def beneficiary_name(self, beneficiary_name):
        """Sets the beneficiary_name of this MessageDepositReceived.

        Es el nombre del beneficiario.  # noqa: E501

        :param beneficiary_name: The beneficiary_name of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._beneficiary_name = beneficiary_name

    @property
    def beneficiary_rfc(self):
        """Gets the beneficiary_rfc of this MessageDepositReceived.  # noqa: E501

        Es el Registro Federal de Contribuyentes (RFC) del beneficiario.  # noqa: E501

        :return: The beneficiary_rfc of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_rfc

    @beneficiary_rfc.setter
    def beneficiary_rfc(self, beneficiary_rfc):
        """Sets the beneficiary_rfc of this MessageDepositReceived.

        Es el Registro Federal de Contribuyentes (RFC) del beneficiario.  # noqa: E501

        :param beneficiary_rfc: The beneficiary_rfc of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._beneficiary_rfc = beneficiary_rfc

    @property
    def cep(self):
        """Gets the cep of this MessageDepositReceived.  # noqa: E501


        :return: The cep of this MessageDepositReceived.  # noqa: E501
        :rtype: MessageCEP
        """
        return self._cep

    @cep.setter
    def cep(self, cep):
        """Sets the cep of this MessageDepositReceived.


        :param cep: The cep of this MessageDepositReceived.  # noqa: E501
        :type: MessageCEP
        """

        self._cep = cep

    @property
    def clave_rastreo(self):
        """Gets the clave_rastreo of this MessageDepositReceived.  # noqa: E501

        Es la clave de rastreo de la transferencia.  # noqa: E501

        :return: The clave_rastreo of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._clave_rastreo

    @clave_rastreo.setter
    def clave_rastreo(self, clave_rastreo):
        """Sets the clave_rastreo of this MessageDepositReceived.

        Es la clave de rastreo de la transferencia.  # noqa: E501

        :param clave_rastreo: The clave_rastreo of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._clave_rastreo = clave_rastreo

    @property
    def confirm_date(self):
        """Gets the confirm_date of this MessageDepositReceived.  # noqa: E501

        Es la Fecha de confirmación de la transferencia.  # noqa: E501

        :return: The confirm_date of this MessageDepositReceived.  # noqa: E501
        :rtype: datetime
        """
        return self._confirm_date

    @confirm_date.setter
    def confirm_date(self, confirm_date):
        """Sets the confirm_date of this MessageDepositReceived.

        Es la Fecha de confirmación de la transferencia.  # noqa: E501

        :param confirm_date: The confirm_date of this MessageDepositReceived.  # noqa: E501
        :type: datetime
        """

        self._confirm_date = confirm_date

    @property
    def currency_code(self):
        """Gets the currency_code of this MessageDepositReceived.  # noqa: E501

        Es el código de divisa de la transferencia. Es en el formato estándar ISO 4217 y es de 3 dígitos. Puede ser \"MXN\" o \"USD\".  # noqa: E501

        :return: The currency_code of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this MessageDepositReceived.

        Es el código de divisa de la transferencia. Es en el formato estándar ISO 4217 y es de 3 dígitos. Puede ser \"MXN\" o \"USD\".  # noqa: E501

        :param currency_code: The currency_code of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def deposit_date(self):
        """Gets the deposit_date of this MessageDepositReceived.  # noqa: E501

        Es la fecha de recepción de la transferencia.  # noqa: E501

        :return: The deposit_date of this MessageDepositReceived.  # noqa: E501
        :rtype: datetime
        """
        return self._deposit_date

    @deposit_date.setter
    def deposit_date(self, deposit_date):
        """Sets the deposit_date of this MessageDepositReceived.

        Es la fecha de recepción de la transferencia.  # noqa: E501

        :param deposit_date: The deposit_date of this MessageDepositReceived.  # noqa: E501
        :type: datetime
        """

        self._deposit_date = deposit_date

    @property
    def depositant(self):
        """Gets the depositant of this MessageDepositReceived.  # noqa: E501

        Es el nombre del depositante en caso de que la transferencia se reciba en una cuenta de depositante.  # noqa: E501

        :return: The depositant of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._depositant

    @depositant.setter
    def depositant(self, depositant):
        """Sets the depositant of this MessageDepositReceived.

        Es el nombre del depositante en caso de que la transferencia se reciba en una cuenta de depositante.  # noqa: E501

        :param depositant: The depositant of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._depositant = depositant

    @property
    def depositant_alias(self):
        """Gets the depositant_alias of this MessageDepositReceived.  # noqa: E501

        Es el alias de la cuenta CLABE del depositante en caso que la transferencia se reciba de una cuenta de depositante  # noqa: E501

        :return: The depositant_alias of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._depositant_alias

    @depositant_alias.setter
    def depositant_alias(self, depositant_alias):
        """Sets the depositant_alias of this MessageDepositReceived.

        Es el alias de la cuenta CLABE del depositante en caso que la transferencia se reciba de una cuenta de depositante  # noqa: E501

        :param depositant_alias: The depositant_alias of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._depositant_alias = depositant_alias

    @property
    def depositant_clabe(self):
        """Gets the depositant_clabe of this MessageDepositReceived.  # noqa: E501

        Es la cuenta CLABE del depositante en caso que la transferencia se reciba en una cuenta de depositante  # noqa: E501

        :return: The depositant_clabe of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._depositant_clabe

    @depositant_clabe.setter
    def depositant_clabe(self, depositant_clabe):
        """Sets the depositant_clabe of this MessageDepositReceived.

        Es la cuenta CLABE del depositante en caso que la transferencia se reciba en una cuenta de depositante  # noqa: E501

        :param depositant_clabe: The depositant_clabe of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._depositant_clabe = depositant_clabe

    @property
    def depositant_email(self):
        """Gets the depositant_email of this MessageDepositReceived.  # noqa: E501

        Es el Correo electrónico (email) del depositante en caso que la transferencia se reciba en una cuenta de depositante  # noqa: E501

        :return: The depositant_email of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._depositant_email

    @depositant_email.setter
    def depositant_email(self, depositant_email):
        """Sets the depositant_email of this MessageDepositReceived.

        Es el Correo electrónico (email) del depositante en caso que la transferencia se reciba en una cuenta de depositante  # noqa: E501

        :param depositant_email: The depositant_email of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._depositant_email = depositant_email

    @property
    def depositant_rfc(self):
        """Gets the depositant_rfc of this MessageDepositReceived.  # noqa: E501

        Es el Registro Federal de Contribuyentes (RFC) del depositante, en caso que la transferencia se reciba en una cuenta de depositante.  # noqa: E501

        :return: The depositant_rfc of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._depositant_rfc

    @depositant_rfc.setter
    def depositant_rfc(self, depositant_rfc):
        """Sets the depositant_rfc of this MessageDepositReceived.

        Es el Registro Federal de Contribuyentes (RFC) del depositante, en caso que la transferencia se reciba en una cuenta de depositante.  # noqa: E501

        :param depositant_rfc: The depositant_rfc of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._depositant_rfc = depositant_rfc

    @property
    def description(self):
        """Gets the description of this MessageDepositReceived.  # noqa: E501

        Es el concepto de la transferencia.  # noqa: E501

        :return: The description of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MessageDepositReceived.

        Es el concepto de la transferencia.  # noqa: E501

        :param description: The description of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def monex_description(self):
        """Gets the monex_description of this MessageDepositReceived.  # noqa: E501

        Es la descripción de Monex para la transferencia.  # noqa: E501

        :return: The monex_description of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._monex_description

    @monex_description.setter
    def monex_description(self, monex_description):
        """Sets the monex_description of this MessageDepositReceived.

        Es la descripción de Monex para la transferencia.  # noqa: E501

        :param monex_description: The monex_description of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._monex_description = monex_description

    @property
    def monex_transaction_id(self):
        """Gets the monex_transaction_id of this MessageDepositReceived.  # noqa: E501

        Es el identificador asignado por Monex a la transferencia.  # noqa: E501

        :return: The monex_transaction_id of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._monex_transaction_id

    @monex_transaction_id.setter
    def monex_transaction_id(self, monex_transaction_id):
        """Sets the monex_transaction_id of this MessageDepositReceived.

        Es el identificador asignado por Monex a la transferencia.  # noqa: E501

        :param monex_transaction_id: The monex_transaction_id of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._monex_transaction_id = monex_transaction_id

    @property
    def reference(self):
        """Gets the reference of this MessageDepositReceived.  # noqa: E501

        Es la referecia de la transferencia.  # noqa: E501

        :return: The reference of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this MessageDepositReceived.

        Es la referecia de la transferencia.  # noqa: E501

        :param reference: The reference of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def sender_account(self):
        """Gets the sender_account of this MessageDepositReceived.  # noqa: E501

        Es la cuenta del ordenante que podría ser un número celular (10 dígitos), una tarjeta de débito (TDD, de 16 dígitos) o Cuenta CLABE interbancaria (18 dígitos).  # noqa: E501

        :return: The sender_account of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._sender_account

    @sender_account.setter
    def sender_account(self, sender_account):
        """Sets the sender_account of this MessageDepositReceived.

        Es la cuenta del ordenante que podría ser un número celular (10 dígitos), una tarjeta de débito (TDD, de 16 dígitos) o Cuenta CLABE interbancaria (18 dígitos).  # noqa: E501

        :param sender_account: The sender_account of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._sender_account = sender_account

    @property
    def sender_bank(self):
        """Gets the sender_bank of this MessageDepositReceived.  # noqa: E501


        :return: The sender_bank of this MessageDepositReceived.  # noqa: E501
        :rtype: MessageInstitution
        """
        return self._sender_bank

    @sender_bank.setter
    def sender_bank(self, sender_bank):
        """Sets the sender_bank of this MessageDepositReceived.


        :param sender_bank: The sender_bank of this MessageDepositReceived.  # noqa: E501
        :type: MessageInstitution
        """

        self._sender_bank = sender_bank

    @property
    def sender_name(self):
        """Gets the sender_name of this MessageDepositReceived.  # noqa: E501

        Es el nombre del ordenante.  # noqa: E501

        :return: The sender_name of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name):
        """Sets the sender_name of this MessageDepositReceived.

        Es el nombre del ordenante.  # noqa: E501

        :param sender_name: The sender_name of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._sender_name = sender_name

    @property
    def sender_rfc(self):
        """Gets the sender_rfc of this MessageDepositReceived.  # noqa: E501

        Es el Registro Federal de Contribuyente (RFC) del ordenante.  # noqa: E501

        :return: The sender_rfc of this MessageDepositReceived.  # noqa: E501
        :rtype: str
        """
        return self._sender_rfc

    @sender_rfc.setter
    def sender_rfc(self, sender_rfc):
        """Sets the sender_rfc of this MessageDepositReceived.

        Es el Registro Federal de Contribuyente (RFC) del ordenante.  # noqa: E501

        :param sender_rfc: The sender_rfc of this MessageDepositReceived.  # noqa: E501
        :type: str
        """

        self._sender_rfc = sender_rfc

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
        if issubclass(MessageDepositReceived, dict):
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
        if not isinstance(other, MessageDepositReceived):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
