# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Parent(models.Model):
    _name = "parent"
    _description = "Parent"

    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    relative = fields.Selection([('father', 'Father'), ('mother', 'Mother')], string='Relative')

    student_id = fields.Many2one('student', string="Student")
