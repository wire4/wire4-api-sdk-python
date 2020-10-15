# wire4-client
 # Referencia de API La API de Wire4 está organizada en torno a REST. Nuestra API tiene URLs predecibles orientadas a los recursos, acepta peticiones en formato JSON, y las respuestas devueltas son formato JSON y utiliza códigos de respuesta HTTP, autenticación y verbos estándares.  Puede usar la API de Wire4 en nuestro entorno de prueba, que no afecta sus productivos ni interactúa con la red bancaria. La URL de conexión que se usa para invocar los servicios determina si la solicitud es en modo en de prueba o en modo producción.    # Autenticación La API de Wire4 utiliza el protocolo OAuth 2.0 para autenticación y autorización.   Para comenzar, es necesario que registre una cuenta en nuestro ambiente de pruebas en [registro](https://app-sndbx.wire4.mx/#/register) y obtenga las credenciales de cliente OAuth 2.0 desde la [consola de administración](https://app-sndbx.wire4.mx/#/dashboard/api-keys).   Esta página ofrece una descripción general de los escenarios de autorización de OAuth 2.0 que admite Wire4.   Después de crear su aplicación con Wire4, asegúrese de tener a la mano su `client_id` y `client_secret`. El siguiente paso es descubrir qué flujo de OAuth2 es el adecuado para sus propósitos.   ## URLS La siguiente tabla muestra las urls de los recursos de autenticación para el ambiente de pruebas.  URL                  | Descripción ------------------------------------ | ------------- https://sandbox-api.wire4.mx/token   | Obtener token de autorización llaves de API (*client_id*, *client_secret*), datos de suscripción (*client_id*, *client_secret*, *user_key*, *user_secret*) o (*refresh_token*) https://sandbox-api.wire4.mx/revoke  | Revocación de token  **Nota:** De acuerdo con el RFC 6749, la URL del token sólo acepta el tipo de contenido x-www-form-urlencoded. El contenido JSON no está permitido y devolverá un error.  ## Scopes Los `scopes` limitan el acceso de una aplicación a los recursos de Wire4. Se ofrecen los siguientes scopes de acuerdo al producto:  Producto                             |Scope                      | Descripción -------------------------------------|------------------------------------ | ------------- SPEI-SPID                            |general                              | Permite llamar a operaciones que no requieren a un cliente Monex suscrito en Wire4, los recursos que se pueden consumir con este scope son: consulta de Instituciones, CEP y generación de una presuscripción. SPEI-SPID                            |spei_admin                           | Permite llamar a operaciones que requieren de un cliente Monex suscrito en Wire4, ya que se proporciona información de saldos, administración de transacciones, cuentas de beneficiarios y cuentas de depositantes. SPEI-SPID                            |spid_admin                           | Permite llamar sólo a operaciones SPID, se requiere de un cliente Monex suscrito en Wire4. CODI                                 |codi_general                         | Permite llamar a operaciones de administración sobre el producto CoDi, como creación y listado de empresas  CODI                                 |codi_admin                           | Permite llamar sólo a operaciones CoDi dentro de un punto de venta, las operaciones incluyen creación, consulta, listado, etc de peticiones de pago CODI                                 |codi_report                          | Permite generar reportes de operaciones CoDi. TODOS                                |device_[dispositivo]                 | Se debe especificar cuando se gestionan token's desde distintos dispositivos.  ## Tipos de autenticación   Wire4 cuenta con dos tipos de autenticación: Autenticación de Aplicación (OAuth 2.0  Client Credentials Grant)  y Autenticación de Usuario de Aplicación (OAuth 2.0 Password Grant).  ### Autenticación de Aplicación  Esta autenticación se obtiene proporcionando únicamente las llaves de API las cuales se pueden consultar en [Llaves de API](https://app-sndbx.wire4.mx/#/dashboard/api-keys) de la consola de administración.  La autenticación de aplicación permite accesso a recursos generales y de administración que dependeran del scope.  Para este tipo de autenticación se sigue el flujo OAuth 2.0 Client Credentials Grant, que se describe más adelante en **Obtener el token de acceso de aplicación**, algunos de los recursos que requieren este tipo de autenticación son:   * [/subscriptions/pre-subscription](link) * [/institutions](link>) * [/ceps](<link>) * [/codi/compaies](<link>)  ### Autenticación de Usuario de Aplicación  Esta autenticación se obtiene proporcionando las llaves de API las cuales se pueden consultar en [Llaves de API](https://app-sndbx.wire4.mx/#/dashboard/api-keys) más el ***user_key*** y ***user_secret*** que se proporcionan al momento de crear una suscripción o un punto de venta, para más información puedes consultar las guías [creación de suscripción](https://www.wire4.mx/#/guides/subscriptions), [creación de punto de venta](https://www.wire4.mx/#/guides/salespoint).  Con este tipo de autenticación se puede acceder a los recursos especificos que requieren configuraciones y acceso mas puntual como información de una cuentas, saldos y administración de transacciones SPEID-SPID o CODI.    ## Obtener token de acceso Antes de que su aplicación pueda acceder a los datos mediante la API de Wire4, debe obtener un token de acceso ***(access_token)*** que le otorgue acceso a la API. En las siguientes secciones se muestra como obtener un token para cada una de las autenticaciones.     ### Obtener el token de acceso para autenticación de aplicación  El primer paso es crear la solicitud de token de acceso (*access_token*), con los parámetros que identifican su aplicación, el siguiente código muestra cómo obtener un `token`.  ``` curl -k -d \"grant_type= client_credentials&scope=general\"  -u \"<client id>:<client secret>\" https://sandbox-api.wire4.mx/token ``` **Ejemplo:**   ``` curl -k -d \"grant_type=client_credentials&scope=general\"  -u \"8e59YqaFW_Yo5dwWNxEY8Lid0u0a:AXahn79hfKWBXKzQfj011x8cvcQa\"  https://sandbox-api.wire4.mx /token ``` Obtendrá una respuesta como la que se muestra  a continuación, donde se debe obtener el *access_token* para realizar llamadas posteriores a la API.   ``` {     \"access_token\":\"eyJ4NXQiOiJZak5sWVdWa05tWmlNR1ZoTldSaU1EUXpaREJpWlRJNU1qYzFZV1ZoWWpneU5UYzJPV05sWVEiLCJraWQiOiJZak5sWVdWa05tWmlNR1ZoTldSaU1EUXpaREJpWlRJNU1qYzFZV1ZoWWpneU5UYzJPV05sWVEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpc21hZWwuZXNjYW1pbGxhQHRjcGlwLnRlY2hAc2FuZGJveC5zcGVpb2suY29tIiwiYXVkIjoiOGU1OVlxYUZXX1lvNWR3V054RVk4TGlkMHUwYSIsIm5iZiI6MTU3MTMyMDg3NywiYXpwIjoiOGU1OVlxYUZXX1lvNWR3V054RVk4TGlkMHUwYSIsInNjb3BlIjoiYW1fYXBwbGljYXRpb25fc2NvcGUgZ2VuZXJhbCIsImlzcyI6ImFwaW0taWRwIiwiZXhwIjoxNTcxMzI0NDc3LCJpYXQiOjE1NzEzMjA4NzcsImp0aSI6ImJkMTdjMjcyLTg4MGQtNDk0ZS1iMTMwLTBiYTkwMjYyN2M4NCJ9.AjngGylkd_Chs5zlIjyLRPu9xPGyz4dfCd_aax2_ts653xrnNMoLpVHUDmaxIDFF2XyBJKH2IAbKxjo6VsFM07QkoPhlysO1PLoAF-Vkt4xYkh-f7nJRl0oOe2utDWFlUdgiAOmx5tPcStrdCEftgNNrjwJ50LXysFjXVshpoST-zIJPLgXknM3esGrkAsLcZRM7XUB187jxLHbtefVYPMvSO31T9pd5_Co9UXdeHpuA98sk_wZknASM1phxXQZAMLRLHz3LYvjCWCr_v80oVCM9SWTzf0vrMI6xphoIfirfWloADKPTTSUpIGBw9ePF_WbEPvbMm_BZaApJcEH2w\",    \"scope\":\"am_application_scope general\",    \"token_type\":\"Bearer\",    \"expires_in\":3600 }  ```  Es posible generar tokens con mas de un scope, en caso que sea necesario utilizar dicho token para hacer mas de una operación. Para generarlo basta con agregarlo a la petición separado por un espacio.     ``` curl -k -d \"grant_type=client_credentials&scope=codi_general codi_report\"  -u \"8e59YqaFW_Yo5dwWNxEY8Lid0u0a:AXahn79hfKWBXKzQfj011x8cvcQa\"  https://sandbox-api.wire4.mx /token ```  ### Obtener el token de acceso para autenticación usuario de aplicación   Antes de que su aplicación pueda acceder a los datos de una cuenta Monex mediante la API de Wire4, debe obtener un token de acceso  (*access_token*) que le otorgue acceso a la API y contar con el  *user_key* y *user_secret* que se proporcionan al momento de crear  una suscripción para más información puedes consultar [creación de suscripción](https://wire4.mx/#/guides/subscriptions) .   El primer paso es crear la solicitud de token de acceso con los parámetros que identifican su aplicación y la suscripción y con `scope` `spei_admin`  ```   curl -k -d \"grant_type=password&scope=spei_admin&username=<user_key>&password=<user_secret>\"  -u \"<client_id>:<client_secret>\" https://sandbox-api.wire4.mx/token ``` **Ejemplo**  ``` curl -k -d \"grant_type=password&scope=spei_admin&username=6 nbC5e99tTO@sandbox.wire4com&password= Nz7IqJGe9h\" -u \" zgMlQbqmOr:plkMJoPXCI\" https://sandbox-api.wire4.mx /token  ```  ``` {     \"access_token\":\"eyJ4NXQiOiJPR1EyTURFM00yTmpObVZoTnpFeE5EWXlObUV4TURKa01qUTJaVEU0TWpGaE1tVmlZakV5TkEiLCJraWQiOiJPR1EyTURFM00yTmpObVZoTnpFeE5EWXlObUV4TURKa01qUTJaVEU0TWpGaE1tVmlZakV5TkEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIzMzE0ODRlZTdjZDRkYWU5MzRmMjY2Zjc5YmY1YWFAZGV2LWllc2NhbWlsbGEuc3BlaW9rLmNvbSIsImF1ZCI6IkJVR0xjNWw1bW5CZXlPeGxtamNUZ0JoS19WTWEiLCJuYmYiOjE1NzEzNDk4ODMsImF6cCI6IkJVR0xjNWw1bW5CZXlPeGxtamNUZ0JoS19WTWEiLCJzY29wZSI6InNwZWlfYWRtaW4iLCJpc3MiOiJhcGltLWlkcCIsImV4cCI6MTU3MTM1MzQ4MywiaWF0IjoxNTcxMzQ5ODgzLCJqdGkiOiJiOWQ1M2Q0MC0xN2MwLTQxOTItYjUwNy0wZWFhN2ZkNDA1MGYifQ.hLTk8AFoIce1GpLcgch-U5aLLgiiFTo49wfBErD8D6VF-H9sG13ZyfAx9T-vQkk2m1zPapYVQjwibz3GRAJMN0Vczs6flV1mUJwFDQbEE-AELPdRcaRFOMBCfF6H9TVLfhFsGb9U2pVR9TLJcKqR57DyO_dIcc9I6d0tIkxqn2VcqypLVi5YQf36WzBbPeG-iPHYpMA-bhr4rwfjKA-O6jm1NSSxNHF4sHS0YHDPoO_x6cCc677MQEe0_CozfnQhoEWNfG8tcWUqhPtmcfjqon1p7PdQoXxriq_R85d06pVO9Se7Q6ok0V8Qgz0MOJ6z3ku6mtZSuba7niMAOt2TyA\",    \"refresh_token\":\"f962d5c6-0d99-3809-8275-11c7aa0aa020\",    \"scope\":\"spei_admin\",    \"token_type\":\"Bearer\",    \"expires_in\":3600 } ```  **Nota:** Los ejemplos anteriores se presentan considerando que se realiza una implementación desde cero,  esto se puede simplificar a sólo configurar sus llaves (*client_id*, *client_secret*),  datos de suscripción (*client_id*, *client_secret*, *user_key*, *user_secret*) si utiliza nuestros sdks.      **Consideraci&oacute;n:** Si la aplicaci&oacute;n en la que implementar&aacute; Wire4 estar&aacute; desplegada en mas de una instancia o servidor en cada solicitud de token debe especificar un scope adicional. La forma de hacer esto es que cuando se solicita un token se debe especificar un scope adicional con el prefijo \"device_\" +  el dispositivo, por ejemplo:                                                                                                                                                                                                                     device_server1<br> device_server2  en consecuencia cada instancia debe operar con el token gestionado. ***Si se opera con el mismo token en instancias diferentes encontrará problemas de Credenciales Inv&aacute;lidas.***  **Ejemplo de solicitud de token para instancias diferentes:**  ``` curl -k -d \"grant_type=password&username=0883b97333046abb76367698b57d9e@sandbox.wire4.mx&password=9e0d81f95705079b9fe1e129315c25&scope=device_server1 codi_admin\" -H \"Authorization: Basic dmZSeURpTHdFbVZqd2VIclp0OWRMbXFmb3YwYTpJQJBuamBac3V6SllLWlJHUkJEYUZrN1BhRmNh\" https://sandbox-api.wire4.mx/token  curl -k -d \"grant_type=password&username=0883b97333046abb76367698b57d9e@sandbox.wire4.mx&password=9e0d81f95705079b9fe1e129315c25&scope=device_server2 codi_admin\" -H \"Authorization: Basic dmZSeURpTHdFbVZqd2VIclp0OWRMbXFmb3YwYTpJQJBuamBac3V6SllLWlJHUkJEYUZrN1BhRmNh\" https://sandbox-api.wire4.mx/token ```  ## Caducidad del token El token de acceso es válido durante 60 minutos (una hora), después de transcurrido este tiempo se debe solicitar un nuevo token,  cuando el token caduca se obtendrá un error ***401 Unauthorized*** con mensaje ***“Invalid Credentials”.***   El nuevo token se puede solicitar  utilizando el último token de actualización (***refresh_token***) que se devolvió en la solicitud del token,   esto sólo aplica para el token de tipo password (Autenticación de Usuario de Aplicación). El siguiente ejemplo muestra cómo obtener un toke con el token de actualización.  ``` curl -k -d \"grant_type=refresh_token&refresh_token=<refresh_token>\" -u \" Client_Id:Client_Secret\" -H \"Content-Type: application/x-www-form-urlencoded\" https://sandbox-api.wire4.mx/oauth2/token ```  **Ejemplo:**  ``` curl -k -d \"grant_type=refresh_token&refresh_token=f932d5c6-0d39-3809-8275-11c7ax0aa020\" -u \"zgMlQbqmOr:plkMJoPXCI\" -H \"Content-Type: application/x-www-form-urlencoded\" https://sandbox-api.wire4.mx/token ```  El token de actualización (***refresh_token***) tiene una duración de hasta 23 horas. Si en este periodo no se utiliza, se tienen que solicitar un nuevo token.  Un token de acceso podría dejar de funcionar por uno de estos motivos:  * El usuario ha revocado el acceso a su aplicación, si un usuario ha solicitado la baja de su aplicación de WIre4. * El token de acceso ha caducado: si el token de acceso ha pasado de una hora, recibirá un error ***401 Unauthorized*** mientras realiza una llamada a la API de Wire4. Cuando esto sucede, debe solicitar un nuevo token utilizando el token de actualización que recibió por última al solicitar un token, sólo aplica si el token en cuestión es de autenticación de usuario de aplicación, en caso contrario solicitar un nuevo token.   ## Revocar token Su aplicación puede revocar mediante programación el token de acceso, una vez revocado el token no podrá hacer uso de él para acceder a la API. El siguiente código muestra un ejemplo de cómo revocar el token:    ```  curl -X POST --basic -u \"<client id>:<client secret>\" -H \"Content-Type: application/x-www-form-urlencoded;charset=UTF-8\" -k -d \"token=<token to revoke>&token_type_hint=access_token\" https://sandbox-api.wire4.mx/revoke ```      **Ejemplo:**  ```   curl -X POST --basic -u \"8e59YqaFW_Yo5dwWNxEY8Lid0u0a:AXahn79hfKWBXKzQfj011x8cvcQa\" -H \"Content-Type: application/x-www-form-urlencoded;charset=UTF-8\" -k -d \"token=eyJ4NXQiOiJZak5sWVdWa05tWmlNR1ZoTldSaU1EUXpaREJpWlRJNU1qYzFZV1ZoWWpneU5UYzJPV05sWVEiLCJraWQiOiJZak5sWVdWa05tWmlNR1ZoTldSaU1EUXpaREJpWlRJNU1qYzFZV1ZoWWpneU5UYzJPV05sWVEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpc21hZWwuZXNjYW1pbGxhQHRjcGlwLnRlY2hAc2FuZGJveC5zcGVpb2suY29tIiwiYXVkIjoiOGU1OVlxYUZXX1lvNWR3V054RVk4TGlkMHUwYSIsIm5iZiI6MTU3MTMyMDg3NywiYXpwIjoiOGU1OVlxYUZXX1lvNWR3V054RVk4TGlkMHUwYSIsInNjb3BlIjoiYW1fYXBwbGljYXRpb25fc2NvcGUgZ2VuZXJhbCIsImlzcyI6ImFwaW0taWRwIiwiZXhwIjoxNTcxMzI0NDc3LCJpYXQiOjE1NzEzMjA4NzcsImp0aSI6ImJkMTdjMjcyLTg4MGQtNDk0ZS1iMTMwLTBiYTkwMjYyN2M4NCJ9.AjngGylkd_Chs5zlIjyLRPu9xPGyz4dfCd_aax2_ts653xrnNMoLpVHUDmaxIDFF2XyBJKH2IAbKxjo6VsFM07QkoPhlysO1PLoAF-Vkt4xYkh-f7nJRl0oOe2utDWFlUdgiAOmx5tPcStrdCEftgNNrjwJ50LXysFjXVshpoST-zIJPLgXknM3esGrkAsLcZRM7XUB187jxLHbtefVYPMvSO31T9pd5_Co9UXdeHpuA98sk_wZknASM1phxXQZAMLRLHz3LYvjCWCr_v80oVCM9SWTzf0vrMI6xphoIfirfWloADKPTTSUpIGBw9ePF_WbEPvbMm_BZaApJcEH2w&token_type_hint=access_token\"  https://sandbox-api.wire4.mx/revoke ```  # Ambientes  Wire4 cuentas con dos ambientes Pruebas (Sandbox) y Producción, son dos ambientes separados los cuales se pueden utilizar simultáneamente. Los usuarios que han sido creados en cada uno de los ambientes no son intercambiables.   Las ligas de acceso a la `api` para cada uno de los ambientes son:  * Pruebas  https://sandbox-api.wire4.mx * Producción https://api.wire4.mx     # Eventos  Los eventos son nuestra forma de informarle cuando algo  sucede en su cuenta. Cuando ocurre un evento se crea un objeto  [Evento](#tag/Webhook-Message). Por ejemplo, cuando se recibe un depósito, se crea un evento TRANSACTION.INCOMING.UPDATED.   Los eventos ocurren cuando cambia el estado de un recurso. El recurso se encuentra dentro del objeto [Evento](#tag/Webhook-Message) en el campo data.  Por ejemplo, un evento TRANSACTION.INCOMING.UPDATED contendrá un depósito y un evento ACCOUNT.CREATED contendrá una cuenta.   Wire4 puede agregar más campos en un futuro, o agregar nuevos valores a campos existentes, por lo que es recomendado que tu endpoint pueda manejar datos adicionales desconocidos. En esta [liga](#tag/Webhook-Message) se encuentra  la definición del objeto [Evento](#tag/Webhook-Message).  ## Tipos de Eventos  Wire4 cuenta con los siguientes tipos de eventos*   | Evento                     | Tipo                               | Objeto                                        | | -------------------------- |----------------------------------- | --------------------------------------------- | | Suscripción                | ENROLLMENT.CREATED                 | [suscription](#tag/subscription)              | | Cuenta de beneficiario     | ACCOUNT.CREATED                    | [beneficiary](#tag/BeneficiaryAccount)           | | Depósito recibido          | TRANSACTION.INCOMING.UPDATED       | [spei_incoming](#tag/deposit)                 | | Transferencia realizada    | TRANSACTION.OUTGOING.RECEIVED      | [spei_outgoing](#tag/transfer)                | | Transferencia SPID enviada | TRANSACTION.OUTGOING.SPID.RECEIVED | [spid_outgoing](#tag/transfer)                | | Transferencias Autorizadas | REQUEST.OUTGOING.CHANGED           | [request_outgoing](#tag/requestOutMsg)        | | Operación CoDi             | CODI.ACTIONS                       |[codi_actions](#tag/codiActions)               | | Punto de venta CoDi        | SALE.POINT.CREATED                 |[codi_sales_point](#tag/codiSalesPoint)        | 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.5
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import wire4_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wire4_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.ComprobanteElectrnicoDePagoCEPApi(wire4_client.ApiClient(configuration))
body = wire4_client.CepSearchBanxico() # CepSearchBanxico | Información para buscar un CEP
authorization = 'authorization_example' # str | Header para token

