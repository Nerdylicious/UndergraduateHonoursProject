from build_binding_protein_data import *
from plot_roc import *

total_pos_samples = 1153
total_neg_samples = 1153
sample_size = 600
folds = 2
to_scale = True

data = build_binding_protein_data_for_cross_validation(total_pos_samples, total_neg_samples, sample_size)
plot(data, to_scale, 'Run 10 (300 DNA-binding protein, 300 non DNA-binding protein)')
