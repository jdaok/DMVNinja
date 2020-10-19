# DMVNinja <img align="right" width="120" height="120" src="https://i.imgur.com/PxWPHrY.png">

When I went to register for an appointment in October, my local CA DMV office was booked out all the way until January 2020. Thankfully, there are always a few people who tend to cancel their appointments a few days in advance.

This bot will constantly check for appointments at your specified DMV office, and always keep you booked for the latest availible behind-the-wheel exam. It includes several features:

* Will store all potential appointments in dateLog.txt
* Set a range of dates where appointments outside of it are ignored
* When a new closest appointment is found, the previous closest one will be cancelled and the new one will be booked instead
* Saves screenshot of appointment confirmation 'CurrentlyBooked.png' for easy access
* Restart browser and repeat when new earliest appointment is booked

![](demo.gif)



### Getting Started

Clone the repository.

```
git clone https://github.com/jdaok/DMVNinja.git
```
Download the requirements (you may need to install pip)
```
cd DMVNinja
pip install -r requirements.txt
```

* Python 3+
* Selenium
* urllib3

You might have to grab the corresponding driver for your browser and OS if the provided one doesn't work. This bot has only been tested on Chrome & Firefox on Windows.

https://chromedriver.chromium.org/downloads (Chrome)
https://github.com/mozilla/geckodriver/releases (Firefox)

Simply place the driver in the project directory.


##### Configuration

Open up the config file and change the values accordingly. 

```
location = 'OAKLAND CLAREMONT'  # Office ID exactly how it appears after selected from dropdown

testType = 'auto'  # 'auto' or 'motor'. 

firstName = "FIRST"
lastName = "LAST"

ID = "Y1234567"

birthMonth = "12"
birthDay = "01"
birthYear = "2001"

phonenum1 = "5101234567"

# //////////////////////

browser = 'Chrome'  # 'Chrome' or 'Firefox'
refreshInterval = 15  # in seconds
desiredDateRange = 365  # in days. If you are only looking for an appointment within the next week, set to 7. If you have no preference, set to 365.
```

Keep in mind:
* If the motorcycle test is selected, the bot will assume the related safety tests have been completed
* Phone number format is 10 digits long

Save, and now you can run the bot.
```
python main.py
```

### Recaptcha

CA DMV recently introduced Google Recaptcha. This bot does not yet include a work around to bypass this. If Recaptcha is encountered on any 'Continue' button, 100 seconds will be provided for the user to manually solve it. (shown in demo.gif) The audio Recaptcha option has always been easier and quicker to solve for me. If Recaptcha is failed, the bot must be manually restarted.

### Notes

* On first run, an appointment will be booked assuming you don't have one booked already. If you do, either cancel it or add it to a new line in dateLog.txt before ruunning.
* The DMV servers will sometimes give you a "Webpage requested not available" error. The bot will refresh the page until appointments can be viewed again.
* Only used for personal non-commercial purposes


Good luck on your driving exam!



