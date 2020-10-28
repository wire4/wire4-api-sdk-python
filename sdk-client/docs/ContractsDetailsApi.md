# wire4_client.ContractsDetailsApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authorization**](ContractsDetailsApi.md#create_authorization) | **POST** /onboarding/accounts/authorize | Devuelve la URL para autorización del usuario Monex
[**obtain_authorized_users**](ContractsDetailsApi.md#obtain_authorized_users) | **GET** /onboarding/accounts/{requestId}/authorized-users | Obtiene los usuarios autorizados
[**obtain_authorized_users_by_contract**](ContractsDetailsApi.md#obtain_authorized_users_by_contract) | **GET** /onboarding/accounts/authorized-users | Obtiene los usuarios autorizados por contrato
[**obtain_contract_details**](ContractsDetailsApi.md#obtain_contract_details) | **POST** /onboarding/accounts/details | Obtiene los detalles de la empresa del contrato

# **create_authorization**
> TokenRequiredResponse create_authorization(body, authorization)

Devuelve la URL para autorización del usuario Monex

Se obtiene la URL para la autorización del usuario Monex.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.ContractsDetailsApi()
body = wire4_client.PreMonexAuthorization() # PreMonexAuthorization | Información para la autorización
authorization = 'authorization_example' # str | Header para token

try:
    # Devuelve la URL para autorización del usuario Monex
    api_response = api_instance.create_authorization(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsDetailsApi->create_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PreMonexAuthorization**](PreMonexAuthorization.md)| Información para la autorización | 
 **authorization** | **str**| Header para token | 

### Return type

[**TokenRequiredResponse**](TokenRequiredResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **obtain_authorized_users**
> list[AuthorizedUsers] obtain_authorized_users(authorization, x_access_key, request_id)

Obtiene los usuarios autorizados

Obtienen los detalles de los usuarios autorizados de Monex.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.ContractsDetailsApi()
authorization = 'authorization_example' # str | Header para token
x_access_key = 'x_access_key_example' # str | La llave de acceso de la aplicación
request_id = 'request_id_example' # str | El identificador de la petición a esta API

try:
    # Obtiene los usuarios autorizados
    api_response = api_instance.obtain_authorized_users(authorization, x_access_key, request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsDetailsApi->obtain_authorized_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **x_access_key** | **str**| La llave de acceso de la aplicación | 
 **request_id** | **str**| El identificador de la petición a esta API | 

### Return type

[**list[AuthorizedUsers]**](AuthorizedUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **obtain_authorized_users_by_contract**
> list[AuthorizedUsers] obtain_authorized_users_by_contract(authorization, x_access_key, contract=contract)

Obtiene los usuarios autorizados por contrato

Obtienen los detalles de los usuarios autorizados por contrato Monex.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.ContractsDetailsApi()
authorization = 'authorization_example' # str | Header para token
x_access_key = 'x_access_key_example' # str | La llave de acceso de la aplicación
contract = 'contract_example' # str | El contrato Monex (optional)

try:
    # Obtiene los usuarios autorizados por contrato
    api_response = api_instance.obtain_authorized_users_by_contract(authorization, x_access_key, contract=contract)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsDetailsApi->obtain_authorized_users_by_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **x_access_key** | **str**| La llave de acceso de la aplicación | 
 **contract** | **str**| El contrato Monex | [optional] 

### Return type

[**list[AuthorizedUsers]**](AuthorizedUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **obtain_contract_details**
> ContractDetailResponse obtain_contract_details(body, authorization, x_access_key)

Obtiene los detalles de la empresa del contrato

Detalles de la compañía relacionada con el contrato de Monex.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.ContractsDetailsApi()
body = wire4_client.ContractDetailRequest() # ContractDetailRequest | Información para obtener los detalles de la companía
authorization = 'authorization_example' # str | Header para token
x_access_key = 'x_access_key_example' # str | La llave de acceso de la aplicación

try:
    # Obtiene los detalles de la empresa del contrato
    api_response = api_instance.obtain_contract_details(body, authorization, x_access_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsDetailsApi->obtain_contract_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContractDetailRequest**](ContractDetailRequest.md)| Información para obtener los detalles de la companía | 
 **authorization** | **str**| Header para token | 
 **x_access_key** | **str**| La llave de acceso de la aplicación | 

### Return type

[**ContractDetailResponse**](ContractDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

