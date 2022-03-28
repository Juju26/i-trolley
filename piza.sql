select pizza_name,
count(pizza_id) as no_sold 
from pizza
where pizza_id=max(count(pizza_id))
 order by pizza_name,no_sold;
 