-- importing into hbtn_0c_0
use hbtn_0c_0;
select city,avg(value) as av_temperature
from temperatures
group by city
order by av_temperature desc;

