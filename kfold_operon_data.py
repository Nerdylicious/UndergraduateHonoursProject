from build_operon_data import *
from kfold_cross_validation import *

total_pos_samples = 250
total_neg_samples = 250
sample_size = 200 
folds = 2
to_scale = True

data = build_operon_data_for_cross_validation(total_pos_samples, total_neg_samples, sample_size)
cross_validate(data, folds, to_scale)
