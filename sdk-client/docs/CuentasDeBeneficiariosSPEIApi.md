# wire4_client.CuentasDeBeneficiariosSPEIApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_accounts_pending_put**](CuentasDeBeneficiariosSPEIApi.md#authorize_accounts_pending_put) | **PUT** /subscriptions/{subscription}/beneficiaries/pending | Recibe la solicitud para agrupar las cuentas SPEI/SPID de beneficiarios en estado pendiente que deben ser autorizadas
[**delete_account_using_delete**](CuentasDeBeneficiariosSPEIApi.md#delete_account_using_delete) | **DELETE** /subscriptions/{subscription}/beneficiaries/spei/{account} | Elimina la cuenta del beneficiario
[**get_available_relationships_monex_using_get**](CuentasDeBeneficiariosSPEIApi.md#get_available_relationships_monex_using_get) | **GET** /subscriptions/{subscription}/beneficiaries/relationships | Consulta de relaciones
[**get_beneficiaries_by_request_id**](CuentasDeBeneficiariosSPEIApi.md#get_beneficiaries_by_request_id) | **GET** /subscriptions/{subscription}/beneficiaries/spei/{requestId} | Consulta los beneficiarios por el identificador de la petición de registro
[**get_beneficiaries_for_account_using_get**](CuentasDeBeneficiariosSPEIApi.md#get_beneficiaries_for_account_using_get) | **GET** /subscriptions/{subscription}/beneficiaries/spei | Consulta los beneficiarios registrados
[**pre_register_accounts_using_post**](CuentasDeBeneficiariosSPEIApi.md#pre_register_accounts_using_post) | **POST** /subscriptions/{subscription}/beneficiaries/spei | Pre-registro de cuentas de beneficiarios.
[**remove_beneficiaries_pending_using_delete**](CuentasDeBeneficiariosSPEIApi.md#remove_beneficiaries_pending_using_delete) | **DELETE** /subscriptions/{subscription}/beneficiaries/spei/request/{requestId} | Eliminación de beneficiarios SPEI® sin confirmar
[**update_amount_limit_account_using_put**](CuentasDeBeneficiariosSPEIApi.md#update_amount_limit_account_using_put) | **PUT** /subscriptions/{subscription}/beneficiaries/spei/{account} | Solicitud para actualizar el monto límite

# **authorize_accounts_pending_put**
> AuthorizedBeneficiariesResponse authorize_accounts_pending_put(body, authorization, subscription)

Recibe la solicitud para agrupar las cuentas SPEI/SPID de beneficiarios en estado pendiente que deben ser autorizadas

Solicta autorizar las cuentas de beneficiarios en estado pendiente agrupandolas en un set de cuentas que pueden incluir tanto cuentas de SPI como de SPID, debe indicar las urls de redireccion en caso de error y en caso de exito<br/>

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
body = wire4_client.UrlsRedirect() # UrlsRedirect | Información de la cuenta del beneficiario
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Recibe la solicitud para agrupar las cuentas SPEI/SPID de beneficiarios en estado pendiente que deben ser autorizadas
    api_response = api_instance.authorize_accounts_pending_put(body, authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->authorize_accounts_pending_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlsRedirect**](UrlsRedirect.md)| Información de la cuenta del beneficiario | 
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

[**AuthorizedBeneficiariesResponse**](AuthorizedBeneficiariesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_using_delete**
> delete_account_using_delete(authorization, account, subscription)

Elimina la cuenta del beneficiario

Borra la cuenta de beneficiario proporcionada relacionada al contrato perteneciente a la subscripción. La cuenta a borrar debe ser una cuenta que opere con SPEI.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
authorization = 'authorization_example' # str | Header para token
account = 'account_example' # str | La cuenta del beneciario que será eliminada
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Elimina la cuenta del beneficiario
    api_instance.delete_account_using_delete(authorization, account, subscription)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->delete_account_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **account** | **str**| La cuenta del beneciario que será eliminada | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_relationships_monex_using_get**
> RelationshipsResponse get_available_relationships_monex_using_get(authorization, subscription)

Consulta de relaciones

Obtiene las posibles relaciones existentes para registrar beneficiarios en Monex. Se debe invocar este recurso antes de pre-registrar una cuenta de beneficiario.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | Identificador de la suscripción a esta API

try:
    # Consulta de relaciones
    api_response = api_instance.get_available_relationships_monex_using_get(authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->get_available_relationships_monex_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| Identificador de la suscripción a esta API | 

### Return type

[**RelationshipsResponse**](RelationshipsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_beneficiaries_by_request_id**
> BeneficiariesResponse get_beneficiaries_by_request_id(authorization, request_id, subscription)

Consulta los beneficiarios por el identificador de la petición de registro

Obtiene los beneficiarios enviados para registro en una petición al contrato relacionado con la suscripción, Los beneficiarios son los que actualmente se encuentran registrados en banca Monex, que pertenezcan a la petición que se solicita.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
authorization = 'authorization_example' # str | Header para token
request_id = 'request_id_example' # str | El identificador de la petición del registro de beneficiarios a esta API
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Consulta los beneficiarios por el identificador de la petición de registro
    api_response = api_instance.get_beneficiaries_by_request_id(authorization, request_id, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->get_beneficiaries_by_request_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **request_id** | **str**| El identificador de la petición del registro de beneficiarios a esta API | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

[**BeneficiariesResponse**](BeneficiariesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_beneficiaries_for_account_using_get**
> BeneficiariesResponse get_beneficiaries_for_account_using_get(authorization, subscription, account=account, beneficiary_bank=beneficiary_bank, beneficiary_name=beneficiary_name, end_date=end_date, init_date=init_date, rfc=rfc, status=status)

Consulta los beneficiarios registrados

Obtiene los beneficiarios registrados al contrato relacionado con la suscripción, Los beneficiarios son los que actualmente se encuentran registrados en banca Monex.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API
account = 'account_example' # str | Cuenta del beneficiario, puede ser Clabe, TDD o Celular (optional)
beneficiary_bank = 'beneficiary_bank_example' # str | Clave del banco beneficiario (optional)
beneficiary_name = 'beneficiary_name_example' # str | Nombre del beneficiario (optional)
end_date = 'end_date_example' # str | Fecha de inicio del perido a filtrar en formato dd-mm-yyyy (optional)
init_date = 'init_date_example' # str | Fecha de inicio del perido a filtrar en formato dd-mm-yyyy (optional)
rfc = 'rfc_example' # str | RFC del beneficiario (optional)
status = 'status_example' # str | Estatus de la cuenta (optional)

try:
    # Consulta los beneficiarios registrados
    api_response = api_instance.get_beneficiaries_for_account_using_get(authorization, subscription, account=account, beneficiary_bank=beneficiary_bank, beneficiary_name=beneficiary_name, end_date=end_date, init_date=init_date, rfc=rfc, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->get_beneficiaries_for_account_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 
 **account** | **str**| Cuenta del beneficiario, puede ser Clabe, TDD o Celular | [optional] 
 **beneficiary_bank** | **str**| Clave del banco beneficiario | [optional] 
 **beneficiary_name** | **str**| Nombre del beneficiario | [optional] 
 **end_date** | **str**| Fecha de inicio del perido a filtrar en formato dd-mm-yyyy | [optional] 
 **init_date** | **str**| Fecha de inicio del perido a filtrar en formato dd-mm-yyyy | [optional] 
 **rfc** | **str**| RFC del beneficiario | [optional] 
 **status** | **str**| Estatus de la cuenta | [optional] 

### Return type

[**BeneficiariesResponse**](BeneficiariesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_register_accounts_using_post**
> TokenRequiredResponse pre_register_accounts_using_post(body, authorization, subscription)

Pre-registro de cuentas de beneficiarios.

Pre-registra una o más cuentas de beneficiario en la plataforma, proporcionando una URL donde el cuentahabiente Monex debe ingresar un valor de su llave digital para confirmar el alta de las cuentas de beneficiarios.<br/>Los posibles valores de <i>relationship</i> y <i>kind_of_relationship</i> se deben  obtener de /subscriptions/{subscription}/beneficiaries/relationships.<br/><br/>La confirmación de registro en Monex se realiza a través de una llamada a los webhooks registrados con el evento ACCOUNT.CREATED.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
body = wire4_client.AccountRequest() # AccountRequest | Información de la cuenta del beneficiario
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Pre-registro de cuentas de beneficiarios.
    api_response = api_instance.pre_register_accounts_using_post(body, authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->pre_register_accounts_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountRequest**](AccountRequest.md)| Información de la cuenta del beneficiario | 
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

[**TokenRequiredResponse**](TokenRequiredResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_beneficiaries_pending_using_delete**
> remove_beneficiaries_pending_using_delete(authorization, request_id, subscription)

Eliminación de beneficiarios SPEI® sin confirmar

Elimina un conjunto de beneficiarios a registrar en la cuenta del cliente Monex relacionada a la suscripción, los beneficiarios no deben haber sido confirmados por el cliente.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
authorization = 'authorization_example' # str | Header para token
request_id = 'request_id_example' # str | Identificador de los beneficiarios a eliminar
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Eliminación de beneficiarios SPEI® sin confirmar
    api_instance.remove_beneficiaries_pending_using_delete(authorization, request_id, subscription)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->remove_beneficiaries_pending_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **request_id** | **str**| Identificador de los beneficiarios a eliminar | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_amount_limit_account_using_put**
> TokenRequiredResponse update_amount_limit_account_using_put(body, authorization, account, subscription)

Solicitud para actualizar el monto límite

Inicia una solicitud para actualizar el monto límite a la cuenta de beneficiario proporcionada relacionada al contrato perteneciente a la subscripción.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CuentasDeBeneficiariosSPEIApi()
body = wire4_client.AmountRequest() # AmountRequest | Información de la cuenta y el monto límite a actualizar
authorization = 'authorization_example' # str | Header para token
account = 'account_example' # str | Cuenta a actualizar
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Solicitud para actualizar el monto límite
    api_response = api_instance.update_amount_limit_account_using_put(body, authorization, account, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuentasDeBeneficiariosSPEIApi->update_amount_limit_account_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AmountRequest**](AmountRequest.md)| Información de la cuenta y el monto límite a actualizar | 
 **authorization** | **str**| Header para token | 
 **account** | **str**| Cuenta a actualizar | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

[**TokenRequiredResponse**](TokenRequiredResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

