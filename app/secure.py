DEBUG = True # This is debug state flags
# SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:qingfing@localhost:3306/fisher'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:qingfing@localhost:3306/fisher'
SECRET_KEY = 'FJASDKLJFKADSJKLFJADSKLJKL8979345491327%^&%^&$%^$'



# Email configure
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '56237395@qq.com'
MAIL_PASSWORD = 'nonjollpgvckbjbg'
MAIL_SUBJECT_PREFIX = '<Fisher>'
MAIL_SENDER = 'Fisher <abc@qq.com>'
