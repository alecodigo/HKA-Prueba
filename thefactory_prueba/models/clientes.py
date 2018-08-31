# -*- coding:utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError

class TheFactoryClientes(models.Model):
    """Registro de Clientes"""
    _name = 'thefactory.clientes'
    _rec_name = 'id_cliente'
    _description = 'Cartera de Clientes de la empresa'

    id_cliente = fields.Char("ID", readonly= True, help='Numero de Identificacion del Cliente')
    cedula = fields.Char('Cedula')
    nombre = fields.Char('Nombre', required=True)
    apellido = fields.Char('Apellido', required=True)
    telefono = fields.Char('Telefono')
    email = fields.Char('Email', required = True)
    fecha_nacimiento = fields.Date('Fecha de Nacimiento', required = True)
    estatus = fields.Selection([('activo','Activo'),('inactivo','Inactivo')])



    @api.constrains('cedula','telefono')
    def revisar_cantidad_digitos(self):
        """ Se revisa que no los campos solo contengan números """
        
        if (self.cedula):
            try:
                if int(self.cedula):
                    pass
            except:
                raise ValidationError("La cedula sólo puede contener números")
        
        if (self.telefono):
            try:
                if int(self.telefono):
                    pass
            except:
                raise ValidationError("El teléfono sólo puede contener números")


    #Se reescribe el método create 
    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('seq_id_clientes') or '/'
        vals['id_cliente'] = seq
        return super(TheFactoryClientes, self).create(vals)