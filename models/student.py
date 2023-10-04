# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date


class Student(models.Model):
    _name = "student"
    _description = "Student"

    name = fields.Char(string="Name")
    age = fields.Integer(compute="_compute_age", string="Age" ,tracking=True)
    birth_day = fields.Date(string="Birth Age")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')

    class_id = fields.Many2one('classs', string="Class")
    parent_id = fields.Many2one('parent', string="Parent")

    subject_ids = fields.Many2many('subject', string='Subject')
    teacher_ids = fields.Many2many('teacher', string='Teacher')

    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birth_day:
                rec.age = today.year - rec.birth_day.year
            else:
                rec.age = 0
