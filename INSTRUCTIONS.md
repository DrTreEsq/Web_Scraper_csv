# Build a Web Scraping Tool
Specific instructions for the project

In this project, the goal is for you to build a web scraping tool from scratch. This web scraper should, extract specific information, transform the data into a CSV file and then save it to disc.

For this project you will use Scrapy, a powerful web scraping tool in Python.

Your Tasks
1. Create a new Github repository with all the necessary files for Scrapy to work. 
###### https://scrapy.org
2. Select a target website where you can capture distinct data
3. Save your selected data into CSV rows and fields
4. Add a README.md file to your Github project that describes what you did
5. Create a Demo Video and reference it in your GitHub Project.

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



3. Saving the parsed data to SQL, or JSON‼️
* $ scrapy crawl constitution
* $ scrapy crawl constitution -o articles.csv
* $ scrapy crawl constitution -o articles.json

# crawl gets syntax error - SyntaxError: invalid syntax - fixed

OTHER
###### text? - not helpful for this site/data
* $ response.css('div.article::text').get()
* $ response.css('article.article_body').get()
###### # cat > scrapy.py <<EOF


Sample Deliverables
* Demo video. Here is an example video you can refer to that explains Python decorators

###### https://www.youtube.com/watch?v=rSRT_eRTBIM


* GitHub repo. Here is a Github repo you can reference with a Scrapy project.


###### https://github.com/alfredodeza/scraping-demo

# scraping-demo
Demo for scraping using scrapy, parsing a real website, extracting key information that is not available through an API and using SQL to query it later.

Install _requirements.txt_ in a virtual environment

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Get started with scrapy: https://docs.scrapy.org/en/latest/intro/tutorial.html

```
$ scrapy startproject cve
$ scrapy genspider exploit cve.mitre.org
```

Use XPath or the CSS module to find nodes. XPath is a query language for finding and selecting nodes in an XML document that is also useful for HTML.

```
$ scrapy shell http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html
>>> response.url
'http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html'
>>> response.css
<bound method TextResponse.css of <200 http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html>>
>>> response.xpath('//table')
[<Selector xpath='//table' data='<table style="width:100%;border-colla...'>, <Selector xpath='//table' data='<table style="text-align:right"><tr><...'>, <Selector xpath='//table' data='<table cellpadding="2" cellspacing="2...'>, <Selector xpath='//table' data='<table cellpadding="2" cellspacing="2...'>, <Selector xpath='//table' data='<table>\n                <tr>\n        ...'>]
>>> len(response.xpath('//table'))
5
>>> response.css('table')
[<Selector xpath='descendant-or-self::table' data='<table style="width:100%;border-colla...'>, <Selector xpath='descendant-or-self::table' data='<table style="text-align:right"><tr><...'>, <Selector xpath='descendant-or-self::table' data='<table cellpadding="2" cellspacing="2...'>, <Selector xpath='descendant-or-self::table' data='<table cellpadding="2" cellspacing="2...'>, <Selector xpath='descendant-or-self::table' data='<table>\n                <tr>\n        ...'>]
>>> len(response.css('table'))
5
```

Find the biggest table:

```
>>> for table in response.css('table'):
...     if len(table.xpath('tr')) >10:
...         print(table)
```

Or:

```
>>> len(response.css('table'))
5
>>> len(response.xpath('//table'))
5
>>> len(response.css('table')[0].xpath('tr'))
3
>>> len(response.css('table')[1].xpath('tr'))
3
>>> len(response.css('table')[2].xpath('tr'))
4
>>> len(response.css('table')[3].xpath('tr'))
10839

```

None of these tables have any method of identificaion so you are forced to look into each table to see if there are enough elements that can signal the table we are interested in, the one that holds several thousand rows.

```
>>> row = data[0]
>>> print(row.getall()[0])
<tr>
<td>EXPLOIT-DB:10102</td>
<td> <a href="http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-4186">CVE-2009-4186</a>
</td>
</tr>
```

Get the value of href using xpath:

```
>>> row.xpath('td//a/@href')[0].extract()
'http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-4186'
```

There is no need for the href though because all CVEs have the same URL construction.

## Local parsing
The first few iterations of parsing an online document will take some effort. Instead of using several requests that get data from a website, download the data _once_ and parse locally. This method has a few positive aspects to it:

- Reduces online requests to 0 for retrying failed attempts
- Increases speed by an order of magnitude since the HTML is already on disk
- Easier to debug or test alternative (or modified) HTML parsing

## CI/CD
Once local parsing is done and you aresatisfied with a few succesful passes, then it is time to start thinking about automation. Any pipeline or pipeline-like service should work, as long as you are clear about the steps to set the project up. CI/CD jobs require like this project need to clearly define its inputs and outputs.

In this case, the input is the HTML, which has to be processed. But the output for the demo is a remote PostgreSQL database in Azure. This creates a pain point that must be resolved: depending on the platform where the job executes, a plugin or helper will be required to move parsed data into the database.

If this job existed in an Azure pipeline job, it would probably be straightforward to connect to the Azure PostgreSQL DB. But this job is running on Github Actions and pushing data to Azure. An Azure Github Action and Azure PostgreSQL action is required to authenticate and push SQL statements over. Further, firewall changes must happen to allow connectivity between Github and Azure.

Azure PostgreSQL Action: https://github.com/azure/postgresql

Go through the instructions. After creating a PostgreSQL instance, install azure-cli locally and generate the secrets needed for authentication:

```
 az ad sp create-for-rbac --name {server-name} --role contributor \
                          --scopes /subscriptions/{subscription-id}/resourceGroups/{resource-group} \
                          --sdk-auth

# Replace {subscription-id}, {resource-group} and {server-name} with the subscription, resource group and name of the Azure PostgreSQL server

# The command should output a JSON object similar to this:

{
  "clientId": "<GUID>",
  "clientSecret": "<GUID>",
  "subscriptionId": "<GUID>",
  "tenantId": "<GUID>",
  (...)
}
```

Follow the rest of the instruction on the Action documentation: https://github.com/azure/postgresql#configure-github-secrets-with-azure-credentials-and-postgresql-connection-strings


### Generating SQL
The Github Action can execute a SQL file and run it against the remote database. For this, the scraper builds a SQL file that is placed in the `sql_files` directory which the workflow file (_main.yml_) picks up later. You can see this in the file itself:

```yaml
      - uses: azure/postgresql@v1
        with:
          connection-string: ${{ secrets.AZURE_POSTGRESQL_CONNECTION_STRING }}
          server-name: exploit-db.postgres.database.azure.com
          plsql-file: "sql_files/*.sql"
```

## Alternatives to Github Actions and Azure
There is no need to use Github Actions or Azure to make this all work. At the end of the scraping, the data can be pushed over to anywhere, like a CSV file. The scraping can also be done using Jenkins or any other CI/CD platform.

Finally, if you run the scraping code locally and the SQL file gets generated, you can use SQLite to populate the database with the newly generated data.



###### resources below
stack overflow
* https://stackoverflow.com/questions/54337540/cannot-run-scrapy-crawl-quotes
* https://stackoverflow.com/questions/42351611/python-scrapy-error-running-scrapy-crawl-with-more-than-one-spider-is-no-long