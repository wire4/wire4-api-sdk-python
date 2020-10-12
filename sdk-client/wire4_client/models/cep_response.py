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


class CepResponse(object):
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
        'account_beneficiary': 'str',
        'account_sender': 'str',
        'amount': 'float',
        'available': 'bool',
        'beneficiary_bank_key': 'str',
        'beneficiary_name': 'str',
        'beneficiary_rfc': 'str',
        'cadena_original': 'str',
        'capture_date': 'datetime',
        'certificate_serial_number': 'str',
        'clave_rastreo': 'str',
        'description': 'str',
        'iva': 'float',
        'operation_date': 'datetime',
        'operation_date_cep': 'datetime',
        'reference': 'str',
        'sender_bank_key': 'str',
        'sender_name': 'str',
        'sender_rfc': 'str',
        'signature': 'str',
        'url_zip': 'str'
    }

    attribute_map = {
        'account_beneficiary': 'account_beneficiary',
        'account_sender': 'account_sender',
        'amount': 'amount',
        'available': 'available',
        'beneficiary_bank_key': 'beneficiary_bank_key',
        'beneficiary_name': 'beneficiary_name',
        'beneficiary_rfc': 'beneficiary_rfc',
        'cadena_original': 'cadena_original',
        'capture_date': 'capture_date',
        'certificate_serial_number': 'certificate_serial_number',
        'clave_rastreo': 'clave_rastreo',
        'description': 'description',
        'iva': 'iva',
        'operation_date': 'operation_date',
        'operation_date_cep': 'operation_date_cep',
        'reference': 'reference',
        'sender_bank_key': 'sender_bank_key',
        'sender_name': 'sender_name',
        'sender_rfc': 'sender_rfc',
        'signature': 'signature',
        'url_zip': 'url_zip'
    }

    def __init__(self, account_beneficiary=None, account_sender=None, amount=None, available=None, beneficiary_bank_key=None, beneficiary_name=None, beneficiary_rfc=None, cadena_original=None, capture_date=None, certificate_serial_number=None, clave_rastreo=None, description=None, iva=None, operation_date=None, operation_date_cep=None, reference=None, sender_bank_key=None, sender_name=None, sender_rfc=None, signature=None, url_zip=None):  # noqa: E501
        """CepResponse - a model defined in Swagger"""  # noqa: E501
        self._account_beneficiary = None
        self._account_sender = None
        self._amount = None
        self._available = None
        self._beneficiary_bank_key = None
        self._beneficiary_name = None
        self._beneficiary_rfc = None
        self._cadena_original = None
        self._capture_date = None
        self._certificate_serial_number = None
        self._clave_rastreo = None
        self._description = None
        self._iva = None
        self._operation_date = None
        self._operation_date_cep = None
        self._reference = None
        self._sender_bank_key = None
        self._sender_name = None
        self._sender_rfc = None
        self._signature = None
        self._url_zip = None
        self.discriminator = None
        if account_beneficiary is not None:
            self.account_beneficiary = account_beneficiary
        if account_sender is not None:
            self.account_sender = account_sender
        if amount is not None:
            self.amount = amount
        if available is not None:
            self.available = available
        if beneficiary_bank_key is not None:
            self.beneficiary_bank_key = beneficiary_bank_key
        if beneficiary_name is not None:
            self.beneficiary_name = beneficiary_name
        if beneficiary_rfc is not None:
            self.beneficiary_rfc = beneficiary_rfc
        if cadena_original is not None:
            self.cadena_original = cadena_original
        if capture_date is not None:
            self.capture_date = capture_date
        if certificate_serial_number is not None:
            self.certificate_serial_number = certificate_serial_number
        if clave_rastreo is not None:
            self.clave_rastreo = clave_rastreo
        if description is not None:
            self.description = description
        if iva is not None:
            self.iva = iva
        if operation_date is not None:
            self.operation_date = operation_date
        if operation_date_cep is not None:
            self.operation_date_cep = operation_date_cep
        if reference is not None:
            self.reference = reference
        if sender_bank_key is not None:
            self.sender_bank_key = sender_bank_key
        if sender_name is not None:
            self.sender_name = sender_name
        if sender_rfc is not None:
            self.sender_rfc = sender_rfc
        if signature is not None:
            self.signature = signature
        if url_zip is not None:
            self.url_zip = url_zip

    @property
    def account_beneficiary(self):
        """Gets the account_beneficiary of this CepResponse.  # noqa: E501

        Cuenta del beneficiario  # noqa: E501

        :return: The account_beneficiary of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_beneficiary

    @account_beneficiary.setter
    def account_beneficiary(self, account_beneficiary):
        """Sets the account_beneficiary of this CepResponse.

        Cuenta del beneficiario  # noqa: E501

        :param account_beneficiary: The account_beneficiary of this CepResponse.  # noqa: E501
        :type: str
        """

        self._account_beneficiary = account_beneficiary

    @property
    def account_sender(self):
        """Gets the account_sender of this CepResponse.  # noqa: E501

        Cuenta del ordenante  # noqa: E501

        :return: The account_sender of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_sender

    @account_sender.setter
    def account_sender(self, account_sender):
        """Sets the account_sender of this CepResponse.

        Cuenta del ordenante  # noqa: E501

        :param account_sender: The account_sender of this CepResponse.  # noqa: E501
        :type: str
        """

        self._account_sender = account_sender

    @property
    def amount(self):
        """Gets the amount of this CepResponse.  # noqa: E501

        Monto de la transferencia  # noqa: E501

        :return: The amount of this CepResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CepResponse.

        Monto de la transferencia  # noqa: E501

        :param amount: The amount of this CepResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def available(self):
        """Gets the available of this CepResponse.  # noqa: E501

        Indica si o no el CEP se encuentra disponible  # noqa: E501

        :return: The available of this CepResponse.  # noqa: E501
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this CepResponse.

        Indica si o no el CEP se encuentra disponible  # noqa: E501

        :param available: The available of this CepResponse.  # noqa: E501
        :type: bool
        """

        self._available = available

    @property
    def beneficiary_bank_key(self):
        """Gets the beneficiary_bank_key of this CepResponse.  # noqa: E501

        Clave del banco beneficiario  # noqa: E501

        :return: The beneficiary_bank_key of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_bank_key

    @beneficiary_bank_key.setter
    def beneficiary_bank_key(self, beneficiary_bank_key):
        """Sets the beneficiary_bank_key of this CepResponse.

        Clave del banco beneficiario  # noqa: E501

        :param beneficiary_bank_key: The beneficiary_bank_key of this CepResponse.  # noqa: E501
        :type: str
        """

        self._beneficiary_bank_key = beneficiary_bank_key

    @property
    def beneficiary_name(self):
        """Gets the beneficiary_name of this CepResponse.  # noqa: E501

        Nombre del beneficiario  # noqa: E501

        :return: The beneficiary_name of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_name

    @beneficiary_name.setter
    def beneficiary_name(self, beneficiary_name):
        """Sets the beneficiary_name of this CepResponse.

        Nombre del beneficiario  # noqa: E501

        :param beneficiary_name: The beneficiary_name of this CepResponse.  # noqa: E501
        :type: str
        """

        self._beneficiary_name = beneficiary_name

    @property
    def beneficiary_rfc(self):
        """Gets the beneficiary_rfc of this CepResponse.  # noqa: E501

        RFC del beneficiario  # noqa: E501

        :return: The beneficiary_rfc of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_rfc

    @beneficiary_rfc.setter
    def beneficiary_rfc(self, beneficiary_rfc):
        """Sets the beneficiary_rfc of this CepResponse.

        RFC del beneficiario  # noqa: E501

        :param beneficiary_rfc: The beneficiary_rfc of this CepResponse.  # noqa: E501
        :type: str
        """

        self._beneficiary_rfc = beneficiary_rfc

    @property
    def cadena_original(self):
        """Gets the cadena_original of this CepResponse.  # noqa: E501

        Cadena original del CEP  # noqa: E501

        :return: The cadena_original of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._cadena_original

    @cadena_original.setter
    def cadena_original(self, cadena_original):
        """Sets the cadena_original of this CepResponse.

        Cadena original del CEP  # noqa: E501

        :param cadena_original: The cadena_original of this CepResponse.  # noqa: E501
        :type: str
        """

        self._cadena_original = cadena_original

    @property
    def capture_date(self):
        """Gets the capture_date of this CepResponse.  # noqa: E501

        Fecha de captura de la transferencia  # noqa: E501

        :return: The capture_date of this CepResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._capture_date

    @capture_date.setter
    def capture_date(self, capture_date):
        """Sets the capture_date of this CepResponse.

        Fecha de captura de la transferencia  # noqa: E501

        :param capture_date: The capture_date of this CepResponse.  # noqa: E501
        :type: datetime
        """

        self._capture_date = capture_date

    @property
    def certificate_serial_number(self):
        """Gets the certificate_serial_number of this CepResponse.  # noqa: E501

        Número de serie del certificado  # noqa: E501

        :return: The certificate_serial_number of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._certificate_serial_number

    @certificate_serial_number.setter
    def certificate_serial_number(self, certificate_serial_number):
        """Sets the certificate_serial_number of this CepResponse.

        Número de serie del certificado  # noqa: E501

        :param certificate_serial_number: The certificate_serial_number of this CepResponse.  # noqa: E501
        :type: str
        """

        self._certificate_serial_number = certificate_serial_number

    @property
    def clave_rastreo(self):
        """Gets the clave_rastreo of this CepResponse.  # noqa: E501

        Clave de rastreo  # noqa: E501

        :return: The clave_rastreo of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._clave_rastreo

    @clave_rastreo.setter
    def clave_rastreo(self, clave_rastreo):
        """Sets the clave_rastreo of this CepResponse.

        Clave de rastreo  # noqa: E501

        :param clave_rastreo: The clave_rastreo of this CepResponse.  # noqa: E501
        :type: str
        """

        self._clave_rastreo = clave_rastreo

    @property
    def description(self):
        """Gets the description of this CepResponse.  # noqa: E501

        Descripción de la transferencia  # noqa: E501

        :return: The description of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CepResponse.

        Descripción de la transferencia  # noqa: E501

        :param description: The description of this CepResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def iva(self):
        """Gets the iva of this CepResponse.  # noqa: E501

        IVA de la transferencia  # noqa: E501

        :return: The iva of this CepResponse.  # noqa: E501
        :rtype: float
        """
        return self._iva

    @iva.setter
    def iva(self, iva):
        """Sets the iva of this CepResponse.

        IVA de la transferencia  # noqa: E501

        :param iva: The iva of this CepResponse.  # noqa: E501
        :type: float
        """

        self._iva = iva

    @property
    def operation_date(self):
        """Gets the operation_date of this CepResponse.  # noqa: E501

        Fecha de operación de la transferencia  # noqa: E501

        :return: The operation_date of this CepResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._operation_date

    @operation_date.setter
    def operation_date(self, operation_date):
        """Sets the operation_date of this CepResponse.

        Fecha de operación de la transferencia  # noqa: E501

        :param operation_date: The operation_date of this CepResponse.  # noqa: E501
        :type: datetime
        """

        self._operation_date = operation_date

    @property
    def operation_date_cep(self):
        """Gets the operation_date_cep of this CepResponse.  # noqa: E501

        Fecha de abono registrada en el CEP  # noqa: E501

        :return: The operation_date_cep of this CepResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._operation_date_cep

    @operation_date_cep.setter
    def operation_date_cep(self, operation_date_cep):
        """Sets the operation_date_cep of this CepResponse.

        Fecha de abono registrada en el CEP  # noqa: E501

        :param operation_date_cep: The operation_date_cep of this CepResponse.  # noqa: E501
        :type: datetime
        """

        self._operation_date_cep = operation_date_cep

    @property
    def reference(self):
        """Gets the reference of this CepResponse.  # noqa: E501

        Referencia numérica de la transferencia  # noqa: E501

        :return: The reference of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this CepResponse.

        Referencia numérica de la transferencia  # noqa: E501

        :param reference: The reference of this CepResponse.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def sender_bank_key(self):
        """Gets the sender_bank_key of this CepResponse.  # noqa: E501

        Clave del banco emisor  # noqa: E501

        :return: The sender_bank_key of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._sender_bank_key

    @sender_bank_key.setter
    def sender_bank_key(self, sender_bank_key):
        """Sets the sender_bank_key of this CepResponse.

        Clave del banco emisor  # noqa: E501

        :param sender_bank_key: The sender_bank_key of this CepResponse.  # noqa: E501
        :type: str
        """

        self._sender_bank_key = sender_bank_key

    @property
    def sender_name(self):
        """Gets the sender_name of this CepResponse.  # noqa: E501

        Nombre del emisor  # noqa: E501

        :return: The sender_name of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name):
        """Sets the sender_name of this CepResponse.

        Nombre del emisor  # noqa: E501

        :param sender_name: The sender_name of this CepResponse.  # noqa: E501
        :type: str
        """

        self._sender_name = sender_name

    @property
    def sender_rfc(self):
        """Gets the sender_rfc of this CepResponse.  # noqa: E501

        RFC del emisor  # noqa: E501

        :return: The sender_rfc of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._sender_rfc

    @sender_rfc.setter
    def sender_rfc(self, sender_rfc):
        """Sets the sender_rfc of this CepResponse.

        RFC del emisor  # noqa: E501

        :param sender_rfc: The sender_rfc of this CepResponse.  # noqa: E501
        :type: str
        """

        self._sender_rfc = sender_rfc

    @property
    def signature(self):
        """Gets the signature of this CepResponse.  # noqa: E501

        Firma del CEP  # noqa: E501

        :return: The signature of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this CepResponse.

        Firma del CEP  # noqa: E501

        :param signature: The signature of this CepResponse.  # noqa: E501
        :type: str
        """

        self._signature = signature

    @property
    def url_zip(self):
        """Gets the url_zip of this CepResponse.  # noqa: E501

        La url al archivo zip del CEP, el cual contiene el xml y pdf  # noqa: E501

        :return: The url_zip of this CepResponse.  # noqa: E501
        :rtype: str
        """
        return self._url_zip

    @url_zip.setter
    def url_zip(self, url_zip):
        """Sets the url_zip of this CepResponse.

        La url al archivo zip del CEP, el cual contiene el xml y pdf  # noqa: E501

        :param url_zip: The url_zip of this CepResponse.  # noqa: E501
        :type: str
        """

        self._url_zip = url_zip

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
        if issubclass(CepResponse, dict):
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
        if not isinstance(other, CepResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
