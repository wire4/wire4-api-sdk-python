# CepSearchBanxico

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Es el monto de la transferencia. Ejemplo 1000.00 | 
**beneficiary_account** | **str** | Es la cuenta de beneficiario. | 
**beneficiary_bank_key** | **str** | Clave del banco beneficiario. Éste valor no esta presente si obtiene de la cuenta del beneficiario, en caso de que sea un número celular éste campo es requerido. se puede obtener del recurso de las &lt;a href&#x3D;\&quot;#operation/getAllInstitutionsUsingGET\&quot;&gt;instituciones.&lt;/a&gt; | [optional] 
**clave_rastreo** | **str** | Es la clave de rastreo de la transferencia. | 
**operation_date** | **str** | Es la fecha de operación de la transferencia, formato: dd-MM-yyyy. | 
**reference** | **str** | Es la referencia numérica de la transferencia. Se valida hasta 7 dígitos. | [optional] 
**sender_account** | **str** | Es la cuenta ordenante, es requerida cuando se no se envía la clave del banco ordenante. | [optional] 
**sender_bank_key** | **str** | Es la clave del banco ordenante, es requerida cuando no se envía la cuenta ordenante.  Se puede obtener del recurso de las &lt;a href&#x3D;\&quot;#operation/getAllInstitutionsUsingGET\&quot;&gt;instituciones.&lt;/a&gt; | [optional] 
**type** | **str** | Es el tipo de cep a consultar, puede ser SPEI o SPID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

