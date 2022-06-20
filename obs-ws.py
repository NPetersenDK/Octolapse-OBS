import asyncio
import simpleobsws
from datetime import datetime

# Outcomment these for logging and troubleshooting (has to be disabled when using OctoLapse)
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Varibles:
filepath = "C:/Users/AAAA/BBBB/CCCC"
fileprefix = "tlapse"

OBSIP = "X.X.X.X"
OBSPORT = "4444"
OBSWSPASSWORD = "OBS WEBSOCKET PW"

parameters = simpleobsws.IdentificationParameters() # Create an IdentificationParameters object
ws = simpleobsws.WebSocketClient(url = 'ws://'+OBSIP+':'+OBSPORT, password = OBSWSPASSWORD, identification_parameters = parameters)

async def make_request():
    await ws.connect() # Make the connection to obs-websocket
    await ws.wait_until_identified() # Wait for the identification handshake to complete

    now = datetime.now()
    date = now.strftime("%d-%m-%Y-%H-%M-%S")
    request = simpleobsws.Request('SaveSourceScreenshot', {'sourceName': "OctoLapse", 'imageFormat': "jpg", 'imageFilePath': filepath+fileprefix+"-"+date+".png"})
    ret = await ws.call(request) # Perform the request
    #if ret.ok(): # Check if the request succeeded
    #    print("Request succeeded! Response data: {}".format(ret.responseData))


    await ws.disconnect() # Disconnect from the websocket server cleanly

loop = asyncio.get_event_loop()
loop.run_until_complete(make_request())
