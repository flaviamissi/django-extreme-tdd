"""
Testing cleanup helpers.
These cleanup functions assume the user uses a separate settings list for local
applications under the name of LOCAL_APPS.
"""
from django.db import connections
from django.apps import apps
#from django.conf import settings


def truncate_tables ():
    #apps = _collect_apps()

    tables = []
    models = apps.get_models()
    for model in models:
        tables.append(_collect_model_table(model))

    # PostgreSQL only - for now
    sql = "TRUNCATE {} RESTART IDENTITY CASCADE;".format(",".join(tables))
    cursor = connections["default"].cursor()
    cursor.execute(sql)


def _collect_model_table(model):
    return model._meta.db_table
