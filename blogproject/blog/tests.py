
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname('__file__')))





MEDIA_URL = '/media/'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'blog/media')
print('PROJECT_ROOT',PROJECT_ROOT)
print('MEDIA_ROOT',MEDIA_ROOT)
print('MEDIA_URL',MEDIA_URL)
print('BASE_DIR',BASE_DIR)