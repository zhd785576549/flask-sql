from lxml import etree
from flask_sql.exceptions import UnknownElement
from flask_sql.modules import SQLModule


class SQLXmlParse(object):

    def __init__(self, filepath):
        self.filepath = filepath
        self.errors = []
        self.root = etree.parse(filepath)

    def parse(self):
        modules = {}
        errors = []
        err_flag = False
        for element in self.root:
            tag = element.tag
            tag = tag.lower()
            module = None
            func_name = None
            if tag == "select":
                func_name, module = self.__parse_select(element)
            elif tag == "update":
                func_name, module = self.__parse_update(element)
            elif tag == "insert":
                func_name, module = self.__parse_insert(element)
            elif tag == "delete":
                func_name, module = self.__parse_delete(element)
            else:
                err_flag = True
                errors.append("{0} unknown tag name {1}".format(self.filepath, element.tag))
            if module and func_name:
                modules[func_name] = module
            elif func_name is None:
                errors.append("{0} unknown tag name {1} not found id".format(self.filepath, element.tag))
        if err_flag:
            raise UnknownElement(errors)
        return modules

    def __parse_select(self, e):
        sql_module = SQLModule()
        func_name = e.get("id")
        parameter_type = e.get("parameterType")
        result_type = e.get("resultType")
        sql_module.parameter_type = parameter_type
        sql_module.result_type = result_type
        sql_module.sql_statement = e.text
        return func_name, sql_module

    def __parse_update(self, e):
        sql_module = SQLModule()
        func_name = e.get("id")
        parameter_type = e.get("parameterType")
        result_type = e.get("resultType")
        sql_module.parameter_type = parameter_type
        sql_module.result_type = result_type
        sql_module.sql_statement = e.text
        return func_name, sql_module

    def __parse_insert(self, e):
        sql_module = SQLModule()
        func_name = e.get("id")
        parameter_type = e.get("parameterType")
        result_type = e.get("resultType")
        sql_module.parameter_type = parameter_type
        sql_module.result_type = result_type
        sql_module.sql_statement = e.text
        return func_name, sql_module

    def __parse_delete(self, e):
        sql_module = SQLModule()
        func_name = e.get("id")
        parameter_type = e.get("parameterType")
        result_type = e.get("resultType")
        sql_module.parameter_type = parameter_type
        sql_module.result_type = result_type
        sql_module.sql_statement = e.text
        return func_name, sql_module
