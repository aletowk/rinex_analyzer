from argparse import ArgumentParser
import matplotlib.pyplot as plt
import georinex as gr
import utils
import tptext as TP

def get_timestamp_array(obs):
    tmp = obs.time.to_dict()['data']
    for i in range(0,len(tmp)):
        tmp[i] = tmp[i].timestamp()
    return tmp

def compare_signals_loop(obs,t_array,obs_types,prn_list):
    flag = True
    
    while(flag):
        # Choose one PRN on which you want to compare to signals:
        print("Choose the PRN from which you wxant to compare 2 signals: ")
        prn = utils.choose_string_in_list(prn_list)
        print("=> Choose signal 1 to compare")
        sig1 = utils.choose_string_in_list(obs_types)
        print("=> Choose signal 2 to compare")
        sig2 = utils.choose_string_in_list(obs_types)

        plt.plot(t_array,obs[sig1].sel(sv=prn).to_dict()["data"],label=sig1)
        plt.plot(t_array,obs[sig2].sel(sv=prn).to_dict()["data"],label=sig2)
        plt.legend( bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
                    ncol=2, mode="expand", borderaxespad=0.)
        plt.show()

        choice = input("Do you want to start again ? (Y/y = yes | other is No): ")
        if(choice == "Y" or choice == "y"):
            flag = True
        else:
            flag = False
        
def main(filename):  
    print(TP.get_intro_str())
    all_data = gr.load(filename)
    
    # get time array and transform it to timestamp
    time_array = get_timestamp_array(all_data)
    # Extract all availables observables except 'time' and 'sv'
    obs_type_list = []
    for var in all_data.variables:
        if(var != 'time' and var != 'sv'):
            obs_type_list.append(var)
    # get list of available PRN in this file
    prn_list = all_data.sv.to_dict()["data"]

    compare_signals_loop(all_data,time_array,obs_type_list,prn_list)


def build_args():
    p = ArgumentParser(description='TP Read Rinex File')
    p.add_argument("-f","--file", help='path to RINEX 2 or RINEX 3 file',required=True)

    return p.parse_args()


if __name__ == "__main__":
    args = build_args()
    main(args.file)


