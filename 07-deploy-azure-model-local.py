# 07-deploy-azure-model-local.py
from azureml.core.webservice import Webservice
from azureml.core.model import InferenceConfig
from azureml.core.environment import Environment
from azureml.core import Workspace
from azureml.core.model import Model
from azureml.core.webservice import LocalWebservice

ws = Workspace.from_config(path='./.azureml',_file_name='config.json')
model = Model(ws,name='mon_rcv_model',version=1)


env = Environment.from_conda_specification(
        name='rcv-aml-env',
        file_path='./.azureml/rcv-local-env.yml'
    )

inference_config = InferenceConfig(entry_script="./src/score.py", environment=env)

deployment_config = LocalWebservice.deploy_configuration(port=6789)

local_service = Model.deploy(workspace=ws, 
                       name='rcv-local', 
                       models=[model], 
                       inference_config=inference_config, 
                       deployment_config = deployment_config)

local_service.wait_for_deployment(show_output=True)
print(f"Scoring URI is : {local_service.scoring_uri}")