import sys
from pyteck.jsr_eval_model import evaluate_model

# List of models to be tested
model_list = ['n-HeptaneMech.cti'
              ]

species_key = 'species-keys.yaml'
data_path = 'data'
data_list = 'nheptane-datalist.txt'
model_path = 'models'


for model in model_list:

    output = evaluate_model(model, spec_keys_file='species-keys.yaml',species_name='methane',
                            dataset_file=data_list, data_path=data_path,
                            model_path=model_path,
                            skip_validation=True
                            )
