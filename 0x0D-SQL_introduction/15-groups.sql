-- listing the number of records with the same score
use hbtn_0c_0;
select score,count(score) as number
from second_table
group by score
order by number desc;

