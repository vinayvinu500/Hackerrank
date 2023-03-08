use hackerrank;
show tables;

-- output: submission_date, count of unique, submissions.hacker_id, hackers.name
-- Note: we need to pick hacker who submits eveyday and print name who made maximum submission on that day

-- data
select * from hackers; -- 500
select * from submissions; -- 2000

-- find the hackers who made first date submissions
select distinct hacker_id from submissions 
where submission_date = "2016-03-01" order by hacker_id; -- 112

-- find the hackers whos submission done eveyday
select 
    submission_date dates,
    count(*) over(partition by submission_date) as unique_hackers,
    first_value(hacker_id) over(partition by submission_date order by submission_date, count(*) desc) as hacker
from submissions as t1
group by submission_date, hacker_id
having hacker_id in (select distinct hacker_id 
                     from submissions as t2 
                     where submission_date = "2016-03-01"
                     order by hacker_id); -- 901


-- final output: 8.0+ version
select distinct
	dates, 
    unique_hackers,
    max_hacker, 
	name
from
(select 
    submission_date dates,
    count(*) over(partition by submission_date) as unique_hackers,
    first_value(hacker_id) over(partition by submission_date order by submission_date, count(*) desc) as max_hacker
from submissions as t1
group by submission_date, hacker_id
having hacker_id in (select distinct hacker_id 
                     from submissions as t2 
                     where submission_date = "2016-03-01"
                     order by hacker_id)) as t1 inner join hackers as t2
on t1.max_hacker = t2.hacker_id
order by 1; -- 15

-- Note: The above code based on starting date only