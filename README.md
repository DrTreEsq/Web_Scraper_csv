# Legal Data scraped from government websites

## The United States Constitution

#### scrapy, xpath, and SQL

###### https://constitutioncenter.org/the-constitution/full-text

###### removing nasa project and exploit spider to change directions with more compatable data
###### https://www.youtube.com/watch?v=s4jtkzHhLzY&t=258s
###### https://github.com/jhnwr/whiskyspider/tree/master

1. TERMINAL - parse in scrapy shell
* pip install scrapy, pip install -r requirements.txt (touch requirements.txt first)
###### ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
* $ scrapy startproject gov
* $ cd gov
* $ scrapy genspider constitution constitutioncenter.org
* $ scrapy shell 
* $ fetch('https://constitutioncenter.org/the-constitution/full-text')
* $ response
###### <200 https://constitutioncenter.org/the-constitution/full-text>
* $ response.url
###### 'https://constitutioncenter.org/the-constitution/full-text'
* $ response.css
###### <bound method TextResponse.css of <200 https://constitutioncenter.org/the-constitution/full-text>>
* $ response.css('article.article_body')
###### get the HTML code from the class name when you inspect the item in browser
######  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' article_body ')]" data='<article class="article_body mb-5">\n<...'>]
* $ response.css('article.article_body').get()
###### set = to var & check length
articles = response.css('article.article_body')
len(articles)
* $ response.css('article.article_body').getall()



2. Python Script - CREATING SCRAPY SPIDER & FOMRAT TO SAVE DATA TO
###### in the spider.py (constitution.py)



3. Saving the parsed data to SQL, or JSON
* $ scrapy crawl constitution
* $ scrapy crawl constitution -0 whisky.sql



OTHER
###### text? - not helpful for this site/data
* $ response.css('div.article::text').get()
* $ response.css('article.article_body').get()
###### # cat > scrapy.py <<EOF




