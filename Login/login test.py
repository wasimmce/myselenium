from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

dynamicbrowser='Chrome'

if dynamicbrowser=='Chrome':
    driver=webdriver.Chrome()
elif dynamicbrowser=='Firefox':
    driver=webdriver.Firefox()
elif dynamicbrowser=='Edge':
    driver=webdriver.Edge()
elif dynamicbrowser=='Ie':
    driver=webdriver.Ie()

driver.implicitly_wait(10)

def ClickAndWait(xpathTarget,xpathExpWait,maxtime):
    for i in range(0,maxtime):
        driver.find_element(By.XPATH,xpathTarget).click()
        if(isElementPresent(xpathExpWait) and driver.find_element(By.XPATH,xpathExpWait).is_displayed()):
            return
        else:
            time.sleep(1)

def isElementPresent(xpathExp):
    s=driver.find_elements(By.XPATH,xpathExp)
    if len(s)==0:
        return False
    else:
        return True
    assert False

def deleteProtfolio():
    driver.find_element(By.ID,"deletePortfolio").click()
    driver.switch_to.alert.accept()
    driver.switch_to.default_content()

def selectDate(d):
    currentdate=datetime.now()
    print(currentdate.strftime("%d/%m/%Y"))
    dt=datetime.strptime(d,"%d/%m/%Y")
    Year=dt.year
    Day=dt.day
    month=dt.strftime("%B")
    print(Year)
    print(Day)
    print(month)
    desiredMonthYear=str(month)+" "+str(Year)
    print(desiredMonthYear)

    while True:
        displayMonthYear=driver.find_element(By.CSS_SELECTOR,'.dpTitleText').text
        if(desiredMonthYear==displayMonthYear):
            driver.find_element('xpath','//td[text()='+str(Day)+']').click()
            break
        else:
            if(dt > currentdate):
                driver.find_element('xpath','//*[@id="datepicker"]/table/tbody/tr[1]/td[4]/button').click()
            elif(dt < currentdate):
                driver.find_element('xpath','//*[@id="datepicker"]/table/tbody/tr[1]/td[2]/button').click()

def getRowwithCellData(Data):
    rows=driver.find_elements('xpath','//table[@class="dataTable sortable"]/tbody/tr')
    for i in range(0,len(rows)):
        row=rows[i]

        cells=row.find_elements(By.TAG_NAME,'td')
        for j in range(0,len(cells)):
            cell=cells[j]
            if cell.text in Data:
                return i+1

    return -1


def BuysellStock(a):
    driver.find_element('name','Buy / Sell').click()
    driver.find_element('id', 'buySellCalendar').click()
    driver.find_element('id','buysellqty').send_keys('500')
    driver.find_element('id', 'buysellprice').send_keys('100')
    currentdate=datetime.now()
    print(currentdate.strftime("%d/%m/%Y"))
    dt=datetime.strptime(a,"%d/%m/%Y")
    Year=dt.year
    Day=dt.day
    month=dt.strftime("%B")
    print(Year)
    print(Day)
    print(month)
    desiredMonthYear=str(month)+" "+str(Year)
    print(desiredMonthYear)

    while True:
        displayMonthYear=driver.find_element(By.CSS_SELECTOR,'.dpTitleText').text
        if(desiredMonthYear==displayMonthYear):
            driver.find_element('xpath','//td[text()='+str(Day)+']').click()
            break
        else:
            if(dt > currentdate):
                driver.find_element('xpath','//*[@id="datepicker"]/table/tbody/tr[1]/td[4]/button').click()
            elif(dt < currentdate):
                driver.find_element('xpath','//*[@id="datepicker"]/table/tbody/tr[1]/td[2]/button').click()


def TransactionHistory():
    # time.sleep(10)
    driver.find_element('xpath', '//*[@id="equityid15510001"]').click()
    # time.sleep(5)
    driver.find_element('name','Transaction History').click()
    time.sleep(10)
    shares=driver.find_elements('xpath','//div[@id="transcations"]/table/tbody/tr/td[3]')
    prices=driver.find_elements('xpath','//div[@id="transcations"]/table/tbody/tr/td[4]')

    totalShares=0
    totalAmount=0
    for i in range(0,len(prices)):
        share=shares[i].text
        price=prices[i].text
        print(share)
        print(price)
        totalShares=int(share)+totalShares
        totalAmount=(int(price)*int(share))+totalAmount

    print(totalAmount)
    print(totalShares)
    avg_price=totalAmount/totalShares
    print(avg_price)


driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.rediff.com/")
driver.find_element('xpath',"//div[@class='cell topicons']/a[2]").click()
driver.find_element('xpath',"//span[@id='signin_info']/a").click()
driver.find_element('id',"useremail").send_keys("wasimmce")
driver.find_element('id',"userpass").send_keys("Rediff1234!")
driver.find_element('id',"loginsubmit").click()
ClickAndWait("//*[@id='createPortfolio']","//*[@id='createPortfolioButton']",10)
# driver.find_element('id',"createPortfolio").click()
driver.find_element('id',"create").clear()
driver.find_element('id',"create").send_keys("11")
driver.find_element('id',"createPortfolioButton").click()
# ClickAndWait("//*[@id='createPortfolioButton']","//*[@id='addStock']",10)
# ClickAndWait("//*[@id='addStock']","//*[@id='addstockname']",10)
e=driver.find_element(By.ID,"portfolioid")
driver.set_page_load_timeout(10)
select=Select(e)
a=select.first_selected_option
print(a.text)
time.sleep(5)
deleteProtfolio()

# wait=WebDriverWait(driver,10)
# element=wait.until(EC.visibility_of_element_located((By.ID,"addStock")))
time.sleep(10)
driver.find_element('id',"addStock").click()
# time.sleep(10)
driver.find_element('id',"addstockname").send_keys("Tata")
addstock=driver.find_elements('xpath',"//div[@id='ajax_listOfOptions']/div")

name='Tata Steel Ltd.'
for i in addstock:
    if(i.text==name):
        i.click()

#date
driver.find_element('id','stockPurchaseDate').click()
selectDate("03/03/2022")
driver.find_element('id','addstockqty').send_keys('100')
driver.find_element('id','addstockprice').send_keys('500')
driver.find_element('id','addStockButton').click()
ir=getRowwithCellData("Tata Steel Ltd.")
print(ir)
wait=WebDriverWait(driver,20)
element=wait.until(EC.visibility_of_element_located(('xpath','//table[@class="dataTable sortable"]/tbody/tr/td/input')))
time.sleep(20)
driver.find_element('xpath','//*[@id="equityid15510001"]').click()
BuysellStock("12/05/2022")
driver.find_element('id','buySellStockButton').click()
time.sleep(20)
TransactionHistory()
