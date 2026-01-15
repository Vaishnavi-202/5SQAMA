# QAMA Framework Setup & Usage Guide

##  Getting Started (Quick Start)

1. **SSH into Linux Test Machine**
   ```bash
   ssh pooja-ase@15.32.151.154
   ```

2. **Generate SSH Key (first time only)**
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@hp.com"
   cat ~/.ssh/id_rsa.pub
   ```
    Add the public key to GitHub.

3. **Clone Repositories**
   ```bash
   git clone git@github.azc.ext.hp.com:viplove-bisen/MobileApps.git
   ```

4. **SSH into Target Windows Device**
   ```bash
   ssh exec@tgtblrwin07d.psr.rd.hpicorp.net
   ```

5. **Run Smoke Tests**
   ```bash
   python3 -m pytest test_suite_1_settings_about.py -m smoke -v    --mobile-device tgtblrwin07d.psr.rd.hpicorp.net --stack rebrand_pie
   ```

---

##  Overview
This document provides setup instructions, SSH key configuration, GitHub repository integration, pytest execution steps, and HPX Windows app installation guidelines for the **QAMA Framework**.  

It covers:  
- SSH setup & GitHub integration  
- Repository cloning  
- Pytest execution steps  
- System configuration reference  
- HPX app installation & management  

---

## SSH Setup & GitHub Integration

### 1. Connect to Linux Test Machine
```bash
ssh pooja-ase@15.32.148.134
ssh viplov-ase@15.32.148.134
```
- **New machine:** `tgtblrwin08d.psr.rd.hpicorp.net (15.32.151.203)`  
- **Old machine (Pooja):** `tgtblrwin07d.psr.rd.hpicorp.net (15.32.151.189)`

Reconnect if session drops:
```bash
ssh pooja-ase@15.32.148.134
```

---

### 2. Generate SSH Key
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@hp.com"
```

### 3. Display Public Key
```bash
cat ~/.ssh/id_rsa.pub
```

