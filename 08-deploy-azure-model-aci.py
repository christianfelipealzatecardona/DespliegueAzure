from azureml.core.model import InferenceConfig
from azureml.core.environment import Environment
from azureml.core import Workspace
from azureml.core.model import Model
from azureml.core.webservice import AciWebservice

ws = Workspace.from_config(path='./.azureml',_file_name='config.json')
model = Model(ws,name='mon_rcv_model',version=2)

env = Environment.from_conda_specification(
        name='rcv-aml-env',
        file_path='./.azureml/rcv-aml-env.yml'
    )

inference_config = InferenceConfig(entry_script="./src/score.py", environment=env)

deployment_config = AciWebservice.deploy_configuration(cpu_cores = 1, memory_gb = 1)

aci_service = Model.deploy(workspace=ws, 
                       name='evento-agudo-service', 
                       models=[model], 
                       inference_config=inference_config, 
                       deployment_config = deployment_config)

aci_service.wait_for_deployment(show_output=True)
print(aci_service.state)