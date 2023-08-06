# MLFlow GCP IAP Plugin

This project will allow for using an MLFlow service endpoint which is protected with IAP by setting an environment variable: `MLFLOW_IAP_CLIENT_ID`.

## Installation

```bash
pip install mlflow-gcp-iap-plugin
```

## Use

```python
import mflow
import os

os.environ["MLFLOW_IAP_CLIENT_ID"] = <CLIENT_ID_VALUE>

# Use mlflow logging as desired...
```


