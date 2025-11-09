from error_log import log
from scrapping import scrapping as s

log.set_custom_log_info("error_log/error.log")

try:
    print("sp")
    var = 1 / 0
except Exception as e:
    log.report(e)


