from odoo import models,fields

class Standard(models.Model):
    _name="student.subject"
    _description="standard"


    name=fields.Char(string="Standard")
    