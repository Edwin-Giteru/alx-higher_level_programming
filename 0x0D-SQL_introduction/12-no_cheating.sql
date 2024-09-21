-- updating the table second_table
use hbtn_0c_0;
update second_table
set score= 10
where name ="Bob";
select score,name from second_table
order by score desc;
