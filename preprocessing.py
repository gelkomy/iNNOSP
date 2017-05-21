'''
% This file reads patient data csv files in a specific path and 
% the output is a dataframe with values of files indexed by the first column
% which is in timeSeries format
% 
% /**************************************************************************** 
%  * Job:             Reading data files and preprocessing                    * 
%  *                                                                          * 
%  *Inputs: path of csv data files
%  *                                                                          * 
%  * Generated on:    Sun, May 14, 2017                                       * 
%  * Generated by:    Emad                                                    * 
%  * Version:         1                                                       * 
%  ****************************************************************************/ 
'''



import pandas as pd
import glob
import csv

def preprocessing(files_path):

    #files_path = r".\data"  #for testing
    all_files = glob.glob(files_path + "/*.csv")  #returns a list of csv files in the path

    frame = pd.DataFrame()  #the frame that will hold the result
    df_list = []


    for file_ in all_files:
        #####This part is to get csv file headers #####
        print "current file is ",file_
        f = open(file_, 'rb')
        reader = csv.reader(f)
        headers = reader.next()

        col_names = []      #holds headers names
        dash_count = 1      
        repeat_count = 1
        
        for i in headers:
            i = i[1:-1]  #To remove the quotes from readed header names
            
            if i == "-":   #This part is to remove duplicate columns named: "-"
                i = "-_"+str(dash_count)  #It becomes -_1, -_2, and so on
                dash_count += 1 

            if i in col_names:  #for repeated channel names add _1, _2,...
                i = i + "_" + str(repeat_count)  
                repeat_count += 1
            col_names.append(i)
        f.close()
        ##############################################
        df = pd.read_csv(file_,index_col=None, header=0, names = col_names, skiprows=1)
        df[col_names[0]]=df[col_names[0]].str.lstrip("'[").str.rstrip("]'")  #To adjust idex column and remove '[  ]'
        
        df[col_names[0]]= pd.to_datetime(df[col_names[0]], format="%H:%M:%S.%f %d/%m/%Y")    #make the first column in time series format   df.index = df[col_names[0]]  #To make the first colomn as the index
        df.index= df[col_names[0]]
        del df[col_names[0]]  #After making it as index, delete it from data
        
        df=df.drop(df.columns[pd.Series(df.columns).str.startswith('-')], axis=1)
        df_list.append(df)   #Append to total dataFrames list
        

    frame = pd.concat(df_list)

    return frame
