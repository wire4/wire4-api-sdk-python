# wire4_client.AutorizacinDeDepsitosApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deposit_auth_configurations**](AutorizacinDeDepsitosApi.md#get_deposit_auth_configurations) | **GET** /subscriptions/{subscription}/configurations/deposit-authorization | Consulta autorización de depósitos
[**put_deposit_auth_configurations**](AutorizacinDeDepsitosApi.md#put_deposit_auth_configurations) | **PUT** /subscriptions/{subscription}/configurations/deposit-authorization | Des/Habilitar autorización de depósitos

# **get_deposit_auth_configurations**
> DepositsAuthorizationResponse get_deposit_auth_configurations(authorization, subscription)

Consulta autorización de depósitos

Obtiene la información de la autorización de depósitos del contrato relacionado a la subscripción.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.AutorizacinDeDepsitosApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Consulta autorización de depósitos
    api_response = api_instance.get_deposit_auth_configurations(authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutorizacinDeDepsitosApi->get_deposit_auth_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

[**DepositsAuthorizationResponse**](DepositsAuthorizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_deposit_auth_configurations**
> DepositsAuthorizationResponse put_deposit_auth_configurations(body, authorization, subscription)

Des/Habilitar autorización de depósitos

Des/Habilitar autorización de depósitos, devuelve la información final de la autorización de depósitos del contrato relacionado a la subscripción al terminar.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.AutorizacinDeDepsitosApi()
body = wire4_client.DepositAuthorizationRequest() # DepositAuthorizationRequest | Deposit Authorization info
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Des/Habilitar autorización de depósitos
    api_response = api_instance.put_deposit_auth_configurations(body, authorization, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutorizacinDeDepsitosApi->put_deposit_auth_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DepositAuthorizationRequest**](DepositAuthorizationRequest.md)| Deposit Authorization info | 
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

[**DepositsAuthorizationResponse**](DepositsAuthorizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

