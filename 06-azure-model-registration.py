# 06-azure-model-registration.py
from azureml.core import Workspace
from azureml.core import Model

if __name__ == "__main__":
    ws = Workspace.from_config(path='./.azureml',_file_name='config.json')

    model = Model.register(model_name='mon_rcv_model',
                           tags={'area': 'udea_training','scoring': 0.80},
                           model_path='outputs/rcv_model.pkl',
                           workspace = ws)
    print(model.name, model.id, model.version, sep='\t')