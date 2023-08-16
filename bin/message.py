import pyautogui
import pyperclip
import random 
import time 
import os

from PyQt5.QtCore import QThread, pyqtSignal

class Message(QThread):
    '''문자 or 사진을 개인, 단체, 또는 개인과 단체에 보내는 클래스 정의'''
    process_signal = pyqtSignal(str)
    finish_signal = pyqtSignal(str)
    
    def __init__(self, parent, msg_type, msg_audience, num_friends, group_chat_names):
        super(Message, self).__init__()
        self.parent = parent
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.msg_type = msg_type
        self.msg_audience = msg_audience 
        self.num_friends = num_friends
        self.group_chat_names = group_chat_names
        self.search_icon = self.fetch_icon_path('search_icon.png')
        self.person_icon = self.fetch_icon_path('person_icon.png')
        self.person_icon_2 = self.fetch_icon_path('person_icon_2.png')
        self.send_file_icon = self.fetch_icon_path('send_file_icon.png')
        self.num_pic_files = None
        self.file_ext = "jpg"
        
    def fetch_icon_path(self, icon_name):
        '''상위 img 폴더 내의 특정 img의 상대경로 반환하기'''
        img_path = os.path.normpath(os.path.join(self.current_path, '../img'))
        icon_path = os.path.normpath(os.path.join(img_path, icon_name))
        return icon_path
    
    def fetch_img_path(self, img_idx, img_ext):
        '''상위 inspirational 폴더 내의 특정 img의 상대경로 반환하기'''
        file_path = os.path.normpath(os.path.join(self.current_path, '../inspirational_img'))
        file_name = str(img_idx) + '.' + img_ext
        img_path = os.path.normpath(os.path.join(file_path, file_name))
        return img_path
    
    def digitize_pic_filename(self):
        '''inspirational_img 폴더 밑의 모든 사진 파일 이름을 숫자로 변환하기'''
        pic_path = os.path.normpath(os.path.join(self.current_path, '../inspirational_img'))
        os.chdir(pic_path)
        self.num_pic_files = len(os.listdir(pic_path))
        self.file_ext = 'jpg'
        for idx, file in enumerate(os.listdir(pic_path), 1):
            temp_name = '{}'.format(str(idx))
            os.rename(file, temp_name)
        time.sleep(random.uniform(0.5,2))
        for idx, file in enumerate(os.listdir(pic_path), 1):
            new_name = '{}.{}'.format(str(idx), 'jpg')
            os.rename(file, new_name)
    
    def send_text_to_individuals(self):
        '''문자를 개인들에게 전송하는 함수'''
        search_icon_location = pyautogui.locateCenterOnScreen(self.search_icon, grayscale=True, confidence=0.7)
        try:
            # search_icon 밑에 있는 내 프로필 사진을 클릭 후 관련 문자 정보를 들고온다.
            search_icon_location = pyautogui.locateCenterOnScreen(self.search_icon, grayscale=True, confidence=0.7)
            search_icon_x_coordinate, search_icon_y_coordinate = search_icon_location
            pyautogui.click(search_icon_x_coordinate, search_icon_y_coordinate + 30)
            pyautogui.keyDown('enter')
            pyautogui.hotkey('ctrl','a')
            pyautogui.hotkey('ctrl','c')
            text = pyperclip.paste()
            pyautogui.keyDown('esc')
            print(text)
            self.process_signal.emit(f"개인에게 보내는 텍스트는 {text}")

            # search_icon을 클릭한 뒤, 키워드('+')를 클릭하고, 순차적으로 친구들에게 문자를 전송한다.
            pyautogui.click(search_icon_x_coordinate, search_icon_y_coordinate)
            time_wait = random.uniform(0.3, 1)
            time.sleep(time_wait)
            pyautogui.write('+')

            for i in range(1,int(self.num_friends)+1):
                time_wait = random.uniform(0.3,2)
                time.sleep(time_wait)
                pyautogui.keyDown('enter')
                print('지금은 {} 번째 친구에게 메세지를 보내고 있습니다.'.format(i))
                self.process_signal.emit(f"지금은 {i} 번째 친구에게 메세지를 보내고 있습니다.")
                
                pyautogui.hotkey('ctrl', 'v')  
                pyautogui.keyDown('enter')
                time.sleep(0.5)
                pyautogui.keyDown('esc')
                pyautogui.keyDown('down')
            
            # search_icon 한번 클릭하고,
            pyautogui.click(search_icon_x_coordinate, search_icon_y_coordinate)  
        except:
            print("search icon 밑에 프로필 창을 찾는 것을 실패했습니다!")
            self.process_signal.emit("search icon 밑에 프로필 창을 찾는 것을 실패했습니다!")
        else:
            try:
                # 다시 프로필로 돌아가기
                person_icon_location = pyautogui.locateCenterOnScreen(self.person_icon, grayscale=True, confidence=0.7)
                person_icon_x_coordinate, person_icon_y_coordinate = person_icon_location
                pyautogui.click(person_icon_x_coordinate, person_icon_y_coordinate)
            except:
                print("좌측 상단에 person_icon 아이콘을 찾는 것을 실패했습니다!")
                self.process_signal.emit("좌측 상단에 person_icon 아이콘을 찾는 것을 실패했습니다!")
            else:
                pass
        
    def send_text_to_groups(self):
        '''문자를 그룹들에게 전송하는 함수'''
        try:
            # search_icon 밑에 있는 내 프로필 사진을 클릭 후 관련 문자 정보를 들고온다.
            search_icon_location = pyautogui.locateCenterOnScreen(self.search_icon, grayscale=True, confidence=0.7)
            search_icon_x_coordinate, search_icon_y_coordinate = search_icon_location
            pyautogui.click(search_icon_x_coordinate, search_icon_y_coordinate + 30)
            pyautogui.keyDown('enter')
            pyautogui.hotkey('ctrl','a')
            pyautogui.hotkey('ctrl','c')
            text = pyperclip.paste()
            pyautogui.keyDown('esc')
            
            print('모든 단톡방에 보내질 현재 메세지는 ', text)
            self.process_signal.emit(f"단톡방에 보내질 현재 메세지는 {text}")
            time_wait = random.uniform(0.3,2)
            time.sleep(time_wait)
        except:
            print("search icon 밑에 프로필 창을 찾는 것을 실패했습니다!")
            self.process_signal.emit(f"search icon 밑에 프로필 창을 찾는 것을 실패했습니다!")
        else:
            try:
                # 그룹챗 아이콘을 클릭한다.
                person_icon_location = pyautogui.locateCenterOnScreen(self.person_icon, grayscale=True, confidence=0.7)
                person_icon_x_coordinate, person_icon_y_coordinate = person_icon_location
                pyautogui.click(person_icon_x_coordinate, person_icon_y_coordinate + 65)

                time_wait = random.uniform(0.3,2)
                time.sleep(time_wait)
            except:
                print("그룹챗 아이콘을 찾는 것을 실패했습니다!")
                self.process_signal.emit(f"그룹챗 아이콘을 찾는 것을 실패했습니다!")
            else:
                try:
                    # 돋보기 아이콘을 클릭한다.
                    inner_search_icon_location = pyautogui.locateCenterOnScreen(self.search_icon, grayscale=True, confidence=0.7)
                    inner_search_icon_x_coordinate, inner_search_icon_y_coordinate = inner_search_icon_location
                    pyautogui.click(inner_search_icon_x_coordinate, inner_search_icon_y_coordinate)
                except:
                    print("search icon을 찾는 것을 실패했습니다!")
                    self.process_signal.emit(f"search icon을 찾는 것을 실패했습니다!")
                    time.sleep(0.5)
                else:
                    try:
                        # 그룹챗 이름을 돌면서, 그룹챗 이름을 입력한다.
                        for chat_name in self.group_chat_names:

                            # 그룹쳇 이름의 한 인스턴스를 저장하여서, 검색창에 붙입니다.
                            pyautogui.write(chat_name)
                            time.sleep(time_wait)

                            # 조금 시간을 두고, 그 그룹챗방에 들어갑니다.
                            time_wait = random.uniform(0.3,2)
                            time.sleep(time_wait)
                            pyautogui.keyDown('enter')

                            # 여기에서 text을 한번 복사붙여 넣기를 해야 합니다
                            pyperclip.copy(text)
                            print('복사된 문자는', text)
                            self.process_signal.emit(f"복사된 문자는 {text}")
                            
                            # 지금 보내고 있는 단톡방의 이름 출력하기
                            print('지금 메세지를 보내고 있는 단톡방은 ', chat_name ,' 방입니다.')
                            self.process_signal.emit(f"지금 메세지를 보내고 있는 단톡방은  {chat_name} 입니다")

                            # 어느 정도 시간 간격을 두고, 문자를 붙입니다.
                            time_wait = random.uniform(0,3.5)
                            time.sleep(time_wait)
                            pyautogui.hotkey('ctrl', 'v')

                            # 문자를 붙이고, enter 키를 내리고 내용을 드디어!!! 전달합니다 !!!
                            time.sleep(time_wait)
                            pyautogui.keyDown('enter')

                            # 일정한 시간을 두고, esc을 누르고 창을 빠져나옵니다.
                            time.sleep(time_wait)
                            pyautogui.keyDown('esc')
                            time_wait = random.uniform(0,2)
                            time.sleep(time_wait)

                            pyautogui.keyDown('esc')
                            for w in range(len(chat_name)):
                                pyautogui.hotkey('backspace')
                            time_wait = random.uniform(0,2)
                            time.sleep(time_wait)
                        
                        # search_icon 한번 클릭하고, 문자 발송을 마무리합니다.
                        pyautogui.click(inner_search_icon_x_coordinate, inner_search_icon_y_coordinate)
                    except:
                        print("그룹챗 이름을 돌면서, 그룹챗 이름을 출력하는 것을 실패했습니다!")
                        self.process_signal.emit(f"그룹챗 이름을 돌면서, 그룹챗 이름을 출력하는 것을 실패했습니다!")
                        time.sleep(0.5)
                    else:
                        pass
                        
    def send_image_to_individuals(self):
        '''이미지를 개인들에게 전송하는 함수'''
        try:
            # 내 프로필 사진을 클릭한다.
            search_icon_location = pyautogui.locateCenterOnScreen(self.search_icon, grayscale=True, confidence=0.7)
            search_icon_x_coordinate, search_icon_y_coordinate = search_icon_location
            time.sleep(1)
            pyautogui.click(search_icon_x_coordinate, search_icon_y_coordinate + 30)
            # self.digitize_pic_filename()
            time.sleep(0.5)
        except:
            print("search icon 밑에 프로필 창을 찾는 것을 실패했습니다!")
            self.process_signal.emit(f"search icon 밑에 프로필 창을 찾는 것을 실패했습니다!")
        else:
            try:
                # 랜덤한 사진을 선택한다.
                random_img_idx = random.randrange(1,self.num_pic_files)
                random_img_ext = self.file_ext
                pyautogui.keyDown('enter')
                time.sleep(2)
                send_file_link_location = pyautogui.locateCenterOnScreen(self.send_file_icon, confidence=0.67)
                x,y = send_file_link_location
                pyautogui.click(x,y)
                # My Chatroom에 복사 해 둔다
                random_img_idx = 21
                img_to_send = self.fetch_img_path(random_img_idx, random_img_ext)
                pyperclip.copy(img_to_send)
                pyautogui.hotkey('ctrl','v')
                time.sleep(1)
                pyautogui.keyDown('enter')
                time.sleep(1)
                pyautogui.keyDown('enter')
                time.sleep(1)
                print("지금 선택된 사진은 {}번째 사진입니다".format(str(random_img_idx)))
                self.process_signal.emit(f"지금 선택된 사진은 {random_img_idx}번째 사진입니다!")
            except:
                print("나의 카카오톡에서 send 클립 아이콘 찾는 것을 실패했습니다!")
                self.process_signal.emit(f"나의 카카오톡에서 send 클립 아이콘 찾는 것을 실패했습니다!")
            else: 
                try:
                    # send_filed의 동북쪽 방향 위에 있는 My Chatroom에 저장된 사진을 들고 온다
                    send_file_link_location = pyautogui.locateCenterOnScreen(self.send_file_icon, confidence=0.67)
                    x,y = send_file_link_location
                    pyautogui.click(x+200,y-350)
                    time.sleep(0.5)
                    pyautogui.hotkey('ctrl', 'c')
                    time.sleep(0.5)
                    pyautogui.keyDown('esc')
                    time.sleep(0.5)
                    pyautogui.keyDown('esc')
                except:
                    print("send icon 찾는 것을 실패해서, 메모리에 사진 복사를 실패했습니다!")
                    self.process_signal.emit(f"send icon 찾는 것을 실패해서, 메모리에 사진 복사를 실패했습니다!")
                else:
                    try:
                        search_icon_location = pyautogui.locateCenterOnScreen(self.search_icon, grayscale=True, confidence=0.7)
                        search_icon_x_coordinate, search_icon_y_coordinate = search_icon_location
                        pyautogui.click(search_icon_x_coordinate, search_icon_y_coordinate)
                        time.sleep(1)
                        pyautogui.write('+')
                        time.sleep(1)
                        for i in range(1,int(self.num_friends)+1):
                            time.sleep(0.5)
                            pyautogui.keyDown('enter')
                            print('지금은 {} 번째 친구에게 이미지를 보내고 있습니다.'.format(i))
                            self.process_signal.emit(f"지금은 {i} 번째 친구에게 이미지를 보내고 있습니다.")
                            pyautogui.hotkey('ctrl', 'v')  
                            pyautogui.keyDown('enter')
                            time.sleep(0.5)
                            pyautogui.keyDown('esc')
                            pyautogui.keyDown('down')
                        print("모든 친구들에게 이미지 전송을 완료했습니다.")
                        self.process_signal.emit(f"모든 친구들에게 이미지 전송을 완료했습니다.")
                        self.finish_signal.emit("작업완료")
                        # search_icon 한번 클릭하고,
                        pyautogui.click(search_icon_x_coordinate, search_icon_y_coordinate)
                        time.sleep(0.5)
                    except:
                        print("search icon 밑에 프로필 창을 찾는 것을 실패했습니다!")
                        self.process_signal.emit(f"search icon 밑에 프로필 창을 찾는 것을 실패했습니다!")
                    else:
                        try:
                            # 다시 프로필로 돌아가기
                            person_icon_location = pyautogui.locateCenterOnScreen(self.person_icon, grayscale=True, confidence=0.7)
                            person_icon_x_coordinate, person_icon_y_coordinate = person_icon_location
                            pyautogui.click(person_icon_x_coordinate, person_icon_y_coordinate)
                        except:
                            print("좌측 상단에 person_icon 아이콘을 찾는 것을 실패했습니다!")
                            self.process_signal.emit("좌측 상단에 person_icon 아이콘을 찾는 것을 실패했습니다!")
                        else:
                            pass

            
    def send_image_to_groups(self):
        '''이미지를 그룹들에게 전송하는 함수'''
        # 내 프로필 사진을 클릭한다.
        try:
            # 내 프로필 사진을 클릭한다.
            search_icon_location = pyautogui.locateCenterOnScreen(self.search_icon, grayscale=True, confidence=0.7)
            search_icon_x_coordinate, search_icon_y_coordinate = search_icon_location
            pyautogui.click(search_icon_x_coordinate, search_icon_y_coordinate + 30)
            # self.digitize_pic_filename()
            time.sleep(0.5)
        except:
            print("search icon 밑에 프로필 창을 찾는 것을 실패했습니다!")
            self.process_signal.emit(f"search icon 밑에 프로필 창을 찾는 것을 실패했습니다!")
        else:
            try:
                # 랜덤한 사진을 선택한다.
                random_img_idx = random.randrange(1,self.num_pic_files)
                random_img_ext = self.file_ext
                pyautogui.keyDown('enter')
                time.sleep(0.5)
                send_file_link_location = pyautogui.locateCenterOnScreen(self.send_file_icon, confidence=0.67)
                x,y = send_file_link_location
                pyautogui.click(x,y)
                # My Chatroom에 복사 해 둔다
                random_img_idx = 21
                img_to_send = self.fetch_img_path(random_img_idx, random_img_ext)
                pyperclip.copy(img_to_send)
                pyautogui.hotkey('ctrl','v')
                time.sleep(0.5)
                pyautogui.keyDown('enter')
                time.sleep(0.5)
                pyautogui.keyDown('enter')
                time.sleep(0.5)
                print("지금 선택된 사진은 {}번째 사진입니다".format(str(random_img_idx)))
                self.process_signal.emit(f"지금 선택된 사진은 {random_img_idx}번째 사진입니다!")
            except:
                print("나의 카카오톡에서 send 클립 아이콘 찾는 것을 실패했습니다!")
                self.process_signal.emit(f"나의 카카오톡에서 send 클립 아이콘 찾는 것을 실패했습니다!")
            else:
                try:
                    # send_filed의 동북쪽 방향 위에 있는 My Chatroom에 저장된 사진을 들고 온다
                    send_file_link_location = pyautogui.locateCenterOnScreen(self.send_file_icon, confidence=0.67)
                    x,y = send_file_link_location
                    pyautogui.click(x+200,y-350)
                    time.sleep(0.5)
                    pyautogui.hotkey('ctrl', 'c')
                    time.sleep(0.5)
                    pyautogui.keyDown('esc')
                    time.sleep(0.5)
                    pyautogui.keyDown('esc')
                except:
                    print("send icon 찾는 것을 실패해서, 메모리에 사진 복사를 실패했습니다!")
                    self.process_signal.emit(f"send icon 찾는 것을 실패해서, 메모리에 사진 복사를 실패했습니다!")
                else:
                    try:
                        # 그룹챗 아이콘을 클릭한다.
                        person_icon_location = pyautogui.locateCenterOnScreen(self.person_icon_2, confidence=0.67)
                        person_icon_x_coordinate, person_icon_y_coordinate = person_icon_location
                        pyautogui.click(person_icon_x_coordinate, person_icon_y_coordinate + 65)
                        time.sleep(0.5)
                    except:
                        print("person icon 찾는 것을 실패해서, 그룹챗 아이콘 클릭에 실패했습니다!")
                        self.process_signal.emit(f"person icon 찾는 것을 실패해서, 그룹챗 아이콘 클릭에 실패했습니다!")
                    else:
                        try:
                            # 돋보기 아이콘을 클릭한다.
                            inner_search_icon_location = pyautogui.locateCenterOnScreen(self.search_icon, confidence=0.7)
                            inner_search_icon_x_coordinate, inner_search_icon_y_coordinate = inner_search_icon_location
                            pyautogui.click(inner_search_icon_x_coordinate, inner_search_icon_y_coordinate)
                            time.sleep(0.5)
                        except:
                            print("search icon 찾는 것을 실패했습니다!")
                            self.process_signal.emit(f"search icon 찾는 것을 실패했습니다!")
                        else:
                            try:
                                # 그룹챗 이름을 돌면서, 그룹챗 이름을 입력한다.
                                for chat_name in self.group_chat_names:

                                    # 그룹쳇 이름의 한 인스턴스를 저장하여서, 검색창에 붙입니다.
                                    pyautogui.write(chat_name)

                                    # 조금 시간을 두고, 그 그룹챗방에 들어갑니다.
                                    time_wait = random.uniform(0.3,2)
                                    time.sleep(time_wait)
                                    pyautogui.keyDown('enter')

                                    print('지금은 {} 채팅방에 이미지를 보내고 있습니다.'.format(chat_name))
                                    self.process_signal.emit(f"지금은 {chat_name} 채팅방에 이미지를 보내고 있습니다!")
                                    pyautogui.hotkey('ctrl', 'v')  
                                    pyautogui.keyDown('enter')
                                    time.sleep(random.uniform(0.3,2))
                                    pyautogui.keyDown('esc')
                                    
                                    for w in range(len(chat_name)):
                                        pyautogui.hotkey('backspace')
                                    time_wait = random.uniform(0,2)
                                    time.sleep(time_wait)
                            except:
                                print("그룹챗 이름을 돌면서, 그룹챗 이름을 입력하면서, 사진 보내기를 실패했습니다!")
                                self.process_signal.emit(f"그룹챗 이름을 돌면서, 그룹챗 이름을 입력하면서, 사진 보내기를 실패했습니다!")
                            else:
                                pass
        
    def run(self):
        if self.msg_type == '문자':
            if self.msg_audience == '개인':
                self.send_text_to_individuals()
            if self.msg_audience == '단체':
                self.send_text_to_groups()
            if self.msg_audience == '개인과 단체':
                self.send_text_to_individuals()
                self.send_text_to_groups()
                
        elif self.msg_type == '사진':
            if self.msg_audience == '개인':
                self.send_image_to_individuals()
            if self.msg_audience == '단체':
                self.send_image_to_groups()
            if self.msg_audience == '개인과 단체':
                self.send_image_to_individuals()
                self.send_image_to_groups()
        
        self.parent.time_worker.working = False