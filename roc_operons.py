from build_operon_data import *
from plot_roc import *

total_pos_samples = 250
total_neg_samples = 250 
sample_size = 300 
folds = 2
to_scale = True

data = build_operon_data_for_cross_validation(total_pos_samples, total_neg_samples, sample_size)
plot(data, to_scale, 'Run 1 (160 positive samples, 160 negative samples)')
