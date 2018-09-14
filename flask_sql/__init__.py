from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker


class FlaskSql(object):

    def __init__(self, app=None):
        self.app = app
        self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('SQLALCHEMY_DATABASE_URI', 'sqlite:///:memory:')
        app.config.setdefault('SQLALCHEMY_BINDS', None)
        app.config.setdefault('SQLALCHEMY_NATIVE_UNICODE', None)
        app.config.setdefault('SQLALCHEMY_ECHO', False)
        app.config.setdefault('SQLALCHEMY_RECORD_QUERIES', None)
        app.config.setdefault('SQLALCHEMY_POOL_SIZE', None)
        app.config.setdefault('SQLALCHEMY_POOL_TIMEOUT', None)
        app.config.setdefault('SQLALCHEMY_POOL_RECYCLE', None)
        app.config.setdefault('SQLALCHEMY_MAX_OVERFLOW', None)
        app.config.setdefault('SQLALCHEMY_COMMIT_ON_TEARDOWN', False)
        app.config.setdefault('SQLALCHEMY_SQL_FOLDER', './sql/')

    def get_app(self):
        if self.app is not None:
            return self.app
        else:
            raise RuntimeError("No application found. Either work inside a view function or push")

    @property
    def engine(self):
        return self.engine
