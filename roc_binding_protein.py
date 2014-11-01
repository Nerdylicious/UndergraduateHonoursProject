from build_binding_protein_data import *
from plot_roc import *

data = build_binding_protein_data_for_cross_validation(700)
plot(data, True)
