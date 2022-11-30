INSERT INTO fact_venta (IdFecha, Fecha, IdSucursal, IdProducto, IdProductoFecha, IdSucursalFecha, IdProductoSucursalFecha)
SELECT	c.IdFecha, 
		g.Fecha,
		g.IdSucursal, 
        NULL AS IdProducto, 
        NULL AS IdProductoFecha, 
        g.IdSucursal * 100000000 + c.IdFecha IdSucursalFecha,
        NULL AS IdProductoSucursalFecha
FROM 	gasto g JOIN calendario c
	ON (g.Fecha = c.fecha)
WHERE g.IdSucursal * 100000000 + c.IdFecha NOT IN (	SELECT	v.IdSucursal * 100000000 + c.IdFecha 
													FROM venta v JOIN calendario c ON (v.Fecha = c.fecha)
													WHERE v.Outlier = 1);
                                                    
################################################################### devuelven un número con el formato SUCURSAL/AÑO/MES/DIA                                                   
use modulo3;

INSERT INTO fact_venta (IdFecha, Fecha, IdSucursal, IdProducto, IdProductoFecha, IdSucursalFecha, IdProductoSucursalFecha)
SELECT	c.IdFecha, 
		co.Fecha,
		NULL AS IdSucursal, 
        co.IdProducto, 
        co.IdProducto * 100000000 + c.IdFecha AS  IdProductoFecha, 
        NULL IdSucursalFecha,
        NULL AS IdProductoSucursalFecha
FROM 	compra co JOIN calendario c
	ON (co.Fecha = c.fecha)
WHERE co.IdProducto * 100000000 + c.IdFecha NOT IN (SELECT	v.IdProducto * 100000000 + c.IdFecha 
													FROM venta v JOIN calendario c ON (v.Fecha = c.fecha)
													WHERE v.Outlier = 1);

################################################################### devuelven un número con el formato producto/AÑO/MES/DIA

######### La finalidad es darle un codigo de valor a un hecho para trabajar de manera más ágil.

################################## not in para excluir. 


create view vista as
SELECT 	co.TipoProducto,
		co.PromedioVentaConOutliers,
        so.PromedioVentaSinOutliers
FROM
	(	SELECT 	tp.TipoProducto, AVG(v.Precio * v.Cantidad) as PromedioVentaConOutliers
		FROM 	venta v 
		JOIN producto p
		ON (v.IdProducto = p.IdProducto)
		JOIN tipo_producto tp
		ON (p.IdTipoProducto = tp.IdTipoProducto)
		GROUP BY tp.TipoProducto
	) co
JOIN
	(	SELECT 	tp.TipoProducto, AVG(v.Precio * v.Cantidad) as PromedioVentaSinOutliers
		FROM 	venta v 
		JOIN producto p
		ON (v.IdProducto = p.IdProducto and v.Outlier = 1)
		JOIN tipo_producto tp
		ON (p.IdTipoProducto = tp.IdTipoProducto)
		GROUP BY tp.TipoProducto
	) so
ON co.TipoProducto = so.TipoProducto;

####################################### producto c/ y s/ outliers

########################################## ON co.TipoProducto = so.TipoProducto; campos claves

###################################################################### 

### 4

select fecha, sum(precio*cantidad) as VentasTotales from venta where fecha = (select min(fecha) from venta)
union
select fecha, sum(precio*cantidad) as VentasTotales from venta where fecha = (select max(fecha) from venta);

select min(fecha),max(fecha) from venta;

######## 5

select v.fecha, v.idproducto, sum(v.precio*v.cantidad)as VentasTotales, Producto  from venta v join producto p on v.idproducto = p.idproducto where v.fecha = (select min(fecha) from venta) group by v.idProducto
union
select v.fecha, v.idproducto, sum(v.precio*v.cantidad) as VentasTotales, Producto from venta v join producto p on v.idproducto = p.idproducto where v.fecha = (select min(fecha) from venta) group by v.idProducto;

####### 6

select fecha, sum(precio*cantidad) as VentasTotales from venta group by Fecha order by sum(precio*cantidad) desc;
 



