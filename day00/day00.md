# Bootcamp Data Engineering

# Day00 - SQL with PostgreSQL

Today, you will learn how to use a SQL database: PostgreSQL.

## Notions of the day

The purpose of the day is first to create, administrate and normalize a PostgreSQL Database. Then, we are going to analyse the data and visualize the content of the database. Finally, we will see advanced notions like caching, replication and backups.

## General rules

* The version of Python to use is 3.7, you can check the version of Python with the following command: `python -V`.
* For this day, you will follow the **[Pep8 standard](https://www.python.org/dev/peps/pep-0008/)**.
* The exercices are ordered from the easiest to the hardest.
* Your exercices are going to be evaluated by someone else so make sure that variables and functions names are appropriated.
* Your man is internet.
* You can also ask question in the dedicated channel in Slack: **[42ai slack](42-ai.slack.com)**.
* If you find any issue or mistakes in the subject please create an issue on our dedicated repository on **[Github issues](https://github.com/42-AI/bootcamp_data-engineering/issues")**.

## Foreword

Data Engineering implies many tasks from organizing the data to putting data systems to productions. Data organization is often a mess in companies and our job is to provide a common, well organized data source. Historically, organization of the data is used to analyze the business and determine future business decision. Those data organizations are called [Data warehouses](https://www.tutorialspoint.com/dwh/index.htm) and are used by business intelligence teams (teams in charge of analyzing the business). This organization of the data follows a [star scheme](https://www.tutorialspoint.com/dwh/dwh_schemas.htm) allowing fast analysis.

Nowadays, we want to answer other cases like providing data to data-science teams. In order to do that we want to provide a common data organization not specific to any project which will be used by anyone who wants it (business intelligence, data scientists, ...). This 
new data organization is called a [Data Lake](https://medium.com/rock-your-data/getting-started-with-data-lake-4bb13643f9). It contains all the company data. The job of data engineering consists of organizing the data :
- ingestion
- storage
- catalog and search engine associated

In order to do that SQL is often used to filter, join, select the data. Today you will discover an open source SQL language, PostgreSQL.

## Helper

Ensure that you have the right Python version and psycopg2 installed.

```
$> which python
/goinfre/miniconda/bin/python
$> python -V
Python 3.7.*
$> which pip
/goinfre/miniconda/bin/pip
```

### Exercice 00 - Setup
### Exercice 01 - Clean
### Exercice 02 - Normalize
### Exercice 03 - Populate
### Exercice 04 - Top_100
### Exercice 05 - Name_lang
### Exercice 06 - K-first
### Exercice 07 - Seniors
### Exercice 08 - Battle_royale
### Exercice 09 - Benefits
### Exercice 10 - Sweet_spot
### Exercice 11 - Price_analysis
### Exercice 12 - Worldwide
### Exercice 13 - Sample
