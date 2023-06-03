import sys
import os
import datetime

# 관련 경로 sys 환경변수에 추가해주기
current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_path)
sys.path.append(os.path.normpath(os.path.join(current_path, '../')))
sys.path.append(os.path.normpath(os.path.join(current_path, '../../')))

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ui.main_ui import Ui_MainWindow
from message import Message
from elapse_timer import TimeDisplayWorker

class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('카카오톡 자동 전송하기 프로그램')
        self.resize(800, 600)
        self.msg_type = None
        self.msg_audience = None
        self.num_friends = None 
        self.group_chat_names = None
        self.group_chat_name_str = None
        self.message_thread = None
        self.init_button_signal()
        self.get_program_input()
        self.set_program_input()
        self.time_worker = TimeDisplayWorker(self)
        self.time_worker.time_signal.connect(self.func_time_emit)
        self.time_worker.job_finished_signal.connect(self.finish_messaging_job)
    
    def init_button_signal(self):
        self.sendButton.clicked.connect(self.check_before_accept)
        self.cancelButton.clicked.connect(self.close)
    
    def get_program_input(self):
        if os.path.exists(current_path + "/program_input.txt"):
            with open(current_path + "/program_input.txt", 'r', encoding='UTF8') as f:
                program_data = f.read()
            f.close()
            
            self.msg_type = program_data.split("\n")[0]
            self.msg_audience = program_data.split("\n")[1]
            self.num_friends = program_data.split("\n")[2]
            self.group_chat_names = program_data.split("\n")[3].split(', ')
    
    def set_program_input(self):
        if self.msg_type == '문자':
            self.msgButton.setChecked(True)
        if self.msg_type == '사진': 
            self.imgButton.setChecked(True)
        if self.msg_audience == '개인':
            self.individualButton.setChecked(True)
        if self.msg_audience == '단체':
            self.groupButton.setChecked(True)
        if self.msg_audience == '개인과 단체':
            self.individaulAndgroupButton.setChecked(True)

        self.numFriendsLineEdit.setText(self.num_friends)
        
        model = QStandardItemModel()
        for name in self.group_chat_names:
            model.appendRow(QStandardItem(name))
        self.listView.setModel(model)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    
    def save_program_input(self):
        self.msg_type = self.msgTypeButtonGroup.checkedButton().text()
        self.msg_audience = self.msgAudienceButtonGroup.checkedButton().text()
        self.group_chat_name_str = ', '.join(e for e in self.group_chat_names)
        
        with open(current_path + "/program_input.txt", 'w', encoding='UTF8') as f:
            try:
                f.write(self.msg_type + "\n")
                f.write(self.msg_audience + "\n")
                f.write(self.numFriendsLineEdit.text().strip() + "\n")
                f.write(self.group_chat_name_str + "\n")
            except Exception as e:
                print(e)
        f.close()
    
    def check_before_accept(self):
        if not self.msgButton.isChecked() and not self.imgButton.isChecked():
            QMessageBox.warning(self, "경고 메세지", "전송할 메세지 종류를 입력하세요!")
            return
        if not self.individualButton.isChecked() and not self.groupButton.isChecked() and not self.individaulAndgroupButton.isChecked():
            QMessageBox.warning(self, "경고 메세지", "메세지를 전송할 대상을 입력하세요!")
            return
        if self.numFriendsLineEdit.text().strip() == '':
            QMessageBox.warning(self, "경고 메세지", "메세지를 전송할 친구의 숫자를 입력하세요!")
            return
        if self.numFriendsLineEdit.text().strip().isdigit() == False:
            QMessageBox.warning(self, "경고 메세지", "보낼 친구란에 순수 숫자만 입력 해주세요!")
            return
    
        self.msg_type = self.msgTypeButtonGroup.checkedButton().text()
        self.msg_audience = self.msgAudienceButtonGroup.checkedButton().text()
        self.num_friends = self.numFriendsLineEdit.text().strip()
        
        # 시작버튼 더블 클릭 방지 및 배치 시간 타이머 설정 시작 -> 크롤링 시작전에 세팅 여부 확인
        self.sendButton.setText("작업 중")
        self.sendButton.setEnabled(False)
        
        self.accept()
    
    def accept(self):
        self.append_text("카카오톡 메세지 전송을 시작합니다.")
        self.time_worker.start()
        self.message_thread = Message(self, self.msg_type, self.msg_audience, self.numFriendsLineEdit.text().strip(), self.group_chat_names)
        self.message_thread.start()
        self.message_thread.process_signal.connect(self.append_text)
        self.message_thread.finish_signal.connect(self.reset_button)
    
    # 현재 시간 계산 후 -> 콘솔 출력 -> GUI 로그창에 표시
    @pyqtSlot(str)
    def append_text(self, msg):
        current_time = str(datetime.datetime.now()).split(".")[0]
        print(current_time + " - " + msg)
        self.plainTextEdit.appendPlainText(current_time + " - " + msg)
    
    @pyqtSlot(str)
    def reset_button(self, msg):
        if msg == '작업완료':
            self.sendButton.setText("시작")
            self.sendButton.setEnabled(True)
    
    def close(self):
        self.sendButton.setText("시작")
        self.sendButton.setEnabled(True)
        # self.timer.stop()
        if self.message_thread is not None:
            self.message_thread.terminate()
            self.append_text("카카오톡 메세지 전송을 중지합니다.")
        else:
            self.append_text("카카오톡 메세지 전송 프로그램을 종료합니다")
            self.__del__()
            QApplication.quit()
    
    @pyqtSlot(int)
    def func_time_emit(self, curr_time):
        self.stop_watch_real_time_label.setText(str(curr_time)+"초")
    
    @pyqtSlot()
    def finish_messaging_job(self):
        if self.time_worker.job_finished_signal:
            print('yeyeye!!!!')
            QMessageBox.information(self, "Finished", "모든 메세지 전송이 정상적으로 종료되었습니다.")
    
    # exe 종료 시그널 -> 해당 객체가 소멸될때 __del__메소드 호출되며 -> 사용자의 로그인 정보를 로컬에 다시 저장
    def __del__(self):
        try:
            self.message_thread.terminate()
        except:
            pass
        try:
            self.save_program_input()
        except:
            pass
    
    # GUI를 닫으면, 호출되는 pyqt 내장함수
    def closeEvent(self, event: QCloseEvent) -> None:
        self.__del__()
        super().closeEvent(event)
    
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(App.exec())