"""
LinkedIn Auto Applier
Developed by Aditya Kumar
GitHub: https://github.com/aditya-life/Linkdin_auto_applier
"""


import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from modules.utilities import get_default_temp_profile, make_directories
from config.app_settings import run_in_background, stealth_mode, disable_extensions, safe_mode, file_name, failed_file_name, logs_folder_path, generated_resume_path
from config.screening import default_resume_path
if stealth_mode:
    import undetected_chromedriver as uc
else: 
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    # from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from modules.utilities import find_default_profile_directory, critical_error_log, print_lg
from selenium.common.exceptions import SessionNotCreatedException
import os
import sys
import subprocess
import plistlib
import re

def get_chrome_major_version() -> int | None:
    chrome_path = None
    try:
        from undetected_chromedriver import find_chrome_executable
        chrome_path = find_chrome_executable()
    except Exception:
        pass

    if sys.platform == 'darwin':
        if chrome_path:
            app_path = chrome_path.split('/Contents/MacOS/')[0]
            plist_path = os.path.join(app_path, 'Contents', 'Info.plist')
            if os.path.exists(plist_path):
                try:
                    with open(plist_path, 'rb') as fp:
                        pl = plistlib.load(fp)
                        version = pl.get("CFBundleShortVersionString")
                        if version:
                            return int(version.split('.')[0])
                except Exception:
                    pass
        try:
            path = chrome_path or "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
            out = subprocess.check_output([path, "--version"]).decode("utf-8").strip()
            match = re.search(r"(\d+)\.", out)
            if match:
                return int(match.group(1))
        except Exception:
            pass

    elif sys.platform.startswith('win'):
        try:
            import winreg
            for key_path in [
                r"Software\Google\Chrome\BLBeacon",
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
            ]:
                for hive in (winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE):
                    try:
                        key = winreg.OpenKey(hive, key_path, 0, winreg.KEY_READ)
                        val, _ = winreg.QueryValueEx(key, "version")
                        winreg.CloseKey(key)
                        if val:
                            return int(val.split('.')[0])
                    except Exception:
                        pass
        except Exception:
            pass

        try:
            search_paths = [
                r"C:\Program Files\Google\Chrome\Application",
                r"C:\Program Files (x86)\Google\Chrome\Application",
                os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application")
            ]
            for p in search_paths:
                if os.path.exists(p):
                    for entry in os.listdir(p):
                        if os.path.isdir(os.path.join(p, entry)) and re.match(r'^\d+\.', entry):
                            return int(entry.split('.')[0])
        except Exception:
            pass

    else:
        try:
            path = chrome_path or "google-chrome"
            out = subprocess.check_output([path, "--version"]).decode("utf-8").strip()
            match = re.search(r"(\d+)\.", out)
            if match:
                return int(match.group(1))
        except Exception:
            pass

    return None

def createChromeSession(isRetry: bool = False):
    make_directories([file_name,failed_file_name,logs_folder_path+"/screenshots",default_resume_path,generated_resume_path+"/temp"])
    # Set up WebDriver with Chrome Profile
    options = uc.ChromeOptions() if stealth_mode else Options()
    if run_in_background:   options.add_argument("--headless")
    if disable_extensions:  options.add_argument("--disable-extensions")

    print_lg("IF YOU HAVE MORE THAN 10 TABS OPENED, PLEASE CLOSE OR BOOKMARK THEM! Or it's highly likely that application will just open browser and not do anything!")
    profile_dir = find_default_profile_directory()
    if isRetry:
        print_lg("Will login with a guest profile, browsing history will not be saved in the browser!")
    elif profile_dir and not safe_mode:
        # Remove SingletonLock to prevent profile lock issues on macOS/Linux
        lock_path = os.path.join(profile_dir, "SingletonLock")
        if os.path.islink(lock_path) or os.path.exists(lock_path):
            try:
                os.unlink(lock_path)
                print_lg("Removed leftover Chrome SingletonLock.")
            except Exception:
                pass
        options.add_argument(f"--user-data-dir={profile_dir}")
        options.add_argument("--profile-directory=Default")
    else:
        print_lg("Logging in with a guest profile, Web history will not be saved!")
        options.add_argument(f"--user-data-dir={get_default_temp_profile()}")
    if stealth_mode:
        # try: 
        #     driver = uc.Chrome(driver_executable_path="C:\\Program Files\\Google\\Chrome\\chromedriver-win64\\chromedriver.exe", options=options)
        # except (FileNotFoundError, PermissionError) as e: 
        #     print_lg("(Undetected Mode) Got '{}' when using pre-installed ChromeDriver.".format(type(e).__name__)) 
            print_lg("Downloading Chrome Driver... This may take some time. Undetected mode requires download every run!")
            version_main = get_chrome_major_version()
            if version_main:
                driver = uc.Chrome(options=options, version_main=version_main)
            else:
                driver = uc.Chrome(options=options)
    else: driver = webdriver.Chrome(options=options) #, service=Service(executable_path="C:\\Program Files\\Google\\Chrome\\chromedriver-win64\\chromedriver.exe"))
    try:
        driver.maximize_window()
    except Exception:
        pass
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)
    return options, driver, actions, wait

try:
    options, driver, actions, wait = None, None, None, None
    options, driver, actions, wait = createChromeSession()
except SessionNotCreatedException as e:
    critical_error_log("Failed to create Chrome Session, retrying with guest profile", e)
    options, driver, actions, wait = createChromeSession(True)
except Exception as e:
    msg = 'Seems like Google Chrome is out dated. Update browser and try again! \n\n\nIf issue persists, try Safe Mode. Set, safe_mode = True in config.py \n\nPlease check GitHub discussions/support for solutions https://github.com/aditya-life/Linkdin_auto_applier \n                                   OR \nReach out in discord (  )'
    if isinstance(e,TimeoutError): msg = "Couldn't download Chrome-driver. Set stealth_mode = False in config!"
    print_lg(msg)
    critical_error_log("In Opening Chrome", e)
    from pyautogui import alert
    alert(msg, "Error in opening chrome")
    try: driver.quit()
    except NameError: exit()
    
