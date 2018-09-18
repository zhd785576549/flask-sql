from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
import os
from flask_sql.exceptions import NotFoundSqlModule
from flask_sql.exceptions import NotFoundModulePath
from flask_sql.parse import SQLXmlParse
import warnings


class FlaskSql(object):
    """
    member:
        app: flask app
        engine: sqlalchemy engine
        xml_folder: xml configure folder path
        modules: sql modules,
                {
                    package.method_name: SQLModel object
                }
                {
                    test.db_interface.get_user_by_username: <object SQLModel at 0x0000027AD57CC110 >
                    test.db_interface.get_user_by_id: <object SQLModel at 0x0000027AD57CC110 >
                }
        session: sqlalchemy sessionmaker
    """

    def __init__(self, app=None):
        self.app = app
        self.engine = None
        self.xml_folder = None
        self.modules = {}
        self.session = None
        self.__init_app(self.app)
        self.__init_engine()
        self.__init_session()
        self.__load_modules()

    def __init_app(self, app):
        app.config.setdefault("SQLALCHEMY_DATABASE_URI", "sqlite:///:memory:")
        app.config.setdefault("SQLALCHEMY_BINDS", None)
        app.config.setdefault("SQLALCHEMY_NATIVE_UNICODE", None)
        app.config.setdefault("SQLALCHEMY_ECHO", False)
        app.config.setdefault("SQLALCHEMY_POOL_SIZE", 100)
        app.config.setdefault("SQLALCHEMY_POOL_TIMEOUT", None)
        app.config.setdefault("SQLALCHEMY_POOL_RECYCLE", None)
        app.config.setdefault("SQLALCHEMY_MAX_OVERFLOW", None)
        app.config.setdefault("SQLALCHEMY_SQL_FOLDER", "./sql/")
        self.folder = app.config.get("SQLALCHEMY_SQL_FOLDER")

    def get_app(self):
        if self.app is not None:
            return self.app
        else:
            raise RuntimeError("No application found. Either work inside a view function or push")

    def __init_engine(self):
        uri = self.app.config.get("SQLALCHEMY_DATABASE_URI")
        pool_size = self.app.config.get("SQLALCHEMY_POOL_SIZE")
        echo = self.app.config.get("SQLALCHEMY_ECHO")
        pool_recycle = self.app.config.get("SQLALCHEMY_POOL_RECYCLE")
        pool_timeout = self.app.config.get("SQLALCHEMY_POOL_TIMEOUT")
        max_overflow = self.app.config.get("SQLALCHEMY_MAX_OVERFLOW")
        convert_unicode = self.app.config.get("SQLALCHEMY_POOL_SIZE")
        self.engine = create_engine(uri, pool_size=pool_size, echo=echo, pool_recycle=pool_recycle,
                                    pool_timeout=pool_timeout, max_overflow=max_overflow,
                                    convert_unicode=convert_unicode)

    def __init_session(self):
        self.session = sessionmaker(bind=self.engine)

    def __check_exists(self, sql_module):
        if len(self.modules):
            return False
        if sql_module in self.modules.keys():
            return True

    def __load_modules(self):
        if os.path.exists(self.folder) is False:
            raise NotFoundModulePath("SQLALCHEMY_SQL_FOLDER {0} path not found".format(self.folder))
        dirs = os.listdir(self.folder)
        for file in dirs:
            filepath = os.path.join(self.folder, file)
            name, ext = os.path.splitext(filepath)
            if os.path.isfile(filepath):
                if ext.lower() == "xml":
                    try:
                        modules = SQLXmlParse(filepath).parse()
                        for module in modules:
                            # insert module to self.modules dict
                            pass
                    except Exception as e:
                        raise
                else:
                    warnings.warn("{0} is not xml file".format(file))
            else:
                warnings.warn("{0} is a folder".format(file))

    def execute(self, module_name, func):
        pass

    def __execute_sql(self, sql):
        session = self.session()
        try:
            session.execute(sql)
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()
