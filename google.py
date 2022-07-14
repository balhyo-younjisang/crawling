from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #클릭후 이미지로딩 기다리기
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q") #검색창 name으로 찾기
elem.send_keys("apple") #키워드 설정
elem.send_keys(Keys.RETURN) # 엔터
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
  image.click() # 클래스 찾아 클릭
  time.sleep(3)
  imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
  #이미지주소 src 다운로드
  urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
  count = count + 1
