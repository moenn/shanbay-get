import json
from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup
import re,sys,os


article_links = []
filename = time.strftime('%Y%m%d')+'.text'
with open(filename,'rt') as f:
	article_links = f.readlines()
# print(article_links)

def get_notes_ap(article_links):
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
	cookie = '_ga=GA1.2.1436192237.1490626408; sessionid=".eJyrVopPLC3JiC8tTi2KT0pMzk7NS1GyUkrOz83Nz9MDS0FFi_VccxMzc3zy0zPznKAKdZB1ZwI1GhoaGpkaGBvUAgC3sB9d:1cuIEJ:b-qNjcBixv57V34Z61ubimDlSPk"; csrftoken=NemVjHwMde5CxyDZvU3YsdaswhHtoDbh; auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImppYW5nbWVuZ3NoZW5nIiwiZGV2aWNlIjowLCJpc19zdGFmZiI6ZmFsc2UsImlkIjoxMTEyNTAzMCwiZXhwIjoxNDkyNzU0ODc3fQ.DQnH2t1PWTHebIiFLAoM-wVTs2bgTahtj5QjGMOZCKw; __utmt=1; __utma=183787513.1436192237.1490626408.1491894239.1491898188.22; __utmb=183787513.16.10.1491898188; __utmc=183787513; __utmz=183787513.1491044137.9.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; userid=11125030'
	referer = ''
	headers = {
		'Accept':'*/*',
		'Accept-Encoding':'gzip, deflate, sdch, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6,en;q=0.4,ja;q=0.2',
		'Connection':'keep-alive',
		'Cookie':cookie,
		'Host':'www.shanbay.com',
		'Referer':referer,
		'User-Agent':user_agent,
		'X-Requested-With':'XMLHttpRequest',
	}
	notes_ap = {}
	for link in article_links:
		
		#合成每篇文章的获取notes 的 url
		article_number = "".join(re.findall('[0-9]+',link))
		# print(article_number)
		url = 'https://www.shanbay.com/api/v1/read/article_content/'+article_number+'/?_='+str(int(round(time.time()*1000)))
		referer = 'https://www.shanbay.com/read/article/'+article_number+'/'
		#访问notes的url
		res = requests.get(url,headers=headers)
		json_text = json.loads(res.text)
		# print(json_text)
		notes_ap[article_number] = list(json_text['data']['notes'].keys())


	return notes_ap

	# print(notes_ap)
notes_ap = {}		
notes_ap.update(get_notes_ap(article_links))
for key,value in notes_ap.items():
	print(key,value)



# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
# cookie = '_ga=GA1.2.1436192237.1490626408; sessionid=".eJyrVopPLC3JiC8tTi2KT0pMzk7NS1GyUkrOz83Nz9MDS0FFi_VccxMzc3zy0zPznKAKdZB1ZwI1GhoaGpkaGBvUAgC3sB9d:1cuIEJ:b-qNjcBixv57V34Z61ubimDlSPk"; csrftoken=NemVjHwMde5CxyDZvU3YsdaswhHtoDbh; auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImppYW5nbWVuZ3NoZW5nIiwiZGV2aWNlIjowLCJpc19zdGFmZiI6ZmFsc2UsImlkIjoxMTEyNTAzMCwiZXhwIjoxNDkyNjY0NjA4fQ.BWdGR1us3c_k3uQ2rrNoAgjmJRhWZvOHwYtw6BYZxFA; __utmt=1; __utma=183787513.1436192237.1490626408.1491625934.1491800608.16; __utmb=183787513.4.10.1491800608; __utmc=183787513; __utmz=183787513.1491044137.9.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; userid=11125030'
# referer = ''
# headers = {
# 	'Accept':'application/json, text/javascript, */*; q=0.01',
# 	'Accept-Encoding':'gzip, deflate, sdch, br',
# 	'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6,en;q=0.4,ja;q=0.2',
# 	'Connection':'keep-alive',
# 	'Cookie':cookie,
# 	'Host':'www.shanbay.com',
# 	'Referer':referer,
# 	'User-Agent':user_agent,
# 	'X-Requested-With':'XMLHttpRequest',
# }


# translog = {}
# for key,value in notes_ap.items():

# 	for ap in value:
# 		url = 'https://www.shanbay.com/api/v1/read/note/?para_id='+ap+'&ipp=3&page=1&_='+str(int(round(time.time()*1000)))
# 		referer = 'https://www.shanbay.com/read/article/'+key+'/'
# 		res = requests.get(url,headers=headers)
# 		raw_json_text = json.loads(res.text)
		
# 		raw_data = []
# 		raw_data.extend(raw_json_text['data']['notes'])
# 		for x in raw_data:
# 			user_id = x['author']['id']
# 			if user_id not in translog.keys():
			
# 				translog[user_id] = {
# 					'username':None,
# 					'nickname':None,  
# 					'nickname':None,  
# 					'num_comments':None, #翻译条数 
# 					'contents':None, #翻译内容
# 					'total_words':None,#总字数
# 					'num_vote':None,#获赞总数
# 				}

# 				translog[user_id]['username'] = x['author']['username']
# 				translog[user_id]['nickname'] = x['author']['username']
# 				translog[user_id]['num_comments'] = 1
# 				translog[user_id]['contents'] = []
# 				translog[user_id]['contents'].append(x['content'])
# 				translog[user_id]['total_words'] = 0
# 				for n in translog[user_id]['contents']:
# 					translog[user_id]['total_words'] += len(n)
# 				translog[user_id]['num_vote'] = x['num_vote']

# 			else:
# 				translog[user_id]['num_comments'] += 1
# 				translog[user_id]['contents'].append(x['content'])
# 				translog[user_id]['total_words'] = 0
# 				for n in translog[user_id]['contents']:
# 					translog[user_id]['total_words'] += len(n)
# 				translog[user_id]['num_vote'] += x['num_vote']

# search_list = {
# 	11125030:'姜萌生',
# 	52563430:'小蜜蜂',
# 	17437957:'涔涔',
# 	36969523:'琪琪',

# }



# for userid,log in translog.items():
# 	print(userid,'\n',log)

# for userid in search_list.keys():
# 	if userid in translog.keys():
# 		print("用户:%s,翻译段落:%s,总字数:%s,获赞数:%s"%(search_list[userid],translog[userid]['num_comments'],translog[userid]['total_words'],translog[userid]['num_vote']))

  




