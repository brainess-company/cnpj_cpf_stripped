from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    cnpj_cpf_stripped = fields.Char(string="CNPJ sem máscara")
