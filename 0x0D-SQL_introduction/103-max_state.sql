-- dispalys max temperatures
use hbtn_0c_0;
select state,max(value) as max_value
from temperatures
group by state
order by state asc
limit 3;

