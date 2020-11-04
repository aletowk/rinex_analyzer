from argparse import ArgumentParser
from matplotlib.pyplot import show, figure
import georinex as gr
import utils


""" Here are examples on how to use it:

# This reads observations and store all in an xarray.Dataset
obs = gr.load('MyRINEXFILE.XXx')

# Get time as an
obs.time

# Plot observables for one satellite in view (sv):
obs['C1C'].sel(sv=['G20']).dropna(dim='time',how='all').plot()
obs['C1C'].sel(sv=['G26']).dropna(dim='time',how='all').plot() # Add G27 measure
obs['C1C'].sel(sv=['G27']).dropna(dim='time',how='all').plot() # Add G26 measure
show() # Show all asked measures

"""

def choose_sat_to_print(sv_list):
    n = utils.get_integer_in_range(1,len(sv_list),"How Many Sat to print [1,"+str(len(sv_list))+"]: ")
    prn_list = []
    for _ in range(n):
        prn = input("Enter one PRN as in list (G01 or G22): ")
        if(sv_list.count(prn) != 1):
            print("Something wrong with your input string: \n",prn,"\nExiting program...")
            print(sv_list)
            exit(1)
        else:
            prn_list.append(prn)
    return prn_list

def choose_observation_to_print():
    allowed_obs = [
                   'C1C','L1C','D1C','S1C', # L1
                   'C2W','L2W','D2W','S2W', # L2W
                   'C2S','L2S','D2S','S2S'  # L2C
                  ]
    print("Allowed obs type :\n",allowed_obs)
    n = utils.get_integer_in_range(1,3,"How Many Obs type to print (1 to 3): ")
    obs_to_print = []
    for _ in range(n):
        obs = input("Enter one obs as proposed above: ")
        if(allowed_obs.count(obs) != 1):
            print("Something wrong with your input string: \n",obs,"\nNot in :")
            print(allowed_obs)
            print("Exiting program...")
            exit(1)
        else:
            obs_to_print.append(obs)
    return obs_to_print

def print_obs_list(obs,str_obs_list,prn_list):
    for obs_type in str_obs_list:
        for prn in prn_list:
            obs[obs_type].sel(sv=[prn]).dropna(dim='time',how='all').plot()
        show()

def main(filename):  
    all_data = gr.load(filename)
    print("Following, the list of PRN availables:")
    sv_array = all_data.sv.values.tolist()
    
    str_to_print = ""
    for gps in sv_array:
        str_to_print += "|" + gps + "|"
    print(str_to_print)
    
    prn_list_to_print = choose_sat_to_print(sv_array)

    obs_list_to_print = choose_observation_to_print()

    print_obs_list(all_data,obs_list_to_print,prn_list_to_print)


def build_args():
    p = ArgumentParser(description='TP Read Rinex File')
    p.add_argument("-f","--file", help='path to RINEX 2 or RINEX 3 file',required=True)

    return p.parse_args()


if __name__ == "__main__":
    args = build_args()
    main(args.file)


