#from task1_readyY import getY
import numpy as np

def getMajorFromVector(a,b):
    countZeros = sum(b[a-3:a+1] == 0);
    countOnes = sum(b[a-3:a+1] == 1);
    countTwos = sum(b[a-3:a+1] == 2);
    countThrees = sum(b[a-3:a+1] == 3);
    myArray = np.array([countZeros,countOnes,countTwos,countThrees]);
    myArray = np.argsort(-myArray)
    #print b[a-3:a+1];
    #print myArray , "myArray[0]: " ,myArray[0];
    #[maxVal,maxIndex] = np.argmax(myArray);
    return myArray[0]



def getWindows(yTimeLine):
    gapClassValue = 999;
    c1 = 0;
    c2 = 0;
    c3 = 0;
    counterIntervals = 0;
    numberOfWindows = 0;
    numberOfWindowsTotal = 0;
    #text_file=r'C:\Users\Yousef Essam\Desktop\Task1-ReadY\Patient14\test.txt'
    #yTimeLine1 = getY(text_file)
    #yTimeLine2 = np.genfromtxt('E:\Inno Tech\V2\Pipeline by Emad\pipeline\yyyy.csv')
    #yTimeLine1 = np.append(yTimeLine1,999);
    yTimeLine[len(yTimeLine)-1] = 999;
    #yTimeLine = yTimeLine1;
    #resAll = np.vstack((yTimeLine1,yTimeLine2,yTimeLine1-yTimeLine2));
    #resAll = np.transpose(resAll);
    #print len(yTimeLine)
    
    for i in range(0,len(yTimeLine)):
        if(yTimeLine[i] == gapClassValue):
            if(c1 != c2):
                counterIntervals = counterIntervals + 1 ;
                diffVal = (c2 - c1);
                numberOfWindows = (((diffVal) - np.mod(diffVal,2))/2) -1;
                #print "diffVal : " , diffVal , " " , "c2-c1: ",c2," - ", c1 
                #print "numberOfWindows : " , numberOfWindows
                numberOfWindowsTotal = numberOfWindowsTotal + numberOfWindows;
                c1 = c2;
            c3 = i;
        else:
            c1 = c3;
            c2 = i;
    
    #print "numberOfWindowsTotal : " , numberOfWindowsTotal     
       
    SimulationDataWindows = np.zeros(numberOfWindowsTotal+1)
    SimulationDataWindows_step = 0;
    c1 = 0;
    c2 = 0;
    c3 = 0;
    counterIntervals = 0;
    numberOfWindows = 0;
    numberOfWindowsTotal = 0;
    
    for i in range(0,len(yTimeLine)):
        if(yTimeLine[i] == gapClassValue):
            if(c1 != c2):
                counterIntervals = counterIntervals + 1 ;
                numberOfWindows = (((c2 - c1) - np.mod((c2 - c1),2))/2) -1;
                for j in range(c1+4, c2+1, 2):
                    SimulationDataWindows_step = SimulationDataWindows_step + 1;
                    temp  = yTimeLine;
                    SimulationDataWindows[SimulationDataWindows_step] = getMajorFromVector(j,temp);
                c1 = c2;
            c3 = i;
        else:
            c1 = c3;
            c2 = i;
    return  SimulationDataWindows[1:]
                         
        