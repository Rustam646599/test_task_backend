import os
from dotenv import load_dotenv
load_dotenv()
DEVELOPMENT_MODE = os.getenv('DEVELOPMENT_MODE')
if DEVELOPMENT_MODE == 'LOCAL':
    from .locale import *
elif DEVELOPMENT_MODE == 'DEVELOPER':
    from .developer import *
elif DEVELOPMENT_MODE == 'PRODUCTION':
    from .production import *
