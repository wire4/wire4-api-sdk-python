# coding: utf-8

"""
    Wire4RestAPI

     # Referencia de API La API de Wire4 está organizada en torno a REST. Nuestra API tiene URLs predecibles orientadas a los recursos, acepta peticiones en formato JSON, y las respuestas devueltas son formato JSON y utiliza códigos de respuesta HTTP, autenticación y verbos estándares.  Puede usar la API de Wire4 en nuestro entorno de prueba, que no afecta sus productivos ni interactúa con la red bancaria. La URL de conexión que se usa para invocar los servicios determina si la solicitud es en modo en de prueba o en modo producción.    # Autenticación La API de Wire4 utiliza el protocolo OAuth 2.0 para autenticación y autorización.   Para comenzar, es necesario que registre una cuenta en nuestro ambiente de pruebas en [registro](https://app-sndbx.wire4.mx/#/register) y obtenga las credenciales de cliente OAuth 2.0 desde la [consola de administración](https://app-sndbx.wire4.mx/#/dashboard/api-keys).   Esta página ofrece una descripción general de los escenarios de autorización de OAuth 2.0 que admite Wire4.   Después de crear su aplicación con Wire4, asegúrese de tener a la mano su `client_id` y `client_secret`. El siguiente paso es descubrir qué flujo de OAuth2 es el adecuado para sus propósitos.   ## URLS La siguiente tabla muestra las urls de los recursos de autenticación para el ambiente de pruebas.  URL                  | Descripción ------------------------------------ | ------------- https://sandbox-api.wire4.mx/token   | Obtener token de autorización llaves de API (*client_id*, *client_secret*), datos de suscripción (*client_id*, *client_secret*, *user_key*, *user_secret*) o (*refresh_token*) https://sandbox-api.wire4.mx/revoke  | Revocación de token  **Nota:** De acuerdo con el RFC 6749, la URL del token sólo acepta el tipo de contenido x-www-form-urlencoded. El contenido JSON no está permitido y devolverá un error.  ## Scopes Los `scopes` limitan el acceso de una aplicación a los recursos de Wire4. Se ofrecen los siguientes scopes de acuerdo al producto:  Producto                             |Scope                      | Descripción -------------------------------------|------------------------------------ | ------------- SPEI-SPID                            |general                              | Permite llamar a operaciones que no requieren a un cliente Monex suscrito en Wire4, los recursos que se pueden consumir con este scope son: consulta de Instituciones, CEP y generación de una presuscripción. SPEI-SPID                            |spei_admin                           | Permite llamar a operaciones que requieren de un cliente Monex suscrito en Wire4, ya que se proporciona información de saldos, administración de transacciones, cuentas de beneficiarios y cuentas de depositantes. SPEI-SPID                            |spid_admin                           | Permite llamar sólo a operaciones SPID, se requiere de un cliente Monex suscrito en Wire4. CODI                                 |codi_general                         | Permite llamar a operaciones de administración sobre el producto CoDi, como creación y listado de empresas  CODI                                 |codi_admin                           | Permite llamar sólo a operaciones CoDi dentro de un punto de venta, las operaciones incluyen creación, consulta, listado, etc de peticiones de pago CODI                                 |codi_report                          | Permite generar reportes de operaciones CoDi. TODOS                                |device_[dispositivo]                 | Se debe especificar cuando se gestionan token's desde distintos dispositivos.  ## Tipos de autenticación   Wire4 cuenta con dos tipos de autenticación: Autenticación de Aplicación (OAuth 2.0  Client Credentials Grant)  y Autenticación de Usuario de Aplicación (OAuth 2.0 Password Grant).  ### Autenticación de Aplicación  Esta autenticación se obtiene proporcionando únicamente las llaves de API las cuales se pueden consultar en [Llaves de API](https://app-sndbx.wire4.mx/#/dashboard/api-keys) de la consola de administración.  La autenticación de aplicación permite accesso a recursos generales y de administración que dependeran del scope.  Para este tipo de autenticación se sigue el flujo OAuth 2.0 Client Credentials Grant, que se describe más adelante en **Obtener el token de acceso de aplicación**, algunos de los recursos que requieren este tipo de autenticación son:   * [/subscriptions/pre-subscription](link) * [/institutions](link>) * [/ceps](<link>) * [/codi/compaies](<link>)  ### Autenticación de Usuario de Aplicación  Esta autenticación se obtiene proporcionando las llaves de API las cuales se pueden consultar en [Llaves de API](https://app-sndbx.wire4.mx/#/dashboard/api-keys) más el ***user_key*** y ***user_secret*** que se proporcionan al momento de crear una suscripción o un punto de venta, para más información puedes consultar las guías [creación de suscripción](https://www.wire4.mx/#/guides/subscriptions), [creación de punto de venta](https://www.wire4.mx/#/guides/salespoint).  Con este tipo de autenticación se puede acceder a los recursos especificos que requieren configuraciones y acceso mas puntual como información de una cuentas, saldos y administración de transacciones SPEID-SPID o CODI.    ## Obtener token de acceso Antes de que su aplicación pueda acceder a los datos mediante la API de Wire4, debe obtener un token de acceso ***(access_token)*** que le otorgue acceso a la API. En las siguientes secciones se muestra como obtener un token para cada una de las autenticaciones.     ### Obtener el token de acceso para autenticación de aplicación  El primer paso es crear la solicitud de token de acceso (*access_token*), con los parámetros que identifican su aplicación, el siguiente código muestra cómo obtener un `token`.  ``` curl -k -d \"grant_type= client_credentials&scope=general\"  -u \"<client id>:<client secret>\" https://sandbox-api.wire4.mx/token ``` **Ejemplo:**   ``` curl -k -d \"grant_type=client_credentials&scope=general\"  -u \"8e59YqaFW_Yo5dwWNxEY8Lid0u0a:AXahn79hfKWBXKzQfj011x8cvcQa\"  https://sandbox-api.wire4.mx /token ``` Obtendrá una respuesta como la que se muestra  a continuación, donde se debe obtener el *access_token* para realizar llamadas posteriores a la API.   ``` {     \"access_token\":\"eyJ4NXQiOiJZak5sWVdWa05tWmlNR1ZoTldSaU1EUXpaREJpWlRJNU1qYzFZV1ZoWWpneU5UYzJPV05sWVEiLCJraWQiOiJZak5sWVdWa05tWmlNR1ZoTldSaU1EUXpaREJpWlRJNU1qYzFZV1ZoWWpneU5UYzJPV05sWVEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpc21hZWwuZXNjYW1pbGxhQHRjcGlwLnRlY2hAc2FuZGJveC5zcGVpb2suY29tIiwiYXVkIjoiOGU1OVlxYUZXX1lvNWR3V054RVk4TGlkMHUwYSIsIm5iZiI6MTU3MTMyMDg3NywiYXpwIjoiOGU1OVlxYUZXX1lvNWR3V054RVk4TGlkMHUwYSIsInNjb3BlIjoiYW1fYXBwbGljYXRpb25fc2NvcGUgZ2VuZXJhbCIsImlzcyI6ImFwaW0taWRwIiwiZXhwIjoxNTcxMzI0NDc3LCJpYXQiOjE1NzEzMjA4NzcsImp0aSI6ImJkMTdjMjcyLTg4MGQtNDk0ZS1iMTMwLTBiYTkwMjYyN2M4NCJ9.AjngGylkd_Chs5zlIjyLRPu9xPGyz4dfCd_aax2_ts653xrnNMoLpVHUDmaxIDFF2XyBJKH2IAbKxjo6VsFM07QkoPhlysO1PLoAF-Vkt4xYkh-f7nJRl0oOe2utDWFlUdgiAOmx5tPcStrdCEftgNNrjwJ50LXysFjXVshpoST-zIJPLgXknM3esGrkAsLcZRM7XUB187jxLHbtefVYPMvSO31T9pd5_Co9UXdeHpuA98sk_wZknASM1phxXQZAMLRLHz3LYvjCWCr_v80oVCM9SWTzf0vrMI6xphoIfirfWloADKPTTSUpIGBw9ePF_WbEPvbMm_BZaApJcEH2w\",    \"scope\":\"am_application_scope general\",    \"token_type\":\"Bearer\",    \"expires_in\":3600 }  ```  Es posible generar tokens con mas de un scope, en caso que sea necesario utilizar dicho token para hacer mas de una operación. Para generarlo basta con agregarlo a la petición separado por un espacio.     ``` curl -k -d \"grant_type=client_credentials&scope=codi_general codi_report\"  -u \"8e59YqaFW_Yo5dwWNxEY8Lid0u0a:AXahn79hfKWBXKzQfj011x8cvcQa\"  https://sandbox-api.wire4.mx /token ```  ### Obtener el token de acceso para autenticación usuario de aplicación   Antes de que su aplicación pueda acceder a los datos de una cuenta Monex mediante la API de Wire4, debe obtener un token de acceso  (*access_token*) que le otorgue acceso a la API y contar con el  *user_key* y *user_secret* que se proporcionan al momento de crear  una suscripción para más información puedes consultar [creación de suscripción](https://wire4.mx/#/guides/subscriptions) .   El primer paso es crear la solicitud de token de acceso con los parámetros que identifican su aplicación y la suscripción y con `scope` `spei_admin`  ```   curl -k -d \"grant_type=password&scope=spei_admin&username=<user_key>&password=<user_secret>\"  -u \"<client_id>:<client_secret>\" https://sandbox-api.wire4.mx/token ``` **Ejemplo**  ``` curl -k -d \"grant_type=password&scope=spei_admin&username=6 nbC5e99tTO@sandbox.wire4com&password= Nz7IqJGe9h\" -u \" zgMlQbqmOr:plkMJoPXCI\" https://sandbox-api.wire4.mx /token  ```  ``` {     \"access_token\":\"eyJ4NXQiOiJPR1EyTURFM00yTmpObVZoTnpFeE5EWXlObUV4TURKa01qUTJaVEU0TWpGaE1tVmlZakV5TkEiLCJraWQiOiJPR1EyTURFM00yTmpObVZoTnpFeE5EWXlObUV4TURKa01qUTJaVEU0TWpGaE1tVmlZakV5TkEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIzMzE0ODRlZTdjZDRkYWU5MzRmMjY2Zjc5YmY1YWFAZGV2LWllc2NhbWlsbGEuc3BlaW9rLmNvbSIsImF1ZCI6IkJVR0xjNWw1bW5CZXlPeGxtamNUZ0JoS19WTWEiLCJuYmYiOjE1NzEzNDk4ODMsImF6cCI6IkJVR0xjNWw1bW5CZXlPeGxtamNUZ0JoS19WTWEiLCJzY29wZSI6InNwZWlfYWRtaW4iLCJpc3MiOiJhcGltLWlkcCIsImV4cCI6MTU3MTM1MzQ4MywiaWF0IjoxNTcxMzQ5ODgzLCJqdGkiOiJiOWQ1M2Q0MC0xN2MwLTQxOTItYjUwNy0wZWFhN2ZkNDA1MGYifQ.hLTk8AFoIce1GpLcgch-U5aLLgiiFTo49wfBErD8D6VF-H9sG13ZyfAx9T-vQkk2m1zPapYVQjwibz3GRAJMN0Vczs6flV1mUJwFDQbEE-AELPdRcaRFOMBCfF6H9TVLfhFsGb9U2pVR9TLJcKqR57DyO_dIcc9I6d0tIkxqn2VcqypLVi5YQf36WzBbPeG-iPHYpMA-bhr4rwfjKA-O6jm1NSSxNHF4sHS0YHDPoO_x6cCc677MQEe0_CozfnQhoEWNfG8tcWUqhPtmcfjqon1p7PdQoXxriq_R85d06pVO9Se7Q6ok0V8Qgz0MOJ6z3ku6mtZSuba7niMAOt2TyA\",    \"refresh_token\":\"f962d5c6-0d99-3809-8275-11c7aa0aa020\",    \"scope\":\"spei_admin\",    \"token_type\":\"Bearer\",    \"expires_in\":3600 } ```  **Nota:** Los ejemplos anteriores se presentan considerando que se realiza una implementación desde cero,  esto se puede simplificar a sólo configurar sus llaves (*client_id*, *client_secret*),  datos de suscripción (*client_id*, *client_secret*, *user_key*, *user_secret*) si utiliza nuestros sdks.      **Consideraci&oacute;n:** Si la aplicaci&oacute;n en la que implementar&aacute; Wire4 estar&aacute; desplegada en mas de una instancia o servidor en cada solicitud de token debe especificar un scope adicional. La forma de hacer esto es que cuando se solicita un token se debe especificar un scope adicional con el prefijo \"device_\" +  el dispositivo, por ejemplo:                                                                                                                                                                                                                     device_server1<br> device_server2  en consecuencia cada instancia debe operar con el token gestionado. ***Si se opera con el mismo token en instancias diferentes encontrará problemas de Credenciales Inv&aacute;lidas.***  **Ejemplo de solicitud de token para instancias diferentes:**  ``` curl -k -d \"grant_type=password&username=0883b97333046abb76367698b57d9e@sandbox.wire4.mx&password=9e0d81f95705079b9fe1e129315c25&scope=device_server1 codi_admin\" -H \"Authorization: Basic dmZSeURpTHdFbVZqd2VIclp0OWRMbXFmb3YwYTpJQJBuamBac3V6SllLWlJHUkJEYUZrN1BhRmNh\" https://sandbox-api.wire4.mx/token  curl -k -d \"grant_type=password&username=0883b97333046abb76367698b57d9e@sandbox.wire4.mx&password=9e0d81f95705079b9fe1e129315c25&scope=device_server2 codi_admin\" -H \"Authorization: Basic dmZSeURpTHdFbVZqd2VIclp0OWRMbXFmb3YwYTpJQJBuamBac3V6SllLWlJHUkJEYUZrN1BhRmNh\" https://sandbox-api.wire4.mx/token ```  ## Caducidad del token El token de acceso es válido durante 60 minutos (una hora), después de transcurrido este tiempo se debe solicitar un nuevo token,  cuando el token caduca se obtendrá un error ***401 Unauthorized*** con mensaje ***“Invalid Credentials”.***   El nuevo token se puede solicitar  utilizando el último token de actualización (***refresh_token***) que se devolvió en la solicitud del token,   esto sólo aplica para el token de tipo password (Autenticación de Usuario de Aplicación). El siguiente ejemplo muestra cómo obtener un toke con el token de actualización.  ``` curl -k -d \"grant_type=refresh_token&refresh_token=<refresh_token>\" -u \" Client_Id:Client_Secret\" -H \"Content-Type: application/x-www-form-urlencoded\" https://sandbox-api.wire4.mx/oauth2/token ```  **Ejemplo:**  ``` curl -k -d \"grant_type=refresh_token&refresh_token=f932d5c6-0d39-3809-8275-11c7ax0aa020\" -u \"zgMlQbqmOr:plkMJoPXCI\" -H \"Content-Type: application/x-www-form-urlencoded\" https://sandbox-api.wire4.mx/token ```  El token de actualización (***refresh_token***) tiene una duración de hasta 23 horas. Si en este periodo no se utiliza, se tienen que solicitar un nuevo token.  Un token de acceso podría dejar de funcionar por uno de estos motivos:  * El usuario ha revocado el acceso a su aplicación, si un usuario ha solicitado la baja de su aplicación de WIre4. * El token de acceso ha caducado: si el token de acceso ha pasado de una hora, recibirá un error ***401 Unauthorized*** mientras realiza una llamada a la API de Wire4. Cuando esto sucede, debe solicitar un nuevo token utilizando el token de actualización que recibió por última al solicitar un token, sólo aplica si el token en cuestión es de autenticación de usuario de aplicación, en caso contrario solicitar un nuevo token.   ## Revocar token Su aplicación puede revocar mediante programación el token de acceso, una vez revocado el token no podrá hacer uso de él para acceder a la API. El siguiente código muestra un ejemplo de cómo revocar el token:    ```  curl -X POST --basic -u \"<client id>:<client secret>\" -H \"Content-Type: application/x-www-form-urlencoded;charset=UTF-8\" -k -d \"token=<token to revoke>&token_type_hint=access_token\" https://sandbox-api.wire4.mx/revoke ```      **Ejemplo:**  ```   curl -X POST --basic -u \"8e59YqaFW_Yo5dwWNxEY8Lid0u0a:AXahn79hfKWBXKzQfj011x8cvcQa\" -H \"Content-Type: application/x-www-form-urlencoded;charset=UTF-8\" -k -d \"token=eyJ4NXQiOiJZak5sWVdWa05tWmlNR1ZoTldSaU1EUXpaREJpWlRJNU1qYzFZV1ZoWWpneU5UYzJPV05sWVEiLCJraWQiOiJZak5sWVdWa05tWmlNR1ZoTldSaU1EUXpaREJpWlRJNU1qYzFZV1ZoWWpneU5UYzJPV05sWVEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpc21hZWwuZXNjYW1pbGxhQHRjcGlwLnRlY2hAc2FuZGJveC5zcGVpb2suY29tIiwiYXVkIjoiOGU1OVlxYUZXX1lvNWR3V054RVk4TGlkMHUwYSIsIm5iZiI6MTU3MTMyMDg3NywiYXpwIjoiOGU1OVlxYUZXX1lvNWR3V054RVk4TGlkMHUwYSIsInNjb3BlIjoiYW1fYXBwbGljYXRpb25fc2NvcGUgZ2VuZXJhbCIsImlzcyI6ImFwaW0taWRwIiwiZXhwIjoxNTcxMzI0NDc3LCJpYXQiOjE1NzEzMjA4NzcsImp0aSI6ImJkMTdjMjcyLTg4MGQtNDk0ZS1iMTMwLTBiYTkwMjYyN2M4NCJ9.AjngGylkd_Chs5zlIjyLRPu9xPGyz4dfCd_aax2_ts653xrnNMoLpVHUDmaxIDFF2XyBJKH2IAbKxjo6VsFM07QkoPhlysO1PLoAF-Vkt4xYkh-f7nJRl0oOe2utDWFlUdgiAOmx5tPcStrdCEftgNNrjwJ50LXysFjXVshpoST-zIJPLgXknM3esGrkAsLcZRM7XUB187jxLHbtefVYPMvSO31T9pd5_Co9UXdeHpuA98sk_wZknASM1phxXQZAMLRLHz3LYvjCWCr_v80oVCM9SWTzf0vrMI6xphoIfirfWloADKPTTSUpIGBw9ePF_WbEPvbMm_BZaApJcEH2w&token_type_hint=access_token\"  https://sandbox-api.wire4.mx/revoke ```  # Ambientes  Wire4 cuentas con dos ambientes Pruebas (Sandbox) y Producción, son dos ambientes separados los cuales se pueden utilizar simultáneamente. Los usuarios que han sido creados en cada uno de los ambientes no son intercambiables.   Las ligas de acceso a la `api` para cada uno de los ambientes son:  * Pruebas  https://sandbox-api.wire4.mx * Producción https://api.wire4.mx     # Eventos  Los eventos son nuestra forma de informarle cuando algo  sucede en su cuenta. Cuando ocurre un evento se crea un objeto  [Evento](#tag/Webhook-Message). Por ejemplo, cuando se recibe un depósito, se crea un evento TRANSACTION.INCOMING.UPDATED.   Los eventos ocurren cuando cambia el estado de un recurso. El recurso se encuentra dentro del objeto [Evento](#tag/Webhook-Message) en el campo data.  Por ejemplo, un evento TRANSACTION.INCOMING.UPDATED contendrá un depósito y un evento ACCOUNT.CREATED contendrá una cuenta.   Wire4 puede agregar más campos en un futuro, o agregar nuevos valores a campos existentes, por lo que es recomendado que tu endpoint pueda manejar datos adicionales desconocidos. En esta [liga](#tag/Webhook-Message) se encuentra  la definición del objeto [Evento](#tag/Webhook-Message).  ## Tipos de Eventos  Wire4 cuenta con los siguientes tipos de eventos*   | Evento                     | Tipo                               | Objeto                                        | | -------------------------- |----------------------------------- | --------------------------------------------- | | Suscripción                | ENROLLMENT.CREATED                 | [suscription](#tag/subscription)              | | Cuenta de beneficiario     | ACCOUNT.CREATED                    | [beneficiary](#tag/BeneficiaryAccount)           | | Depósito recibido          | TRANSACTION.INCOMING.UPDATED       | [spei_incoming](#tag/deposit)                 | | Transferencia realizada    | TRANSACTION.OUTGOING.RECEIVED      | [spei_outgoing](#tag/transfer)                | | Transferencia SPID enviada | TRANSACTION.OUTGOING.SPID.RECEIVED | [spid_outgoing](#tag/transfer)                | | Transferencias Autorizadas | REQUEST.OUTGOING.CHANGED           | [request_outgoing](#tag/requestOutMsg)        | | Operación CoDi             | CODI.ACTIONS                       |[codi_actions](#tag/codiActions)               | | Punto de venta CoDi        | SALE.POINT.CREATED                 |[codi_sales_point](#tag/codiSalesPoint)        |   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from wire4_client.models.message_institution import MessageInstitution  # noqa: F401,E501


class MessagePaymentStatePending(object):
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
        'account': 'str',
        'amount': 'float',
        'beneficiary_account': 'str',
        'beneficiary_bank': 'MessageInstitution',
        'beneficiary_name': 'str',
        'concept': 'str',
        'currency_code': 'str',
        'detention_message': 'str',
        'error_message': 'str',
        'order_id': 'str',
        'payment_order_id': 'int',
        'pending_reason': 'str',
        'reference': 'int',
        'request_id': 'str',
        'status_code': 'str',
        'transaction_id': 'int'
    }

    attribute_map = {
        'account': 'account',
        'amount': 'amount',
        'beneficiary_account': 'beneficiary_account',
        'beneficiary_bank': 'beneficiary_bank',
        'beneficiary_name': 'beneficiary_name',
        'concept': 'concept',
        'currency_code': 'currency_code',
        'detention_message': 'detention_message',
        'error_message': 'error_message',
        'order_id': 'order_id',
        'payment_order_id': 'payment_order_id',
        'pending_reason': 'pending_reason',
        'reference': 'reference',
        'request_id': 'request_id',
        'status_code': 'status_code',
        'transaction_id': 'transaction_id'
    }

    def __init__(self, account=None, amount=None, beneficiary_account=None, beneficiary_bank=None, beneficiary_name=None, concept=None, currency_code=None, detention_message=None, error_message=None, order_id=None, payment_order_id=None, pending_reason=None, reference=None, request_id=None, status_code=None, transaction_id=None):  # noqa: E501
        """MessagePaymentStatePending - a model defined in Swagger"""  # noqa: E501
        self._account = None
        self._amount = None
        self._beneficiary_account = None
        self._beneficiary_bank = None
        self._beneficiary_name = None
        self._concept = None
        self._currency_code = None
        self._detention_message = None
        self._error_message = None
        self._order_id = None
        self._payment_order_id = None
        self._pending_reason = None
        self._reference = None
        self._request_id = None
        self._status_code = None
        self._transaction_id = None
        self.discriminator = None
        if account is not None:
            self.account = account
        if amount is not None:
            self.amount = amount
        if beneficiary_account is not None:
            self.beneficiary_account = beneficiary_account
        if beneficiary_bank is not None:
            self.beneficiary_bank = beneficiary_bank
        if beneficiary_name is not None:
            self.beneficiary_name = beneficiary_name
        if concept is not None:
            self.concept = concept
        if currency_code is not None:
            self.currency_code = currency_code
        if detention_message is not None:
            self.detention_message = detention_message
        if error_message is not None:
            self.error_message = error_message
        if order_id is not None:
            self.order_id = order_id
        if payment_order_id is not None:
            self.payment_order_id = payment_order_id
        if pending_reason is not None:
            self.pending_reason = pending_reason
        if reference is not None:
            self.reference = reference
        if request_id is not None:
            self.request_id = request_id
        if status_code is not None:
            self.status_code = status_code
        if transaction_id is not None:
            self.transaction_id = transaction_id

    @property
    def account(self):
        """Gets the account of this MessagePaymentStatePending.  # noqa: E501

        Cuenta del ordenante  # noqa: E501

        :return: The account of this MessagePaymentStatePending.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this MessagePaymentStatePending.

        Cuenta del ordenante  # noqa: E501

        :param account: The account of this MessagePaymentStatePending.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def amount(self):
        """Gets the amount of this MessagePaymentStatePending.  # noqa: E501

        Monto de la transferencia  # noqa: E501

        :return: The amount of this MessagePaymentStatePending.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this MessagePaymentStatePending.

        Monto de la transferencia  # noqa: E501

        :param amount: The amount of this MessagePaymentStatePending.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def beneficiary_account(self):
        """Gets the beneficiary_account of this MessagePaymentStatePending.  # noqa: E501

        Cuenta del beneficiario  # noqa: E501

        :return: The beneficiary_account of this MessagePaymentStatePending.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_account

    @beneficiary_account.setter
    def beneficiary_account(self, beneficiary_account):
        """Sets the beneficiary_account of this MessagePaymentStatePending.

        Cuenta del beneficiario  # noqa: E501

        :param beneficiary_account: The beneficiary_account of this MessagePaymentStatePending.  # noqa: E501
        :type: str
        """

        self._beneficiary_account = beneficiary_account

    @property
    def beneficiary_bank(self):
        """Gets the beneficiary_bank of this MessagePaymentStatePending.  # noqa: E501


        :return: The beneficiary_bank of this MessagePaymentStatePending.  # noqa: E501
        :rtype: MessageInstitution
        """
        return self._beneficiary_bank

    @beneficiary_bank.setter
    def beneficiary_bank(self, beneficiary_bank):
        """Sets the beneficiary_bank of this MessagePaymentStatePending.


        :param beneficiary_bank: The beneficiary_bank of this MessagePaymentStatePending.  # noqa: E501
        :type: MessageInstitution
        """

        self._beneficiary_bank = beneficiary_bank

    @property
    def beneficiary_name(self):
        """Gets the beneficiary_name of this MessagePaymentStatePending.  # noqa: E501

        Nombre del beneficiario  # noqa: E501

        :return: The beneficiary_name of this MessagePaymentStatePending.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_name

    @beneficiary_name.setter
    def beneficiary_name(self, beneficiary_name):
        """Sets the beneficiary_name of this MessagePaymentStatePending.

        Nombre del beneficiario  # noqa: E501

        :param beneficiary_name: The beneficiary_name of this MessagePaymentStatePending.  # noqa: E501
        :type: str
        """

        self._beneficiary_name = beneficiary_name

    @property
    def concept(self):
        """Gets the concept of this MessagePaymentStatePending.  # noqa: E501

        Concepto de la transferencia de salida  # noqa: E501

        :return: The concept of this MessagePaymentStatePending.  # noqa: E501
        :rtype: str
        """
        return self._concept

    @concept.setter
    def concept(self, concept):
        """Sets the concept of this MessagePaymentStatePending.

        Concepto de la transferencia de salida  # noqa: E501

        :param concept: The concept of this MessagePaymentStatePending.  # noqa: E501
        :type: str
        """

        self._concept = concept

    @property
    def currency_code(self):
        """Gets the currency_code of this MessagePaymentStatePending.  # noqa: E501

        Código de la moneda de la transferencia de salida  # noqa: E501

        :return: The currency_code of this MessagePaymentStatePending.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this MessagePaymentStatePending.

        Código de la moneda de la transferencia de salida  # noqa: E501

        :param currency_code: The currency_code of this MessagePaymentStatePending.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def detention_message(self):
        """Gets the detention_message of this MessagePaymentStatePending.  # noqa: E501

        Mensaje de detención de Monex, indica la causa por la cuál esta detenida la operación en Monex  # noqa: E501

        :return: The detention_message of this MessagePaymentStatePending.  # noqa: E501
        :rtype: str
        """
        return self._detention_message

    @detention_message.setter
    def detention_message(self, detention_message):
        """Sets the detention_message of this MessagePaymentStatePending.

        Mensaje de detención de Monex, indica la causa por la cuál esta detenida la operación en Monex  # noqa: E501

        :param detention_message: The detention_message of this MessagePaymentStatePending.  # noqa: E501
        :type: str
        """

        self._detention_message = detention_message

    @property
    def error_message(self):
        """Gets the error_message of this MessagePaymentStatePending.  # noqa: E501

        Mensaje de error  # noqa: E501

        :return: The error_message of this MessagePaymentStatePending.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this MessagePaymentStatePending.

        Mensaje de error  # noqa: E501

        :param error_message: The error_message of this MessagePaymentStatePending.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def order_id(self):
        """Gets the order_id of this MessagePaymentStatePending.  # noqa: E501

        El identificador de la transferencia de salida  # noqa: E501

        :return: The order_id of this MessagePaymentStatePending.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this MessagePaymentStatePending.

        El identificador de la transferencia de salida  # noqa: E501

        :param order_id: The order_id of this MessagePaymentStatePending.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def payment_order_id(self):
        """Gets the payment_order_id of this MessagePaymentStatePending.  # noqa: E501

        El identificador de la orden de pago de Monex de la transferencia de salida  # noqa: E501

        :return: The payment_order_id of this MessagePaymentStatePending.  # noqa: E501
        :rtype: int
        """
        return self._payment_order_id

    @payment_order_id.setter
    def payment_order_id(self, payment_order_id):
        """Sets the payment_order_id of this MessagePaymentStatePending.

        El identificador de la orden de pago de Monex de la transferencia de salida  # noqa: E501

        :param payment_order_id: The payment_order_id of this MessagePaymentStatePending.  # noqa: E501
        :type: int
        """

        self._payment_order_id = payment_order_id

    @property
    def pending_reason(self):
        """Gets the pending_reason of this MessagePaymentStatePending.  # noqa: E501

        Estatus que identifica la causa por la que la transferencia esta en pendiente, los posibles estatus son: FI=Fondos Insuficientes | FM=Firma mancomunada, en espera de ingreso de segundo token de autorización | DP=Se detecto una transferencia duplicada que esta en espera de confirmación o de eliminación  # noqa: E501

        :return: The pending_reason of this MessagePaymentStatePending.  # noqa: E501
        :rtype: str
        """
        return self._pending_reason

    @pending_reason.setter
    def pending_reason(self, pending_reason):
        """Sets the pending_reason of this MessagePaymentStatePending.

        Estatus que identifica la causa por la que la transferencia esta en pendiente, los posibles estatus son: FI=Fondos Insuficientes | FM=Firma mancomunada, en espera de ingreso de segundo token de autorización | DP=Se detecto una transferencia duplicada que esta en espera de confirmación o de eliminación  # noqa: E501

        :param pending_reason: The pending_reason of this MessagePaymentStatePending.  # noqa: E501
        :type: str
        """

        self._pending_reason = pending_reason

    @property
    def reference(self):
        """Gets the reference of this MessagePaymentStatePending.  # noqa: E501

        Referecia de la transferencia  # noqa: E501

        :return: The reference of this MessagePaymentStatePending.  # noqa: E501
        :rtype: int
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this MessagePaymentStatePending.

        Referecia de la transferencia  # noqa: E501

        :param reference: The reference of this MessagePaymentStatePending.  # noqa: E501
        :type: int
        """

        self._reference = reference

    @property
    def request_id(self):
        """Gets the request_id of this MessagePaymentStatePending.  # noqa: E501

        El identificador, en esta API, de la petición de envío de la transferencia de salida  # noqa: E501

        :return: The request_id of this MessagePaymentStatePending.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this MessagePaymentStatePending.

        El identificador, en esta API, de la petición de envío de la transferencia de salida  # noqa: E501

        :param request_id: The request_id of this MessagePaymentStatePending.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def status_code(self):
        """Gets the status_code of this MessagePaymentStatePending.  # noqa: E501

        El estado de la transferencia de salida, deberá ser PENDING  # noqa: E501

        :return: The status_code of this MessagePaymentStatePending.  # noqa: E501
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this MessagePaymentStatePending.

        El estado de la transferencia de salida, deberá ser PENDING  # noqa: E501

        :param status_code: The status_code of this MessagePaymentStatePending.  # noqa: E501
        :type: str
        """

        self._status_code = status_code

    @property
    def transaction_id(self):
        """Gets the transaction_id of this MessagePaymentStatePending.  # noqa: E501

        El identificador de Monex de la transferencia de salida, podría no estar presente por lo que Usted debería hacer referencias mediate el paymentOrderID  # noqa: E501

        :return: The transaction_id of this MessagePaymentStatePending.  # noqa: E501
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this MessagePaymentStatePending.

        El identificador de Monex de la transferencia de salida, podría no estar presente por lo que Usted debería hacer referencias mediate el paymentOrderID  # noqa: E501

        :param transaction_id: The transaction_id of this MessagePaymentStatePending.  # noqa: E501
        :type: int
        """

        self._transaction_id = transaction_id

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
        if issubclass(MessagePaymentStatePending, dict):
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
        if not isinstance(other, MessagePaymentStatePending):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
