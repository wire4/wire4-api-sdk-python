# wire4_client.CargosRecurrentesApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_recurring_charge_using_post**](CargosRecurrentesApi.md#register_recurring_charge_using_post) | **POST** /recurring-charge | Registro de cargos recurrentes

# **register_recurring_charge_using_post**
> ConfirmRecurringCharge register_recurring_charge_using_post(body, authorization)

Registro de cargos recurrentes

 Se registra una solicitud para generar un plan de cargos recurrentes. En la respuesta se proporcionará una dirección URL que lo llevará al sitio donde se le solicitará ingresar los datos de tarjeta a la que se aplicarán los cargos de acuerdo al plan seleccionado.<br> Nota: Debe considerar que para hacer uso de esta funcionalidad debe contar con un scope  especial

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.CargosRecurrentesApi()
body = wire4_client.RecurringChargeRequest() # RecurringChargeRequest | Información de la solicitud para aplicar cargos recurrentes
authorization = 'authorization_example' # str | Header para token

try:
    # Registro de cargos recurrentes
    api_response = api_instance.register_recurring_charge_using_post(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CargosRecurrentesApi->register_recurring_charge_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecurringChargeRequest**](RecurringChargeRequest.md)| Información de la solicitud para aplicar cargos recurrentes | 
 **authorization** | **str**| Header para token | 

### Return type

[**ConfirmRecurringCharge**](ConfirmRecurringCharge.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

