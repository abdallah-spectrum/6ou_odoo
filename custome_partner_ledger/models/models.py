# -*- coding: utf-8 -*-

from odoo import models, fields, api


class customepartnerledgerReport(models.Model):
    _name = 'account.custome_partner_ledger'
    _inherit='account.partner.ledger'
    _description = 'custome_partner_ledger.custome_partner_ledger'

    def remove_domain_condition(self,domains, condition):
        updated_domains = []
        for domain in domains:
            if domain != condition:
                updated_domains.append(domain)
        return updated_domains

    # modify get option model remove recivable payable filter
    @api.model
    def _get_options_domain(self, options):
        # OVERRIDE
        # Handle filter_unreconciled + filter_account_type
        domain = super(customepartnerledgerReport, self)._get_options_domain(options)
        domain += self._get_filter_partners_domain(options)

        if options.get('unreconciled'):
            domain += ['&', ('full_reconcile_id', '=', False), ('balance', '!=', '0')]
        exch_code = self.env['res.company'].browse(self.env.context.get('company_ids')).mapped(
            'currency_exchange_journal_id')
        if exch_code:
            domain += ['!', '&', '&', '&', ('credit', '=', 0.0), ('debit', '=', 0.0), ('amount_currency', '!=', 0.0),
                       ('journal_id.id', 'in', exch_code.ids)]

        # domain.append(('account_id.internal_type', 'in', [t['id'] for t in self._get_options_account_type(options)]))


        # filter domain from internal type option
        updated_domain=[]
        for index in range(len(domain)):
            if domain[index][0] != 'account_id.internal_type':
                updated_domain.append(domain[index])




        return updated_domain
