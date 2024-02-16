from Adafruit_IO import Client, Feed, Data
aio = Client("chaitu3663","aio_xhxn58SYDY15eTpVu99DfQCfgtRf")

feed = Feed(name='LAPTOP/SYSTEM')

# Send the Feed to IO to create.
# The returned object will contain all the details about the created feed.
result = aio.create_feed(feed)