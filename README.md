# shanbay-get
与扇贝网相关的小爬虫    

依赖的第三方库:  
[selenium](http://www.seleniumhq.org/)  
[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)  
[phantomJS](http://phantomjs.org/)  

### get_today_article_links.py  
用来获取扇贝今日更新的所有文章，一般有 15 篇左右。链接存放到 *get_today_article_links.py* 所在目录下的  *%Y%m%d.txt* 文件中。  
需要更改这行代码 >>  *driver = webdriver.PhantomJS(executable_path=r'你的phantomJS可执行文件所在路径')*

### get_notes_links.py      
获取今日更新文章上的所有笔记。  
爬取规则有遗漏，需要更改...
