# TransactionOutgoing

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Monto de la transferencia | 
**beneficiary** | [**Account**](Account.md) |  | [optional] 
**beneficiary_account** | **str** | Cuenta del beneficiario, podría ser un número celular, TDD o Cuenta CLABE interbancaria  | 
**beneficiary_bank_key** | **str** | La clave del banco beneficiario, proprocionada por BANXICO, este campo solo es obligatario cuando la cuenta beneficiaria es un número celular (*). | [optional] 
**concept** | **str** | Concepto de la transferencia | 
**currency_code** | **str** | Código de moneda en la que opera la cuenta | 
**email** | **list[str]** | Lista de email del beneficiario,es opcional | [optional] 
**order_id** | **str** | Referencia de la transferencia asignada por el cliente | 
**reference** | **int** | Referencia numérica de la transferencia | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

