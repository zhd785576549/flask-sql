class SQLModule(object):

    def __init__(self):
        self.sql_statement = None
        self.parameter_type = None
        self.result_type = None
        self.timeout = None
        self.func = None

    @property
    def sql_statement(self):
        return self.sql_statement

    @sql_statement.setter
    def sql_statement(self, sql):
        self.sql_statement = sql

    @property
    def result_type(self):
        return self.result_type

    @result_type.setter
    def result_type(self, result_type):
        self.result_type = result_type

    @property
    def timeout(self):
        return self.timeout

    @timeout.setter
    def timeout(self, timeout):
        self.timeout = timeout

    @property
    def parameter_type(self):
        return self.parameter_type

    @parameter_type.setter
    def parameter_type(self, parameter_type):
        self.parameter_type = parameter_type

    @property
    def func(self):
        return self.func

    @func.setter
    def func(self, func):
        self.func = func
