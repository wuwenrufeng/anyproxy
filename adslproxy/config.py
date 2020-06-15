#coding:utf-8

# 拨号间隔
ADSL_CYCLE = 100

# 拨号出错重试间隔
ADSL_ERROR_CYCLE = 5

# ADSL命
ADSL_BASH = 'adsl-stop;adsl-start'

# 代理运行端口
PROXY_PORT = 8888

# 客户端唯一标识
CLIENT_NAME = 'ads11'

# 拨号网卡
ADSL_IFNAME = 'ppp0'

# Redis数据库ip
# REDIS_HOST = 'localhost'
REDIS_HOST = '114.116.13.33'

# Redis数据库密码，如无则填None
# REDIS_PASSWORD = None
REDIS_PASSWORD = "mredis333"

# Redis数据库端口
REDIS_PORT = 6379

# 代理池键名
PROXY_KEY = 'adsl'

# 测试URL
TEST_URL = 'https://www.baidu.com/'

# 测试超时时间
TEST_TIMEOUT = 20

# API端口
API_PORT = 8000