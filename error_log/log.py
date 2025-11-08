# DEBUG → সব message দেখায় (ডেভেলপমেন্টে কাজে লাগে)
# INFO → সাধারণ তথ্য
# WARNING → সতর্কবার্তা
# ERROR → ত্রুটি
# CRITICAL → খুব গুরুতর ত্রুটি
# 'a' → Append mode   &    'w' → Write mode(First Clear Then New Log ADD)
import logging


def set_custom_log_info(filename):
    logging.basicConfig(level=logging.INFO, filename=filename, format='%(asctime)s %(message)s', filemode='w')


def report(e: Exception):
    logging.exception(str(e))
