from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from youtube_download_manoj import download_audio_by_name
import time
import os
from mp3Converter import convert_folder_mp4_to_mp3

def song_list():
    total = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[1]/div[5]/div/span[2]')
    total = total.text
    total =int(total.split(" ")[0])
    song_names = []
    for i in range(total-1):
        page.send_keys(Keys.ARROW_DOWN)
        xpath = f'//div[contains(@aria-rowindex,"{i+2}")]'
        # time.sleep(0.1)
        element = driver.find_element(By.XPATH,xpath)
        song_names.append(element.text)
    driver.close()
    return song_names


playlist_id = input("enter the url of your spotify playlist : ").split("/")[-1]
driver = webdriver.Chrome()
driver.get("https://open.spotify.com/playlist/"+playlist_id)
time.sleep(3)
page = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/div')
# page.click()
# page.send_keys(Keys.PAGE_DOWN)
# print("clicked!!!!!!!!!!!!!!")
time.sleep(2)
folder_name = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[1]/div[5]/span[2]/h1').text


songs_list =song_list()

songs = [i.split("\n") for i in songs_list]
final_songs = []
for i in songs:
    if len(i)>=3:
        final_songs.append(i[1]+','+i[2])
i=1
for song in final_songs:
    print(i,end="")
    i=i+1
    download_audio_by_name(song,folder_name)
current_dir = f"{os.getcwd()}/{folder_name}"
convert_folder_mp4_to_mp3(current_dir)
