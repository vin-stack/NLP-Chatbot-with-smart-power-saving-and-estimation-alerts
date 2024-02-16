from Adafruit_IO import Client, Feed, Data
ADAFRUIT_IO_USERNAME = "chaitu3663"
ADAFRUIT_IO_KEY = "aio_xhxn58SYDY15eTpVu99DfQCfgtRf"
aio = Client('ADAFRUIT_IO_USERNAME','ADAFRUIT_IO_KEY')
currentTemperature = aio.receive('DEVICE1').value