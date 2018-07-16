# -*- coding: utf-8 -*-
# Part of Qualified Contacts.
# See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models


class PartnerQualifier(models.Model):
    _name = 'bss.partner.qualifier'
    _description = "Partner Qualifier"

    name = fields.Char('Name', size=64, translate=True, required=True)
    protected = fields.Boolean('Protected', default=False)


class Partner(models.Model):
    _inherit = 'res.partner'
    _logger = logging.getLogger(_inherit)

    contact_qualifier_id = fields.Many2one(
        'bss.partner.qualifier', "Relation")
    has_custom_address = fields.Boolean("Has Custom Address")

    @api.onchange('parent_id')
    def onchange_parent_id(self):
        res = super(Partner, self).onchange_parent_id()
        if self.type == 'contact' and self.has_custom_address:
            for f in self._address_fields():
                res['value'].pop(f, None)
        return res

    @api.onchange('type', 'has_custom_address')
    def onchange_parent_address(self):
        if self.type == 'contact':
            if self.has_custom_address:
                for f in self._address_fields():
                    setattr(self, f, False)
        elif self.has_custom_address:
            self.has_custom_address = False
            if self.parent_id:
                for f in self._address_fields():
                    setattr(self, f, getattr(self.parent_id, f))
