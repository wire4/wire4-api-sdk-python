# coding: utf-8

# flake8: noqa
"""
    Wire4RestAPI

    Referencia de la API de Wire4  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from wire4_client.models.account import Account
from wire4_client.models.account_request import AccountRequest
from wire4_client.models.account_response import AccountResponse
from wire4_client.models.account_spid import AccountSpid
from wire4_client.models.amount_request import AmountRequest
from wire4_client.models.balance import Balance
from wire4_client.models.balance_list_response import BalanceListResponse
from wire4_client.models.beneficiaries_query_register_status import BeneficiariesQueryRegisterStatus
from wire4_client.models.beneficiaries_response import BeneficiariesResponse
from wire4_client.models.beneficiary_institution import BeneficiaryInstitution
from wire4_client.models.billing import Billing
from wire4_client.models.billing_transaction import BillingTransaction
from wire4_client.models.cep_response import CepResponse
from wire4_client.models.cep_search_banxico import CepSearchBanxico
from wire4_client.models.contact_request import ContactRequest
from wire4_client.models.deposit import Deposit
from wire4_client.models.depositant import Depositant
from wire4_client.models.depositants_register import DepositantsRegister
from wire4_client.models.depositants_response import DepositantsResponse
from wire4_client.models.error_response import ErrorResponse
from wire4_client.models.get_depositants import GetDepositants
from wire4_client.models.institution import Institution
from wire4_client.models.institutions_list import InstitutionsList
from wire4_client.models.message_account_beneficiary import MessageAccountBeneficiary
from wire4_client.models.message_cep import MessageCEP
from wire4_client.models.message_deposit_received import MessageDepositReceived
from wire4_client.models.message_institution import MessageInstitution
from wire4_client.models.message_payment import MessagePayment
from wire4_client.models.message_request_changed import MessageRequestChanged
from wire4_client.models.message_subscription import MessageSubscription
from wire4_client.models.message_web_hook import MessageWebHook
from wire4_client.models.payment import Payment
from wire4_client.models.payments_request_id import PaymentsRequestId
from wire4_client.models.person import Person
from wire4_client.models.pre_enrollment_data import PreEnrollmentData
from wire4_client.models.pre_enrollment_response import PreEnrollmentResponse
from wire4_client.models.relationship import Relationship
from wire4_client.models.relationships_response import RelationshipsResponse
from wire4_client.models.spid_beneficiaries_response import SpidBeneficiariesResponse
from wire4_client.models.spid_beneficiary_response import SpidBeneficiaryResponse
from wire4_client.models.spid_classification_dto import SpidClassificationDTO
from wire4_client.models.spid_classifications_response_dto import SpidClassificationsResponseDTO
from wire4_client.models.timestamp import Timestamp
from wire4_client.models.token_required_response import TokenRequiredResponse
from wire4_client.models.transaction_outgoing import TransactionOutgoing
from wire4_client.models.transaction_outgoing_spid import TransactionOutgoingSpid
from wire4_client.models.transactions_outgoing_register import TransactionsOutgoingRegister
from wire4_client.models.webhook_request import WebhookRequest
from wire4_client.models.webhook_response import WebhookResponse
from wire4_client.models.webhooks_list import WebhooksList
