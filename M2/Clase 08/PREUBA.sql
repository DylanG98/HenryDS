use gastronomiacaba;

drop table clientes;

select * from oferta_gastronomica;


LOAD DATA LOCAL INFILE 'Restaurantescabacomma1.csv' 
INTO TABLE oferta_gastronomica
FIELDS TERMINATED BY ','
IGNORE 1 ROWS: