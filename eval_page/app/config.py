import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY ='test'
	DEBUG = False


class DevelopmentConfig(Config):
	# uncomment the line below to use postgres
	# SQLALCHEMY_DATABASE_URI = postgres_local_base
	DEBUG = True
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'pybo.db')
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:qwerqwer123@mysql:3306/pybo'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:demo@mysql:3306/storage'

# class TestingConfig(Config):
# 	DEBUG = True
# 	TESTING = True
# 	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'pybo.db')
# 	PRESERVE_CONTEXT_ON_EXCEPTION = False
# 	SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
	DEBUG = False
	# uncomment the line below to use postgres
	# SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
	dev=DevelopmentConfig,
	prod=ProductionConfig
)

key = Config.SECRET_KEY