#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import constantStrings


class BrowserInstance():
    driver = webdriver.Firefox()

    def startBrowser(self):
        self.driver.firefox_profile.profile_dir \
            = "/home/bibek/.mozilla/firefox/27jnvdb2.default"
        self.driver.get("http://www.omegle.com")
        for each in constantStrings.tags:
            self.driver.find_element_by_css_selector('.topiceditor.newtopicinput')\
                       .send_keys(each)
            self.driver.find_element_by_css_selector('.topiceditor.newtopicinput'')\
                       .send_keys(Keys.ENTER)
            self.driver.find_element_by_id('textbtn').click()

    def chatDisconnect(self):
        self.driver.find_element_by_class_name('disconnectbtn').click()
        self.driver.find_element_by_class_name('disconnectbtn').click()


def reply(instance, newMessage):
    if 'disconnected.' in newMessage:
        instance.chatDisconnect()
        return 0
#    elif ("male" in newMessage) or (" m" in newMessage):
#        return "okay!"
    else:
        return ""


def main():
    newOne = BrowserInstance()
    newOne.startBrowser()


main()



# # main chat loop begins
# notNewMessage = constantStrings.welcomeMsg
# waited_time = 0

# # Wait time for connection to happen.
# time.sleep(7)


# def chatloop(driver):
#     while True:


#         if not len(newMessage):
#             waited_time += 2
#         else:
#             print(newMessage)
#             waited_time = 0
#             notNewMessage += newMessage

#             # reply Handling and switching.
#             message = reply(newMessage)
#             if message:
#                 driver.find_element_by_class_name('chatmsgwrapper').send_keys(message)
#                 driver.find_element_by_class_name('sendbtn').click()
#             elif message == 0:
#                 notNewMessage = constantStrings.welcomeMsg
#                 waited_time = 0
#                 time.sleep(2)
#                 newMessage = ''
#             if waited_time > 30:
#                 chatDisconnect()
#                 time.sleep(1)
