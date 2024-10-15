import schedule
import time
from lib.classes.CsvSource import CsvSources

def check_for_new_files():
    csv_source.check_for_new_files()

schedule.every(10).seconds.do(check_for_new_files)

csv_source = CsvSources()

while True:
    schedule.run_pending()