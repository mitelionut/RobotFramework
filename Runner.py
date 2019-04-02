import time
import os

timestamp = time.strftime("%Y%m%d-%H%M%S")
log_file = "log_webdemo_" + timestamp + ".html"
report_file = "report_webdemo" + timestamp + ".html"
output_file = "output_webdemo" + timestamp + ".xml"
html_tag1 = "Application_Name:WebDemoOfTheMillenium"
html_tag2 = "Version:1.0"

comanda = "robot -r " + report_file + " -l " + log_file + " -M " + html_tag1 + " -M " + html_tag2 +" login_tests"

os.system(comanda)