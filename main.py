from GazeTracker import Setup, GazeLoop
import numpy as np
from Validation import validation
import time
from GetData import GetData

# Variablessu
fail = 0
filename1 = 'ECG_CH1'
filename2 = 'ECG_CH2'
initialState = [np.zeros(6),np.zeros(3),np.zeros(2)]
DataHor, DataVer, blinkingImage, params = Setup(filename1, filename2, initialState)
"""#time.sleep(10)
GetData(filename1) #truncates files
GetData(filename2) #truncates file
trial1Square, trial1Row, trial1Column = validation(params, filename1,filename2)
#time.sleep(10)
GetData(filename1) #truncates files
GetData(filename2) #truncates file
trial2Square, trial2Row, trial2Column = validation(params, filename1,filename2)
#time.sleep(10)
GetData(filename1) #truncates files
GetData(filename2) #truncates file
trial3Square, trial3Row, trial3Column = validation(params, filename1,filename2)
#time.sleep(10)
GetData(filename1) #truncates files
GetData(filename2) #truncates file
trial4Square, trial4Row, trial4Column = validation(params, filename1,filename2)



resultSquare = (trial1Square + trial2Square+trial3Square+ trial4Square)/4
resultRow = (trial1Row + trial2Row + trial3Row + trial4Row)/4
resultColumn = (trial1Column + trial2Column + trial3Column + trial4Column)/4    

print("Square accuracy" + str(resultSquare))
print("Row accuracy" + str(resultRow))
print("Column accuracy" + str(resultColumn))"""



GazeLoop(DataHor, DataVer, blinkingImage, params, filename1, filename2)
"""thread1.start()
thread2.start()
    
"""
