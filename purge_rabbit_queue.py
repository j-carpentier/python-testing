# python
import argparse

from amqplib import client_0_8 as amqp

def parse_the_things():
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help='rabbit hostname')
    parser.add_argument('user', help='rabbit user')
    parser.add_argument('password', help='rabbit password')
    parser.add_argument('vhost', help='rabbit virtual host')
    parser.add_argument('queue', help='queue needing to be purged')
    options = parser.parse_args()
    return options


# example
# HOST = "rabbitmq01.example.com:5672"
# USER = "nova"
# PASSWORD = "**********"
# VHOST = "nova"
# PURGE_QUEUE = "compute.c-10-23-43-13"
 
options = parse_the_things()
HOST = options.host + ":5672"
USER = options.user
PASSWORD = options.password
VHOST = options.vhost
PURGE_QUEUE = options.queue

conn = amqp.Connection(host=HOST, userid=USER, password=PASSWORD,
                       virtual_host=VHOST, insist=False)
chnl = conn.channel()
chnl.queue_purge(PURGE_QUEUE)

quit()
