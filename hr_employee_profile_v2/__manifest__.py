{
    "name": "HR Employee Profile V2",
    "version": "19.0.2.0.0",
    "depends": ["hr", "mail"],  # mail para attachments quizá
    "data": [
        "security/ir.model.access.csv",
        "views/hr_employee_views.xml",
        "views/hr_employee_work_experience_views.xml",
        "views/hr_employee_reference_views.xml",
        "views/hr_employee_study_views.xml",
        "views/hr_employee_technical_study_views.xml",
    ],
    "installable": True,
    "application": False,
}