### 4. Add SSH Key to GitHub  
Follow GitHub Docs:  
[🔗 GitHub – Connecting with SSH](https://docs.github.com/en/enterprise-server@3.15/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

---

### 5. Clone Repositories via SSH
```bash
git clone git@github.azc.ext.hp.com:QAMA/android_settings.git
git clone git@github.azc.ext.hp.com:QAMA/JarvisAPI.git
git clone git@github.azc.ext.hp.com:QAMA/SPL.git
git clone git@github.azc.ext.hp.com:QAMA/AMS.git
git clone git@github.azc.ext.hp.com:viplove-bisen/MobileApps.git
```

---

## ⚙️ Pytest Execution & Configuration

### 1. SSH into Target Windows Device
```bash
ssh exec@tgtblrwin06d.psr.rd.hpicorp.net
ssh exec@tgtblrwin07d.psr.rd.hpicorp.net
ssh exec@tgtblrwin08d.psr.rd.hpicorp.net
```

### 2. Run Smoke Tests
```bash
python3 -m pytest test_suite_1_settings_about.py -m smoke -v --mobile-device tgtblrwin07d.psr.rd.hpicorp.net --stack rebrand_pie
```

### 3. Run OTA Tests
```bash
python3 -m pytest test_suite_1_settings_about.py -m ota -v --mobile-device tgtblrwin07d.psr.rd.hpicorp.net --stack rebrand_pie --skip-reinstall --skip-app-string --capture-video
```

### 4. Example `system_config.json`
```json
{
  "executor_url": "tgtblrwin07d.psr.rd.hpicorp.net",
  "executor_port": "11000",
  "printer_power_config": {"type": "manual", "pcs_url": "15.32.150.248", "instance": ""},
  "default_wifi": {"ssid": "sandbox", "passwd": "12345678"},
  "database_info": {"url": "http://hppsrv2.sdg.rd.hpicorp.net:5984/", "user":"service", "password":"service"},
  "image_bank_root": "/work/jay/ImageBank",
  "github_enterprise_token": "<REPLACE_WITH_TOKEN>",
  "github_partner_token": "<REPLACE_WITH_TOKEN>",
  "nexus_int_token": "<REPLACE_WITH_TOKEN>"
}
```

---

##  Remote System Management

### Reboot Windows Machine
```bash
shutdown /r /t 0
```

### Verify & Kill myHP App
```bash
tasklist | findstr /I "myhp"
taskkill /F /IM HP.myHP.exe
```

### Check Installed HPX Package
```powershell
PowerShell -Command "Get-AppxPackage -Name *myhp*"
```

---

##  HPX App Installation (Manual via CMD/PowerShell)

### 1. Navigate to Build Directory
```cmd
cd "C:\Users\exec\Desktop\<BUILD_FOLDER>\HP.HPX_<version>_Test"
```

### 2. List Installer Files
```cmd
dir *.appx
dir *.msix
dir *.appxbundle
dir *.msixbundle
dir *.zip
```

### 3. Extract ZIP (if needed)
```powershell
Expand-Archive -Path "C:\path\to\HP.HPX_x64.zip" -DestinationPath "unzipped"
cd unzipped
dir *.msix
```

### 4. Install App
#### For x64:
```powershell
Get-AppxPackage *myHP* | Remove-AppxPackage
Add-AppxPackage -Path "C:\path\to\HP.HPX_x64.msixbundle"
```

#### For ARM:
```powershell
Add-AppxPackage -Path "C:\path\to\HP.HPX_ARM64.msix"
```

### 5. Install Dependencies (if required)
```powershell
Add-AppxPackage -Path "C:\path\to\dependency.msix"
```

---

##  Key Utility Commands

- Find if HPX app is running:
  ```cmd
  tasklist | findstr /I "myhp"
  ```

- Stop myHP process:
  ```powershell
  Stop-Process -Name "HP.myHP" -Force
  ```

- Launch myHP via protocol:
  ```powershell
  Start-Process myHP:AD2F1837.myHP_v10z8vjag6ke6
  ```

- Remove busy lock file:
  ```powershell
  Remove-Item .\busy.lock -Force
  ```

---

## References
- [GitHub SSH Setup](https://docs.github.com/en/enterprise-server@3.15/authentication/connecting-to-github-with-ssh)  
- [ServiceNow Anyware Client](https://hpitprod.service-now.com/hpAnyware_user)  


Test suite repo

SAF presentation: https://hp-my.sharepoint.com/:p:/p/jiurong_yang/EfGWE8Y8cdBDvyOiZbk3bDgButDwRwaxOcUYaXSk0gBwiw?e=mOkIey

Pytest: https://docs.pytest.org

Pytest area of focus: https://docs.pytest.org/en/6.2.x/fixture.html

https://www.tutorialspoint.com/pytest/pytest_conftest_py.htm

https://docs.pytest.org/en/latest/how-to/usage.html
                      
https://docs.pytest.org/en/6.2.x/assert.html
                                     
https://docs.pytest.org/en/6.2.x/parametrize.html

Python debugger: https://docs.python.org/3/library/pdb.html

NOTE: Learning to use the debugger is very important 

Selenium: https://www.selenium.dev/documentation/en/getting_started/

NOTE: Selenium Grid is also a tool that needs to be understood

Another Tutorial: https://selenium-python.readthedocs.io/getting-started.html

Selenium github: https://github.com/SeleniumHQ/selenium

Python selenium client: https://github.com/SeleniumHQ/selenium/tree/trunk/py

Pep-8 Style Guide: https://www.python.org/dev/peps/pep-0008/

Appium Github: https://github.com/appium/appium

Appium python client github: https://github.com/appium/python-client

Appium tutorial: https://www.youtube.com/watch?v=seolp-8oxHM

Important Appium documentation: 

Desired Capacities: http://appium.io/docs/en/writing-running-appium/caps/

IOS Real device: http://appium.io/docs/en/drivers/ios-xcuitest-real-devices/

Android Real device: http://appium.io/docs/en/drivers/android-uiautomator2/#real-device-setup

Hybrid App testing: http://appium.io/docs/en/writing-running-appium/web/hybrid/

Locator strategies:

Xpath: https://devhints.io/xpath (Only xpath 1.0 should be supported, could change in the future)

Css selector: https://www.freecodecamp.org/news/css-selectors-cheat-sheet/ (Web context only)

Selenium locator guide: https://blog.thedigitalgroup.com/locator-strategies-in-selenium-webdriver

Appium locator guide: http://appium.io/docs/en/commands/element/find-elements/

NOTE: Xpath and css selctor are the most important as they have the functionality of all locator strategies 

Git Tutorial: https://git-scm.com/docs/gittutorial

QAMA FAQ: https://github.azc.ext.hp.com/QAMA/MobileApps/wiki/QAMA-FAQ (Highly recommended)
