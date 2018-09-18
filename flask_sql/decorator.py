def flask_sql(bind_db):
    """
    Decorator for flask SQL
    :param bind_db:  FlaskSql object
    :return: None
    """
    def inner(func):
        def wrapper(*args, **kwargs):
            module = func.__module__
            name = func.__name__
            sql_module_name = "{0}.{1}".format(module, name)
            bind_db.execute(sql_module_name, func)
