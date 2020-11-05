from argparse import ArgumentParser
import matplotlib.pyplot as plt
import georinex as gr
import utils
import tptext as TP
import statistics as ST


def get_timestamp_array(obs):
    tmp = obs.time.to_dict()['data']
    for i in range(0,len(tmp)):
        tmp[i] = tmp[i].timestamp()
    return tmp

def compare_signals_loop(obs,t_array,obs_types,prn_list):
    flag = True
    print("*** [COMPARE SIGNALS] ***\n")
    print("This function will allow you to choose one PRN and 2 signals to compare")
    print("When it is done, it will plot those signals on the same graph")
    print("After that, by closing the graph window, some statistics will be prompted in your terminal")
    print("So, you will be asked if you want to do it once again on may be another PRN and others signals\n")

    while(flag):
        # Choose one PRN on which you want to compare to signals:
        print("\nChoose the PRN from which you wxant to compare 2 signals: ")
        prn = utils.choose_string_in_list(prn_list)
        print("=> Choose signal 1 to compare")
        sig1 = utils.choose_string_in_list(obs_types)
        print("=> Choose signal 2 to compare")
        sig2 = utils.choose_string_in_list(obs_types)

        sig1_array = obs[sig1].sel(sv=prn).to_dict()["data"]
        sig2_array = obs[sig2].sel(sv=prn).to_dict()["data"]
        plt.plot(t_array,sig1_array,label=sig1)
        plt.plot(t_array,sig2_array,label=sig2)
        plt.legend( bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
                    ncol=2, mode="expand", borderaxespad=0.)
        plt.show()

        print("\nHere are stats about those signals:\n")
        make_some_stats(sig1,sig1_array)
        make_some_stats(sig2,sig2_array)

        choice = input("Do you want to start again ? (Y/y = yes | other is No): ")
        if(choice == "Y" or choice == "y"):
            flag = True
        else:
            flag = False

def make_some_stats(sig_str,obs):
    print("\tThe mean of ",sig_str," is: ",ST.mean(obs))
    print("\tThe std of ",sig_str," is: ",ST.stdev(obs))

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


