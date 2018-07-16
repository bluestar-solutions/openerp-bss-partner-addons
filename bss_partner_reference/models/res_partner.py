# -*- coding: utf-8 -*-
# Part of Automatic Partner Reference.
# See LICENSE file for full copyright and licensing details.

from odoo import _, models, fields, api
from odoo.exceptions import UserError


class Partner(models.Model):
    _inherit = 'res.partner'

    ref = fields.Char('Reference', size=64, index=True, readonly=True)

    @api.model
    def create(self, vals):
        if 'ref' not in vals:
            vals['ref'] = self.env['ir.sequence'].get('bss.partner.ref')
        return super(Partner, self).create(vals)


class PartnerReferenceConfig(models.TransientModel):
    _name = 'bss.partner.reference.config'
    _inherit = 'res.config'

    GENERATE_REFS = [
        ('none', 'None'),
        ('empty', 'For partners with empty references'),
        ('all', 'For all existing partners')]

    generate_ref = fields.Selection(
        GENERATE_REFS, "Generate References", required=True)

    @api.multi
    def execute(self):
        self.ensure_one()
        Partner = self.env['res.partner'].with_context(active_test=False)
        Sequence = self.env['ir.sequence']
        partners = Partner
        if self.generate_ref == 'all':
            partners += Partner.search([])
        elif self.generate_ref == 'empty':
            partners += Partner.search([
                '|', ('ref', '=', False), ('ref', '=', '')])
        for partner in partners:
            partner.ref = Sequence.next_by_code('bluestar.partner.ref')

        partners = Partner.search([
            '|', ('ref', '=', False), ('ref', '=', '')])
        if partners:
            raise UserError(_("There is empty references !"))

        self.env.cr.execute("""
            SELECT COUNT(ref)
            FROM res_partner
            GROUP BY ref
            HAVING ( COUNT(ref) > 1 )""")
        if self.env.cr.rowcount > 0:
            raise UserError(_('There is duplicates references !'))
