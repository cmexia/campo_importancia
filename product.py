# -*- encoding: utf-8 -*-
 
from osv import osv, fields
 
class product_product(osv.osv):
    _name = 'product.product' 
    _inherit = 'product.product' 
 
    #Agregamos el campo al formulario producto o a la tabla product_product
    _columns = {
				'importancia_property': fields.property( 'product_product', type='char', size=5, string="Importancia", method=True ),
        }
product_product()