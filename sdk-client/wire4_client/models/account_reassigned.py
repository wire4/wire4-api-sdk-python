# coding: utf-8

"""
    Wire4RestAPI

     # Referencia de API La API de Wire4 está organizada en torno a REST. Nuestra API tiene URLs predecibles orientadas a los recursos, acepta peticiones en formato JSON, y las respuestas devueltas son formato JSON y utiliza códigos de respuesta HTTP, autenticación y verbos estándares.  Puede usar la API de Wire4 en nuestro entorno de prueba, que no afecta sus productivos ni interactúa con la red bancaria. La URL de conexión que se usa para invocar los servicios determina si la solicitud es en modo en de prueba o en modo producción.    # Autenticación La API de Wire4 utiliza el protocolo OAuth 2.0 para autenticación y autorización.   Para comenzar, es necesario que registre una cuenta en nuestro ambiente de pruebas en [registro](https://app-sndbx.wire4.mx/#/register) y obtenga las credenciales de cliente OAuth 2.0 desde la [consola de administración](https://app-sndbx.wire4.mx/#/dashboard/api-keys).   Esta página ofrece una descripción general de los escenarios de autorización de OAuth 2.0 que admite Wire4.   Después de crear su aplicación con Wire4, asegúrese de tener a la mano su `client_id` y `client_secret`. El siguiente paso es descubrir qué flujo de OAuth2 es el adecuado para sus propósitos.   ## URLS La siguiente tabla muestra las urls de los recursos de autenticación para el ambiente de pruebas.  URL                  | Descripción ------------------------------------ | ------------- https://sandbox-api.wire4.mx/token   | Obtener token de autorización llaves de API (*client_id*, *client_secret*), datos de suscripción (*client_id*, *client_secret*, *user_key*, *user_secret*) o (*refresh_token*) https://sandbox-api.wire4.mx/revoke  | Revocación de token  **Nota:** De acuerdo con el RFC 6749, la URL del token sólo acepta el tipo de contenido x-www-form-urlencoded. El contenido JSON no está permitido y devolverá un error.  ## Scopes Los `scopes` limitan el acceso de una aplicación a los recursos de Wire4. Se ofrecen los siguientes scopes de acuerdo al producto:  Producto                             |Scope                      | Descripción -------------------------------------|------------------------------------ | ------------- SPEI-SPID                            |general                              | Permite llamar a operaciones que no requieren a un cliente Monex suscrito en Wire4, los recursos que se pueden consumir con este scope son: consulta de Instituciones, CEP y generación de una presuscripción. SPEI-SPID                            |spei_admin                           | Permite llamar a operaciones que requieren de un cliente Monex suscrito en Wire4, ya que se proporciona información de saldos, administración de transacciones, cuentas de beneficiarios y cuentas de depositantes. SPEI-SPID                            |spid_admin                           | Permite llamar sólo a operaciones SPID, se requiere de un cliente Monex suscrito en Wire4. CODI                                 |codi_general                         | Permite llamar a operaciones de administración sobre el producto CoDi, como creación y listado de empresas  CODI                                 |codi_admin                           | Permite llamar sólo a operaciones CoDi dentro de un punto de venta, las operaciones incluyen creación, consulta, listado, etc de peticiones de pago CODI                                 |codi_report                          | Permite generar reportes de operaciones CoDi. TODOS                                |device_[dispositivo]                 | Se debe especificar cuándo se gestionan token's desde distintos dispositivos.  ## Tipos de autenticación   Wire4 cuenta con dos tipos de autenticación: Autenticación de Aplicación (OAuth 2.0  Client Credentials Grant)  y Autenticación de Usuario de Aplicación (OAuth 2.0 Password Grant).  ### Autenticación de Aplicación  Esta autenticación se obtiene proporcionando únicamente las llaves de API las cuáles se pueden consultar en [Llaves de API](https://app-sndbx.wire4.mx/#/dashboard/api-keys) de la consola de administración.  La autenticación de aplicación permite accesso a recursos generales y de administración que dependeran del scope.  Para este tipo de autenticación se sigue el flujo OAuth 2.0 Client Credentials Grant, que se describe más adelante en **Obtener el token de acceso de aplicación**, algunos de los recursos que requieren este tipo de autenticación son:   * [/subscriptions/pre-subscription](link) * [/institutions](link>) * [/ceps](<link>) * [/codi/compaies](<link>)  ### Autenticación de Usuario de Aplicación  Esta autenticación se obtiene proporcionando las llaves de API las cuáles se pueden consultar en [Llaves de API](https://app-sndbx.wire4.mx/#/dashboard/api-keys) más el ***user_key*** y ***user_secret*** que se proporcionan al momento de crear una suscripción o un punto de venta, para más información puedes consultar las guías [creación de suscripción](https://www.wire4.mx/#/guides/subscriptions), [creación de punto de venta](https://www.wire4.mx/#/guides/salespoint).  Con este tipo de autenticación se puede acceder a los recursos especificos que requieren configuraciones y acceso más puntual como información de una cuentas, saldos y administración de transacciones SPEID-SPID o CODI.    ## Obtener token de acceso Antes de que su aplicación pueda acceder a los datos mediante la API de Wire4, debe obtener un token de acceso ***(access_token)*** que le otorgue acceso a la API. En las siguientes secciones se muestra como obtener un token para cada una de las autenticaciones.     ### Obtener el token de acceso para autenticación de aplicación  El primer paso es crear la solicitud de token de acceso (*access_token*), con los parámetros que identifican su aplicación, el siguiente código muestra cómo obtener un `token`.  ``` curl -k -d \"grant_type= client_credentials&scope=general\"  -u \"<client id>:<client secret>\" https://sandbox-api.wire4.mx/token ``` **Ejemplo:**   ``` curl -k -d \"grant_type=client_credentials&scope=general\"  -u \"8e59YqaFW_Yo5dwWNxEY8Lid0u0a:AXahn79hfKWBXKzQfj011x8cvcQa\"  https://sandbox-api.wire4.mx /token ``` Obtendrá una respuesta como la que se muestra a continuación, donde se debe obtener el *access_token* para realizar llamadas posteriores a la API.   ``` {     \"access_token\":\"eyJ4NXQiOiJZak5sWVdWa05tWmlNR1ZoTldSaU1EUXpaREJpWlRJNU1qYzFZV1ZoWWpneU5UYzJPV05sWVEiLCJraWQiOiJZak5sWVdWa05tWmlNR1ZoTldSaU1EUXpaREJpWlRJNU1qYzFZV1ZoWWpneU5UYzJPV05sWVEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpc21hZWwuZXNjYW1pbGxhQHRjcGlwLnRlY2hAc2FuZGJveC5zcGVpb2suY29tIiwiYXVkIjoiOGU1OVlxYUZXX1lvNWR3V054RVk4TGlkMHUwYSIsIm5iZiI6MTU3MTMyMDg3NywiYXpwIjoiOGU1OVlxYUZXX1lvNWR3V054RVk4TGlkMHUwYSIsInNjb3BlIjoiYW1fYXBwbGljYXRpb25fc2NvcGUgZ2VuZXJhbCIsImlzcyI6ImFwaW0taWRwIiwiZXhwIjoxNTcxMzI0NDc3LCJpYXQiOjE1NzEzMjA4NzcsImp0aSI6ImJkMTdjMjcyLTg4MGQtNDk0ZS1iMTMwLTBiYTkwMjYyN2M4NCJ9.AjngGylkd_Chs5zlIjyLRPu9xPGyz4dfCd_aax2_ts653xrnNMoLpVHUDmaxIDFF2XyBJKH2IAbKxjo6VsFM07QkoPhlysO1PLoAF-Vkt4xYkh-f7nJRl0oOe2utDWFlUdgiAOmx5tPcStrdCEftgNNrjwJ50LXysFjXVshpoST-zIJPLgXknM3esGrkAsLcZRM7XUB187jxLHbtefVYPMvSO31T9pd5_Co9UXdeHpuA98sk_wZknASM1phxXQZAMLRLHz3LYvjCWCr_v80oVCM9SWTzf0vrMI6xphoIfirfWloADKPTTSUpIGBw9ePF_WbEPvbMm_BZaApJcEH2w\",    \"scope\":\"am_application_scope general\",    \"token_type\":\"Bearer\",    \"expires_in\":3600 }  ```  Es posible generar tokens con más de un scope, en caso que sea necesario utilizar dicho token para hacer más de una operación. Para generarlo basta con agregarlo a la petición separado por un espacio.     ``` curl -k -d \"grant_type=client_credentials&scope=codi_general codi_report\"  -u \"8e59YqaFW_Yo5dwWNxEY8Lid0u0a:AXahn79hfKWBXKzQfj011x8cvcQa\"  https://sandbox-api.wire4.mx /token ```  ### Obtener el token de acceso para autenticación usuario de aplicación   Antes de que su aplicación pueda acceder a los datos de una cuenta Monex mediante la API de Wire4, debe obtener un token de acceso  (*access_token*) que le otorgue acceso a la API y contar con el  *user_key* y *user_secret* que se proporcionan al momento de crear  una suscripción para más información puedes consultar [creación de suscripción](https://wire4.mx/#/guides/subscriptions) .   El primer paso es crear la solicitud de token de acceso con los parámetros que identifican su aplicación y la suscripción y con `scope` `spei_admin`  ```   curl -k -d \"grant_type=password&scope=spei_admin&username=<user_key>&password=<user_secret>\"  -u \"<client_id>:<client_secret>\" https://sandbox-api.wire4.mx/token ``` **Ejemplo**  ``` curl -k -d \"grant_type=password&scope=spei_admin&username=6 nbC5e99tTO@sandbox.wire4com&password= Nz7IqJGe9h\" -u \" zgMlQbqmOr:plkMJoPXCI\" https://sandbox-api.wire4.mx /token  ```  ``` {     \"access_token\":\"eyJ4NXQiOiJPR1EyTURFM00yTmpObVZoTnpFeE5EWXlObUV4TURKa01qUTJaVEU0TWpGaE1tVmlZakV5TkEiLCJraWQiOiJPR1EyTURFM00yTmpObVZoTnpFeE5EWXlObUV4TURKa01qUTJaVEU0TWpGaE1tVmlZakV5TkEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIzMzE0ODRlZTdjZDRkYWU5MzRmMjY2Zjc5YmY1YWFAZGV2LWllc2NhbWlsbGEuc3BlaW9rLmNvbSIsImF1ZCI6IkJVR0xjNWw1bW5CZXlPeGxtamNUZ0JoS19WTWEiLCJuYmYiOjE1NzEzNDk4ODMsImF6cCI6IkJVR0xjNWw1bW5CZXlPeGxtamNUZ0JoS19WTWEiLCJzY29wZSI6InNwZWlfYWRtaW4iLCJpc3MiOiJhcGltLWlkcCIsImV4cCI6MTU3MTM1MzQ4MywiaWF0IjoxNTcxMzQ5ODgzLCJqdGkiOiJiOWQ1M2Q0MC0xN2MwLTQxOTItYjUwNy0wZWFhN2ZkNDA1MGYifQ.hLTk8AFoIce1GpLcgch-U5aLLgiiFTo49wfBErD8D6VF-H9sG13ZyfAx9T-vQkk2m1zPapYVQjwibz3GRAJMN0Vczs6flV1mUJwFDQbEE-AELPdRcaRFOMBCfF6H9TVLfhFsGb9U2pVR9TLJcKqR57DyO_dIcc9I6d0tIkxqn2VcqypLVi5YQf36WzBbPeG-iPHYpMA-bhr4rwfjKA-O6jm1NSSxNHF4sHS0YHDPoO_x6cCc677MQEe0_CozfnQhoEWNfG8tcWUqhPtmcfjqon1p7PdQoXxriq_R85d06pVO9Se7Q6ok0V8Qgz0MOJ6z3ku6mtZSuba7niMAOt2TyA\",    \"refresh_token\":\"f962d5c6-0d99-3809-8275-11c7aa0aa020\",    \"scope\":\"spei_admin\",    \"token_type\":\"Bearer\",    \"expires_in\":3600 } ```  **Suscripciones in activas**   En caso de intentar obtener el token de acceso para una suscriptión que no esta activa obtendra una respuesta de error con código 400 ``` curl -k -d \"grant_type=password&scope=spei_admin&username=6 nbC5e99tTO@sandbox.wire4com&password= Nz7IqJGe9h\" -u \" zgMlQbqmOr:plkMJoPXCI\" https://sandbox-api.wire4.mx /token  ``` ``` {     \"error_description\": \"Error while authenticating user from user store\",     \"error\": \"invalid_grant\" } ```    Una vez que la suscripción se reactive podrá generar el token de acceso de forma normal.    **Nota:** Los ejemplos anteriores se presentan considerando que se realiza una implementación desde cero,  esto se puede simplificar a sólo configurar sus llaves (*client_id*, *client_secret*),  datos de suscripción (*client_id*, *client_secret*, *user_key*, *user_secret*) si utiliza nuestros sdks.      **Consideraci&oacute;n:** Si la aplicaci&oacute;n en la que implementar&aacute; Wire4 estar&aacute; desplegada en más de una instancia o servidor en cada solicitud de token debe especificar un scope adicional. La forma de hacer esto es que, cuándo se solicita un token se debe especificar un scope adicional con el prefijo \"device_\" +  el dispositivo, por ejemplo:                                                                                                                                                                                                                     device_server1<br> device_server2  en consecuencia cada instancia debe operar con el token gestionado. ***Si se opera con el mismo token en instancias diferentes encontrará problemas de Credenciales Inv&aacute;lidas.***  **Ejemplo de solicitud de token para instancias diferentes:**  ``` curl -k -d \"grant_type=password&username=0883b97333046abb76367698b57d9e@sandbox.wire4.mx&password=9e0d81f95705079b9fe1e129315c25&scope=device_server1 codi_admin\" -H \"Authorization: Basic dmZSeURpTHdFbVZqd2VIclp0OWRMbXFmb3YwYTpJQJBuamBac3V6SllLWlJHUkJEYUZrN1BhRmNh\" https://sandbox-api.wire4.mx/token  curl -k -d \"grant_type=password&username=0883b97333046abb76367698b57d9e@sandbox.wire4.mx&password=9e0d81f95705079b9fe1e129315c25&scope=device_server2 codi_admin\" -H \"Authorization: Basic dmZSeURpTHdFbVZqd2VIclp0OWRMbXFmb3YwYTpJQJBuamBac3V6SllLWlJHUkJEYUZrN1BhRmNh\" https://sandbox-api.wire4.mx/token ```  ## Caducidad del token El token de acceso es válido durante 60 minutos (una hora), después de transcurrido este tiempo se debe solicitar un nuevo token,  cuando el token caduca se obtendrá un error ***401 Unauthorized*** con mensaje ***“Invalid Credentials”.***   El nuevo token se puede solicitar  utilizando el último token de actualización (***refresh_token***) que se devolvió en la solicitud del token,   esto sólo aplica para el token de tipo password (Autenticación de Usuario de Aplicación). El siguiente ejemplo muestra cómo obtener un toke con el token de actualización.  ``` curl -k -d \"grant_type=refresh_token&refresh_token=<refresh_token>\" -u \" Client_Id:Client_Secret\" -H \"Content-Type: application/x-www-form-urlencoded\" https://sandbox-api.wire4.mx/oauth2/token ```  **Ejemplo:**  ``` curl -k -d \"grant_type=refresh_token&refresh_token=f932d5c6-0d39-3809-8275-11c7ax0aa020\" -u \"zgMlQbqmOr:plkMJoPXCI\" -H \"Content-Type: application/x-www-form-urlencoded\" https://sandbox-api.wire4.mx/token ```  El token de actualización (***refresh_token***) tiene una duración de hasta 23 horas. Si en este periodo no se utiliza, se tienen que solicitar un nuevo token.  Un token de acceso podría dejar de funcionar por uno de estos motivos:  * El usuario ha revocado el acceso a su aplicación, si un usuario ha solicitado la baja de su aplicación de WIre4. * El token de acceso ha caducado: si el token de acceso ha pasado de una hora, recibirá un error ***401 Unauthorized*** mientras realiza una llamada a la API de Wire4. Cuando esto sucede, debe solicitar un nuevo token utilizando el token de actualización que recibió por última al solicitar un token, sólo aplica si el token en cuestión es de autenticación de usuario de aplicación, en caso contrario solicitar un nuevo token.   ## Revocar token Su aplicación puede revocar mediante programación el token de acceso, una vez revocado el token no podrá hacer uso de él para acceder a la API. El siguiente código muestra un ejemplo de cómo revocar el token:    ```  curl -X POST --basic -u \"<client id>:<client secret>\" -H \"Content-Type: application/x-www-form-urlencoded;charset=UTF-8\" -k -d \"token=<token to revoke>&token_type_hint=access_token\" https://sandbox-api.wire4.mx/revoke ```      **Ejemplo:**  ```   curl -X POST --basic -u \"8e59YqaFW_Yo5dwWNxEY8Lid0u0a:AXahn79hfKWBXKzQfj011x8cvcQa\" -H \"Content-Type: application/x-www-form-urlencoded;charset=UTF-8\" -k -d \"token=eyJ4NXQiOiJZak5sWVdWa05tWmlNR1ZoTldSaU1EUXpaREJpWlRJNU1qYzFZV1ZoWWpneU5UYzJPV05sWVEiLCJraWQiOiJZak5sWVdWa05tWmlNR1ZoTldSaU1EUXpaREJpWlRJNU1qYzFZV1ZoWWpneU5UYzJPV05sWVEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJpc21hZWwuZXNjYW1pbGxhQHRjcGlwLnRlY2hAc2FuZGJveC5zcGVpb2suY29tIiwiYXVkIjoiOGU1OVlxYUZXX1lvNWR3V054RVk4TGlkMHUwYSIsIm5iZiI6MTU3MTMyMDg3NywiYXpwIjoiOGU1OVlxYUZXX1lvNWR3V054RVk4TGlkMHUwYSIsInNjb3BlIjoiYW1fYXBwbGljYXRpb25fc2NvcGUgZ2VuZXJhbCIsImlzcyI6ImFwaW0taWRwIiwiZXhwIjoxNTcxMzI0NDc3LCJpYXQiOjE1NzEzMjA4NzcsImp0aSI6ImJkMTdjMjcyLTg4MGQtNDk0ZS1iMTMwLTBiYTkwMjYyN2M4NCJ9.AjngGylkd_Chs5zlIjyLRPu9xPGyz4dfCd_aax2_ts653xrnNMoLpVHUDmaxIDFF2XyBJKH2IAbKxjo6VsFM07QkoPhlysO1PLoAF-Vkt4xYkh-f7nJRl0oOe2utDWFlUdgiAOmx5tPcStrdCEftgNNrjwJ50LXysFjXVshpoST-zIJPLgXknM3esGrkAsLcZRM7XUB187jxLHbtefVYPMvSO31T9pd5_Co9UXdeHpuA98sk_wZknASM1phxXQZAMLRLHz3LYvjCWCr_v80oVCM9SWTzf0vrMI6xphoIfirfWloADKPTTSUpIGBw9ePF_WbEPvbMm_BZaApJcEH2w&token_type_hint=access_token\"  https://sandbox-api.wire4.mx/revoke ```  # Ambientes  Wire4 cuentas con dos ambientes Pruebas (Sandbox) y Producción, son dos ambientes separados los cuáles se pueden utilizar simultáneamente. Los usuarios que han sido creados en cada uno de los ambientes no son intercambiables.   Las ligas de acceso a la `api` para cada uno de los ambientes son:  * Pruebas  https://sandbox-api.wire4.mx * Producción https://api.wire4.mx     # Eventos  Los eventos son nuestra forma de informarle cuando algo sucede en su cuenta. Cuando ocurre un evento se crea un objeto  [Evento](#tag/Webhook-Message). Por ejemplo, cuando se recibe un depósito, se crea un evento TRANSACTION.INCOMING.UPDATED.   Los eventos ocurren cuando cambia el estado de un recurso. El recurso se encuentra dentro del objeto [Evento](#tag/Webhook-Message) en el campo data.  Por ejemplo, un evento TRANSACTION.INCOMING.UPDATED contendrá un depósito y un evento ACCOUNT.CREATED contendrá una cuenta.   Wire4 puede agregar más campos en un futuro, o agregar nuevos valores a campos existentes, por lo que es recomendado que tu endpoint pueda manejar datos adicionales desconocidos. En esta [liga](#tag/Webhook-Message) se encuentra  la definición del objeto [Evento](#tag/Webhook-Message).  ## Tipos de Eventos  Wire4 cuenta con los siguientes tipos de eventos*   | Evento                               | Tipo                               | Objeto                                                  | | ------------------------------------ |----------------------------------- | ------------------------------------------------------- | | Suscripción                          | ENROLLMENT.CREATED                 | [suscription](#tag/subscription)                        | | Cuenta de beneficiario               | ACCOUNT.CREATED                    | [beneficiary](#tag/BeneficiaryAccount)                  | | Depósito recibido                    | TRANSACTION.INCOMING.UPDATED       | [spei_incoming](#tag/deposit)                           | | Solicitud de autorización de depósito| TRANSACTION.INCOMING.AUTHORIZATION | [spei_incoming_authorization](#tag/depositAuthorization)| | Transferencia realizada              | TRANSACTION.OUTGOING.RECEIVED      | [spei_outgoing](#tag/transfer)                          | | Transferencia SPID enviada           | TRANSACTION.OUTGOING.SPID.RECEIVED | [spid_outgoing](#tag/transfer)                          | | Transferencias Autorizadas           | REQUEST.OUTGOING.CHANGED           | [request_outgoing](#tag/requestOutMsg)                  | | Operación CoDi                       | CODI.ACTIONS                       | [codi_actions](#tag/codiActions)                        | | Punto de venta CoDi                  | SALE.POINT.CREATED                 | [codi_sales_point](#tag/codiSalesPoint)                 |   # Codigos de Error Al registrar transferencias tanto SPEI como SPID se aplican las validaciones de formato de datos a la petición descritas en la definición de cada recurso. Si la petición contiene errores, se genera una respuesta de error 409 que contiene el listado de las validaciones que no fueran exitosas.  Por cada error detectado se genera un elemento \"error\" que contiene el order_id de la transacción que genero el error, el código de error y un mensaje con más información sobre el mismo.  Si una misma transacción contiene varios errores, la respuesta  tendrá un elemento en la lista \"errors\" por cada validación que no fue exitosa.  Existen dos casos por los cuales alguno de los elementos en el listado de errores puede no contener order_id:  * Si alguna transacción no provee esta información  * En caso de transacciones SPEI, si el error está en las URLs ya que son datos relacionados a un lote de transacciones     **Ejemplo:**    ```   {      \"http_status\": 409,     \"message\": \"La divisa es incorrecta para esta transacción se espera: MXP, y se recibió: MXPD., El identificador 18e9c4a3-8c7a-42e8-99f4-ebi7r5r6y034 esta duplicado.\",     \"errors\": [         {             \"error\": \"La divisa es incorrecta para esta transacción se espera: MXP, y se recibió: MXPD.\",             \"code\": \"TR-1010\",             \"order_id\": \"18e9c4a3-8c7a-42e8-99f4-ebi7r5r6y034\"         },         {             \"error\": \"El identificador 18e9c4a3-8c7a-42e8-99f4-ebi7r5r6y034 esta duplicado.\",             \"code\": \"TR-1004\",             \"order_id\": \"18e9c4a3-8c7a-42e8-99f4-ebi7r5r6y034\"         }     ] }  ```      ## Códigos de error para generación de transferencias SPEI/SPID | Código                        | Descripción                                                                        | |-------------------------------|-----------------------------------------------------------------------------------| |A-1001     |La URL para éxito es requerida                                                                         | | A-1002  |La URL para retorno en caso de error es requerida                                                      | | TR-1001  |La petición debe incluir al menos una transacción                                                      | | TR-1002  |El identificador de la transacción es requerido                                                         | | TR-1003  |El identificador de la transacción no es valido                                                         | | TR-1004  |El identificador de la transacción esta duplicado                                                       | | TR-1005  |El monto de la transacción es requerido                                                                | | TR-1006  |El valor del monto no es valido                                                                        | | TR-1007  |La cuenta de beneficiario es requerida                                                                  | | TR-1008  |La cuenta de beneficiario no es valida                                                                  | | TR-1009  |El código de moneda es requerido                                                                       | | TR-1010  |El código de moneda no es valido                                                                       | | TR-1011  |El listado de email supera 10 elementos                                                                | | TR-1012  |La referencia es requerida                                                                             | | TR-1013  |La referencia no es valida                                                                             | | TR-1014  |El concepto es requerido                                                                               | | TR-1015  |El concepto no es valido                                                                               | | TR-1016  |El identificador de clasificación SPID es requerido                                                      |  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from wire4_client.models.beneficiary_institution import BeneficiaryInstitution  # noqa: F401,E501
from wire4_client.models.institution import Institution  # noqa: F401,E501
from wire4_client.models.person import Person  # noqa: F401,E501


class AccountReassigned(object):
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
        'bank': 'Institution',
        'beneficiary_account': 'str',
        'currency_code': 'str',
        'email': 'list[str]',
        'institution': 'BeneficiaryInstitution',
        'kind_of_relationship': 'str',
        'numeric_reference_spei': 'str',
        'payment_concept_spei': 'str',
        'person': 'Person',
        'register_date': 'datetime',
        'relationship': 'str',
        'rfc': 'str',
        'status': 'str'
    }

    attribute_map = {
        'amount_limit': 'amount_limit',
        'bank': 'bank',
        'beneficiary_account': 'beneficiary_account',
        'currency_code': 'currency_code',
        'email': 'email',
        'institution': 'institution',
        'kind_of_relationship': 'kind_of_relationship',
        'numeric_reference_spei': 'numeric_reference_spei',
        'payment_concept_spei': 'payment_concept_spei',
        'person': 'person',
        'register_date': 'register_date',
        'relationship': 'relationship',
        'rfc': 'rfc',
        'status': 'status'
    }

    def __init__(self, amount_limit=None, bank=None, beneficiary_account=None, currency_code=None, email=None, institution=None, kind_of_relationship=None, numeric_reference_spei=None, payment_concept_spei=None, person=None, register_date=None, relationship=None, rfc=None, status=None):  # noqa: E501
        """AccountReassigned - a model defined in Swagger"""  # noqa: E501
        self._amount_limit = None
        self._bank = None
        self._beneficiary_account = None
        self._currency_code = None
        self._email = None
        self._institution = None
        self._kind_of_relationship = None
        self._numeric_reference_spei = None
        self._payment_concept_spei = None
        self._person = None
        self._register_date = None
        self._relationship = None
        self._rfc = None
        self._status = None
        self.discriminator = None
        self.amount_limit = amount_limit
        if bank is not None:
            self.bank = bank
        self.beneficiary_account = beneficiary_account
        if currency_code is not None:
            self.currency_code = currency_code
        if email is not None:
            self.email = email
        if institution is not None:
            self.institution = institution
        self.kind_of_relationship = kind_of_relationship
        if numeric_reference_spei is not None:
            self.numeric_reference_spei = numeric_reference_spei
        if payment_concept_spei is not None:
            self.payment_concept_spei = payment_concept_spei
        if person is not None:
            self.person = person
        if register_date is not None:
            self.register_date = register_date
        self.relationship = relationship
        self.rfc = rfc
        if status is not None:
            self.status = status

    @property
    def amount_limit(self):
        """Gets the amount_limit of this AccountReassigned.  # noqa: E501

        Es el monto límite permitido que se registra para la cuenta. Por ejemplo 1000.00.  # noqa: E501

        :return: The amount_limit of this AccountReassigned.  # noqa: E501
        :rtype: float
        """
        return self._amount_limit

    @amount_limit.setter
    def amount_limit(self, amount_limit):
        """Sets the amount_limit of this AccountReassigned.

        Es el monto límite permitido que se registra para la cuenta. Por ejemplo 1000.00.  # noqa: E501

        :param amount_limit: The amount_limit of this AccountReassigned.  # noqa: E501
        :type: float
        """
        if amount_limit is None:
            raise ValueError("Invalid value for `amount_limit`, must not be `None`")  # noqa: E501

        self._amount_limit = amount_limit

    @property
    def bank(self):
        """Gets the bank of this AccountReassigned.  # noqa: E501


        :return: The bank of this AccountReassigned.  # noqa: E501
        :rtype: Institution
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """Sets the bank of this AccountReassigned.


        :param bank: The bank of this AccountReassigned.  # noqa: E501
        :type: Institution
        """

        self._bank = bank

    @property
    def beneficiary_account(self):
        """Gets the beneficiary_account of this AccountReassigned.  # noqa: E501

        Es la cuenta del beneficiario, podría ser teléfono celular (se valida que sea de 10 dígitos), Tarjeta de débito (TDD, se valida que sea de 16 dígitos) o cuenta CLABE (se valida que sea de 18 dígitos). <br/><br/>Por ejemplo Teléfono celular: 5525072600, TDD: 4323 1234 5678 9123, CLABE: 032180000118359719.  # noqa: E501

        :return: The beneficiary_account of this AccountReassigned.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_account

    @beneficiary_account.setter
    def beneficiary_account(self, beneficiary_account):
        """Sets the beneficiary_account of this AccountReassigned.

        Es la cuenta del beneficiario, podría ser teléfono celular (se valida que sea de 10 dígitos), Tarjeta de débito (TDD, se valida que sea de 16 dígitos) o cuenta CLABE (se valida que sea de 18 dígitos). <br/><br/>Por ejemplo Teléfono celular: 5525072600, TDD: 4323 1234 5678 9123, CLABE: 032180000118359719.  # noqa: E501

        :param beneficiary_account: The beneficiary_account of this AccountReassigned.  # noqa: E501
        :type: str
        """
        if beneficiary_account is None:
            raise ValueError("Invalid value for `beneficiary_account`, must not be `None`")  # noqa: E501

        self._beneficiary_account = beneficiary_account

    @property
    def currency_code(self):
        """Gets the currency_code of this AccountReassigned.  # noqa: E501

        Es el código de divisa. Es en el formato estándar de 3 dígitos, por ejemplo para el peso mexicano: <b>MXP</b>, para el dólar estadounidense: <b>USD</b>.<br/><br/>Este dato es opcional, al registrar una cuenta si no se cuenta con este valor se asignará <b>MXP</b>  # noqa: E501

        :return: The currency_code of this AccountReassigned.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this AccountReassigned.

        Es el código de divisa. Es en el formato estándar de 3 dígitos, por ejemplo para el peso mexicano: <b>MXP</b>, para el dólar estadounidense: <b>USD</b>.<br/><br/>Este dato es opcional, al registrar una cuenta si no se cuenta con este valor se asignará <b>MXP</b>  # noqa: E501

        :param currency_code: The currency_code of this AccountReassigned.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def email(self):
        """Gets the email of this AccountReassigned.  # noqa: E501

        Es una lista de correos electrónicos (emails). Se valida el formato de email. Este campo es opcional.  # noqa: E501

        :return: The email of this AccountReassigned.  # noqa: E501
        :rtype: list[str]
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccountReassigned.

        Es una lista de correos electrónicos (emails). Se valida el formato de email. Este campo es opcional.  # noqa: E501

        :param email: The email of this AccountReassigned.  # noqa: E501
        :type: list[str]
        """

        self._email = email

    @property
    def institution(self):
        """Gets the institution of this AccountReassigned.  # noqa: E501


        :return: The institution of this AccountReassigned.  # noqa: E501
        :rtype: BeneficiaryInstitution
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """Sets the institution of this AccountReassigned.


        :param institution: The institution of this AccountReassigned.  # noqa: E501
        :type: BeneficiaryInstitution
        """

        self._institution = institution

    @property
    def kind_of_relationship(self):
        """Gets the kind_of_relationship of this AccountReassigned.  # noqa: E501

        Es el tipo de relación que se tiene con el propietario de la cuenta. Para registrar una cuenta, este valor se debe obtener del recurso <a href=\"#operation/getAvailableRelationshipsMonexUsingGET\">relationships.</a> <br /><br /><b>Nota:</b> <em>Si en la respuesta de Monex esta propiedad es nula, tampoco estará presente en esta respuesta.</em>  # noqa: E501

        :return: The kind_of_relationship of this AccountReassigned.  # noqa: E501
        :rtype: str
        """
        return self._kind_of_relationship

    @kind_of_relationship.setter
    def kind_of_relationship(self, kind_of_relationship):
        """Sets the kind_of_relationship of this AccountReassigned.

        Es el tipo de relación que se tiene con el propietario de la cuenta. Para registrar una cuenta, este valor se debe obtener del recurso <a href=\"#operation/getAvailableRelationshipsMonexUsingGET\">relationships.</a> <br /><br /><b>Nota:</b> <em>Si en la respuesta de Monex esta propiedad es nula, tampoco estará presente en esta respuesta.</em>  # noqa: E501

        :param kind_of_relationship: The kind_of_relationship of this AccountReassigned.  # noqa: E501
        :type: str
        """
        if kind_of_relationship is None:
            raise ValueError("Invalid value for `kind_of_relationship`, must not be `None`")  # noqa: E501

        self._kind_of_relationship = kind_of_relationship

    @property
    def numeric_reference_spei(self):
        """Gets the numeric_reference_spei of this AccountReassigned.  # noqa: E501

        Es la referencia numérica a utilizar cuando se realice una transferencia y no se especifique una referencia.  # noqa: E501

        :return: The numeric_reference_spei of this AccountReassigned.  # noqa: E501
        :rtype: str
        """
        return self._numeric_reference_spei

    @numeric_reference_spei.setter
    def numeric_reference_spei(self, numeric_reference_spei):
        """Sets the numeric_reference_spei of this AccountReassigned.

        Es la referencia numérica a utilizar cuando se realice una transferencia y no se especifique una referencia.  # noqa: E501

        :param numeric_reference_spei: The numeric_reference_spei of this AccountReassigned.  # noqa: E501
        :type: str
        """

        self._numeric_reference_spei = numeric_reference_spei

    @property
    def payment_concept_spei(self):
        """Gets the payment_concept_spei of this AccountReassigned.  # noqa: E501

        Es el concepto de pago a utilizar cuando se realice una transferencia y no se especifique un concepto  # noqa: E501

        :return: The payment_concept_spei of this AccountReassigned.  # noqa: E501
        :rtype: str
        """
        return self._payment_concept_spei

    @payment_concept_spei.setter
    def payment_concept_spei(self, payment_concept_spei):
        """Sets the payment_concept_spei of this AccountReassigned.

        Es el concepto de pago a utilizar cuando se realice una transferencia y no se especifique un concepto  # noqa: E501

        :param payment_concept_spei: The payment_concept_spei of this AccountReassigned.  # noqa: E501
        :type: str
        """

        self._payment_concept_spei = payment_concept_spei

    @property
    def person(self):
        """Gets the person of this AccountReassigned.  # noqa: E501


        :return: The person of this AccountReassigned.  # noqa: E501
        :rtype: Person
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this AccountReassigned.


        :param person: The person of this AccountReassigned.  # noqa: E501
        :type: Person
        """

        self._person = person

    @property
    def register_date(self):
        """Gets the register_date of this AccountReassigned.  # noqa: E501

        Es la fecha en la que se registró el beneficiario. Ésta fecha viene en formato ISO 8601 con zona horaria, ejemplo: <strong>2020-10-27T11:03:15.000-06:00</strong>.  # noqa: E501

        :return: The register_date of this AccountReassigned.  # noqa: E501
        :rtype: datetime
        """
        return self._register_date

    @register_date.setter
    def register_date(self, register_date):
        """Sets the register_date of this AccountReassigned.

        Es la fecha en la que se registró el beneficiario. Ésta fecha viene en formato ISO 8601 con zona horaria, ejemplo: <strong>2020-10-27T11:03:15.000-06:00</strong>.  # noqa: E501

        :param register_date: The register_date of this AccountReassigned.  # noqa: E501
        :type: datetime
        """

        self._register_date = register_date

    @property
    def relationship(self):
        """Gets the relationship of this AccountReassigned.  # noqa: E501

        Es la relación con el propietario de la cuenta, para registrar este valor se debe obtener del recurso <a href=\"#operation/getAvailableRelationshipsMonexUsingGET\">relationships.</a> <br/> <br/> <b>Nota:</b> Si en la respuesta de Monex, sta propiedad es nula, tampoco estará presente en esta respuesta.  # noqa: E501

        :return: The relationship of this AccountReassigned.  # noqa: E501
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """Sets the relationship of this AccountReassigned.

        Es la relación con el propietario de la cuenta, para registrar este valor se debe obtener del recurso <a href=\"#operation/getAvailableRelationshipsMonexUsingGET\">relationships.</a> <br/> <br/> <b>Nota:</b> Si en la respuesta de Monex, sta propiedad es nula, tampoco estará presente en esta respuesta.  # noqa: E501

        :param relationship: The relationship of this AccountReassigned.  # noqa: E501
        :type: str
        """
        if relationship is None:
            raise ValueError("Invalid value for `relationship`, must not be `None`")  # noqa: E501

        self._relationship = relationship

    @property
    def rfc(self):
        """Gets the rfc of this AccountReassigned.  # noqa: E501

        Es el Registro Federal de Contribuyentes (RFC) de la persona o institución propietaria dela cuenta. <br/> <br/><b>Nota:</b> Si en la respuesta de Monex esta propiedad es nula, tampoco estará presente en esta respuesta.  # noqa: E501

        :return: The rfc of this AccountReassigned.  # noqa: E501
        :rtype: str
        """
        return self._rfc

    @rfc.setter
    def rfc(self, rfc):
        """Sets the rfc of this AccountReassigned.

        Es el Registro Federal de Contribuyentes (RFC) de la persona o institución propietaria dela cuenta. <br/> <br/><b>Nota:</b> Si en la respuesta de Monex esta propiedad es nula, tampoco estará presente en esta respuesta.  # noqa: E501

        :param rfc: The rfc of this AccountReassigned.  # noqa: E501
        :type: str
        """
        if rfc is None:
            raise ValueError("Invalid value for `rfc`, must not be `None`")  # noqa: E501

        self._rfc = rfc

    @property
    def status(self):
        """Gets the status of this AccountReassigned.  # noqa: E501

        Es el estado en el que se encuentra el registo del beneficiario.<br>Los valores pueden ser:<ul style=\"font-size: 12px; font-weight: 600;\"><li>RECEIVED</li><li>DELETED</li><li>REQUEST_ERROR_BY_MONEX</li><li>REQUESTED_TO_MONEX</li><li>NOTIFIED_BY_MONEX</li><li>NOTIFIED_BY_SPEIOK<li></li>NOTIFIED_WITH_ERROR_BY_SPEIOK</li><li>PENDING</li></ul>  # noqa: E501

        :return: The status of this AccountReassigned.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountReassigned.

        Es el estado en el que se encuentra el registo del beneficiario.<br>Los valores pueden ser:<ul style=\"font-size: 12px; font-weight: 600;\"><li>RECEIVED</li><li>DELETED</li><li>REQUEST_ERROR_BY_MONEX</li><li>REQUESTED_TO_MONEX</li><li>NOTIFIED_BY_MONEX</li><li>NOTIFIED_BY_SPEIOK<li></li>NOTIFIED_WITH_ERROR_BY_SPEIOK</li><li>PENDING</li></ul>  # noqa: E501

        :param status: The status of this AccountReassigned.  # noqa: E501
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
        if issubclass(AccountReassigned, dict):
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
        if not isinstance(other, AccountReassigned):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
