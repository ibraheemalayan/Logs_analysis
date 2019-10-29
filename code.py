#!/usr/bin/env python3
###########################
#  MADE BY Ibraheem Alyan #
###########################

#######################################
# ALL the work is done inside the SQL #
#######################################

import psycopg2 as dbc

print("running ... \n")

db = None

try:
    db = dbc.connect(database="news")
except psycopg2.Error as e:
    print("Unable to connect to the database")
    print(e.pgerror)
    print(e.diag.message_detail)
    sys.exit(1)

c = db.cursor()

print("making reports ...\n")

######################################################################
#                           question 1                               #
######################################################################

first_question_query = (
  "select count , path , title from articles_view_count limit 3;")

c.execute(first_question_query)
top_articles = c.fetchall()

print("REPORET :\n\n")
print(" > What are the most popular three articles of all time?\n")

Q_1_Answer_list = []

for a in top_articles:
    Q_1_Answer_list.append((a[2], a[0]))
    print("   >>> \'" + a[2] + "\' got " + str(a[0]) + " views")

######################################################################
#                           question 2                               #
######################################################################

second_question_query = (
  "select name , sum(count) as total_views from articles_views_authors"
  " group by name order by total_views desc;")

c.execute(second_question_query)
top_authors = c.fetchall()

print("\n\n > Who are the most popular article authors of all time?\n")

Q_2_Answer_list = []

for a in top_authors:
    Q_2_Answer_list.append((a[0], a[1]))
    print("   >>> \'" + a[0] + "\' got " + str(a[1]) + " views")

######################################################################
#                           question 3                               #
######################################################################

third_question_query = (
  "select views_in_each_day.day , "
  "( cast(errors_in_each_day.errors as decimal) / "
  "cast(views_in_each_day.views as decimal) ) as ERR_Percentage "
  "from errors_in_each_day join views_in_each_day "
  "on views_in_each_day.day =  errors_in_each_day.day "
  "WHERE ( ( cast(errors_in_each_day.errors as decimal) / "
  "cast(views_in_each_day.views as decimal) ) >= 0.01 )"
  " order by ERR_Percentage desc;")

c.execute(third_question_query)
Most_errors_days = c.fetchall()

print("\n\n > On which days did more than 1% of requests lead to errors?\n")

Q_3_Answer_list = []

for r in Most_errors_days:
    Q_3_Answer_list.append((r[0], r[1]))
    print(
      "   >>> on \'" + str(r[0]) + "\' more than " + str(r[1]) +
      "% of requests lead to errors")

db.close()
print("\n\nThe source code for this program was wrriten by Ibraheem Alayan")

