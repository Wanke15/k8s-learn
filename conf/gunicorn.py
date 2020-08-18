bind = '0.0.0.0:3080'

workers = 4

proc_name = 'app'

loglevel = 'debug'

logfile = './log/debug.log'

accesslog = "./log/access.log"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s %(D)d'

timeout = 90

keepalive = 75  # needs to be longer than the ELB idle timeout

worker_class = 'gevent'
