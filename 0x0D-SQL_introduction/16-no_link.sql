-- script that list all records of the table
use hbtn_0c_0;
select score,name
from second_table
where name is not null and name != ""
order by score desc;

