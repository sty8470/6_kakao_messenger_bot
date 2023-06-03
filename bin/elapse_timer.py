import sys
import os
  
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import *

current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_path)
sys.path.append(os.path.normpath(os.path.join(current_path, '../')))
sys.path.append(os.path.normpath(os.path.join(current_path, '../../')))

class TimeDisplayWorker(QThread):
    time_signal = pyqtSignal(int)
    job_finished_signal = pyqtSignal(bool)
    
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.working = True
        self.job_finished = False

    def run(self):        
        curr_time = 0
        self.working = True
        while self.working:
            self.time_signal.emit(curr_time)            
            curr_time += 1
            self.sleep(1)
        self.job_finished_signal.emit(True)
    def stop(self):
        # https://developer-mistive.tistory.com/58
        self.working = False
        self.quit()
        self.wait(5000)