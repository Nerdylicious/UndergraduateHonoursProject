from build_binding_protein_data import *
from kfold_cross_validation import *

data = build_binding_protein_data_for_cross_validation(200)
cross_validate(data, 2, True)
