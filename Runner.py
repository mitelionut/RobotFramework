import time
import os

timestamp = time.strftime("%Y%m%d-%H%M%S")
log_file = "log_webdemo_" + timestamp + ".html"
report_file = "report_webdemo" + timestamp + ".html"
output_file = "output_webdemo" + timestamp + ".xml"
html_tag1 = "Application_Name:WebDemoOfTheMillenium"
html_tag2 = "Version:1.0"

comanda = "robot -r {0} -l {1} -M {2} -M {3} -d {4} login_tests".format(report_file, log_file, html_tag1, html_tag2, timestamp)

os.system(comanda)