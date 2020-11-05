

def get_intro_str():
    str_to_return =  'This script will extract all observables for the passed RINEX file\n'
    str_to_return += 'In this RINEX file, you might find the following GPS observables:\n'
    str_to_return += 'C1C : Pseudorange of the L1C signal\n'
    str_to_return += 'L1C : Phase measurement of the L1C signal\n'
    str_to_return += 'D1C : Doppler of the L1C signal\n'
    str_to_return += 'S1C : SNR ratio of the L1C signal\n'
    str_to_return += 'C2W : Pseudorange of the L2\"P\" signal\n'
    str_to_return += 'L2W : Phase measurement of the L2\"P\" signal\n'
    str_to_return += 'D2W : Doppler of the L2\"P\" signal\n'
    str_to_return += 'S2W : SNR ratio of the L2\"P\" signal\n'
    str_to_return += 'C2S : Pseudorange of the L2C signal\n'
    str_to_return += 'L2S : Phase measurement of the L2C signal\n'
    str_to_return += 'D2S : Doppler of the L2C signal\n'
    str_to_return += 'S2S : SNR ratio of the L2C signal\n'
    return str_to_return