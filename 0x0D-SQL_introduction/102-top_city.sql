-- displaying top 3cities temperatures during july and august
use hbtn_0c_0;
select city,avg(value) as avg_temperature
from temperatures
where month in(7,8)
group by city
order by avg_temperature desc
limit 3;

