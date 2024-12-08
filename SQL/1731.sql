# Write your MySQL query statement below
select mng.employee_id, mng.name,
count(emp.reports_to) as reports_count, round(avg(emp.age)) as average_age
from Employees emp
inner join Employees mng on mng.employee_id = emp.reports_to
group by emp.reports_to
order by mng.employee_id
