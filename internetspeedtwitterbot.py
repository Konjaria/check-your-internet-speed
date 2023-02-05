"""
Author: Saba Konjaria
Created at: 05-Feb-2023
"""
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class InternetSpeedTwitterBot:
    def __init__(self, down, up):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.down = None
        self.up = None
        self.internet_provider = None
        self.promised_down = down
        self.promised_up = up

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        self.internet_provider = self.driver.find_element(By.XPATH, "//*[@id=\"container\"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[1]/div[3]/div[2]").text
        GO = self.driver.find_element(By.XPATH, "//*[@id=\"container\"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        GO.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, "//*[@id=\"container\"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        self.up = self.driver.find_element(By.XPATH, "//*[@id=\"container\"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        print("down: ", self.down)
        print("up: ", self.up)

    def tweet_at_provider(self, username, password):
        self.driver.get(url="https://twitter.com/")
        log_in_button = self.driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a/div/span/span")
        print(f'{log_in_button.text} Button Has been found successfully.')
        log_in_button.click()
        time.sleep(2)
        # put in  username
        username_button = self.driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        username_button.send_keys(str(username))
        username_button.send_keys(Keys.ENTER)
        # hold on for a while till next button won't be triggered
        time.sleep(13)
        # put in password
        password_button = self.driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password_button.send_keys(str(password))
        password_button.send_keys(Keys.ENTER)
        # and again hold on for a while
        time.sleep(15)
        # find a field where we have to post on a twitter
        wazoo = self.driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span/span")
        print(wazoo.text)
        wazoo.send_keys(f"Hey {self.internet_provider}, why is my internet speed {self.down}down/{self.up}up when I pay for {self.promised_down}down/{self.promised_up}up!!"
                         f"150down/10up?")

        # final step: tweet on Twitter
        tweet_button = self.driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        tweet_button.click()

        time.sleep(30)
        self.driver.quit()


    def check_for_tweet(self):
        return self.promised_down < self.down or self.promised_up < self.up


bot = InternetSpeedTwitterBot(down='your-internet-provider-promised-down',
                              up='your-internet-provider-promised-up')

bot.get_internet_speed()
if bot.check_for_tweet():
    bot.tweet_at_provider(username="your-username",
                          password="your-password")

