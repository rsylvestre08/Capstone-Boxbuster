from flask_marshmallow import Marshmallow
from marshmallow import post_load, fields
from database.models import Administrator, Clublevel, MypaymentHistory, Survey
from database.models import User, Car

ma = Marshmallow()

# Auth Schemas
class RegisterSchema(ma.Schema):
    """
    Schema used for registration, includes password
    """
    id = fields.Integer(primary_key=True)
    email = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    address = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    zip_code = fields.String(required=True)
    club_level = fields.String(required=False)

    class Meta:
        fields = ("id", "email",  "username", "password", "first_name", "last_name", "address", "city", "state", "zip_code", "club_level")

    @post_load
    def create_user(self, data, **kwargs):
        return User(**data)
    
class UserSchema(ma.Schema):
    """
    Schema used for displaying users, does NOT include password
    """
    id = fields.Integer(primary_key=True)
    email = fields.String(required=True)
    username = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    address = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    zip_code = fields.String(required=True)
    club_level = fields.String(required=False)
    
    class Meta:
        fields =  ("id", "email",  "username", "first_name", "last_name", "address", "city", "state", "zip_code", "club_level")

register_schema = RegisterSchema()
user_schema = UserSchema()
users_schema = UserSchema(many=True)


# Car Schemas
class CarSchema(ma.Schema):
    id = fields.Integer(primary_key=True)
    make = fields.String(required=True)
    model = fields.String(required=True)
    year = fields.Integer()
    user_id = fields.Integer()
    user = ma.Nested(UserSchema, many=False)
    class Meta:
        fields = ("id", "make", "model", "year", "user_id", "user")
    
    @post_load
    def create_car(self, data, **kwargs):
        return Car(**data)
car_schema = CarSchema()
cars_schema = CarSchema(many=True)


# TODO: Add your schemas below

class AdministratorSchema(ma.Schema):
    id = fields.Integer(primary_key=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    class Meta:
        fields = ("id", "username", "password")
    
    @post_load
    def create_administrator(self, data, **kwargs):
        return Administrator(**data)
administrator_schema = AdministratorSchema()
administrators_schema = AdministratorSchema(many=True)


class ClubLevelSchema(ma.Schema):
    id = fields.Integer(primary_key=True)
    platinum = fields.String(required=True)
    gold = fields.String(required=True)
    silver = fields.String(required=True)
    bronze = fields.String(required=True)
    price = fields.String(required=True)
    user_id = fields.Integer()
    user = ma.Nested(UserSchema, many=False)
    class Meta:
        fields = ("id", "platinum", "gold", "silver", "bronze", "price", "user_id", "user")

    @post_load
    def create_clublevel(self, data, **kwargs):
        return Clublevel(**data)
clublevel_schema = ClubLevelSchema() 
clublevels_schema = ClubLevelSchema(many=True)


class MyPaymentHistorySchema(ma.Schema):
    id = fields.Integer(primary_key=True)
    total_owed = fields.Float()
    billing_cycle = fields.Date()
    user_id = fields.Integer()
    class Meta: 
        fields = ("id", "total_owed", "billing_cycle", "user_id")
    
    @post_load
    def create_mypaymenthistory(self, data, **kwargs):
        return MyPaymentHistorySchema(**data)
mypaymenthistory_schema = MyPaymentHistorySchema()
mypaymenthistorys_schema = MyPaymentHistorySchema(many=True)


class SurveySchema(ma.Schema):
    id = fields.Integer(primary_key=True)
    genre_preference = fields.String(required=True)
    budget = fields.Float()
    nationality = fields.String(required=True)
    user_id = fields.Integer()
    class Meta:
        fields = ("id", "genre_preference", "budget", "nationality", "user_id")
    @post_load
    def create_survey(self, data, **kwargs):
        return SurveySchema(**data)
survey_schema = SurveySchema()    
surveys_schema = SurveySchema(many=True)



















