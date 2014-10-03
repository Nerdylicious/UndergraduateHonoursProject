#Purpose: A program that calculates the distance between two strings based on Kolmogorov complexity
from lzw import compress, calculate_bits

#calculate an approximation for K(x) given a string x
#given a string x, the Kolmogorov complexity K(x) is the minimum number of bits
#into which the string can be compressed without losing information
def approximate_KC_string(x):

    compressed_string = compress(x)
    total_bits = calculate_bits(compressed_string)
    return total_bits

#calculate an approximation for K(xy) given string x and string y
def approximate_KC_concat(x, y):

    concat = x + y
    compressed_string = compress(concat)
    total_bits = calculate_bits(compressed_string)
    return total_bits

#calculate an approximation for K(xy), which is the denominator in Normalized Information Distance
def approximate_KC_concat_for_normalization(x, y):

    total_bits_1 = approximate_KC_concat(x, y)
    total_bits_2 = approximate_KC_concat(y, x)
    average = float(total_bits_1 + total_bits_2) / 2
    return average

#calculate an approximation for K(x|y) by calculating K(x|y) = K(xy) - K(y)
def approxiate_KC_conditional(x, y):

    KC_concat = approximate_KC_concat(x, y)
    KC_y = approximate_KC_string(y)
    KC_conditional = KC_concat - KC_y
    return KC_conditional

#calculate an approximation for NID = (K(x|y) + K(y|x)) / K(xy)
#two identical sequences will have NID = 0
#two sequences with no common information will have NID = 1
#but, we a performing an approximation of NID based on Kolmogorov complexity,
#so the NID returned from this function will only give us an upper bound
def approximate_NID(x, y):

    KC_conditional_xy = approxiate_KC_conditional(x, y)
    KC_conditional_yx = approxiate_KC_conditional(y, x)
    KC_concat_normalization = approximate_KC_concat_for_normalization(x, y)
    NID = float(KC_conditional_xy + KC_conditional_yx) / KC_concat_normalization
    #print "\nK(x|y) = %f, K(y|x) = %f, K(xy) = %f" % (KC_conditional_xy, KC_conditional_yx, KC_concat_normalization)
    return NID

def approximate_NID_v2(x, y):
    
    KC_conditional_xy = approxiate_KC_conditional(x, y)
    KC_conditional_yx = approxiate_KC_conditional(y, x)
    KC_x = approximate_KC_string(x)
    KC_y = approximate_KC_string(y)
    NID = (float(max(KC_conditional_xy, KC_conditional_yx)))/(max(KC_x, KC_y))
    #print "\nK(x|y) = %f, K(y|x) = %f, K(x) = %f, K(y) = %f" % (KC_conditional_xy, KC_conditional_yx, KC_x, KC_y)
    return NID
