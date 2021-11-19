from azureml.core import Workspace, Experiment, Environment, ScriptRunConfig

ws = Workspace.from_config(path='./.azureml', _file_name='config.json')
# trazabilidad de los experimentos lanzados en Azure
experiment = Experiment(workspace=ws, name='dia1-experimento-testing-workspace')
# linea me ejecuta el Script que como resultado será print('Validando en el workspace de la monografía...')
run_config = ScriptRunConfig(source_directory='./src', script='test-ws.py', compute_target='cpu-cluster-mon')
# me devuelve el status de la ejecución
run = experiment.submit(run_config)
# me devuelve la url
aml_url = run.get_portal_url()
# imprima la url local para ir directamente al experimeinto
print(f'clic para ir a la url del experimento:  {aml_url}')