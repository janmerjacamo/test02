
from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    x_home_phone = fields.Char('Teléfono de Casa')
    x_dpi = fields.Char('DPI')
    x_dpi_extended = fields.Char('Extendido en')
    x_birth_place = fields.Char('Lugar de Nacimiento')
    x_nit = fields.Char('NIT')
    x_driver_license = fields.Char('Licencia de Conducir')
    x_igss = fields.Char('Afiliación IGSS')
    x_municipality = fields.Char('Municipio de Residencia')
    x_department_residence = fields.Char('Departamento de Residencia')
    x_other_income = fields.Boolean('Posee Otros Ingresos')
    x_has_vehicle = fields.Boolean('Posee Vehículo')
    x_vehicle_type = fields.Char('Tipo Vehículo')
    x_vehicle_brand = fields.Char('Marca Vehículo')
    x_has_debts = fields.Boolean('Posee Deudas')
    x_debt_amount = fields.Float('Monto Deuda')
    x_emergency_phone = fields.Char('Teléfono Emergencia')

    x_father_name = fields.Char('Nombre del Padre')
    x_father_phone = fields.Char('Teléfono del Padre')
    x_mother_name = fields.Char('Nombre de la Madre')
    x_mother_phone = fields.Char('Teléfono de la Madre')
    x_spouse_name = fields.Char('Nombre Cónyuge')
    x_spouse_phone = fields.Char('Teléfono Cónyuge')
    x_spouse_address = fields.Char('Dirección Cónyuge')
    x_children_count = fields.Integer('Número de Hijos')
    x_siblings_count = fields.Integer('Número de Hermanos')

    x_smokes = fields.Boolean('Fuma')
    x_drinks = fields.Boolean('Bebe')
    x_sports = fields.Boolean('Realiza Actividades Deportivas')
    x_weight = fields.Float('Peso')
    x_height = fields.Float('Altura')
    x_disabilities = fields.Text('Impedimentos')
    x_disease = fields.Text('Padece Alguna Enfermedad')
    x_medication = fields.Text('Toma Algún Medicamento')
    x_blood_type = fields.Selection([
        ('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),
        ('AB+','AB+'),('AB-','AB-'),('O+','O+'),('O-','O-')
    ], string='Tipo de Sangre')

    x_job_position_service = fields.Char('Nombre del Puesto de Servicio')
    x_hr_manager = fields.Char('Responsable RRHH')
    x_housing_type = fields.Selection([
        ('propio','Propio'),
        ('alquilado','Alquilado'),
        ('familiar','Familiar')
    ], string='Vivienda')
    x_years_residence = fields.Char('Tiempo de Vivir Allí')
    x_reentry_date = fields.Date('Fecha de Reingreso')
    x_job_address = fields.Char('Dirección del Puesto')
    x_direct_manager = fields.Char('Jefe Inmediato')
    x_assigned_department = fields.Char('Departamento Asignado')
    x_position_change_date = fields.Date('Fecha Cambio Puesto')
    x_new_position_name = fields.Char('Nombre del Puesto Nuevo')
    x_contract_condition = fields.Selection([
        ('fijo','Fijo'),
        ('temporal','Temporal')
    ], string='Condición')
    x_benefits = fields.Selection([
        ('none','Sin Prestaciones'),
        ('full','Completas'),
        ('half','50%')
    ], string='Prestaciones')
