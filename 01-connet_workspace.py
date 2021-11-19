from azureml.core.authentication import InteractiveLoginAuthentication
from azureml.core import Workspace

interactive_auth = InteractiveLoginAuthentication(tenant_id="99e1e721-7184-498e-8aff-b2ad4e53c1c2")
ws = Workspace.get(name='mlw-udea-mon',
            subscription_id='80986424-c91c-4671-9d12-d7de41662014',
            resource_group='rg-udea-mon',
            location='eastus',
            auth=interactive_auth
            )
ws.write_config(path='.azureml')