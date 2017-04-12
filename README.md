# shanbay-get
与扇贝网相关的小爬虫  

get_today_article_links.py  
用来获取扇贝的今日更新的所有文章的链接，一般有 15 篇左右。  
链接存放到 *get_today_article_links.py* 所在目录下的  *%Y%m%d.txt* 文件中。  

需要更改这行代码 >>  *driver = webdriver.PhantomJS(executable_path=r'你的phantomJS可执行文件所在路径')*

依赖的第三方库:  
[selenium](http://www.seleniumhq.org/)  
[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)  
[phantomJS](http://phantomjs.org/)  


get_notes_links.py      
用来获取今天所有文章的所有段落的 AP 标记值。返回的是一个字典 *{'article_num':'para_ap'}*        
爬取规则有遗漏，需要更改...
