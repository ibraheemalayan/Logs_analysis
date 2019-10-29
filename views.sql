--
--
--

drop view if exists 
articles_views_authors,articles_view_count,errors_in_each_day,views_in_each_day;

--

create view articles_view_count as (
select count(*) as count , log.path , articles.title 
from log join articles on concat('/article/',articles.slug) = log.path 
where ((path like '/article/%') and (status = '200 OK')) 
group by log.path,articles.title order by count desc);

--

create view articles_views_authors as (
select articles_view_count.* , authors.name from 
(articles_view_count join articles on articles_view_count.title = articles.title) 
join authors on authors.id = articles.author);

-- 

create view views_in_each_day as (
select  date(time) as day, count(*) as views from log group by day);

--

create view errors_in_each_day as (
select  date(time) as day, count(*) as errors 
from log where status != '200 OK' group by day);
