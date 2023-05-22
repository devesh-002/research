import csv
import pandas as pd

path="/home/devesh/projects/Competition/research/india-election-data/assembly-elections/"
filename="assembly.csv"
filename=path+filename

df=pd.read_csv(filename)
df_har=df[df["ST_NAME"]=="Haryana"]
year_list=["1968","1972","1977","1982","1987","1991","1996"]

top_2_year_list={}
set_of_states=set()
for year in year_list:

    df_year=df_har[df_har["YEAR"]==year]
    num_state=df_year["AC_NO"].unique()
    l={}
    
    for state_num in num_state:
        
        x_df=df_year[df_year["AC_NO"]==state_num]
        top_1=None;top_2=None;total=0;
        for index, row in x_df.iterrows():
            if(row["#"]==1):
                top_1=row.copy()
            elif(row["#"]==2):
                top_2=row.copy()
            
            total+=row["VOTES"]

        val=((top_1["VOTES"]/total)+(top_2["VOTES"]/total))*100        
        l[top_1["AC_NAME"]]=val
        set_of_states.add(top_1["AC_NAME"])

    top_2_year_list[year]=l
cutoff=80
# print(top_2_year_list)
for state in set_of_states:
    l=[]
    for year in year_list:
        if state in top_2_year_list[year]:
            l.append(top_2_year_list[year][state])
    check=True
    for val in l:
        if(val>cutoff):
            check=False
            break
    if(check==True):
        print(state)

# for cutoff < 10YAMUNA NAGAR
# for cutoff > 10
# ADAMPUR
# SONEPAT

"""
sum greater than 80
GHARAUNDA
RADAUR
NILOKHERI
HATHIN
SHAHABAD

"""