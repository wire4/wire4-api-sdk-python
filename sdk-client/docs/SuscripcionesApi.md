# wire4_client.SuscripcionesApi

All URIs are relative to *https://sandbox-api.wire4.mx/wire4/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_subscription_status_using_put**](SuscripcionesApi.md#change_subscription_status_using_put) | **PUT** /subscriptions/{subscription}/status | Cambia el estatus de la suscripción
[**pre_enrollment_monex_user_using_post**](SuscripcionesApi.md#pre_enrollment_monex_user_using_post) | **POST** /subscriptions/pre-subscription | Registra una pre-suscripción
[**remove_enrollment_user_using_delete**](SuscripcionesApi.md#remove_enrollment_user_using_delete) | **DELETE** /subscriptions/{subscription} | Elimina una suscripción por el identificador de la suscripción
[**remove_subscription_pending_status_using_delete**](SuscripcionesApi.md#remove_subscription_pending_status_using_delete) | **DELETE** /subscriptions/pre-subscription/{subscription} | Elimina una pre-suscripción

# **change_subscription_status_using_put**
> change_subscription_status_using_put(body, authorization, subscription)

Cambia el estatus de la suscripción

Se cambia el estatus de la suscripción, los posibles valores son ACTIVE ó INACTIVE

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.SuscripcionesApi()
body = wire4_client.SubscriptionChangeStatusRequest() # SubscriptionChangeStatusRequest | request
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | subscription

try:
    # Cambia el estatus de la suscripción
    api_instance.change_subscription_status_using_put(body, authorization, subscription)
except ApiException as e:
    print("Exception when calling SuscripcionesApi->change_subscription_status_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionChangeStatusRequest**](SubscriptionChangeStatusRequest.md)| request | 
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| subscription | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_enrollment_monex_user_using_post**
> PreEnrollmentResponse pre_enrollment_monex_user_using_post(body, authorization)

Registra una pre-suscripción

Registra una pre-suscripción para operar un contrato a través de un aplicación socio de la plataforma, proporcionando una URL donde el cliente Monex debe autorizar el acceso a los datos de su cuenta a el socio.<br/>Una vez que el cuentahabiente autorice el acceso, se envía un mensaje webhook con el evento 'ENROLLMENT.CREATED', el cuál contiene los datos de acceso a esta API.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.SuscripcionesApi()
body = wire4_client.PreEnrollmentData() # PreEnrollmentData | Información para la pre-suscripción
authorization = 'authorization_example' # str | Header para token

try:
    # Registra una pre-suscripción
    api_response = api_instance.pre_enrollment_monex_user_using_post(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuscripcionesApi->pre_enrollment_monex_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PreEnrollmentData**](PreEnrollmentData.md)| Información para la pre-suscripción | 
 **authorization** | **str**| Header para token | 

### Return type

[**PreEnrollmentResponse**](PreEnrollmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_enrollment_user_using_delete**
> remove_enrollment_user_using_delete(authorization, subscription)

Elimina una suscripción por el identificador de la suscripción

Elimina una suscripción, una vez eliminada ya no se podrán realizar operacions en el API utilizando esta suscripción

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.SuscripcionesApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Elimina una suscripción por el identificador de la suscripción
    api_instance.remove_enrollment_user_using_delete(authorization, subscription)
except ApiException as e:
    print("Exception when calling SuscripcionesApi->remove_enrollment_user_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_subscription_pending_status_using_delete**
> remove_subscription_pending_status_using_delete(authorization, subscription)

Elimina una pre-suscripción

Se elimina una pre-suscripción, sólo se elimina en caso de que el cliente Monex no haya concedido su autorización de acceso (token), es decir que la pre-suscripcion este pendiente.

### Example
```python
from __future__ import print_function
import time
import wire4_client
from wire4_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wire4_client.SuscripcionesApi()
authorization = 'authorization_example' # str | Header para token
subscription = 'subscription_example' # str | El identificador de la suscripción a esta API

try:
    # Elimina una pre-suscripción
    api_instance.remove_subscription_pending_status_using_delete(authorization, subscription)
except ApiException as e:
    print("Exception when calling SuscripcionesApi->remove_subscription_pending_status_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Header para token | 
 **subscription** | **str**| El identificador de la suscripción a esta API | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

