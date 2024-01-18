# Minimalistic Python Server Code
This repo contains an example of the basic, boilerplate code for a Python-based HTTP server. The server was coded on and designed to run on a Linux-based Raspberry Pi (Raspberry Pi Zero W to be specific), but can be extrapolated to run on almost any OS-based device.

The server code can be found in the [server.py](./server.py) module.

[This learing resource](https://realpython.com/python-sockets/) was used for learning as I made this.

## Making Requests
When the server is running, the client will need to make HTTP requests to the server using both the server device's local IP address **and** port number it is listening on. For example:

![example request](https://i.imgur.com/yEQI3HN.png)

In the above example, HTTP requests are being made through Postman, directing the requests at the server's local IP address, followed by a colon, and the port number the server is listening on (configured in the server code).

If you instead want to simply *only* want to have to specify the server's IP address and *not* a port number, I *believe* you simply need to run the server on the HTTP-dedicated port, **port 80**. But, running it on a "privileged" port, ports between 0 and 1023, will require `sudo` or `root` privileges to run and begin listening on.
