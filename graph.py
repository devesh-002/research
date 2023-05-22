import matplotlib.pyplot  as plt
from adjustText import adjust_text
import os
import mplcursors
import pandas as pd
import numpy as np
initialdir="/home/devesh/projects/research"
try:
    os.mkdir(initialdir+"/graphs")
except:
    pass
path=initialdir+"/india-election-data/assembly-elections/"
filename="assembly.csv"

filename=path+filename
df=pd.read_csv(filename)
state_list=df["ST_NAME"].unique()

bbox = dict(boxstyle ="round", fc ="0.8")
arrowprops = dict(
    arrowstyle = "->",
    connectionstyle = "angle, angleA = 0, angleB = 90,\
    rad = 10")
offset = 2

def plot_file(arr_x,arr,name,passed_text,dirname):
    plt.title(name)
    plt.scatter(arr_x,arr)
    print(passed_text)
    texts = []
    for i, txt in enumerate(passed_text):
      if(i==5):
          break
      plt.annotate(txt, (arr_x[i], arr[i]),bbox=bbox,arrowprops=arrowprops)
    path=dirname+name+".png"
    plt.savefig(path)
    plt.close()
arr=[];name="";arr_x=[];txt=[]
def isfloat(num):
    try:
        float(num)
        return True
    except :
        return False


for state_ in state_list:
# state="Haryana"

    df_har=df[df["ST_NAME"]==state_]
    state=state_.split(" ")
    state="_".join(state)
    print(state)
    # filename=filename+"/"+state
    # f=open(filename+".csv","r")
    # data=f.readlines()

    year_list=df_har["YEAR"].unique()
    print(year_list)
    # exit(0)
    # year_list=["1968","1972","1977","1982","1987","1991","1996"]
    maindir=initialdir+"/graphs/"+state+"/"
    try:
            os.mkdir(maindir)
    except:
            pass

    for year in year_list:
        dirname=initialdir+"/graphs/"+state+"/"+state+"_"+str(year)+"/"

        try:
            os.mkdir(dirname)
        except:
            pass

        df_year=df_har[df_har["YEAR"]==year]
        num_state=df_year["AC_NO"].unique()

        for state_num in num_state:
            arr_x=[]# party
            arr_y=[] # votes
            arr_name=[]# name
            x_df=df_year[df_year["AC_NO"]==state_num]
            name=""
            for index, row in x_df.iterrows():
                arr_x.append(row["PARTY"])
                arr_y.append(row["VOTES"])
                arr_name.append(row["NAME"])
                name=row["AC_NAME"]

            plot_file(arr_x,arr_y,name+"_"+str(year),arr_name,dirname)


# for line in data:
#     split=line.strip().split(",")
#     if(len(split)==1):
#         if(arr==[]):
#             pass
#         else:
#             plot_file(arr_x,arr,name,txt)
#             arr=[];arr_x=[];txt=[]
#         continue
    
#     if(split[-1]==''):
#         name=split[1].split(".")[-1].strip()
#     elif(split[-1].isdigit()==True):

#         arr_x= [x for x in arr_x if x is not None]
#         arr= [x for x in arr if x is not None ]
#         new_arr=[]
#         for val in arr:
#             try: 
#                 new_arr.append(float(val.replace("%","")))
#             except:
#                 pass    
#         arr=new_arr
#         # print(arr)
#         # print(arr_x)
#         plot_file(arr_x,arr,name,txt)
#         arr=[];name="";arr_x=[];txt=[]
        
#     else:
#         endval=split[-1]
#         # print(endval.strip().replace("%",""))
#         if(isfloat(endval.strip().replace("%",""))==False):
#             continue
#         arr.append(split[-1])
#         arr_x.append(split[-3])
#         txt.append(split[1])

