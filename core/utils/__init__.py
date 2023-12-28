import os, json
from dotenv import load_dotenv, find_dotenv
from .compare_tables import difference
from .log import log_this_guy

dotenv=find_dotenv()
load_dotenv(dotenv)

cic_settings = json.loads(os.environ.get("CIC_SETTINGS", {}))
erp_settings = json.loads(os.environ.get("ERP_SETTINGS", {}))
venda_settings = json.loads(os.environ.get("VENDA_SETTINGS", {}))
pdv_settings = json.loads(os.environ.get("PDV_SETTINGS", {}))

UTILS_PATH = os.path.dirname(os.path.abspath(__file__))
CORE_PATH = os.path.dirname(UTILS_PATH)
PROJECT_PATH = os.path.dirname(CORE_PATH)

SQL_PACKAGE_PATH = os.path.join(CORE_PATH, "sql")