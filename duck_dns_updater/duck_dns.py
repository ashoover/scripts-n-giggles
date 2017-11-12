# hits duck dns to update your IP and adds record of it to a log file in the same dir.


import logging
import requests

domain_to_update = ''
duck_dns_api_key = ''

url = 'https://www.duckdns.org/update?domains={}&token={}&ip='.format(domain_to_update, duck_dns_api_key)
log_file = 'duck_dns.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

r = requests.get(url)
status_code = r.status_code

if status_code == 200:
    log_this = 'Status OK! :) ' + 'Status code is : ' + str(status_code)
    logging.info(log_this)
else:
    log_this = 'Status BAD! :( ' + 'Status code is : ' + str(status_code)
    logging.error(log_this)

