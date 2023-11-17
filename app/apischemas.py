from flask_restplus import fields


UserModel = {
    'First_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'password': fields.String(required=True),
    'email': fields.String(required=True),
    'contact_number': fields.String(),
    'farm_location': fields.String()
}


