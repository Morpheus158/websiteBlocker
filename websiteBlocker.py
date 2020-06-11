import time
import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
localhost = "127.0.0.1"
page_list = ["www.facebook.com", "www.youtube.com"]
wh_start = 8
wh_end = 16

while True:
    my_time = dt.datetime.now()

    if int(my_time.hour) > wh_start and int(my_time.hour) < wh_end:
        with open(hosts_path, "r+") as hosts:
            read_file = hosts.read()
            for page in page_list:
                if not page in read_file:
                    hosts.write(localhost + " " + page + "\n")
    else:
        with open(hosts_path, "r+") as hosts:
            read_file = hosts.readlines()
            hosts.seek(0)
            for line in read_file:
                if not any(site in line for site in page_list):
                    hosts.write(line)
            hosts.truncate()

    time.sleep(10)