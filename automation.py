from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

name = input("Enter name of the WhatsApp user or group: ")
msg = input("Type the message you'd want to send: ")
count = int(input("How may msgs do you want to send: "))

input("have you scanned the qr code? If yes type any letter and hit Enter: ")

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

# msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[1]/div/div[2]")
# msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]")
msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")


for i in range(count):
    msg_box.send_keys(msg)
    # driver.find_element_by_xpath(" //*[@id='main']/footer/div[1]/div[2]/div/div[2]/button").click()
    # driver.find_element_by_xpath(" //*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[2]/button").click()

    


print("done")
