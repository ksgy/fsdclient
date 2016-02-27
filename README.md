# FSD Client

### Connect to Private FSD server with X-Plane 64 bit 

If you're running and flying on a private [FSD server](https://flightsimulatornetwork.wordpress.com/installing-windows-fsd-server/) you can only use X-Plane 32 bit with [XSquawkbox](http://www.xsquawkbox.net/xsb/download/)

This small Python and [FlyWithLua](https://github.com/X-Friese/FlyWithLua) script tries to solve this problem.

### What it does?

The Lua script creates a file every now and then and writes all the required flight data to a file.

The Python script reads that file opens a socket to the FSD server and sends your flight data, so you appear on radar :)

### TODO

- [ ] GUI
- [ ] Multiplayer planes
- [ ] Use [ExtPlane](https://github.com/vranki/ExtPlane) or [Python Interface for X-Plane](http://www.xpluginsdk.org/python_interface.htm) instead of writing a file with Lua


