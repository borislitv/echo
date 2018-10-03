#!/usr/bin/env python

from cocaine.logger import Logger
from cocaine.worker import Worker
import msgpack

DEFAULT_HEADERS = [('Content-type', 'text/plain')]

log = Logger()

def echo(request, response):
    log.info("entire echo()")
    yield request.read()
    log.info("do echo().request.read()")
    response.write(msgpack.packb((200, DEFAULT_HEADERS)))
    log.info("do echo().response.write() with code and headers")
    response.write("echo")
    log.info("do echo().response.write(echo), next echo().response.close()")
    response.close()
    log.info("do echo().response.close() and exit now")

def main():
    log.info("entire main()")
    w = Worker()
    log.info("do main().Worker()")
    w.run({"http": echo})

if __name__ == "__main__":
    log.info("start echo application worker. prior main()")
    main()
