# 03-train-mon-aml.py
from azureml.core import Workspace
from azureml.core import Experiment
from azureml.core import Environment
from azureml.core import ScriptRunConfig

if __name__ == "__main__":
    #Connect to Azure ML WorkSpace
    ws = Workspace.from_config(path='./.azureml',_file_name='config.json')

    #Experiment
    experiment = Experiment(workspace=ws, name='dia1-experimento-entrenamiento-monografia')
    config = ScriptRunConfig(source_directory='./src',
                             script='rcv_model.py',
                             compute_target='cpu-cluster-mon')

    # set up pytorch environment
    env = Environment.from_conda_specification(
        name='project-env',
        file_path='./.azureml/rcv-aml-env.yml'
    )

    config.run_config.environment = env

    #Execute experiment
    run = experiment.submit(config)

    #Print url
    aml_url = run.get_portal_url()
    print(aml_url)