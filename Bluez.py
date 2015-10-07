# File: Bluez.py / Note: Simple Class To Connect To Bluetooth Devices
# Date: --/--/-- / Author: Shaid Khan
#!/usr/bin/python

# Note For Developers:  In Reality You Should Not Import The Entire
# Module When It Come To Actual Program (Really For Standard Sake).
# For Those Who Are New To Python: "#!/usr/bin/python" = UNIX 
# Note: Required PyBluez Library
from bluetooth import *;

class Bluez:
    " Note: Simple Class To Connect To Bluetooth Devices "
    
    def __init__(self, device_name = "Default Devices", port = 1):
        """ Note: Constructor Method To Initialise Bluez 
            @param: device_name = Connecting Device Name
            'param: port :: Socket Port Number """
        # Note: _mac Used To Store Device Mac Address
        self._name = device_name;
        self._mac = None;

    def __str__(self):
        """ Note: Method To Return String Instance """
        return "Device: " + self._name + self._mac;

    @property
    def name(self):
        """ Note: Return Store Name Of Device """
        return self._name;

    @property
    def mac(self):
        """ Note: Return Store Mac Address """
        return self._mac;

    def quick_s(self):
        """ Note: Method To Quickly Scan For Devices """
        # Note: Quickly Use This To Search Fr Device
        try:
            devices = discover_devices(8, True, True);
            if (len(devices) > 0):
                print devices;
        except IOError:
            self.__messages(0);

    def search(self):
        """ Note: Method To Scan For Nearby Devices """
        try:
            devices = discover_devices(8, True, True);
            if (len(devices) > 0):
                self.__confirm(devices);
                print devices;
            else:
                self.__messages(1);
        except IOError:
            self.__messages(0);

    def __confirm(self, arr):
        # Note: Method To Confirm The Device 
        # @param: arr = List Of Devices "
        for device in arr:
            if (self._name == device[1]):
                if (is_valid_address(device[0])):
                    self._mac = device[0];
                    self.__messages(1)
                    self.__connect();
                else:
                    self.__message(1);

    def __connect(self):
        # Note: Method To Connect To Device "
        sock = BluetoothSocket(RFCOMM);
        sock.connect((self._mac, 1));
        self.__str__()
        
    def __messages(self, num):
        # Note: Method To Display Messages "
        if num == 0:
            print " Check Bluetooth Module ";
        if num == 1:
            print " Device Not Found ";
        if num == 2:
            print " Device Found ";

 
if __name__ == "__main__":
    bluez = Bluez("YOUR DEVICE NAME")
    bluez.search()
