# -*- coding: utf-8 -*-
from odoo import api, fields, models
class Classs(models.Model):
    _name = "classs"
    _description = "Classs"

    name = fields.Char(string="Name")

    student_ids = fields.One2many('student','class_id',string="Student")
    teacher_ids = fields.Many2many('teacher',string='Teacher')

