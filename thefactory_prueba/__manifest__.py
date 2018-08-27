# -*- coding: utf-8 -*-

{
    'name' : 'The Factory HKA clientes',
    'version' : '0.1',
    'website' : 'https://www.thefactoryhka.com/ve/',
    'summary' : 'Clientes',
    'description' : """ Módulo para el almacenamiento de clientes""",
    'depends': [
                'base'
            ],
    'data': [
                'security/ir.model.access.csv',
                'data/ir.sequence.xml',
                'views/clientes_views.xml',
            ],
    'installable': True,
    'application': True,
}