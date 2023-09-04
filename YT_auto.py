import pyttsx3 as p
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

class music():
    def __init__(self):
        # Khởi tạo trình duyệt Firefox
        self.driver = webdriver.Firefox()

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        
        # Chờ cho trang web tải hoàn toàn và phần tử có ID 'dismissible' xuất hiện
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'dismissible')))
        
        video = self.driver.find_element(By.ID, 'dismissible')
        video.click()
        

# assist = music()
# assist.play('Wonder sea breeze')