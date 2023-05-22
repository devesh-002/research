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
        num_state=df_year["AC_NO"].unique()
        
        
        for state_name in name_of_cons:
            try:
                x_df=df_year[df_year["AC_NAME"]==state_name]
                
                top_1=int(x_df[x_df["#"]==1]["VOTES"])+int(x_df[x_df["#"]==2]["VOTES"]);
                total=x_df["VOTES"].sum()
                # print(top_1)
                if state_name in l:
                    l[state_name].append(100*(top_1/total))

                else:
                    # temp=
                    
                    l[state_name]=[100*(top_1/total)]
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
    buckets=[(80,100),(70,80),(60,70)]

    for val in buckets:
        print(val)
        low=val[0];up=val[1]
        for key in name_of_cons:
            if(len(l[key])>2 and all (x >=low for x in l[key]) and all (x <up for x in l[key])):
                print(key)
                # print(l[key])
    print("################################################################################################")

    """
    for 5<val<30
    GOHANA RATI RAM [13.511006846886167, 18.87040640157847, 8.480120072496602] multiple parties, weird.
    HASSANGARH RAGHBIR SINGH [19.215829974349578, 27.341352811795694, 7.7986260080918886] IND CPI CPM
    HATHIN HEMRAJ [28.993989865262993, 29.26115412979351, 8.700299769943996] HVC,INLD multiple states haryana, himachal pradesh
    """