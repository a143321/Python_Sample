from chrome_driver import SeleniumChromeAccess
import time
import os

desktop_path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Desktop"
path = desktop_path.replace('/', os.sep)

# Chrome Driverを起動する
driver = SeleniumChromeAccess(False, desktop_path)

# サイトに移動
driver.change_url("https://www.google.com/?hl=ja")

driver.get_image("/html/body/div/div[6]/span/center/div[1]/img")

driver.get_screen_shot(desktop_path, "test.png")

# # フィールドに文字列を入力
# driver.input_textbox_using_XPath("/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input", "test")

# # Enterキーを押す
# driver.input_Enter("/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")

# # 画像ボタンを押す
# driver.click_button_using_XPath("/html/body/div[7]/div[3]/div[4]/div/div/div[1]/div/div/div[1]/div/div[3]/a")

# driver.get_image("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/a[1]/div[1]/img")

# # 5秒スリープする

# # time.sleep(5)

# # driver.close_driver()
