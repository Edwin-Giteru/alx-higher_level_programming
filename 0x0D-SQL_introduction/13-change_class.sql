-- removing all the records with score below 5
use hbtn_0c_0;
delete from  second_table
where score <= 5;
select score, name 
from second_table
order by score desc;
