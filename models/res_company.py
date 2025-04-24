from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    cnpj_cpf_stripped = fields.Char(string="CNPJ sem máscara")
