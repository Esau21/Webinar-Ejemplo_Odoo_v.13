from odoo import models,fields

class Ejemplo(models.Model):
    _name = "wb.tareas"

    name = fields.Char("Nombre")
    status = fields.Selection(selection=[("borrador","Borrador"), ("hecho","Hecho"),("pendiente","Pendiente")])
