# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Teacher(models.Model):
    _name = "teacher"
    _description = "Teacher"

    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')

    student_ids = fields.Many2many('student', string='Student')
    subject_id = fields.Many2one('subject', string='Subject')

