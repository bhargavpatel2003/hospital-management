from odoo import models,fields,api,_

class Student(models.Model):
    _name="school.teacher"
    _description="Teacher"


    name=fields.Char(string="Name")
    dob=fields.Date(string="Date Of Birth")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    gendor=fields.Selection([("male","Male"),("female","Female")],string="Gender",default='male')

    student_ids = fields.One2many("school.student", "teacher_id", string="Class Students")

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []

        if name:
            domain = ['|','|',('name', operator, name), ('gendor', operator, name),('phone',operator,name)]

        domain += args
        res =self._search(domain, limit=limit, access_rights_uid=name_get_uid) 
 
        return res