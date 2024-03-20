import logging
import os

from celery.schedules import crontab
from flask_caching.backends.filesystemcache import FileSystemCache

logger = logging.getLogger()

SECRET_KEY = "WwABW928J2Z%aJN5a7AQ6^bRRk!F7m6DAvs68cdN"
#PREVIOUS_SECRET_KEY = "change your existing SECRET_KEY to the PREVIOUS_SECRET_KEY and rotate with commands from Superset application container" 

#DATABASE_DIALECT = os.getenv("DATABASE_DIALECT", "postgresql")
#DATABASE_USER = os.getenv("DATABASE_USER", "api")
#DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "WBCLIuPEhgW47KiYIMINcGHFpOlMu29ejGpDW2fpIZ9Re2oFtYu5bNQVP2hRHMiB")
#DATABASE_HOST = os.getenv("DATABASE_HOST", "10.0.0.2")
#DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
#DATABASE_DB = os.getenv("DATABASE_DB", "api")
#
## The SQLAlchemy connection string.
#SQLALCHEMY_DATABASE_URI = (
#    f"{DATABASE_DIALECT}://"
#    f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
#    f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"
#)
#
#REDIS_HOST = os.getenv("REDIS_HOST", "redis")
#REDIS_PORT = os.getenv("REDIS_PORT", "6379")
#REDIS_CELERY_DB = os.getenv("REDIS_CELERY_DB", "0")
#REDIS_RESULTS_DB = os.getenv("REDIS_RESULTS_DB", "1")

RESULTS_BACKEND = FileSystemCache("/app/superset_home/sqllab")

#CACHE_CONFIG = {
#    "CACHE_TYPE": "RedisCache",
#    "CACHE_DEFAULT_TIMEOUT": 300,
#    "CACHE_KEY_PREFIX": "superset_",
#    "CACHE_REDIS_HOST": REDIS_HOST,
#    "CACHE_REDIS_PORT": REDIS_PORT,
#    "CACHE_REDIS_DB": REDIS_RESULTS_DB,
#}
#DATA_CACHE_CONFIG = CACHE_CONFIG
#
#
#class CeleryConfig:
#    broker_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB}"
#    imports = ("superset.sql_lab",)
#    result_backend = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULTS_DB}"
#    worker_prefetch_multiplier = 1
#    task_acks_late = False
#    beat_schedule = {
#        "reports.scheduler": {
#            "task": "reports.scheduler",
#            "schedule": crontab(minute="*", hour="*"),
#        },
#        "reports.prune_log": {
#            "task": "reports.prune_log",
#            "schedule": crontab(minute=10, hour=0),
#        },
#    }
#
#
#CELERY_CONFIG = CeleryConfig

FEATURE_FLAGS = {"ALERT_REPORTS": True,
            "ENABLE_TEMPLATE_PROCESSING":True,
            "DASHBOARD_VIRTUALIZATION":True,
            "EMBEDDABLE_CHARTS":True,
            "ENABLE_CORS":True,
            "EMBEDDED_SUPERSET":True,
        }
CORS_OPTIONS={
    'supports_credentials': True,
    'allow_headers': [
        'X-CSRFToken', 'Content-Type', 'Origin', 'X-Requested-With', 'Accept',
    ],
    'resources': [
         '/superset/csrf_token/' , # auth
         '/api/v1/formData/',  # sliceId => formData
         '/superset/explore_json/*',  # legacy query API, formData => queryData
         '/api/v1/query/',  # new query API, queryContext => queryData
         '/superset/fetch_datasource_metadata/'  # datasource metadata

    ],
    'origins': ['https://platform.staging.qubedoo.com:443','http://localhost:3001','http://localhost:3000'],
} 
logging.getLogger('flask_cors').level = logging.DEBUG        

ALERT_REPORTS_NOTIFICATION_DRY_RUN = True
WEBDRIVER_BASEURL = "http://superset:8088/"
# The base URL for the email report hyperlinks.
WEBDRIVER_BASEURL_USER_FRIENDLY = WEBDRIVER_BASEURL

SQLLAB_CTAS_NO_LIMIT = True

#
# Optionally import superset_config_docker.py (which will have been included on
# the PYTHONPATH) in order to allow for local settings to be overridden
#
try:
    import superset_config_docker
    from superset_config_docker import *  # noqa

    logger.info(
        f"Loaded your Docker configuration at " f"[{superset_config_docker.__file__}]"
    )
except ImportError:
    logger.info("Using default Docker config...")

