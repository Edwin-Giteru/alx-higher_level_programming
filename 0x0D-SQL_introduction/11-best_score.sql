-- select the best
use hbtn_0c_0;
select score ,name
from second_table
where score >=10
order by score desc;
