from odoo import models,fields

class Standard(models.Model):
    _name="student.standard"
    _description="standard"


    name=fields.Char(string="Standard")
    subject_id=fields.Many2many("student.subject",string="Subject")