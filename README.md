# wire4_sdk

Wire4SDK - packages (paquetes) de Python para el API de Wire4

Referencia del SDK para el consumo del API de Wire4

Este SDK es hecho y distrubuido por Wire4:

- Versión del API de Wire4: 1.1.10
- Versión del paquete SDK: 1.1.10

## Requerimientos.

Python 2.7 and 3.4+

## <a name="installation"></a>Instalación y Uso
### Instalación con 'pip'

Los paquetes de Python están alojados en Github, puedes instalarlo directamente de Github

```sh
pip install git+https://github.com/wire4/wire4-api-sdk-python#subdirectory=sdk-client
pip install git+https://github.com/wire4/wire4-api-sdk-python#subdirectory=authenticator
```
(puede ser que necesites ejecutar el comando `pip` con privilegios de root (administrador): `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Para la versión de Python 2.7 es necesario instalar un paquete adicional para compatibilidad: 

```sh
pip install enum34
```

### Instalación usando Setuptools

Despues de clonar el repositorio de Github

```sh
git clone https://github.com/wire4/wire4-api-sdk-python.git
```

Entrar a la subcarpeta ya sea (authenticator o sdk-client) y ejecutar:

```sh
python setup.py install --user
```
(o `sudo python setup.py install` para instalar el paquete para todos los usuarios)

Para más información [Setuptools](http://pypi.python.org/pypi/setuptools).

### Importar los paquetes

Para importar los paquetes, en Python 3.4+:
```python
import wire4_client
import wire4_auth 
```

En Python 2.7

```python
import wire4_client
import wire4_auth_p27 
```


## Para comenzar a usar

Primero debes seguir la guía de [instalación](#installation) y ejecutar el siguiente código de ejemplo:
```python
# Importar los paquetes
import sys

from wire4_client import CepSearchBanxico, ComprobanteElectrnicoDePagoCEPApi, CepResponse
from wire4_client.rest import ApiException

from wire4_auth.auth.oauth_wire4 import OAuthWire4
from wire4_auth.core.environment_enum import EnvironmentEnum

CLIENT_ID = "FxUWmqYGZuv8O1qjxstvIyJothMa"

CLIENT_SECRET = "kjwbkrPVgXsnaUGzthj55dsFhx4a"

# Create the authenticator to obtain access token
# The token URL and Service URL are defined for this environment enum value.
oauth_wire = OAuthWire4(CLIENT_ID, CLIENT_SECRET, EnvironmentEnum.SANDBOX)

try:
    # Obtain an access token use application flow and scope "general"
    oauth_token_app = oauth_wire.obtain_access_token_app("general")
except ApiException as ex:
    print("Exception to obtain access token %s\n" % ex, file=sys.stderr)
    # Optional manage exception in access token flow
    sys.exit(-100)

# create an instance of the API class and add the bearer token to request
api_instance = ComprobanteElectrnicoDePagoCEPApi(OAuthWire4.get_default_api_client(oauth_token_app))

# build body with info (check references for more info: types, required fields, etc.)
body = CepSearchBanxico(amount="8963.25", beneficiary_account="072680004657656853",
                        beneficiary_bank_key="40072", clave_rastreo="58735618", operation_date="05-12-2018",
                        reference="1122334", sender_account="112680000156896531", sender_bank_key="40112")

try:
    response = api_instance.obtain_transaction_cep_using_post(body)
    print(response)
except ApiException as ex:
    print("Exception when calling the API %s\n" % ex, file=sys.stderr)
    # Optional manage exception in access token flow
    sys.exit(-100)
```


