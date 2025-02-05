from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from core.models.teachers import Teacher

class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        load_instance = True