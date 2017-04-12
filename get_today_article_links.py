from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re



#加载页面
pattern = re.compile(r'\d{4}-\d{2}-\d{2}')  #匹配日期
driver = webdriver.PhantomJS(executable_path=r'C:\Users\jms29\Downloads\phantomjs-2.1.1-windows\bin\phantomjs')#构建无头浏览器，用来解析 Js 记载内容
driver.get('https://www.shanbay.com/read/news/')
time.sleep(5) #显式延时5秒，等待页面完全加载
while True:
	try:
		load_more_btn = driver.find_element_by_class_name('loadNewsBtn')  #"加载更多"按钮
		load_more_btn.click()
		print('load...more...')
	except:
		print('no more hint')
		
		

	try:
		driver.find_element_by_class_name('noMoreHint')	# "没有更多了"按钮。找到后就退出循环
		break
	except:
		print('loading...')
		

#解析出文章链接
soup = BeautifulSoup(driver.page_source,'lxml')
raw_links = []
for tag in soup.find_all('a',attrs={'class':'current'}):
	raw_links.append(tag['href'])

for tag in soup.find_all('a',attrs={'class':'linkContainer'}):
	try:
		#匹配到"xxxx-xx-xx"的日期格式，说明到了昨天的新闻处
		if re.fullmatch(pattern,tag.parent.previous_sibling.span.get_text()):
			break
	except:
		print('未到达昨日新闻处！')
	raw_links.append(tag['href'])

links = [ 'https://www.shanbay.com'+n for n in raw_links]
for n in links:
	print(n)
driver.close()

#存储链接到本地文件
filename = time.strftime('%Y%m%d')+'.text'
with open(filename,'wt') as f:
	for link in links:
		f.write(link+'\n')


