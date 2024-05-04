from bson import ObjectId

#*> Custom validator for Pydantic models that validates and converts ObjectId values to strings.
class PyObjectIdValidator(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, values):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return str(v)