try:
    # Consulta de CEP
    api_response = api_instance.obtain_transaction_cep_using_post(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComprobanteElectrnicoDePagoCEPApi->obtain_transaction_cep_using_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ComprobanteElectrnicoDePagoCEPApi* | [**obtain_transaction_cep_using_post**](docs/ComprobanteElectrnicoDePagoCEPApi.md#obtain_transaction_cep_using_post) | **POST** /ceps | Consulta de CEP
*ContactoApi* | [**send_contact_using_post**](docs/ContactoApi.md#send_contact_using_post) | **POST** /contact | Solicitud de contacto
*ContractsDetailsApi* | [**create_authorization**](docs/ContractsDetailsApi.md#create_authorization) | **POST** /onboarding/accounts/authorize | Devuelve la URL para autorización del usuario Monex
*ContractsDetailsApi* | [**obtain_authorized_users**](docs/ContractsDetailsApi.md#obtain_authorized_users) | **GET** /onboarding/accounts/{requestId}/authorized-users | Obtiene los usuarios autorizados
*ContractsDetailsApi* | [**obtain_authorized_users_by_contract**](docs/ContractsDetailsApi.md#obtain_authorized_users_by_contract) | **GET** /onboarding/accounts/authorized-users | Obtiene los usuarios autorizados por contrato
*ContractsDetailsApi* | [**obtain_contract_details**](docs/ContractsDetailsApi.md#obtain_contract_details) | **POST** /onboarding/accounts/details | Obtiene los detalles de la empresa del contrato
*CuentasDeBeneficiariosSPEIApi* | [**authorize_accounts_pending_put**](docs/CuentasDeBeneficiariosSPEIApi.md#authorize_accounts_pending_put) | **PUT** /subscriptions/{subscription}/beneficiaries/pending | Recibe la solicitud para agrupar las cuentas SPEI/SPID de beneficiarios en estado pendiente que deben ser autorizadas
*CuentasDeBeneficiariosSPEIApi* | [**delete_account_using_delete**](docs/CuentasDeBeneficiariosSPEIApi.md#delete_account_using_delete) | **DELETE** /subscriptions/{subscription}/beneficiaries/spei/{account} | Elimina la cuenta del beneficiario
*CuentasDeBeneficiariosSPEIApi* | [**get_available_relationships_monex_using_get**](docs/CuentasDeBeneficiariosSPEIApi.md#get_available_relationships_monex_using_get) | **GET** /subscriptions/{subscription}/beneficiaries/relationships | Consulta de relaciones
*CuentasDeBeneficiariosSPEIApi* | [**get_beneficiaries_by_request_id**](docs/CuentasDeBeneficiariosSPEIApi.md#get_beneficiaries_by_request_id) | **GET** /subscriptions/{subscription}/beneficiaries/spei/{requestId} | Consulta los beneficiarios por el identificador de la petición de registro
*CuentasDeBeneficiariosSPEIApi* | [**get_beneficiaries_for_account_using_get**](docs/CuentasDeBeneficiariosSPEIApi.md#get_beneficiaries_for_account_using_get) | **GET** /subscriptions/{subscription}/beneficiaries/spei | Consulta los beneficiarios registrados
*CuentasDeBeneficiariosSPEIApi* | [**pre_register_accounts_using_post**](docs/CuentasDeBeneficiariosSPEIApi.md#pre_register_accounts_using_post) | **POST** /subscriptions/{subscription}/beneficiaries/spei | Pre-registro de cuentas de beneficiarios.
*CuentasDeBeneficiariosSPEIApi* | [**remove_beneficiaries_pending_using_delete**](docs/CuentasDeBeneficiariosSPEIApi.md#remove_beneficiaries_pending_using_delete) | **DELETE** /subscriptions/{subscription}/beneficiaries/spei/request/{requestId} | Eliminación de beneficiarios SPEI® sin confirmar
*CuentasDeBeneficiariosSPEIApi* | [**update_amount_limit_account_using_put**](docs/CuentasDeBeneficiariosSPEIApi.md#update_amount_limit_account_using_put) | **PUT** /subscriptions/{subscription}/beneficiaries/spei/{account} | Solicitud para actualizar el monto límite
*CuentasDeBeneficiariosSPIDApi* | [**get_spid_beneficiaries_for_account**](docs/CuentasDeBeneficiariosSPIDApi.md#get_spid_beneficiaries_for_account) | **GET** /subscriptions/{subscription}/beneficiaries/spid | Consulta los beneficiarios SPID registrados
*CuentasDeBeneficiariosSPIDApi* | [**pre_register_accounts_using_post1**](docs/CuentasDeBeneficiariosSPIDApi.md#pre_register_accounts_using_post1) | **POST** /subscriptions/{subscription}/beneficiaries/spid | Pre-registro de cuentas de beneficiarios SPID
*DepositantesApi* | [**get_depositants_using_get**](docs/DepositantesApi.md#get_depositants_using_get) | **GET** /subscriptions/{subscription}/depositants | Consulta de cuentas de depositantes
*DepositantesApi* | [**register_depositants_using_post**](docs/DepositantesApi.md#register_depositants_using_post) | **POST** /subscriptions/{subscription}/depositants | Registra un nuevo depositante
*EmpresasCoDiApi* | [**obtain_companies**](docs/EmpresasCoDiApi.md#obtain_companies) | **GET** /codi/companies | Consulta de empresas CODI
*EmpresasCoDiApi* | [**register_company_using_post**](docs/EmpresasCoDiApi.md#register_company_using_post) | **POST** /codi/companies | Registro de empresas CODI
*FacturasApi* | [**billings_report_by_id_using_get**](docs/FacturasApi.md#billings_report_by_id_using_get) | **GET** /billings/{id} | Consulta de facturas por identificador
*FacturasApi* | [**billings_report_using_get**](docs/FacturasApi.md#billings_report_using_get) | **GET** /billings | Consulta de facturas
*InstitucionesApi* | [**get_all_institutions_using_get**](docs/InstitucionesApi.md#get_all_institutions_using_get) | **GET** /institutions | Información de instituciones bancarias.
*LmitesDeMontosApi* | [**obtain_configurations_limits**](docs/LmitesDeMontosApi.md#obtain_configurations_limits) | **GET** /subscriptions/{suscription}/configurations | Consulta las configuraciones para el contrato asocaido al enrolamiento en la aplicación
*LmitesDeMontosApi* | [**update_configurations**](docs/LmitesDeMontosApi.md#update_configurations) | **PUT** /subscriptions/{suscription}/configurations | Actualiza las configuraciones por subscripción
*OperacionesCoDiApi* | [**consult_codi_operations**](docs/OperacionesCoDiApi.md#consult_codi_operations) | **POST** /codi/charges | Obtiene las operaciones generadas a partir de peticiones de pago CoDi® de forma paginada, pudiendo aplicar filtros
*PeticionesDePagoPorCoDiApi* | [**consult_codi_request_by_order_id**](docs/PeticionesDePagoPorCoDiApi.md#consult_codi_request_by_order_id) | **GET** /codi/sales-point/charges | Obtiene la información de una petición de pago CODI® por orderId para un punto de venta
*PeticionesDePagoPorCoDiApi* | [**generate_codi_code_qr**](docs/PeticionesDePagoPorCoDiApi.md#generate_codi_code_qr) | **POST** /codi/sales-point/charges | Genera un código QR para un pago mediante CODI®
*PuntosDeVentaCoDiApi* | [**create_sales_point**](docs/PuntosDeVentaCoDiApi.md#create_sales_point) | **POST** /codi/companies/salespoint | Registra un punto de venta asociado a una empresa
*PuntosDeVentaCoDiApi* | [**obtain_sale_points**](docs/PuntosDeVentaCoDiApi.md#obtain_sale_points) | **GET** /codi/companies/salespoint | Obtiene los puntos de venta asociados a una empresa
*SaldoApi* | [**get_balance_using_get**](docs/SaldoApi.md#get_balance_using_get) | **GET** /subscriptions/{subscription}/balance | Consulta los saldo de una cuenta
*SuscripcionesApi* | [**pre_enrollment_monex_user_using_post**](docs/SuscripcionesApi.md#pre_enrollment_monex_user_using_post) | **POST** /subscriptions/pre-subscription | Registra una pre-suscripción
*SuscripcionesApi* | [**remove_enrollment_user_using_delete**](docs/SuscripcionesApi.md#remove_enrollment_user_using_delete) | **DELETE** /subscriptions/{subscription} | Elimina una suscripción por el identificador de la suscripción
*SuscripcionesApi* | [**remove_subscription_pending_status_using_delete**](docs/SuscripcionesApi.md#remove_subscription_pending_status_using_delete) | **DELETE** /subscriptions/pre-subscription/{subscription} | Elimina una pre-suscripción
*TransferenciasSPEIApi* | [**create_authorization_transactions_group**](docs/TransferenciasSPEIApi.md#create_authorization_transactions_group) | **POST** /subscriptions/{subscription}/transactions/group | Agrupa un conjunto de transacciones bajo un mismo request_id para autorizar
*TransferenciasSPEIApi* | [**drop_transactions_pending_using_delete**](docs/TransferenciasSPEIApi.md#drop_transactions_pending_using_delete) | **DELETE** /subscriptions/{subscription}/transactions/outcoming/spei/request/{requestId} | Eliminación de transferencias SPEI® pendientes
*TransferenciasSPEIApi* | [**incoming_spei_transactions_report_using_get**](docs/TransferenciasSPEIApi.md#incoming_spei_transactions_report_using_get) | **GET** /subscriptions/{subscription}/transactions/incoming/spei | Consulta de transferencias recibidas
*TransferenciasSPEIApi* | [**out_comming_spei_request_id_transactions_report_using_get**](docs/TransferenciasSPEIApi.md#out_comming_spei_request_id_transactions_report_using_get) | **GET** /subscriptions/{subscription}/transactions/outcoming/spei/{requestId} | Consulta de transferencias de salida por identificador de petición
*TransferenciasSPEIApi* | [**outgoing_spei_transactions_report_using_get**](docs/TransferenciasSPEIApi.md#outgoing_spei_transactions_report_using_get) | **GET** /subscriptions/{subscription}/transactions/outcoming/spei | Consulta de transferencias realizadas
*TransferenciasSPEIApi* | [**register_outgoing_spei_transaction_using_post**](docs/TransferenciasSPEIApi.md#register_outgoing_spei_transaction_using_post) | **POST** /subscriptions/{subscription}/transactions/outcoming/spei | Registro de transferencias
*TransferenciasSPIDApi* | [**get_spid_classifications_using_get**](docs/TransferenciasSPIDApi.md#get_spid_classifications_using_get) | **GET** /subscriptions/{subscription}/beneficiaries/spid/classifications | Consulta las clasificaciones para operaciones con SPID
*TransferenciasSPIDApi* | [**register_outgoing_spid_transaction_using_post**](docs/TransferenciasSPIDApi.md#register_outgoing_spid_transaction_using_post) | **POST** /subscriptions/{subscription}/transactions/outcoming/spid | Registro de transferencias SPID
*WebhooksApi* | [**get_webhook**](docs/WebhooksApi.md#get_webhook) | **GET** /webhooks/{id} | Consulta de Webhook
*WebhooksApi* | [**get_webhooks**](docs/WebhooksApi.md#get_webhooks) | **GET** /webhooks | Consulta de Webhooks
*WebhooksApi* | [**register_webhook**](docs/WebhooksApi.md#register_webhook) | **POST** /webhooks | Alta de Webhook

## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountDetail](docs/AccountDetail.md)
 - [AccountReassigned](docs/AccountReassigned.md)
 - [AccountRequest](docs/AccountRequest.md)
 - [AccountResponse](docs/AccountResponse.md)
 - [AccountSpid](docs/AccountSpid.md)
 - [AddressCompany](docs/AddressCompany.md)
 - [AmountRequest](docs/AmountRequest.md)
 - [AuthorizationTransactionGroup](docs/AuthorizationTransactionGroup.md)
 - [AuthorizedBeneficiariesResponse](docs/AuthorizedBeneficiariesResponse.md)
 - [AuthorizedUsers](docs/AuthorizedUsers.md)
 - [Balance](docs/Balance.md)
 - [BalanceListResponse](docs/BalanceListResponse.md)
 - [BeneficiariesQueryRegisterStatus](docs/BeneficiariesQueryRegisterStatus.md)
 - [BeneficiariesResponse](docs/BeneficiariesResponse.md)
 - [BeneficiaryInstitution](docs/BeneficiaryInstitution.md)
 - [Billing](docs/Billing.md)
 - [BillingTransaction](docs/BillingTransaction.md)
 - [CepResponse](docs/CepResponse.md)
 - [CepSearchBanxico](docs/CepSearchBanxico.md)
 - [CertificateRequest](docs/CertificateRequest.md)
 - [CodiCodeQrResponseDTO](docs/CodiCodeQrResponseDTO.md)
 - [CodiCodeRequestDTO](docs/CodiCodeRequestDTO.md)
 - [CodiOperationResponseDTO](docs/CodiOperationResponseDTO.md)
 - [CodiOperationsFiltersRequestDTO](docs/CodiOperationsFiltersRequestDTO.md)
 - [CompanyRegistered](docs/CompanyRegistered.md)
 - [CompanyRequested](docs/CompanyRequested.md)
 - [Compay](docs/Compay.md)
 - [ConfigurationsLimits](docs/ConfigurationsLimits.md)
 - [ContactRequest](docs/ContactRequest.md)
 - [ContractDetailRequest](docs/ContractDetailRequest.md)
 - [ContractDetailResponse](docs/ContractDetailResponse.md)
 - [Deposit](docs/Deposit.md)
 - [Depositant](docs/Depositant.md)
 - [DepositantsRegister](docs/DepositantsRegister.md)
 - [DepositantsResponse](docs/DepositantsResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [GetDepositants](docs/GetDepositants.md)
 - [Institution](docs/Institution.md)
 - [InstitutionsList](docs/InstitutionsList.md)
 - [Item](docs/Item.md)
 - [MessageAccountBeneficiary](docs/MessageAccountBeneficiary.md)
 - [MessageCEP](docs/MessageCEP.md)
 - [MessageCodiAction](docs/MessageCodiAction.md)
 - [MessageConfigurationsLimits](docs/MessageConfigurationsLimits.md)
 - [MessageDepositReceived](docs/MessageDepositReceived.md)
 - [MessageInstitution](docs/MessageInstitution.md)
 - [MessagePayment](docs/MessagePayment.md)
 - [MessagePaymentStatePending](docs/MessagePaymentStatePending.md)
 - [MessageRequestChanged](docs/MessageRequestChanged.md)
 - [MessageSalesPoint](docs/MessageSalesPoint.md)
 - [MessageSubscription](docs/MessageSubscription.md)
 - [MessageUserAuthorized](docs/MessageUserAuthorized.md)
 - [MessageWebHook](docs/MessageWebHook.md)
 - [Operations](docs/Operations.md)
 - [PagerResponseDto](docs/PagerResponseDto.md)
 - [Payment](docs/Payment.md)
 - [PaymentCODI](docs/PaymentCODI.md)
 - [PaymentRequestCodiResponseDTO](docs/PaymentRequestCodiResponseDTO.md)
 - [PaymentsRequestId](docs/PaymentsRequestId.md)
 - [Person](docs/Person.md)
 - [PreEnrollmentData](docs/PreEnrollmentData.md)
 - [PreEnrollmentResponse](docs/PreEnrollmentResponse.md)
 - [PreMonexAuthorization](docs/PreMonexAuthorization.md)
 - [Relationship](docs/Relationship.md)
 - [RelationshipsResponse](docs/RelationshipsResponse.md)
 - [SalesPoint](docs/SalesPoint.md)
 - [SalesPointFound](docs/SalesPointFound.md)
 - [SalesPointRequest](docs/SalesPointRequest.md)
 - [SalesPointRespose](docs/SalesPointRespose.md)
 - [SpidBeneficiariesResponse](docs/SpidBeneficiariesResponse.md)
 - [SpidBeneficiaryResponse](docs/SpidBeneficiaryResponse.md)
 - [SpidClassificationDTO](docs/SpidClassificationDTO.md)
 - [SpidClassificationsResponseDTO](docs/SpidClassificationsResponseDTO.md)
 - [TokenRequiredResponse](docs/TokenRequiredResponse.md)
 - [TransactionOutgoing](docs/TransactionOutgoing.md)
 - [TransactionOutgoingSpid](docs/TransactionOutgoingSpid.md)
 - [TransactionsOutgoingRegister](docs/TransactionsOutgoingRegister.md)
 - [UpdateConfigurationsRequestDTO](docs/UpdateConfigurationsRequestDTO.md)
 - [UrlsRedirect](docs/UrlsRedirect.md)
 - [UserCompany](docs/UserCompany.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookRequest](docs/WebhookRequest.md)
 - [WebhookResponse](docs/WebhookResponse.md)
 - [WebhooksList](docs/WebhooksList.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author


