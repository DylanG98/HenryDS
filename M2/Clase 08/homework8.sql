use gastronomiacaba;
drop table oferta_gastronomica;
select * from ofertagastronomica order by categoria asc;

delete from oferta_gastronomica where id_local > 1;

LOAD DATA INFILE 'Restaurantescabacomma1.csv' 
INTO TABLE oferta_gastronomica
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

show global variables like 'local_infile';

select count(barrio) as 'Cantidad Pubs', barrio from ofertagastronomica group by barrio order by count(barrio) desc LIMIT 1;

#select count(*) as Cantidad,categoria, barrio from ofertagastronomica where categoria = 'PUB' group by barrio having count(*)>= (select MAX(Cantidad) FROM ;

select * from ofertagastronomica where categoria = ' ';
