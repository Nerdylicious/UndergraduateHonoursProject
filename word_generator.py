import string
import random

def generate_random_word(char_set, size):
    return ''.join(random.choice(char_set) for i in range(size))

def generate_similar_word(char_set, cutoff, common_sequence):
    random_sequence = generate_random_word(char_set, cutoff)
    return common_sequence + random_sequence
