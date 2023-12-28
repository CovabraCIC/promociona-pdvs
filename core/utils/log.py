import pandas as pd
from datetime import date, datetime

def log_this_guy(pdv: str, msg: str):
    """Armazene os dados de log."""
    pdv = pdv
    msg = msg
    log_date = date.today()
    log_time = datetime.now()

    data_log = {'log_date': log_date, 'log_time': log_time, 'escopo': msg, "pdv": pdv}
    df_log = pd.DataFrame(data_log, index=[0])
    return df_log