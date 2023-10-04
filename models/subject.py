# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Subject(models.Model):
    _name = "subject"
    _description = "Subject"

    name = fields.Char(string="Name")
