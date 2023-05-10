from .models import User


def model_schema(collection, bd_instance):
    bd_instance["id"] = str(bd_instance.pop("_id"))
    if collection == 'users':
        return User(**bd_instance)
