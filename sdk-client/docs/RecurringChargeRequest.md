# RecurringChargeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_return_url** | **str** | Es la dirección URL a la que se redirigirá en caso de que el usuario cancele. | 
**charges** | **int** | Número de cargos que se aplicarán a la tarjeta del cliente final a partir de la fecha del primer cargo | 
**customer** | [**Customer**](Customer.md) |  | 
**first_charge_date** | **datetime** | Fecha en la que se aplicará el primer cargo a la tarjeta del cliente final  | 
**order_id** | **str** | Número de orden asignado por el cliente de Wire4 | 
**product** | [**Product**](Product.md) |  | 
**return_url** | **str** | Es la dirección URL a la que se redirigirá en caso de éxito. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

