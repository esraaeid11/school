# -*- coding: utf-8 -*-
{
    'name': 'School',
    'version': '15.0.0.1',
    'category': 'school',
    'auther': 'odoo mates',
    'summary': 'school system',
    'sequance': -100,
    'description': """school system""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/student.xml',
        'views/teacher.xml',
        'views/subject.xml',
        'views/menu.xml',
        'views/classs.xml',
        'views/parent.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
