import time
import os

timestamp = time.strftime("%Y%m%d-%H%M%S")
log_file = "log_webdemo_" + timestamp + ".html"
report_file = "report_webdemo" + timestamp + "html"
output_file = "output_webdemo" + timestamp + ".xml"

comanda = "robot -r " + report_file + " -l " + log_file + " login_tests"

os.system(comanda)