SELECT * FROM modulo3.cliente;

#1))))

select distinct  c.Nombre_y_Apellido, v.IdProducto, v.Precio from venta v join cliente c on c.IdCliente = v.IdCliente ;

#2))))

select c.Nombre_y_Apellido, sum(v.Cantidad) from cliente c left join venta v on c.IdCliente = v.IdCliente group by c.Nombre_y_Apellido;

#3))))

select c.IdCliente,c.Nombre_y_Apellido, sum(v.Cantidad) as Cantidad, year(v.Fecha) as Año from venta v left join cliente c on c.IdCliente = v.IdCliente group by year(v.Fecha) , c.IdCliente order by c.Nombre_y_Apellido, v.Fecha asc;

select idCliente, sum(cantidad) from venta where idcliente = 896 and year(Fecha) = 2018;

#4)))) 

select c.Nombre_y_Apellido, v.IdProducto, sum(v.Cantidad) from venta v left join cliente c on c.IdCliente = v.IdCliente group by v.IdProducto order by c.Nombre_y_Apellido;

#5))))

select  l.Localidad as Localidad ,sum(v.Cantidad) as Cantidad_productos_vendidos, sum(v.precio * v.Cantidad) as Ganancias, count(v.idventa) as Total_ventas
from sucursal s
left join venta v on s.IdSucursal =  v.IdSucursal
left join localidad l on s.IdLocalidad = l.IdLocalidad 
where v.Outlier = 1
group by  l.Localidad
order by  l.Localidad;

#6))))

select  p.provincia as Provincia ,sum(v.Cantidad) as Cantidad_productos_vendidos, count(v.idventa) as Total_ventas
from venta v
left join cliente c on v.idcliente = c.idcliente
left join localidad l on c.IdLocalidad = l.IdLocalidad 
left join provincia p on l.IdProvincia = p.IdProvincia
group by  p.provincia;














