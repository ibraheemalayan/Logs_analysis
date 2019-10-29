# Logs Analysis - Udacity
### Full Stack Web Development ND
_______________________
## Prerequisites
* Python 3 > [https://realpython.com/installing-python/]
* Vagrant [https://www.vagrantup.com/docs/installation/]
* VirtualBox 3 [https://www.virtualbox.org/wiki/Downloads]
* psycopg2 [http://initd.org/psycopg/docs/install.html]

## Owner
Ibraheem Alyan

## Questions that the code will answer:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors? 

## Setup Instructions

> make sure to install all the prerequisites above before continuing

> the program python code is written in "code.py" file .
> before running "code.py" make sure to create the required views by running the SQL code in "views.sql" file .

 I put my effort to do all the process in the DB engine with SQL, the python code is so simple, it only prints the output of the SQL code.

* for the first question, first the (articles_view_count) view will get the views fo each path that leads to an article then the first hard-coded query in the python code will obtain the top 3 articles from the view and print them.

* for the second question, (articles_views_authors) view will use the previous view with the author id added to it ,then the python hard-coded query will group the results by the author name summing for each author the views his articles got and it will print the authors list sorted by popularity.

* for the third question, (views_in_each_day) view calculates the number of requests in each day, and the (errors_in_each_day) view will count the requests the lead to errors each day, after that the python hard-coded query will divid the answers from (views_in_each_day)&(errors_in_each_day) to get the percentage of errors in each day and prints the ones above 1%.

## HOPE it works with you ... 

