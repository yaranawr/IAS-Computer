def hex_to_bin(hex_value):
    return bin(int(hex_value, 16))[2:].zfill(40)

def bin_to_hex(bin_value):
    return hex(int(bin_value, 2))[2:].upper()

def check_word(word):
    if not all(bit in '01' for bit in word):
        return False, "Error: word is not a binary code."
    if len(word) != 40:
        return False, "Error: word length is different from 40 bits."  
    return True, None