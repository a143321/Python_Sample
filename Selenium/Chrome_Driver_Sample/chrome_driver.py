from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select    # Selectタグが扱えるエレメントに変化させる為の関数を呼び出す
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import pyautogui

MAX_WAIT_TIME_SEC = 60

class SeleniumChromeAccess():

    def __init__(self, headless_setting : bool = False, download_dir : str = None):
        # headless_setting : ヘッドレスモード有無
        self.headless_setting = headless_setting

        # ファイルダウンロードディレクトリ指定
        self.download_dir = download_dir

        # chrome driver element : 
        self.driver = self.get_web_driver()

    def get_web_driver(self):

        CHROME_DRIVER_PATH = "chromedriver.exe"
        options = Options()

        if not (self.download_dir == None or self.download_dir == ""):
            options.add_experimental_option("prefs", {
            "download.default_directory" : self.download_dir,
            "profile.default_content_setting_values.automatic_downloads": 2,
            })


        if self.headless_setting:
            # ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
            options.add_argument('--headless')

        return webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)

    def change_url(self, url_path):
        self.driver.get(url_path)


    # 要素を取得する関数
    def get_element(self, element_XPath : str):
        
        element = WebDriverWait(self.driver, MAX_WAIT_TIME_SEC).until(
            EC.presence_of_element_located((By.XPATH, element_XPath))
        )
        return element
    
    
    # XPathを用いて、ボタンをクリックする
    def click_button_using_XPath(self, element_XPath : str):
        
        element = self.get_element(element_XPath)

        element.click()

        return element


    # XPathを用いて、テキストボックスに文字列を入力する
    def input_textbox_using_XPath(self, element_XPath : str, send_code : str):
        
        element = self.get_element(element_XPath)
        
        # 検索テキストボックスをクリアする
        for item in range(0,100) :
            element.send_keys(Keys.BACK_SPACE)
                                    
        element.send_keys(send_code)
        
        return element


    def input_Enter(self, element_XPath : str):

        element = self.get_element(element_XPath)

        element.send_keys(Keys.ENTER)


    # 要素のテキスト文を取得する関数
    def get_element_text_using_XPath(self, element_XPath : str) -> str:
        return self.get_element(element_XPath).text


    # 右クリックメニューを開いて画像を保存する
    # 注意 : 本処理中では、別画面をアクティブにしないでください。「pyautogui」のキー入力が失敗します
    def get_image(self, element_XPath : str):
        element = self.get_element(element_XPath)   
        ActionChains(self.driver).context_click(element).perform()
        
        # ダイアログ画面に対してはActionChainsのsendkeyが及ばないのでpyautoguiを利用
        time.sleep(3)                    # ファイル保存ダイアログ表示待ち時間
        pyautogui.press('v')             # 現在のアクティブ画面で、「v」キーを入力するため、自動化処理中に別画面をアクティブにするとそちらに「v」キーを入力します
        time.sleep(3)                    # ファイル保存ダイアログ表示待ち時間
        pyautogui.press('enter')


    # 要素を取得する関数
    def get_element_by_class_name(self, path : str):
        
        element = WebDriverWait(self.driver, MAX_WAIT_TIME_SEC).until(
            EC.presence_of_element_located((By.CLASS_NAME, path))
        )
        return element


    # class名を用いて、ボタンをクリックする
    def click_button_using_class_name(self, element_class_name : str):
        
        element = self.get_element_by_class_name(element_class_name)
        
        element.click()

        return element


    # class名を用いて、テキストボックスに文字列を入力する
    def input_textbox_using_class_name(self, element_class_name : str, send_code : str):
        
        element = self.get_element_by_class_name(element_class_name)
        
        # 検索テキストボックスをクリアする
        for item in range(0,100) :
            element.send_keys(Keys.BACK_SPACE)
                                    
        element.send_keys(send_code)


    # ID名を用いて、ドロップダウンリストから選択する
    def select_dropdown_list_using_id(self, element_id : str, type_name : str):
        
        element = WebDriverWait(self.driver, MAX_WAIT_TIME_SEC).until(
            EC.presence_of_element_located((By.ID, element_id))
        )
        
        element.click()

        # 取得したエレメントをSelectタグに対応したエレメントに変化させる
        type_element = Select(element)

        # 選択したいvalueを指定する
        type_element.select_by_value(type_name)
        
        element.click()


    # ID名を用いて、テキストボックスに文字列を入力する
    def input_textbox_using_id(self, element_id : str, send_code : str):
        
        element = WebDriverWait(self.driver, MAX_WAIT_TIME_SEC).until(
            EC.presence_of_element_located((By.ID, element_id))
        )
        
        # 検索テキストボックスをクリアする
        for item in range(0,100) :
            element.send_keys(Keys.BACK_SPACE)
        
        element.send_keys(send_code)


    # HTML name属性を用いて、ボタンをクリックする
    def click_button_using_name_attribute(self, element_name_attribute : str):
        
        element = WebDriverWait(self.driver, MAX_WAIT_TIME_SEC).until(
            EC.presence_of_element_located((By.NAME, element_name_attribute))
        )
        
        element.click()


    # キャプチャを取得する
    def get_screen_shot(self, folder_path, file_path):

        folder_path = folder_path.replace(os.path.sep, '/')
        
        os.makedirs(folder_path, exist_ok=True)

        full_path = os.path.join(folder_path, file_path)

        self.driver.save_screenshot(full_path)

    def close_driver(self):
        self.driver.quit()
            




