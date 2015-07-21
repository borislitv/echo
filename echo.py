#!/usr/bin/env python

from cocaine.worker import Worker
import msgpack

DEFAULT_HEADERS = [('Content-type', 'text/plain')]


def echo(request, response):
    yield request.read()
    response.write(msgpack.packb((200, DEFAULT_HEADERS)))
    response.write("echo")
    response.close()

def main():
    w = Worker()
    w.run({"http": echo})

if __name__ == "__main__":
    main()
