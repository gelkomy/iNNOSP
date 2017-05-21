from PrepareYVector import getY
from PrepareWindowsVector import getWindows

#text_file=r'C:\Users\Yousef Essam\Desktop\Task1-ReadY\Patient14\test.txt'
text_file=r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\Patient14\chb14-summary.txt'
yTimeLine = getY(text_file)

windows = getWindows(yTimeLine)