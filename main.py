from scrapping import wlog

wlog.set_custom_log_info('error_log/error.log')

try:
    raise Exception
except Exception as e:
    # noinspection PyTypeChecker
    wlog.report(str(e))
