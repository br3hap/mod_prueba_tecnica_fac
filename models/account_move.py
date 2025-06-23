# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    blood_type = fields.Many2one('blood.type', string='Tipo de Sangre')

    def button_comment(self):
        values = {
            'id':'view_type_remaining_sand_form',
            'name':u'Tipo de Sangre',
            'view_type':'form',
            'view_mode':'form',
            'target':'new',
            'context':{
                'default_move_id':self.id,
                'exclude_blood_type': self.blood_type.id,
            },
            'res_model':'type.remaining.sand',
            'domain': [('id', '!=', self.blood_type.id)],
            'type':'ir.actions.act_window',
        }

        return values
    

    def action_download_report(self):
        self.ensure_one()
        return self.env.ref('mod_prueba_tecnica_fac.action_report_account_move_simple').report_action(self)
