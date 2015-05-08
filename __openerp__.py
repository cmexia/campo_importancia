# -*- coding: utf-8 -*-
{
    'name': 'Campo de importancia',
    'version': '2.0',
    'category': 'TyP',
    'description': """

        Este modulo agrega el campo de lista de importancia a la ficha del producto
    """,
    'author': 'cMexia',
    'website':'www.typrefrigeracion.com.mx',
    'depends': ['base','product','purchase'],
    'update_xml': [
        'importancia_view.xml',
	'comprador_view.xml',
    'fecha_pedido_view.xml',
        ],
    'installable': True,
    'active': False,
    'certificate' : False,
}
