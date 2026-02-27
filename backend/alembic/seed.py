import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.config import ADMIN_USER, ADMIN_PASSWORD

print("Admin:", ADMIN_USER, ADMIN_PASSWORD)