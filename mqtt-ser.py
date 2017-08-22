#!/usr/bin/env python

"""
mqtt-ser.py - monitor the serial port and send the data to the MQTT server on
topic: "topic/debug" (initial hello message)
topic: "home/debug" + port + "/chipkit/mqtt" (msg line from the serial port)

https://pypi.python.org/pypi/paho-mqtt/1.1

MQTT Client

You can use the client class as an instance, within a class or by
subclassing. The general usage flow is as follows:

    Create a client instance
    Connect to a broker using one of the connect*() functions
    Call one of the loop*() functions to maintain network traffic flow with the broker
    Use subscribe() to subscribe to a topic and receive messages
    Use publish() to publish messages to the broker
    Use disconnect() to disconnect from the broker

Callbacks will be called to allow the application to process events as
necessary. These callbacks are described below.

http://www.hivemq.com/blog/mqtt-essentials-part-1-introducing-mqtt
http://www.hivemq.com/blog/mqtt-essentials-part2-publish-subscribe
http://www.hivemq.com/blog/mqtt-essentials-part-3-client-broker-connection-establishment
http://www.hivemq.com/blog/mqtt-essentials-part-4-mqtt-publish-subscribe-unsubscribe
http://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices

"""

# From my Turbine code
import os                       # env stuff, etc.
import sys
import time
import signal
import traceback
import atexit

# From the Arduino site
import serial

print >>sys.stderr, "ser.py starting"

# ----------------------------------------------------------------------------
# set debug on the command line
# (export NJCDEBUG=1; python ./turbine-test.py)
njcDebug = os.getenv('NJCDEBUG', 0)

# ------------------------------------------------------------------------------
# Get the user options
if(len(sys.argv) == 2) :
    port = sys.argv[1];
else :
    port = "/dev/ttyAMA0"
#

# Serial speed 9600
Speed = 115200

###
### Perhaps I need a way to open the port without the reset
###
ser = serial.Serial(port, Speed)

print >>sys.stderr, "Got the serial port"

# Need to catch ^C
# ==============================================================================
# At the end make sure we get the error log
def cleanup():
    print >>sys.stderr, 'all_done()'
#

# Catch ^C
def interrupt_handler(signal, frame):
    print "\nInterrupt handled"
    sys.exit(0)
#

# Deal with a user interrupt (^C)
signal.signal(signal.SIGINT, interrupt_handler)

# ------------------------------------------------------------------------------
#
print >>sys.stderr, "starting loop"

# loop forever
while True:
    """
    I need to add a catch here so when the device reboots and we lose the USB
    connection we reconnect.
    """

    # I think we're missing the mqClient.loop() function
    # I think this will be handled above in the:
    # mqClient.loop_start()

    # Get the serial output and print it to MQ #
    # Need to catch
    try:
        txt =  time.strftime('%X ') + ser.readline().rstrip('\n')
        print txt

    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print >>sys.stderr, "SER Error: %s" % e
        # Close
        ser.close()
        # Sleep
        time.sleep(2)
        # Reopen
        ser = serial.Serial(port, Speed)
        print >>sys.stderr, "Reopen the serial port"
    # try/except

        
###
# -[ fini ]---------------------------------------------------------------------
