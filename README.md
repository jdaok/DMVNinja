# DMVNinja

When I went to register for an appointment in October, my local CA DMV office was booked out all the way until January 2020. Thankfully, there are always a few people who tend to cancel their appointments a few days in advance! 

This bot will constantly check for appointments at your specified DMV office, and always keep you booked for the latest availible behind-the-wheel exam. It includes several features:

* Set a range of dates where appointments outside of it are ignored
* Will store all potential appointments in dateLog.txt
* When a new closest appointment is found, the previous closest one will be cancelled and the new one will be booked instead
* Saves screenshot of appointment confirmation 'CurrentlyBooked.png' for easy access
* Restart browser and repeat when new earliest appointment is booked

![](demo.gif)
(Booked appointment immeadiately because running for first time)


### Getting Started

Set up and install (Work in progress)

### Requirements

* Python 3+
* Selenium
* urllib3

You may need to grab the corresponding driver for your browser if the provided one is outdated. This bot has only been tested on Chrome on Windows. Simply place it in the same directory.

https://chromedriver.chromium.org/downloads


### Configuration

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

refreshInterval = 15  # in seconds
desiredDateRange = 365  # in days. If you are only looking for an appointment within the next week, set to 7. If you have no preference, set to 365.

```

Keep in mind:
* If the motorcycle test is selected, the bot will assume the related safety tests have been completed
* Make sure the phone number format is 10 digits long!

### CAPTCHA

On every blue "Continue" button on the DMV site, there is a possibility of CAPTCHA. I have not yet found a work around to bypass this yet (it wouldn't be a good implementation of CAPTCHA then!) If CAPTCHA is encountered on any 'Continue' button, 100 seconds will be provided for the user to manually solve it. The audio CAPTCHA option has always been easier and quicker to solve for me.

### Notes

* The DMV website will not be able to locate you in the system if the information in the config file is not accurate
* On first run, an appointment will be booked assuming you don't have one booked already.
* The DMV servers will sometimes give you a "Webpage requested not availible" error. The bot will refresh the page until appointments can be viewed again.
* The datelog.txt file is not meant to be interacted with manually.

Good luck on your driving exam!



