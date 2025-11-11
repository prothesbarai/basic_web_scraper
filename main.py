from error_log import log
from scrapping import s


log.set_custom_log_info("error_log/error.log")

try:
    print("sp")
    var = 1 / 0
    s = Student("Prothes")
    s.display()
except Exception as e:
    log.report(e)


