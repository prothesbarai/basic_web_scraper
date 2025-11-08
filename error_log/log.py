# DEBUG → সব message দেখায় (ডেভেলপমেন্টে কাজে লাগে)
# INFO → সাধারণ তথ্য
# WARNING → সতর্কবার্তা
# ERROR → ত্রুটি
# CRITICAL → খুব গুরুতর ত্রুটি

import logging


def set_custom_log_info(filename):
    logging.basicConfig(level=logging.INFO, filename=filename, format='%(asctime)s %(message)s')


def report(e: Exception):
    logging.exception(str(e))
