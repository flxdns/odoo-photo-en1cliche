# -*- coding: utf-8 -*-
{
    'name': "e1c_data",
    'summary': """""",
    'description': """""",
    'author': "En 1 Cliché",
    'website': "https://en1cliche.fr",
    'category': '',
    'version': '0.1',
    'license': 'LGPL-3',
    'application': False,

    # any module necessary for this one to work correctly
    'depends': [
        'e1c_config',
    ],

    # always loaded
    'data': [
        'data/company.xml',
        'data/prestation_stage.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
