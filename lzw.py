#Purpose: An implementation of the Lempel-Ziv-Welch compression algorithm with variable-width codes

#compress a string to a list of output symbols
def compress(uncompressed_string):

    #build the dictionary
    dict_size = 256
    #d = dict((key, value) for (key, value) in interable
    dictionary = dict((chr(i), i) for i in xrange(dict_size))

    w = ""
    compressed_values = []
    for c in uncompressed_string:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            #add w to the output
            compressed_values.append(dictionary[w])
            #add wc to the dictionary
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    if w:
        compressed_values.append(dictionary[w])

    return compressed_values 

#count bits assuming algorithm uses variable-width codes
def calculate_bits(compressed_values):

    size = len(compressed_values)
    total_bits = 0

    #characters are stored in 9-12 bits if compressed
    #(characters are stored in 8 bits if uncompressed)
    #if we need to move up a code width level, then we continue to use that 
    #code width level until we have to move up again
    code_width = 0 
    for output in compressed_values:
        if (output >= 0) and (output < 512) and (code_width < 9):
            code_width = 9
        if (output >= 512) and (output < 1024) and (code_width < 10):
            code_width = 10
        if (output >= 1024) and (output < 2048) and (code_width < 11):
            code_width = 11
        if (output >= 2048) and (code_width < 12):
            code_width = 12
        total_bits += code_width 

    return total_bits
