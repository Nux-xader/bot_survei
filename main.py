import random, sys, os
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

firefox_options = Options()
firefox_options.add_argument("--headless")

# Set driver
def setDriver(openBrowser=True):
	path = "/home/nux/Project/Python/scrapOlshop/autoCheck/geckodriver"
	if sys.platform == "win32":
		path = "geckodriver.exe"

	if openBrowser:
		browser = webdriver.Firefox(executable_path=path)
	else:
		browser = webdriver.Firefox(executable_path=path, firefox_options=firefox_options)
	return browser

def clr():
	if sys.platform == "win32":
		os.system('cls')
	else:
		os.system('clear')

def randDigit():
	result = ''
	for i in range(random.randint(0, 4)):
		result+=str(random.randint(0, 9))
	return result

def randChoice(driver, amount):
	for i in range(2, amount+2):
		choice = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div['+str(i)+']/div/div/div[2]/div/span/div/label['+str(random.randint(1, 3))+']/div[2]/div/div/div[3]/div')
		choice.click()
	sleep(1)


def main(driver, name, gender, domisili, wa, npwp=1):
	driver.get('https://docs.google.com/forms/d/e/1FAIpQLSf21KTlVQHpH0h6ZsXj76MRcHtHdBZzLQrmJdZ01iMPR_TLJQ/viewform')
	sleep(4)
	a = '/html/body/div/div[2]/form/div[2]/div/div[2]/div/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
	if npwp:
		a = '/html/body/div/div[2]/form/div[2]/div/div[2]/div/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
	npwp = driver.find_element_by_xpath(a)
	npwp.click()

	# Next
	accept = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span')
	accept.click()
	sleep(4)


	email = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
	email.send_keys(name+randDigit()+'@gmail.com')

	gend = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
	if gender.lower() == 'p':
		gend = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
	gender = driver.find_element_by_xpath(gend)
	gender.click()

	old = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div['+str(random.randint(1, 2))+']/label/div/div[1]/div/div[3]/div')
	old.click()

	clickSchool = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]')
	clickSchool.click()
	sleep(1)

	school = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div['+str(random.randint(6, 8))+']/span')
	school.click()
	sleep(1)

	dom = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
	dom.send_keys(domisili)

	phone = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
	phone.send_keys(wa)
	# Next
	driver.execute_script("window.scrollTo(0, 6000)")
	sleep(1)
	accept = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div[2]/span/span')
	accept.click()


	sleep(4)
	randChoice(driver=driver , amount=6)
	# Next
	driver.execute_script("window.scrollTo(0, 6000)")
	sleep(1)
	accept = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div[2]/span/span')
	accept.click()


	sleep(4)
	randChoice(driver=driver, amount=3)
	# Next
	driver.execute_script("window.scrollTo(0, 6000)")
	sleep(1)
	accept = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div[2]/span/span')
	accept.click()

	sleep(4)
	randChoice(driver=driver, amount=7)
	driver.execute_script("window.scrollTo(0, 6000)")
	sleep(1)
	accept = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div[2]/span/span')
	accept.click()

	sleep(4)
	driver.quit()


phone = """853-6036-3600
855-2443-9796
856-0163-8705
857-4398-0143
857-4734-6466
857-9280-5558
858-6622-3185
859-6028-9135
877-2211-9024
877-4227-2941
878-1206-7970
878-1401-5119
878-5200-7627
878-6401-7333
878-8884-1788
882-1819-6473
882-9106-6596
895-2386-9896
896-5356-6916
896-6205-6602
896-9616-7457
897-2268-998""".replace('-', '').split('\n')
name = """Adelia
Abdul Malik
Rahmatiani
Ady Alana
Raafi
Husnayan
Pratista
Abshari Nuria
Abdul Hanan
Khalilur Rahman
Iqbal Gafur
Intan
Farid Ahda Muttaqin
Rahmatiani
Raasyid
Irma Damayanti
Husamuddin
Khazinun Katsiran
Fitiya
Afra Naila
Abdul Majid
Faranisa
Damayanti
Martini
Yeni Irawati
Irawati
Audie Maesa
Adriana Faranisa
Elvarette
Irma
Adrien Saralee
Fariz Dzakir
Inamul Wafi
Azzahra
Naila
Khathir
Intan Martini
Angela
Fannan Sayyidi
Fredella
Abdul Mannan
Irbad Abdul
Husni""".split('\n')
data = [['p'], ['l'], ['p'], ['l'], ['l'], ['l'], ['p'], ['l'], ['l'], ['l'],
		['l'], ['p'], ['l'], ['p'], ['l'], ['p'], ['l'], ['l'], ['p'], ['p'],
		['l'], ['p'], ['p'], ['p'], ['p'], ['p'], ['p'], ['p'], ['p'], ['p'],
		['l'], ['l'], ['l'], ['p'], ['p'], ['l'], ['p'], ['p'], ['l'], ['p'],
		['l'] , ['l'], ['l']]
domisili = """1. Jakarta Pusat (DKI Jakarta)
2. Teluk Bintuni (Papua Barat)
3. Kediri (Jawa Timur)
4. Kepulauan Anambas (Kepulauan Riau)
5. Mimika (Papua)
6. Bontang (Kalimantan Timur)
7. Kutai Timur (Kalimantan Timur)
8. Natuna (Kepulauan Riau)
9. Cilegon (Banten)
10. Kutai Kartanegara (Kalimantan Timur)
11. Jakarta Utara (DKI Jakarta)
12. Jakarta Selatan (DKI Jakarta)
13. Tana Tidung (Kalimantan Utara)
14. Bengkalis (Kepulauan Riau)
15. Kepulauan Seribu (DKI Jakarta)
16. Surabaya (Jawa Timur)
17. Paser (Kalimantan Timur)
18. Siak (Riau)
19. Balikpapan (Kalimantan Timur)
20. Berau (Kalimantan Timur)""".split('\n')
dom = []
for i in domisili:
	dom.append(i.split('. ')[1].split(' (')[0])
dataBase = []
for x, y in zip(data, name):
	x.append(y.lower().replace(' ', ''))
	dataBase.append(x)
data = []
for i in dataBase:
	i.append(dom[random.randint(0,19)])
	data.append(i)
dataBase = []
for x, y in zip(data, phone):
	x.append("08"+y)
	dataBase.append(x)
clr()
for num, i in enumerate(dataBase):
	# name = str(input("Nama = "))
	# gender = str(input("Gender = "))
	# domisili = str(input("Domisili = "))
	# wa = str(input("wa = "))
	gender, name, domisili, wa = i[0], i[1], i[2], i[3]
	driver = setDriver()
	main(driver=driver, name=name, gender=gender, domisili=domisili, wa=wa)
	print(num+1)
	sleep(random.randint(3,7))