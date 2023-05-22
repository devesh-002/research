import csv
import pandas as pd
from collections import defaultdict
initialdir="/home/devesh/projects/research"

path=initialdir+"/india-election-data/assembly-elections/"
filename="assembly.csv"
filename=path+filename
df=pd.read_csv(filename)
state_list=df["ST_NAME"].unique()
state="Himachal Pradesh"

for state in state_list:
    print("################################################################################################")
    print(state.upper())
    df_har=df[df["ST_NAME"]==state]
    year_list=df_har["YEAR"].unique()
    top_2_year_list={}
    set_of_states=set()
    l= defaultdict(list)
    name_of_cons=df_har["AC_NAME"].unique()

    for year in year_list:

        df_year=df_har[df_har["YEAR"]==year]
        # num_state=df_year["AC_NO"].unique()
        

        for state_name in name_of_cons:
            try:
                x_df=df_year[df_year["AC_NAME"]==state_name]
                names_list=x_df["NAME"].unique()
                total=x_df["VOTES"].sum()
                for name in names_list:
                    top_1=int(x_df[x_df["NAME"]==name]["VOTES"])
                    f_name="-".join(state_name.lower().split(" "))+"_"+"-".join(name.lower().split(" "))
                    # print(f_name)
                    if f_name in l:
                        l[f_name].append(100*(top_1/total))

                    else:
                        # temp=
                        l[f_name]=[100*(top_1/total)]
            except:
                continue
            # for index, row in x_df.iterrows():            
            #     key=row["AC_NAME"]+"_"+row["NAME"]
            #     key=key.replace(" ","")
            #     if key in l:
            #         l[key].append((row["VOTES"]/total)*100)
            #     else:
            #         l[key]=[(row["VOTES"]/total)*100]
    # print(l)
    buckets=[(2,5),(5,20)]

    for val in buckets:
        print(val)
        low=val[0];up=val[1]
        for key in list(l.keys()):
            if(len(l[key])>=3 and all (x >=low for x in l[key]) and all (x <up for x in l[key]) ):
                print(key)
                print(l[key])
    print("################################################################################################")
# and all (x >=low for x in l[key]) and all (x <up for x in l[key])
# "-".join(state_name.lower().split(" "))+"_"+