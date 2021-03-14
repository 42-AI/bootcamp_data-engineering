# Module00 - SQL with PostgreSQL

In this module, you will learn how to use a SQL database: PostgreSQL.

## Notions of the module

The purpose of the module is at first to create, administrate and normalize a PostgreSQL Database. Then, we are going to analyse the data and visualize the content of the database. Finally, we will see advanced notions like caching, replication and backups.

## General rules

* The version of Python to use is 3.7, you can check the version of Python with the following command: `python -V`.
* you will follow the **[Pep8 standard](https://www.python.org/dev/peps/pep-0008/)**.
* The exercises are ordered from the easiest to the hardest.
* Your exercises are going to be evaluated by someone else so make sure that variables and functions names are appropriated.
* Your man is the internet.
* You can also ask any question in the dedicated channel in Slack: **[42ai slack](https://42-ai.slack.com)**.
* If you find any issue or mistakes in the subject please create an issue on our dedicated repository on **[Github issues](https://github.com/42-AI/bootcamp_data-engineering/issues")**.

## Foreword

Data Engineering implies many tasks from organizing the data to putting data systems to productions. Data organization is often a mess in companies and our job is to provide a common, well-organized data source. Historically, the organization of the data is used to analyze the business and determine future business decisions. Those data organizations are called [Data warehouses](https://www.tutorialspoint.com/dwh/index.htm) and are used by business intelligence teams (teams in charge of analyzing the business). This organization of the data follows a [star scheme](https://www.tutorialspoint.com/dwh/dwh_schemas.htm) allowing fast analysis.

Nowadays, we want to meet other cases' needs such as providing data to data science teams or other projects. To do so, we want to deliver a common data organization which won't be project-specific but which will be used by anyone willing to (business intelligence, data scientists, ...). This 
new data organization is called a [Data Lake](https://medium.com/rock-your-data/getting-started-with-data-lake-4bb13643f9). It contains all the company data. The job of data engineering consists of organizing the data :
- ingestion
- storage
- catalog and search engine associated

To do that SQL is often used to filter, join, select the data. During the module, you will discover an open-source SQL language, PostgreSQL.

### Exercise 00 - Setup
### Exercise 01 - Clean
### Exercise 02 - Normalize
### Exercise 03 - Populate
### Exercise 04 - Top_100
### Exercise 05 - Name_lang
### Exercise 06 - K-first
### Exercise 07 - Seniors
### Exercise 08 - Battle_royale
### Exercise 09 - Benefits
### Exercise 10 - Sweet_spot
### Exercise 11 - Price_analysis
### Exercise 12 - Worldwide
### Exercise 13 - Italian_market
### Exercise 14 - Sample
