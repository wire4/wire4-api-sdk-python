# wire4_client.LmitesDeMontosApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**obtain_configurations_limits**](LmitesDeMontosApi.md#obtain_configurations_limits) | **GET** /subscriptions/{suscription}/configurations | Consulta las configuraciones para el contrato asocaido al enrolamiento en la aplicación
[**update_configurations**](LmitesDeMontosApi.md#update_configurations) | **PUT** /subscriptions/{suscription}/configurations | Actualiza las configuraciones por subscripción

# **obtain_configurations_limits**
> MessageConfigurationsLimits obtain_configurations_limits(authorization, suscription)

Consulta las configuraciones para el contrato asocaido al enrolamiento en la aplicación

Consulta las configuraciones para el contrato asocaido al enrolamiento en la aplicación.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.LmitesDeMontosApi()
authorization = 'authorization_example' # str | Header para token
suscription = 'suscription_example' # str | Identificador de la suscripción a esta API

try:
    # Consulta las configuraciones para el contrato asocaido al enrolamiento en la aplicación
    api_response = api_instance.obtain_configurations_limits(authorization, suscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LmitesDeMontosApi->obtain_configurations_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **suscription** | **str**| Identificador de la suscripción a esta API | 

### Return type

[**MessageConfigurationsLimits**](MessageConfigurationsLimits.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configurations**
> update_configurations(body, authorization, suscription)

Actualiza las configuraciones por subscripción

Actualiza las configuraciones de un contrato asociado a una subscripción

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.LmitesDeMontosApi()
body = wire4_client.UpdateConfigurationsRequestDTO() # UpdateConfigurationsRequestDTO | updateConfigurationsResquestDTO
authorization = 'authorization_example' # str | Header para token
suscription = 'suscription_example' # str | suscription

try:
    # Actualiza las configuraciones por subscripción
    api_instance.update_configurations(body, authorization, suscription)
except ApiException as e:
    print("Exception when calling LmitesDeMontosApi->update_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateConfigurationsRequestDTO**](UpdateConfigurationsRequestDTO.md)| updateConfigurationsResquestDTO | 
 **authorization** | **str**| Header para token | 
 **suscription** | **str**| suscription | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

