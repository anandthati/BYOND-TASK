from settings import * 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost","127.0.0.1","0.0.0.0","http://ktrajesh.ap-south-1.elasticbeanstalk.com/"]

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#PIPELINE['PIPELINE_ENABLED'] = False
#Envrions not set for these to get the actual values
DATABASES = {
    'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('RDS_DB_NAME','abc'),
        'USER': os.getenv('RDS_USERNAME','def'),
        'PASSWORD': os.getenv('RDS_PASSWORD','xyz'),
        'HOST': os.getenv('RDS_HOSTNAME','localhost'),
        'PORT': os.getenv('RDS_PORT',''),
               }
            }
#S3 Storage settings for development
AWS_AKey=os.getenv('AWS_ACCESS_KEY_ID',"ASDASDASDDFSFSASD")
AWS_SKey=os.getenv('AWS_SECRET_ACCESS_KEY',"asdsadasdasdasdsd")
AWS_BName='falconproduction-storage'
AWS_RName='ap-south-1'
AWS_BName_BMP='falconproduction-bmp-storage'
