# -*- encoding: utf-8 -*-
 
from osv import osv, fields
 
class product_product(osv.osv):
    _name = 'product.product' 
    _inherit = 'product.product' 
 
    #Agregamos el campo al formulario producto o a la tabla product_product
    _columns = {
                'importancia': fields.char('Importancia',size=5),
        }
product_product()
