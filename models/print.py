from odoo import models, fields, api

class RecruitmentCard(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def get_recruitment_cards(self):
        recruitment_cards = self.search([('recruitment', '=', True)])
        return recruitment_cards
    
    def action_recruitment_cards(self):
        employee_id = self.env.context.get('active_id')
        employee = self.env['hr.employee'].browse(employee_id)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Карточки рекрутинга',
            'res_model': 'hr.applicant',
            'view_mode': 'kanban',
            'target': 'current',
            'domain': [('email_from', 'ilike', employee.work_email)],
            'views': [[False, 'kanban'], [False, 'form']],
        }