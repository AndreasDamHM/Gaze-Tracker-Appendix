import tkinter as tk
import time
from SignalProcessing import SignalProcessingTime
import numpy as np
from GetData import targetCreation, GetData
from DidIBlink import blinkTraining, didIBlink

class DotMatrix(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create 3x3 grid of Canvas widgets that fill the entire screen
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        cell_width = screen_width // 3
        cell_height = screen_height // 3
        self.cells = []
        for i in range(3):
            row = []
            for j in range(3):
                cell = tk.Canvas(self, width=cell_width, height=cell_height, bg='black')
                cell.grid(row=i, column=j)
                row.append(cell)
            self.cells.append(row)

        # Create dot in center cell
        self.current_dot = (1, 1)
        self.draw_dot()
        self.update()
        #time.sleep(2.5)  Add 2.5-second delay at start

    def draw_dot(self):
        # Clear previous dot
        for row in self.cells:
            for cell in row:
                cell.delete('all')

        # Draw current dot in center of current cell
        x, y = self.current_dot
        cell_width = self.cells[x][y].winfo_width()
        cell_height = self.cells[x][y].winfo_height()
        dot_size = min(cell_width, cell_height) // 16
        dot_x = cell_width // 2
        dot_y = cell_height // 2
        self.cells[x][y].create_oval(dot_x - dot_size, dot_y - dot_size, dot_x + dot_size, dot_y + dot_size,
                                     fill='white')

    def delete_dot(self):
        # Clear previous dot
        for row in self.cells:
            for cell in row:
                cell.delete('all')

        # Draw current dot in center of current cell
        x, y = self.current_dot
        cell_width = self.cells[x][y].winfo_width()
        cell_height = self.cells[x][y].winfo_height()
        dot_size = min(cell_width, cell_height) // 16
        dot_x = cell_width // 2
        dot_y = cell_height // 2
        self.cells[x][y].create_oval(dot_x - dot_size, dot_y - dot_size, dot_x + dot_size, dot_y + dot_size,
                                     fill='black')

    def run_animation(self):
        # Light up each dot in turn for 5 seconds

        label = tk.Label(self, text='Follow the dot with your eyes', bg='black', fg='white',
                         font=('Arial', 18))
        label.grid(row=0, column=1)
        self.update()
        time.sleep(1.5)
        label.destroy()

        left = 5.2
        right = 25.8
        midHor = 15.5
        top = 3.3
        bottom = 16.7
        midVer = 10.0

        self.current_dot = (1, 1)  # middle dot
        self.draw_dot()
        self.update()
        time.sleep(1)
        DataHor00, DataVer00, TargetHor00, TargetVer00 = targetCreation('ECG_CH1', 'ECG_CH2', 0.0, 0.0) #data not used in training
        time.sleep(2.22)
        DataHor1, DataVer1,TargetHor1, TargetVer1 = targetCreation('ECG_CH1', 'ECG_CH2', midHor, midVer)
        self.current_dot = (0, 0)  # top left dot
        self.draw_dot()
        self.update()
        time.sleep(0.5)
        DataHor01, DataVer01, TargetHor01, TargetVer01 = targetCreation('ECG_CH1', 'ECG_CH2', 0.0, 0.0) #data not used in training
        time.sleep(2.22)
        DataHor2, DataVer2,TargetHor2, TargetVer2 = targetCreation('ECG_CH1', 'ECG_CH2', left, top)
        self.current_dot = (2, 2)  # bottom right dot
        self.draw_dot()
        self.update()
        time.sleep(0.5)
        DataHor02, DataVer02, TargetHor02, TargetVer02 = targetCreation('ECG_CH1', 'ECG_CH2', 0.0, 0.0) #data not used in training
        time.sleep(2.22)
        DataHor3, DataVer3,TargetHor3, TargetVer3 = targetCreation('ECG_CH1', 'ECG_CH2', right, bottom)
        self.current_dot = (2, 0)  # bottom left dot
        self.draw_dot()
        self.update()
        time.sleep(0.5)
        DataHor03, DataVer03, TargetHor03, TargetVer03 = targetCreation('ECG_CH1', 'ECG_CH2', 0.0, 0.0) #data not used in training
        time.sleep(2.22)
        DataHor4, DataVer4, TargetHor4, TargetVer4 = targetCreation('ECG_CH1', 'ECG_CH2', left, bottom)
        self.current_dot = (0, 2)  # top right dot
        self.draw_dot()
        self.update()
        time.sleep(0.5)
        DataHor04, DataVer04, TargetHor04, TargetVer04 = targetCreation('ECG_CH1', 'ECG_CH2', 0.0, 0.0) #data not used in training
        time.sleep(2.22)
        DataHor5, DataVer5,TargetHor5, TargetVer5 = targetCreation('ECG_CH1', 'ECG_CH2', right, top)
        self.current_dot = (1, 0)  # middle left dot
        self.draw_dot()
        self.update()
        time.sleep(0.5)
        DataHor05, DataVer05, TargetHor05, TargetVer05 = targetCreation('ECG_CH1', 'ECG_CH2', 0.0, 0.0) #data not used in training
        time.sleep(2.22)
        DataHor6, DataVer6, TargetHor6, TargetVer6 = targetCreation('ECG_CH1', 'ECG_CH2', left, midVer)
        self.current_dot = (1, 2)  # middle right dot
        self.draw_dot()
        self.update()
        time.sleep(0.5)
        DataHor06, DataVer06, TargetHor06, TargetVer06 = targetCreation('ECG_CH1', 'ECG_CH2', 0.0, 0.0) #data not used in training
        time.sleep(2.22)
        DataHor7, DataVer7, TargetHor7, TargetVer7 = targetCreation('ECG_CH1', 'ECG_CH2', right, midVer)
        self.current_dot = (0, 1)  # top middle dot
        self.draw_dot()
        self.update()
        time.sleep(0.5)
        DataHor07, DataVer07, TargetHor07, TargetVer07 = targetCreation('ECG_CH1', 'ECG_CH2', 0.0, 0.0) #data not used in training
        time.sleep(2.22)
        DataHor8, DataVer8, TargetHor8, TargetVer8 = targetCreation('ECG_CH1', 'ECG_CH2', midHor, top)
        self.current_dot = (2, 1)  # bottom middle dot
        self.draw_dot()
        self.update()
        time.sleep(0.5)
        DataHor08, DataVer08, TargetHor08, TargetVer08 = targetCreation('ECG_CH1', 'ECG_CH2', 0.0, 0.0) #data not used in training
        time.sleep(2.22)
        DataHor9, DataVer9, TargetHor9, TargetVer9 = targetCreation('ECG_CH1', 'ECG_CH2', midHor, bottom)
        self.current_dot = (0, 1)  # top middle dot
        self.draw_dot()
        self.update()
        time.sleep(0.5)
        DataHor09, DataVer09, TargetHor09, TargetVer09 = targetCreation('ECG_CH1', 'ECG_CH2', 0.0, 0.0) #data not used in training
        time.sleep(2.22)
        DataHor10, DataVer10, TargetHor10, TargetVer10 = targetCreation('ECG_CH1', 'ECG_CH2', midHor, top)
        self.current_dot = (2, 1)  # bottom middle dot
        self.draw_dot()
        self.update()
        time.sleep(0.5)
        DataHor010, DataVer010, TargetHor010, TargetVer010 = targetCreation('ECG_CH1', 'ECG_CH2', 0.0, 0.0) #data not used in training
        time.sleep(2.22)
        DataHor11, DataVer11, TargetHor11, TargetVer11 = targetCreation('ECG_CH1', 'ECG_CH2', midHor, bottom)
        time.sleep(2)
        DataHor011, DataVer011, TargetHor011, TargetVer011 = targetCreation('ECG_CH1', 'ECG_CH2', 0.0, 0.0)


        targetsHor = np.hstack((TargetHor00, TargetHor1, TargetHor01, TargetHor2, TargetHor02, TargetHor3, TargetHor03, TargetHor4, TargetHor04,
                                TargetHor5, TargetHor05,TargetHor6, TargetHor06, TargetHor7, TargetHor07, TargetHor8, TargetHor08, TargetHor9,
                                TargetHor09, TargetHor10,TargetHor010, TargetHor11, TargetHor011))
        targetsVer = np.hstack((TargetVer00, TargetVer1, TargetVer01, TargetVer2, TargetVer02, TargetVer3, TargetVer03, TargetVer4, TargetVer04,
                                TargetVer5, TargetVer05,TargetVer6, TargetVer06, TargetVer7, TargetVer07, TargetVer8, TargetVer08, TargetVer9,
                                TargetVer09, TargetVer10,TargetVer010, TargetVer11, TargetVer011))
        DataHor = np.hstack((DataHor00, DataHor1, DataHor01, DataHor2, DataHor02, DataHor3, DataHor03, DataHor4, DataHor04,DataHor5, DataHor05,
                             DataHor6, DataHor06, DataHor7, DataHor07, DataHor8, DataHor08, DataHor9, DataHor09, DataHor10,DataHor010, DataHor11,
                             DataHor011))
        DataVer = np.hstack((DataVer00, DataVer1, DataVer01, DataVer2, DataVer02, DataVer3, DataVer03, DataVer4, DataVer04,DataVer5, DataVer05,
                             DataVer6, DataVer06, DataVer7, DataVer07, DataVer8, DataVer08, DataVer9, DataVer09, DataVer10,DataVer010, DataVer11,
                             DataVer011))

        return DataHor, DataVer, targetsHor, targetsVer

    def blinkingApp(self):
        # Textbox
        label = tk.Label(self, text='Blink when the dot appears in the middle of the screen', bg='black', fg='white', font=('Arial',15))
        label.grid(row=0, column=1)
        self.current_dot = (1, 1)  # middle dot
        self.delete_dot()
        self.update()
        GetData('ECG_CH2')  # truncate
        GetData('ECG_CH1')
        time.sleep(4)
        for i in range(4):
            self.draw_dot()
            self.update()
            time.sleep(0.5)
            self.delete_dot()
            self.update()
            time.sleep(2)
        blinkDataVer = GetData('ECG_CH2')
        blinkDataHor = GetData('ECG_CH1')
        return blinkDataVer, blinkDataHor



def calibrationGUI(KEY1, KEY2):

    root = tk.Tk()
    root.attributes('-fullscreen', True)  # Make GUI fill entire screen
    root.title('Dot Matrix')
    root.attributes('-topmost', True)
    app = DotMatrix(master=root)
    app.pack()
    file1 = open(
        "C:/Users/andre/OneDrive/Dokumenter/Texas Instruments/Bio-Sensing/projects/AFE4960EVM/GUI/" + KEY1 + ".csv",
        'r+')
    file2 = open(
        "C:/Users/andre/OneDrive/Dokumenter/Texas Instruments/Bio-Sensing/projects/AFE4960EVM/GUI/" + KEY2 + ".csv",
        'r+')
    file1.truncate(0)
    file2.truncate(0)
    file1.close()
    file2.close()
    DataHor, DataVer, targetsHor, targetsVer = app.run_animation()
    blinkingDataVer, blinkingDataHor = app.blinkingApp()
    root.destroy()

    return DataHor, DataVer, targetsHor, targetsVer, blinkingDataVer, blinkingDataHor

"""root = tk.Tk()
root.attributes('-fullscreen', True)  # Make GUI fill entire screen
root.title('Dot Matrix')
root.attributes('-topmost', True)
app = DotMatrix(master=root)
app.pack()
blinkingDataVer, blinkingDataHor,_,_,_,_ = app.run_animation()
root.destroy()
blinkingImage = blinkTraining(blinkingDataVer, blinkingDataHor)

"""








