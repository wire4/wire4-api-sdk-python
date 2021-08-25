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
from wire4_client.models.beneficiary_institution import BeneficiaryInstitution  # noqa: F401,E501
from wire4_client.models.institution import Institution  # noqa: F401,E501


class SpidBeneficiaryResponse(object):
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
        'amount_limit': 'float',
        'authorization_date': 'datetime',
        'bank': 'Institution',
        'beneficiary_account': 'str',
        'email': 'list[str]',
        'institution': 'BeneficiaryInstitution',
        'kind_of_relationship': 'str',
        'numeric_reference_spid': 'str',
        'payment_concept_spid': 'str',
        'register_date': 'datetime',
        'relationship': 'str',
        'rfc': 'str',
        'status': 'str'
    }

    attribute_map = {
        'amount_limit': 'amount_limit',
        'authorization_date': 'authorization_date',
        'bank': 'bank',
        'beneficiary_account': 'beneficiary_account',
        'email': 'email',
        'institution': 'institution',
        'kind_of_relationship': 'kind_of_relationship',
        'numeric_reference_spid': 'numeric_reference_spid',
        'payment_concept_spid': 'payment_concept_spid',
        'register_date': 'register_date',
        'relationship': 'relationship',
        'rfc': 'rfc',
        'status': 'status'
    }

    def __init__(self, amount_limit=None, authorization_date=None, bank=None, beneficiary_account=None, email=None, institution=None, kind_of_relationship=None, numeric_reference_spid=None, payment_concept_spid=None, register_date=None, relationship=None, rfc=None, status=None):  # noqa: E501
        """SpidBeneficiaryResponse - a model defined in Swagger"""  # noqa: E501
        self._amount_limit = None
        self._authorization_date = None
        self._bank = None
        self._beneficiary_account = None
        self._email = None
        self._institution = None
        self._kind_of_relationship = None
        self._numeric_reference_spid = None
        self._payment_concept_spid = None
        self._register_date = None
        self._relationship = None
        self._rfc = None
        self._status = None
        self.discriminator = None
        self.amount_limit = amount_limit
        if authorization_date is not None:
            self.authorization_date = authorization_date
        if bank is not None:
            self.bank = bank
        self.beneficiary_account = beneficiary_account
        if email is not None:
            self.email = email
        self.institution = institution
        self.kind_of_relationship = kind_of_relationship
        if numeric_reference_spid is not None:
            self.numeric_reference_spid = numeric_reference_spid
        if payment_concept_spid is not None:
            self.payment_concept_spid = payment_concept_spid
        if register_date is not None:
            self.register_date = register_date
        self.relationship = relationship
        if rfc is not None:
            self.rfc = rfc
        if status is not None:
            self.status = status

    @property
    def amount_limit(self):
        """Gets the amount_limit of this SpidBeneficiaryResponse.  # noqa: E501

        Monto límite permitido para la cuenta. Ejemplo: 1000.00  # noqa: E501

        :return: The amount_limit of this SpidBeneficiaryResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount_limit

    @amount_limit.setter
    def amount_limit(self, amount_limit):
        """Sets the amount_limit of this SpidBeneficiaryResponse.

        Monto límite permitido para la cuenta. Ejemplo: 1000.00  # noqa: E501

        :param amount_limit: The amount_limit of this SpidBeneficiaryResponse.  # noqa: E501
        :type: float
        """
        if amount_limit is None:
            raise ValueError("Invalid value for `amount_limit`, must not be `None`")  # noqa: E501

        self._amount_limit = amount_limit

    @property
    def authorization_date(self):
        """Gets the authorization_date of this SpidBeneficiaryResponse.  # noqa: E501

        La fecha en la que se registro el beneficiario.  # noqa: E501

        :return: The authorization_date of this SpidBeneficiaryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._authorization_date

    @authorization_date.setter
    def authorization_date(self, authorization_date):
        """Sets the authorization_date of this SpidBeneficiaryResponse.

        La fecha en la que se registro el beneficiario.  # noqa: E501

        :param authorization_date: The authorization_date of this SpidBeneficiaryResponse.  # noqa: E501
        :type: datetime
        """

        self._authorization_date = authorization_date

    @property
    def bank(self):
        """Gets the bank of this SpidBeneficiaryResponse.  # noqa: E501


        :return: The bank of this SpidBeneficiaryResponse.  # noqa: E501
        :rtype: Institution
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """Sets the bank of this SpidBeneficiaryResponse.


        :param bank: The bank of this SpidBeneficiaryResponse.  # noqa: E501
        :type: Institution
        """

        self._bank = bank

    @property
    def beneficiary_account(self):
        """Gets the beneficiary_account of this SpidBeneficiaryResponse.  # noqa: E501

        Cuenta del beneficiario debe ser una cuenta CLABE. Ejemplo: 032180000118359719.  # noqa: E501

        :return: The beneficiary_account of this SpidBeneficiaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_account

    @beneficiary_account.setter
    def beneficiary_account(self, beneficiary_account):
        """Sets the beneficiary_account of this SpidBeneficiaryResponse.

        Cuenta del beneficiario debe ser una cuenta CLABE. Ejemplo: 032180000118359719.  # noqa: E501

        :param beneficiary_account: The beneficiary_account of this SpidBeneficiaryResponse.  # noqa: E501
        :type: str
        """
        if beneficiary_account is None:
            raise ValueError("Invalid value for `beneficiary_account`, must not be `None`")  # noqa: E501

        self._beneficiary_account = beneficiary_account

    @property
    def email(self):
        """Gets the email of this SpidBeneficiaryResponse.  # noqa: E501

        Lista de correos electrónicos (emails), este dato es opcional.  # noqa: E501

        :return: The email of this SpidBeneficiaryResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SpidBeneficiaryResponse.

        Lista de correos electrónicos (emails), este dato es opcional.  # noqa: E501

        :param email: The email of this SpidBeneficiaryResponse.  # noqa: E501
        :type: list[str]
        """

        self._email = email

    @property
    def institution(self):
        """Gets the institution of this SpidBeneficiaryResponse.  # noqa: E501


        :return: The institution of this SpidBeneficiaryResponse.  # noqa: E501
        :rtype: BeneficiaryInstitution
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """Sets the institution of this SpidBeneficiaryResponse.


        :param institution: The institution of this SpidBeneficiaryResponse.  # noqa: E501
        :type: BeneficiaryInstitution
        """
        if institution is None:
            raise ValueError("Invalid value for `institution`, must not be `None`")  # noqa: E501

        self._institution = institution

    @property
    def kind_of_relationship(self):
        """Gets the kind_of_relationship of this SpidBeneficiaryResponse.  # noqa: E501

        Es el tipo de relación que se tiene con el propietario de la cuenta. Para registrar una cuenta, este valor se debe obtener del recurso <a href=\"#operation/getAvailableRelationshipsMonexUsingGET\"> relationships.</a> <br /><br /><b>Nota:</b> <em>Si en la respuesta de Monex esta propiedad es nula, tampoco estará presente en esta respuesta.</em>  # noqa: E501

        :return: The kind_of_relationship of this SpidBeneficiaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._kind_of_relationship

    @kind_of_relationship.setter
    def kind_of_relationship(self, kind_of_relationship):
        """Sets the kind_of_relationship of this SpidBeneficiaryResponse.

        Es el tipo de relación que se tiene con el propietario de la cuenta. Para registrar una cuenta, este valor se debe obtener del recurso <a href=\"#operation/getAvailableRelationshipsMonexUsingGET\"> relationships.</a> <br /><br /><b>Nota:</b> <em>Si en la respuesta de Monex esta propiedad es nula, tampoco estará presente en esta respuesta.</em>  # noqa: E501

        :param kind_of_relationship: The kind_of_relationship of this SpidBeneficiaryResponse.  # noqa: E501
        :type: str
        """
        if kind_of_relationship is None:
            raise ValueError("Invalid value for `kind_of_relationship`, must not be `None`")  # noqa: E501

        self._kind_of_relationship = kind_of_relationship

    @property
    def numeric_reference_spid(self):
        """Gets the numeric_reference_spid of this SpidBeneficiaryResponse.  # noqa: E501

        Referencia numérica.  # noqa: E501

        :return: The numeric_reference_spid of this SpidBeneficiaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._numeric_reference_spid

    @numeric_reference_spid.setter
    def numeric_reference_spid(self, numeric_reference_spid):
        """Sets the numeric_reference_spid of this SpidBeneficiaryResponse.

        Referencia numérica.  # noqa: E501

        :param numeric_reference_spid: The numeric_reference_spid of this SpidBeneficiaryResponse.  # noqa: E501
        :type: str
        """

        self._numeric_reference_spid = numeric_reference_spid

    @property
    def payment_concept_spid(self):
        """Gets the payment_concept_spid of this SpidBeneficiaryResponse.  # noqa: E501

        Concepto de pago.  # noqa: E501

        :return: The payment_concept_spid of this SpidBeneficiaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_concept_spid

    @payment_concept_spid.setter
    def payment_concept_spid(self, payment_concept_spid):
        """Sets the payment_concept_spid of this SpidBeneficiaryResponse.

        Concepto de pago.  # noqa: E501

        :param payment_concept_spid: The payment_concept_spid of this SpidBeneficiaryResponse.  # noqa: E501
        :type: str
        """

        self._payment_concept_spid = payment_concept_spid

    @property
    def register_date(self):
        """Gets the register_date of this SpidBeneficiaryResponse.  # noqa: E501

        La fecha en la que se registro el beneficiario.  # noqa: E501

        :return: The register_date of this SpidBeneficiaryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._register_date

    @register_date.setter
    def register_date(self, register_date):
        """Sets the register_date of this SpidBeneficiaryResponse.

        La fecha en la que se registro el beneficiario.  # noqa: E501

        :param register_date: The register_date of this SpidBeneficiaryResponse.  # noqa: E501
        :type: datetime
        """

        self._register_date = register_date

    @property
    def relationship(self):
        """Gets the relationship of this SpidBeneficiaryResponse.  # noqa: E501

        Es la relación con el propietario de la cuenta, para registrar este valor se debe obtener del recurso <a href=\"#operation/getAvailableRelationshipsMonexUsingGET\">relationships.</a> <br/> <br/> <b>Nota:</b> Si en la respuesta de Monex, sta propiedad es nula, tampoco estará presente en esta respuesta.  # noqa: E501

        :return: The relationship of this SpidBeneficiaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """Sets the relationship of this SpidBeneficiaryResponse.

        Es la relación con el propietario de la cuenta, para registrar este valor se debe obtener del recurso <a href=\"#operation/getAvailableRelationshipsMonexUsingGET\">relationships.</a> <br/> <br/> <b>Nota:</b> Si en la respuesta de Monex, sta propiedad es nula, tampoco estará presente en esta respuesta.  # noqa: E501

        :param relationship: The relationship of this SpidBeneficiaryResponse.  # noqa: E501
        :type: str
        """
        if relationship is None:
            raise ValueError("Invalid value for `relationship`, must not be `None`")  # noqa: E501

        self._relationship = relationship

    @property
    def rfc(self):
        """Gets the rfc of this SpidBeneficiaryResponse.  # noqa: E501

        Es el Registro federal de contribuyentes (RFC) de la persona o institución propietaria de la cuenta. <br/> <br/><b>Nota:</b> Se valida el formato de RFC.  # noqa: E501

        :return: The rfc of this SpidBeneficiaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._rfc

    @rfc.setter
    def rfc(self, rfc):
        """Sets the rfc of this SpidBeneficiaryResponse.

        Es el Registro federal de contribuyentes (RFC) de la persona o institución propietaria de la cuenta. <br/> <br/><b>Nota:</b> Se valida el formato de RFC.  # noqa: E501

        :param rfc: The rfc of this SpidBeneficiaryResponse.  # noqa: E501
        :type: str
        """

        self._rfc = rfc

    @property
    def status(self):
        """Gets the status of this SpidBeneficiaryResponse.  # noqa: E501

        El estado en el que se encuentra el registo del beneficiario.<br><br> Los valores pueden ser: <b>\"RECEIVED\", \"DELETED\", \"REQUEST_ERROR_BY_MONEX\", \"REQUESTED_TO_MONEX\", \"NOTIFIED_BY_MONEX\", \"NOTIFIED_BY_SPEIOK\", \"NOTIFIED_WITH_ERROR_BY_SPEIOK\" y \"PENDING\"</b>  # noqa: E501

        :return: The status of this SpidBeneficiaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SpidBeneficiaryResponse.

        El estado en el que se encuentra el registo del beneficiario.<br><br> Los valores pueden ser: <b>\"RECEIVED\", \"DELETED\", \"REQUEST_ERROR_BY_MONEX\", \"REQUESTED_TO_MONEX\", \"NOTIFIED_BY_MONEX\", \"NOTIFIED_BY_SPEIOK\", \"NOTIFIED_WITH_ERROR_BY_SPEIOK\" y \"PENDING\"</b>  # noqa: E501

        :param status: The status of this SpidBeneficiaryResponse.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(SpidBeneficiaryResponse, dict):
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
        if not isinstance(other, SpidBeneficiaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
