import random

proxies_pool = [
    # "112.85.166.214:999",
    # "60.13.42.169:999",
    # "60.13.42.45:999",
    # "163.204.243.191:999",
    # "60.13.42.178:999",
    # "112.85.171.8:999",
    # "120.83.110.145:999",
    # "117.28.96.229:999",
    # "120.83.104.230:999",
    # "180.107.24.148:811",
    # "183.166.161.127:80",
    # "123.120.55.121:811",
    # "58.34.118.95:811",
    # "61.178.149.237:5904",
    # "120.79.147.254:900",
    # "123.52.43.64:811",
    # "222.93.105.7:811",
    # "61.157.136.105:80",
    # "117.80.66.184:80",
    # "119.129.238.253:811",
    # "120.83.104.230:999",
    # "180.107.24.148:811",
    # "183.166.161.127:80",
    # "106.75.8.141:80",
    # "180.154.173.175:811",
    # "120.79.147.254:900",
    # "123.52.43.64:811",
    # "222.93.105.7:811",
    # "61.157.136.105:80",
    # "117.80.66.184:80",
    # "119.129.238.253:811",
    # "60.13.42.226:999",
    # "163.204.244.74:999",
    # "180.117.133.103:811",
    # "123.163.96.232:999",
    # "112.85.128.170:999",
    # "60.169.114.242:80",
    # "163.204.244.162:999",
    # "60.13.42.125:999",
    # "122.4.29.17:6123",
    # "113.65.5.14:811",
    # "111.226.211.21:811",
    # "124.112.162.147:80",
    # "175.16.20.48:8",
    # "61.135.155.82:44",
    # "113.117.108.226:6123",
    # "117.95.195.98:999",
    # "163.204.244.48:999",
    # "163.204.245.140:999",
    # "163.204.245.207:999",
    # "163.204.242.74:999",
    # "112.85.128.143:999",
    # "114.239.42.181:999",
    # "163.204.246.121:999",
    # "60.13.42.211:999",
    # "42.159.91.248:808",
    # "112.87.70.125:999",
    # "60.13.42.209:999",
    # "119.5.164.149:6123",
    # "120.83.105.198:999",
    # "112.87.68.39:999",
    # "112.87.68.39:999",
    # "112.87.68.39:999",
    # "112.85.165.3:999",
    # "122.193.245.197:999",
    # "112.85.128.245:999",
    "139.227.162.32:811"
    ]

proxies = {
    'http': "http://{}".format(random.choice(proxies_pool)),
    'https': "https://{}".format(random.choice(proxies_pool))
}

print(proxies)