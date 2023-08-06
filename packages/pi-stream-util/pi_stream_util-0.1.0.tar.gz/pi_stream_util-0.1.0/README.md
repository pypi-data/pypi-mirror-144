# pi_stream_util

*Self managed stream processor for PI Web API Channels*

pi_stream_util is an abstraction layer built on the [piwebasync](https://github.com/newvicx/piwebasync) `WebsocketClient`. It is designed to be a reliable and resilient message processor for incoming data from a PI Web API channel connection. The purpose of pi_stream_util is to receive incoming messages from a channel endpoint, handle the messages, and pass the processed messages onto an async queue. Typically, messages passed along to the queue are picked up by a producer process which publishes the messages to a broker.

## Installation

Install pi_stream_util using pip:

```
pip install pi-stream-util
```

## Usage

### Basic usage

```python
import asyncio

from piwebasync import Controller, WebsocketMessage
from pi_stream_util import Stream

def handler(message: WebsocketMessage):
    return WebsocketMessage

async def main():
    webid = 'my_webid'
    request = Controller('wss', 'mypihost', root='piwebapi').streamsets.get_channel_adhoc([webid])
    queue = asyncio.Queue()
    stream = Stream(queue)
    # Start the stream
    stream_id = await stream.start(request, handler)
    # Stream will start processing messages and putting them in the queue
    # Stop the stream
    await stream.stop()
    
```

### Live Updating

You can update a stream in real time to add additional points/attributes

```python
new_request = Controller('wss', 'mypihost', root='piwebapi').streamsets.get_channel_adhoc([webid, new_webid])
await stream.update(new_request)
```

If an update fails, the default behavior is to rollback the stream to the previous request. If an update fails but the stream rolls back successfully, a `ChannelRollback` error will be raised. Optionally you can set `rollback=False` and if an update fails, a `ChannelUpdateError` will be raised and the stream will not process anymore messages

### Stream Error Callbacks

You can assign a callback function to be called when the stream encounters an error and closes the websocket connection. This feature is helpful when you have several streams running under a manager type object. The callback can trigger the manager to send an alert and potentially try and restart the stream. The callback can be set as an optional parameter in the `start()` coroutine

```python
def error_callback(fut: asyncio.Future):
    print("Stream encountered an error")
    
await stream.start(request, handler, on_error_callback=error_callback)
```

### Stopping the Stream

You can stop the stream by calling the `stop()` coroutine. This will handle cleanly closing the websocket connection. `stop()` is idempotent, meaning multiple calls to `stop()` will have no effect and will just return immediately. When `stop()` is called for the first time, if the stream encountered an error during processing, that error will be raised when calling `stop()`

```python
try:
    await stream.stop()
except PIWebAsyncException:
    # Do something with error
    raise
```

## Requirements

- piwebasync>=0.1.1

## Supports

- python>=3.9