from odoo import models, fields, api

class HrEmployeeWorkExperience(models.Model):
    _name = "hr.employee.work.experience"
    _description = "Experiencia Laboral del Empleado"
    _order = "sequence, start_date desc"

    employee_id = fields.Many2one("hr.employee", string="Empleado", required=True, ondelete="cascade")
    sequence = fields.Integer("Secuencia", default=10)
    company_name = fields.Char("Nombre de la Empresa", required=True)
    position = fields.Char("Puesto que ocupaba")
    start_date = fields.Date("Fecha Inicio")
    end_date = fields.Date("Fecha Fin")
    duration = fields.Char("Tiempo laborado", compute="_compute_duration", store=True)
    salary = fields.Float("Salario")
    reason_leave = fields.Text("Motivo de retiro")
    immediate_boss = fields.Char("Jefe inmediato")
    company_phone = fields.Char("Teléfono de la empresa")
    can_request_references = fields.Boolean("¿Se puede pedir referencias?")

    @api.depends("start_date", "end_date")
    def _compute_duration(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                delta = rec.end_date - rec.start_date
                rec.duration = f"{delta.days // 30} meses" if delta.days < 365 else f"{delta.days // 365} años"
            else:
                rec.duration = ""
