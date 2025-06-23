# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class AccountMoveDue_dateWizard(models.TransientModel):
    _name = 'account.move.due_date.wizard'
    _description = _('AccountMoveDue_dateWizard')

    due_date = fields.Date(string="Nueva fecha de vencimiento", required=True)

    def action_apply_due_date(self):
        active_id = self.env.context.get('active_id')
        if not active_id:
            return
        invoice = self.env['account.move'].browse(active_id)
        invoice.write({'invoice_date_due': self.due_date})
        return {'type': 'ir.actions.act_window_close'}
