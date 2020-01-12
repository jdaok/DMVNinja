from datetime import datetime
# Config File

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
refreshInterval = 45  # in seconds

#Specify dates to exclude from appointment search
earliestDate = datetime(1954, 1, 1).date() #formatted year, month, day. No preference => set to = date.today()
latestDate = datetime(9999, 12, 31).date() #No preference => set to = datetime(9999, 12, 31).date()
