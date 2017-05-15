import numpy as np

class SeizureItem:
     def __init__(self, startTime, endTime):
       self.startTime = int(startTime.replace('\n',''))
       self.endTime = int(endTime.replace('\n',''))
     def displaySeizureData(self):
       print "Start : ", self.startTime,  ", End: ", self.endTime

class EdfItem:
    fileName = '';
    fileStartTime = 0;
    fileEndTime = 0;
    fileNoOfSeizures =  0;
    seizuresList = [];

def convertTimeToSeconds(input_time):
    #print input_time
    timeParts = input_time.split(':');
    h = int(timeParts[0])
    m = int(timeParts[1])
    s = int(timeParts[2])
    #print h,m,s
    return (h*3600) + (m*60) +(s)

def getY(summary_file):
    #step1: read the summay file that contains all data about patient
    #text_file=r'C:\Users\Yousef Essam\Desktop\Task1-ReadY\Patient14\test.txt'
    text_file = summary_file
    thresholdValue = 30;
    gapClassValue = 999;
    
    patientFile = open(text_file)
    
    #step2: build an actual list of patient time line without seizures
    count = 0
    lines = patientFile.readlines();
    listOfSeizures = [];
    edfItemList = [];
    edf = EdfItem()          
    flag = False;
    for i in range(0,len(lines)):
        line = lines[i]
        if(flag == True):
            #print 'Add New EDf'
            edf.seizuresList = listOfSeizures;
            edfItemList.append(edf);
            flag = False;
        if ('.edf' in line):
            #print 'New EDf'
            edf = EdfItem();
            listOfSeizures = [];
            flag = False;
            count = count + 1;
        if('File Name' in line):
            #print (count),'',line
            #print (count),line.split(':')
            fname = line.split(':')[1];
            edf.fileName = fname;
            #print fname
        if('File Start Time' in line):
            #print (count),'',line
            #print (count),line.split(':')
            fileStartTime = line.split(':')[1]+':'+line.split(':')[2]+":"+line.split(':')[3];
            edf.fileStartTime = fileStartTime.replace('\n','');
            #print fileStartTime
        if('File End Time' in line):
            #print (count),'',line
            #print (count),line.split(':')
            fileEndTime = line.split(':')[1]+':'+line.split(':')[2]+":"+line.split(':')[3];
            edf.fileEndTime = fileEndTime.replace('\n','');
            #print fileEndTime
        if('Number of Seizures in File' in line):
            #print (count),'',line
            #print (count),line.split(':')
            count += 1
            numberOfSeizure = int(line.split(':')[1]);
            edf.fileNoOfSeizures = numberOfSeizure;
            if(numberOfSeizure > 0):
                #print numberOfSeizure
                listOfSeizures = [];
                for j in range(1,numberOfSeizure+1):
                    i += 1; # advances to next lines based on the number of availble seizures (start Time)
                    line = lines[i];
                    tempSeizureStart = '';
                    tempSeizureEnd = '';
                    if('seconds' in line):
                        tempSeizureStart = line.split(':')[1];
                        #print tempSeizureStart
                    i += 1; # advances to next lines based on the number of availble seizures (end Time)
                    line = lines[i];
                    if('seconds' in line):
                        tempSeizureEnd = line.split(':')[1];
                        #print tempSeizureEnd
                    seizureObj = SeizureItem(tempSeizureStart.split(' ')[1],tempSeizureEnd.split(' ')[1])
                    listOfSeizures.append(seizureObj)
                    #print j
                #print listOfSeizures
                #listOfSeizures[0].displaySeizureData()
            flag = True;      
    
    #The following code to add the last item in the summary file
    if(flag == True):
        #print 'Add New EDf'
        edf.seizuresList = listOfSeizures;
        edfItemList.append(edf);
        flag = False;
    #end Adding
    
    #print len(edfItemList)
    
    subtract_value = 0;
    flag = 0;
    days = 1;
    prevTime = -1;
    file_duration=0;
    numberOfEdfItems = len(edfItemList);
    
    for i in range(0,numberOfEdfItems):
        tempEdfItem = edfItemList[i];
        #print "-------Iteration--(" , i ,")------------"
        #print tempEdfItem.fileName
        sTime =  tempEdfItem.fileStartTime;
        eTime =  tempEdfItem.fileEndTime;
        sTime_seconds = convertTimeToSeconds(sTime);
        if (i == 0):
            # Got the start of TimeLine
           subtract_value = sTime_seconds;
         
        #solve the problem of days differnce in the Timeline                                       
       
        
        if(prevTime > sTime_seconds):
            days = days + 1
        #print  'sTime_seconds :' ,sTime_seconds
        #print  'subtract_value :' ,subtract_value
        diff = sTime_seconds-subtract_value;
        
        if(diff <= 0 or flag == 1):
            flag = 1;
            diff = diff + (86400*(days-1)); # add 24 hours in seconds unit;                               
        
        prevTime = sTime_seconds;
        file_duration = convertTimeToSeconds(eTime) - sTime_seconds;
        #print tempEdfItem.fileStartTime,convertTimeToSeconds(sTime)
        #print tempEdfItem.fileEndTime,convertTimeToSeconds(eTime)
        #print  'file_duration :' ,file_duration                                        
        endTimePrev = diff + file_duration;
        #print 'endTimePrev :',endTimePrev
       
        #print tempEdfItem.fileNoOfSeizures
        #print len(tempEdfItem.seizuresList)
       
        #print "------------------------------------"        
    
    
    SimulationData = np.zeros(endTimePrev+1)
    
    subtract_value = 0;
    flag = 0;
    days = 1;
    prevTime = -1;
    prevc2Start = -1;
    endTimePrev = 0;
    offset = 1;
    for i in range(0,numberOfEdfItems):
        tempEdfItem = edfItemList[i];
        #print "-------Iteration--(" , i ,")------------"
        #print tempEdfItem.fileName
        sTime =  tempEdfItem.fileStartTime;
        eTime =  tempEdfItem.fileEndTime;
        sTime_seconds = convertTimeToSeconds(sTime);
        if (i == 0):
            # Got the start of TimeLine
           #print "First Iteration Start :" ,  sTime_seconds
           subtract_value = sTime_seconds;
         
        #solve the problem of days differnce in the Timeline                                       
       
        
        if(prevTime > sTime_seconds):
            days = days + 1
        #print  'sTime_seconds :' ,sTime_seconds
        #print  'subtract_value :' ,subtract_value
        diff = sTime_seconds-subtract_value;
        
        if(diff <= 0 or flag == 1):
            flag = 1;
            diff = diff + (86400*(days-1)); # add 24 hours in seconds unit;
            #print "Difference : " , diff;                            
        
        prevTime = convertTimeToSeconds(sTime);
        miniGap = diff - endTimePrev;
        miniGapStart = endTimePrev+1;
        miniGapEnd = diff+1;
        #print "Mini Gap start :" ,miniGap , " " ,miniGapStart," ",miniGapEnd;
        if((diff - endTimePrev) > thresholdValue):
           gapDuration = (diff - endTimePrev);
           #print  "Yes - " , gapDuration 
           SimulationData[endTimePrev:endTimePrev+gapDuration-1]=gapClassValue;
        
        file_duration = convertTimeToSeconds(eTime) - sTime_seconds;
        endTimePrev = diff + file_duration;
        #print "file_duration : " , file_duration;    
        #print "endTimePrev : " , endTimePrev;    
        
        seizure_period = -1;
        
        if(len(tempEdfItem.seizuresList) > 0):
            for t in range(0,len(tempEdfItem.seizuresList)):
                seizure_period = -1;
                #print "t: ",t
                #print tempEdfItem.seizuresList[0].startTime
                seizure_period = tempEdfItem.seizuresList[t].startTime;
                #print "seizure Before : " , seizure_period;
                seizure_period = seizure_period + diff;
                #print "seizure After : " , seizure_period;
                
                sPointc1Start = seizure_period-3600;
                sPointc1End = seizure_period;
                sPointc2Start = seizure_period;
                sPointc2End = seizure_period+180;
                sPointc3Start = seizure_period+180;
                sPointc3End = seizure_period+1980;
                #print "c1 ",sPointc1Start, " c1" ,sPointc1End;
                #print "c2 ",sPointc2Start, " c2" ,sPointc2End;
                #print "c3 ",sPointc3Start, " c3" ,sPointc3End;
                
                if(sPointc1Start<=0):
                    sPointc1Start = 1;
                    
                SimulationData[sPointc1Start:sPointc1End]=1;
                SimulationData[sPointc2Start:sPointc2End]=2;
                SimulationData[sPointc3Start:sPointc3End]=3;
                
                if(prevc2Start > 0):
                    SimulationData[prevc2Start:prevc2End]=2;
                
                prevc2Start = sPointc2Start;
                prevc2End = sPointc2End;                          
            
            
        if (i != 0):
            SimulationData[miniGapStart:miniGapEnd-1]=gapClassValue;
        #print tempEdfItem.fileNoOfSeizures
        #print len(tempEdfItem.seizuresList)
       
        #print "------------------------------------"    
    return SimulationData
          
                      
            
        


