# MessageDepositAuthorizationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Monto de la transferencia | [optional] 
**beneficiary_account** | **str** | Cuenta del beneficiario | [optional] 
**beneficiary_name** | **str** | Nombre del beneficiario | [optional] 
**beneficiary_rfc** | **str** | RFC del beneficiario | [optional] 
**clave_rastreo** | **str** | Clave de rastreo de la transferencia | [optional] 
**confirm_date** | **datetime** | Fecha de confirmación de la transferencia | [optional] 
**currency_code** | **str** | Código de moneda de la transferencia, puede ser MXP, USD | [optional] 
**deposit_date** | **datetime** | Fecha de recepción de la transferencia | [optional] 
**depositant** | **str** | Nombre del depositante, en caso que la transferencia se reciba en una cuenta de depositante | [optional] 
**depositant_clabe** | **str** | CLABE del depositante, en caso que la transferencia se reciba en una cuenta de depositante | [optional] 
**depositant_email** | **str** | Correo electrónico del depositante, en caso que la transferencia se reciba en una cuenta de depositante | [optional] 
**depositant_rfc** | **str** | RFC del depositante, en caso que la transferencia se reciba en una cuenta de depositante | [optional] 
**description** | **str** | Concepto de la transferencia | [optional] 
**monex_description** | **str** | Descripción de Monex para la transferencia | [optional] 
**monex_transaction_id** | **str** | Identificador asignado por Monex a la transferencia | [optional] 
**reference** | **str** | Referecia de la transferencia | [optional] 
**sender_account** | **str** | Cuenta del ordenante, podría ser un número celular, TDD o Cuenta CLABE interbancaria | [optional] 
**sender_bank** | [**MessageInstitution**](MessageInstitution.md) |  | [optional] 
**sender_name** | **str** | Nombre del ordenante | [optional] 
**sender_rfc** | **str** | RFC del ordenante | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

