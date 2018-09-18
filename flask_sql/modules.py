class SQLModule(object):

    def __init__(self):
        self.sql_statement = None
        self.parameter_type = None
        self.result_type = None

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
    def parameter_type(self):
        return self.parameter_type

    @parameter_type.setter
    def parameter_type(self, parameter_type):
        self.parameter_type = parameter_type
