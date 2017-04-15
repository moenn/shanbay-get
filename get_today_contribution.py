import time,os,sys
import re
import json
import requests
import pickle
from bs4 import BeautifulSoup

def get_team_data():
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
	cookie = '_ga=GA1.2.1436192237.1490626408; sessionid=".eJyrVopPLC3JiC8tTi2KT0pMzk7NS1GyUkrOz83Nz9MDS0FFi_VccxMzc3zy0zPznKAKdZB1ZwI1GhoaGpkaGBvUAgC3sB9d:1cyHWp:hOiSyosmYEc05QDzE_ZpARxXDQs"; auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImppYW5nbWVuZ3NoZW5nIiwiZGV2aWNlIjowLCJpc19zdGFmZiI6ZmFsc2UsImlkIjoxMTEyNTAzMCwiZXhwIjoxNDkzMDkxOTQyfQ.4Gj-7WIjhHBTUA5b2__xTpBxheK3CF4IUuw4Ju7_CEQ; __utmt=1; csrftoken=aPzCTxxfXOGkbrxobkzY9MGo4qX9mIIZ; __utma=183787513.1436192237.1490626408.1491998164.1492227939.28; __utmb=183787513.7.10.1492227939; __utmc=183787513; __utmz=183787513.1491911352.24.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); userid=11125030'

	headers = {
	'Accept':'*/*',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6,en;q=0.4,ja;q=0.2',
	'Connection':'keep-alive',
	'Content-type':'application/json;charset=UTF-8',
	'Cookie':cookie,
	'Host':'www.shanbay.com',
	'Origin':'https://www.shanbay.com',
	'Referer':'https://www.shanbay.com/team/members/',
	'User-Agent':user_agent,
	'X-CSRFToken':'aPzCTxxfXOGkbrxobkzY9MGo4qX9mIIZ',
	}
	urls = []
	num = range(1,47)
	for i in num:
		urls.append('https://www.shanbay.com/team/members/?page='+str(i)+'#p1')
	
	nickname = []
	user_id = []
	points = []
	session = requests.Session()
	
	for url in urls:
		try:
			page_source = session.post(url,headers=headers,timeout=1).text
		except:
			print('连接%s失败!'%url)
			sys.exit(0)

		soup = BeautifulSoup(page_source,'lxml')

		#获取昵称，ID
		user_tags = soup.find_all('a',{'class':'nickname'})
		for user in user_tags:
			nickname.append(str(user.string))
			user_id.append(int(re.findall(r'\d+',user.get('href'))[0]))
		#获取贡献值
		point_tags = soup.find_all('td',{'class':'points'})
		for point in point_tags:
			points.append(str(point.string))

	#组合数据,最后返回一个 dict
	nick_points = [list(n) for n in zip(nickname,points)]
	team_data = dict(zip(user_id,nick_points))
	return team_data

if __name__ == '__main__':
	team_data = get_team_data()
	directory = 'shanbay_contribution2017'
	if not os.path.exists(directory):
		os.makedirs(directory)
	with open('shanbay_contribution2017\\'+time.strftime('%Y%m%d')+'.pkl','wb') as f:
		pickle.dump(team_data,f,pickle.HIGHEST_PROTOCOL)

