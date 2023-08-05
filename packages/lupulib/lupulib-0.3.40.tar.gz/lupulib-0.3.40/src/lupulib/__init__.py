# SYS imports
import os
import sys
from trace import Trace

# Append subdirectories to sys.path
ppath = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))
print(ppath)
qpath = os.path.dirname(__file__)
print(qpath)
fpath = os.path.join(os.path.dirname(__file__), 'devices')
sys.path.append(qpath)
sys.path.append(fpath)
print(sys.path)

# Old imports for API Calls
# import requests
# from requests.exceptions import HTTPError

# General Imports
import pickle
import time
import logging
import json
# import yaml
from pathlib import Path

# New imports to optimize API-Calls
from typing import Dict
import asyncio
import aiohttp
import urllib.error
import urllib.parse
import urllib.request

# Import from lupulib
import lupulib
import lupulib.devices
from lupulib.devices.binary_sensor import LupusecBinarySensor
from lupulib.devices.sensor import LupusecSensor
from lupulib.devices.switch import LupusecSwitch
from lupulib.devices.thermal_switch import LupusecThemalSwitch
from lupulib.devices.updown_switch import LupusecUpDownSwitch
import lupulib.constants as CONST
import lupulib.exceptions
# from lupulib.exceptions import LupusecParseError, LupusecRequestError, LupusecResponseError
# from lupulib.devices.binary_sensor import LupusecBinarySensor
# from lupulib.devices.switch import LupusecSwitch


_LOGGER = logging.getLogger(__name__)
home = str(Path.home())
# print(home)


class LupusecAPI:
    """Interface to Lupusec Webservices."""

    def __init__(self, username, password, ip_address) -> None:
        """LupusecAPI constructor to interface Lupusec Alarm System."""
        self._username = username
        self._password = password
        self._ip_address = ip_address
        _LOGGER.debug("LupusecAPI: ip-address=%s, username=%s, pwd=%s", 
            self._ip_address, self._username, self._password)
        self._url = "http://{}/action/".format(ip_address)
        self._model = "unknown"
        self._auth = None
        if self._username != None and self._password != None:
            self._auth = aiohttp.BasicAuth(login=self._username, password=self._password, encoding='utf-8')
            _LOGGER.debug("...set aiohttp.BasicAuth")
        self._system = None
        self._token = None

        # Try to access local cache file
        _LOGGER.debug(f"Check for Cache-File: {home}/{CONST.HISTORY_CACHE_NAME}")
        try:
            self._history_cache = pickle.load(
                open(home + "/" + CONST.HISTORY_CACHE_NAME, "rb")
            )
            _LOGGER.debug("...file exists.")
        # If local cache file does not exist -> create one    
        except Exception as e:
            _LOGGER.debug(e)
            self._history_cache = []
            pickle.dump(
                self._history_cache, open(home + "/" + CONST.HISTORY_CACHE_NAME, "wb")
            )
            _LOGGER.debug("...file created.")       

        # Set cache timestamps
        _LOGGER.debug(f"Cache current timestamp: {time.time()}")       
        self._cacheStampS = time.time()
        self._cacheStampP = time.time()
        #self._panel = self.get_panel()

        # Set device caches to none
        self._cacheBinarySensors = None
        self._cacheSensors = None
        self._cacheSwitches = None
        self._devices = None
        self._apiDevices = None


    # ToDo: should renamed to: _async_api_get()
    async def _async_api_call(ip, client, action_url) -> Dict:
        """Generic sync method to call the Lupusec API"""
        # Generate complete URL from Constants.py
        url = f'{CONST.URL_HTTP}{ip}{CONST.URL_ACTION}{action_url}'
        _LOGGER.debug("_async_api_call() called: URL=%s", url)
        start_time = time.time()
        _LOGGER.debug(f"Starttime: {start_time}")

        try:
            async with client.get(url) as resp:
                _LOGGER.debug("Response_Status=%s", resp.status)
                _LOGGER.debug("Content_Type=%s", resp.headers["content-type"])

                # check for Response Status other than 200
                if resp.status != 200:
                    _LOGGER.error(f"ERROR: Response status = {resp.status}")
                    return {}

                # check for non-JSON Response Headers   
                if not resp.headers["content-type"].strip().startswith("application/json"):
                    _LOGGER.error(f"ERROR: Content Type is not JSON = {resp.headers['content-type']}")
                    return {}

                # Get Response Body
                # content = await resp.json()
                content = await resp.text()

                # ToDo: check for empty body, size = 0
                content = content.replace(chr(245), "")
                content = content.replace("\t", "")
                clean_content = json.loads(content)
                _LOGGER.debug("Data Type of Response: =%s", type(clean_content))
                end_time = time.time()
                _LOGGER.debug(f"Endtime: {end_time}")   
                _LOGGER.debug(f"Duration: {end_time - start_time} seconds") 
                _LOGGER.debug("API-Call finished.")              
                return clean_content

        except aiohttp.client_exceptions.ClientConnectorError:
            _LOGGER.error("Cannot connect to: ", url)
            return {}

        except aiohttp.ContentTypeError:
            _LOGGER.error("JSON decode failed")
            return {}


    async def _async_api_post(ip, client, action_url, params) -> Dict:
        """Generic sync method to call the Lupusec API"""
        # Generate complete URL from Constants.py
        url = f'{CONST.URL_HTTP}{ip}{CONST.URL_ACTION}{action_url}'
        _LOGGER.debug("_async_api_post() called: URL=%s", url)
        start_time = time.time()
        _LOGGER.debug(f"Starttime: {start_time}")

        try:
            async with client.post(url, data=params, ssl=False) as resp:
                # check for Response Status other than 200
                _LOGGER.debug("Response_Status=%s", resp.status)
                if resp.status != 200:
                    _LOGGER.error(f"ERROR: Response status = {resp.status}")
                    return {}

                # check for non-JSON Response Headers   
                _LOGGER.debug("Content_Type=%s", resp.headers["content-type"])              
                if not resp.headers["content-type"].strip().startswith("application/json"):
                    _LOGGER.error(f"ERROR: Content Type is not JSON = {resp.headers['content-type']}")
                    content = await resp.text()
                    print(content)
                    return {}

                # Get Response Body
                content = await resp.text()

                # ToDo: check for empty body, size = 0
                content = content.replace(chr(245), "")
                content = content.replace("\t", "")
                clean_content = json.loads(content)
                _LOGGER.debug("Data Type of Response: =%s", type(clean_content))
                end_time = time.time()
                _LOGGER.debug(f"Endtime: {end_time}")   
                _LOGGER.debug(f"Duration: {end_time - start_time} seconds") 
                _LOGGER.debug("API-Call finished.")              
                return clean_content

        except aiohttp.client_exceptions.ClientConnectorError:
            _LOGGER.error("Cannot connect to: ", url)
            return {}

        except aiohttp.ContentTypeError:
            _LOGGER.error("JSON decode failed")
            return {}



    async def async_get_token(self) -> int:
        """Async method to get the a session token from Lupusec System."""
        _LOGGER.debug("__init__.py.async_get_token() called: ")

         # Get Session Token
        async with aiohttp.ClientSession(auth=self._auth) as client:
            tasks = []

            # INFO_REQUEST
            _LOGGER.debug("__init__.py.async_get_system(): REQUEST=%s", CONST.TOKEN_REQUEST)
            tasks.append(asyncio.ensure_future(LupusecAPI._async_api_call(self._ip_address, client, CONST.TOKEN_REQUEST)))

            # Print response list
            _LOGGER.debug("await asyncio.gather(*tasks)...")
            response_list = await asyncio.gather(*tasks)
            _LOGGER.debug("done. check content in response_list...")
            for content in response_list:
                print(content)
                _LOGGER.debug("response.getsizeof(): %s", sys.getsizeof(content)) 
                if (sys.getsizeof(content) > 0):
                    _LOGGER.debug("RESULT_RESPONSE: %s", content[CONST.RESPONSE_RESULT]) 
                    if (content[CONST.RESPONSE_RESULT] = 1)
                        _LOGGER.debug("RESPONSE_MESSAGE: %s", content[CONST.RESPONSE_MESSAGE]) 
                        if (content[CONST.RESPONSE_MESSAGE] <> "")
                            self._token = content[CONST.RESPONSE_MESSAGE]
                            _LOGGER.debug("Token: %s", self._token)    
                            return content[CONST.RESPONSE_RESULT]
                    return 0
                return 0
            return 0
        _LOGGER.debug("__init__.py.async_get_token() finished.")  

    async def async_get_system(self) -> None:
        """Async method to get the system info."""
        _LOGGER.debug("__init__.py.async_get_system() called: ")

         # Get System Info
        async with aiohttp.ClientSession(auth=self._auth) as client:
            tasks = []

            # INFO_REQUEST
            _LOGGER.debug("__init__.py.async_get_system(): REQUEST=%s", CONST.INFO_REQUEST)
            tasks.append(asyncio.ensure_future(LupusecAPI._async_api_call(self._ip_address, client, CONST.INFO_REQUEST)))

            # Print response list
            _LOGGER.debug("await asyncio.gather(*tasks)...")
            response_list = await asyncio.gather(*tasks)
            _LOGGER.debug("done. check content in response_list...")
            for content in response_list:
                print(content)
                if CONST.INFO_HEADER in content:
                    self._system = content[CONST.INFO_HEADER]
                    _LOGGER.debug("System Info: %s", self._system)                    
                    print("  Hardware-Version: ", self._system[CONST.SYS_HW_VERSION])
                    print("  Firmware-Version: ", self._system[CONST.SYS_SW_VERSION])                    

            # return devices.system.LupusecSystem(content)

        _LOGGER.debug("__init__.py.async_get_system() finished.")            


    async def async_set_mode(self, mode) -> None:
        """Async method to set alarm mode."""
        _LOGGER.debug("__init__.py.async_set_mode() called: ")
        _LOGGER.info("...set mode: %s", mode)

        params = {"mode": mode, "area": 1}

         # Set Alarm Mode
        async with aiohttp.ClientSession(auth=self._auth) as client:
            _LOGGER.debug("auth.encode: %s", self._auth.decode())            
            tasks = []

            # Get Session Token
            _LOGGER.debug("__init__.py.async_set_mode(): REQUEST=%s", CONST.TOKEN_REQUEST)
            tasks.append(asyncio.ensure_future(LupusecAPI.async_get_token()))
            _LOGGER.debug("await asyncio.gather(*tasks)...")
            response_list = await asyncio.gather(*tasks)
            _LOGGER.debug("done. check content in response_list...")
            for content in response_list:
                print(content)
                if (content <> 0):
                    _LOGGER.debug("Token: %s", self._token)
                    # SET_ALARM_REQUEST
                    _LOGGER.debug("__init__.py.async_set_mode(): REQUEST=%s", CONST.SET_ALARM_REQUEST)
                    tasks.append(asyncio.ensure_future(LupusecAPI._async_api_post(self._ip_address, client, 
                        CONST.SET_ALARM_REQUEST, params)))

                    # Print response list
                    _LOGGER.debug("await asyncio.gather(*tasks)...")
                    response_list = await asyncio.gather(*tasks)
                    _LOGGER.debug("done. check content in response_list...")
                    for content in response_list:
                        print(content)  
                        else
                            _LOGGER.debug("ERROR: no session Token available.")
            
        _LOGGER.debug("__init__.py.async_set_mode() finished.")


    def get_power_switches(self):
        _LOGGER.debug("get_power_switches() called:")
        stampNow = time.time()
        length = len(self._devices)
        if self._cachePss is None or stampNow - self._cacheStampP > 2.0:
            self._cacheStamp_p = stampNow
            response = self._request_get("pssStatusGet")
            response = self.clean_json(response.text)["forms"]
            powerSwitches = []
            counter = 1
            for pss in response:
                powerSwitch = {}
                if response[pss]["ready"] == 1:
                    powerSwitch["status"] = response[pss]["pssonoff"]
                    powerSwitch["device_id"] = counter + length
                    powerSwitch["type"] = CONST.TYPE_POWER_SWITCH
                    powerSwitch["name"] = response[pss]["name"]
                    powerSwitches.append(powerSwitch)
                else:
                    _LOGGER.debug("Pss skipped, not active")
                counter += 1
            self._cachePss = powerSwitches

        return self._cachePss


    def get_sensors(self):
        _LOGGER.debug("get_sensors() called:")
        stamp_now = time.time()
        if self._cacheSensors is None or stamp_now - self._cacheStampS > 2.0:
            self._cacheStampS = stamp_now
            response = self._request_get(self.api_sensors)
            response = self.clean_json(response.text)["senrows"]
            sensors = []
            for device in response:
                device["status"] = device["cond"]
                device["device_id"] = device[self.api_device_id]
                device.pop("cond")
                device.pop(self.api_device_id)
                if not device["status"]:
                    device["status"] = "Geschlossen"
                else:
                    device["status"] = None
                sensors.append(device)
            self._cacheSensors = sensors

        return self._cacheSensors


    async def api_get_devices(self) -> Dict:
        """Async method to get the device list from Lupusec System."""
        _LOGGER.debug("__init__.py.async_get_devices() called: ")
        # Get System Info
        async with aiohttp.ClientSession(auth=self._auth) as client:
            tasks = []

            # Device List REQUEST
            _LOGGER.debug("__init__.py.async_get_devices(): REQUEST=%s", CONST.DEVICE_LIST_REQUEST)
            tasks.append(asyncio.ensure_future(LupusecAPI._async_api_call(self._ip_address, client, CONST.DEVICE_LIST_REQUEST)))

            # Print response list
            _LOGGER.debug("await asyncio.gather(*tasks)...")
            response_list = await asyncio.gather(*tasks)
            _LOGGER.debug("done. check content in response_list...")
            for content in response_list:
                # Retreive Device Liste from Response
                if CONST.DEVICE_LIST_HEADER in content:
                    device_content = content[CONST.DEVICE_LIST_HEADER]
                    print("Number of devices=", len(device_content))                    
                    api_devices = []
                    for device in device_content:
                        #if "openClose" in device:
                        #        device["status"] = device["openClose"]
                        #        device.pop("openClose")
                        #device["device_id"] = device[self.api_device_id]
                        #device.pop("cond")
                        #device.pop(self.api_device_id)
                        #if device["status"] == "{WEB_MSG_DC_OPEN}":
                        #    print("yes is open " + device["name"])
                        #    device["status"] = 1
                        #if device["status"] == "{WEB_MSG_DC_CLOSE}" or device["status"] == "0":
                        #    device["status"] = "Geschlossen"
                        print("sid: ", device["sid"], ", name: ", device["name"], 
                            ", type: ", device["type"], ", status: ", device["status"])
                        api_devices.append(device)
                self._apiDevices = api_devices

        _LOGGER.debug("__init__.py.async_get_devices() finished.")            
        return self._apiDevices



    def get_panel(self):
        _LOGGER.debug("get_panel() called:")
	    # we are trimming the json from Lupusec heavily, since its bullcrap
        response = self._request_get("panelCondGet")
        if response.status_code != 200:
            raise Exception("Unable to get panel " + response.status_code)
        panel = self.clean_json(response.text)["updates"]
        panel["mode"] = panel[self.api_mode]
        panel.pop(self.api_mode)

        if self.model == 2:
            panel["mode"] = CONST.XT2_MODES_TO_TEXT[panel["mode"]]
        panel["device_id"] = CONST.ALARM_DEVICE_ID
        panel["type"] = CONST.ALARM_TYPE
        panel["name"] = CONST.ALARM_NAME

        history = self.get_history()

        if self.model == 1:
            for histrow in history:
                if histrow not in self._history_cache:
                    if (
                        CONST.MODE_ALARM_TRIGGERED
                        in histrow[CONST.HISTORY_ALARM_COLUMN]
                    ):
                        panel["mode"] = CONST.STATE_ALARM_TRIGGERED
                    self._history_cache.append(histrow)
                    pickle.dump(
                        self._history_cache,
                        open(home + "/" + CONST.HISTORY_CACHE_NAME, "wb"),
                    )
        elif self.model == 2:
            _LOGGER.debug("Alarm on XT2 not implemented")
        return panel

 
    def get_history(self):
        _LOGGER.debug("get_history() called: ")
        response = self._request_get(CONST.HISTORY_REQUEST)
        return self.clean_json(response.text)[CONST.HISTORY_HEADER]


    def refresh(self):
        _LOGGER.debug("refresh() called: ")
        """Do a full refresh of all devices and automations."""
        self.get_devices(refresh=True)


    async def get_devices(self, refresh=True) -> Dict:
        """Get all devices from Lupusec."""
        _LOGGER.debug("get_devices() called: ")
        # Make API-call only, if device list is empty or needs refresh
        if refresh or self._devices is None:
            _LOGGER.debug("...refreshing all devices...")
            if self._devices is None:
                self._devices = {}

            # timestamp_now = time.time()
            # if self._cacheSensors is None or timestamp_now - self._cacheStampS > CONST.UPDATE_FREQ:
            # Call api_get_devices()

            _LOGGER.debug("...starting API-Call api_get_devices()...")
            responseObject = await LupusecAPI.api_get_devices(self)
            #if responseObject and not isinstance(responseObject, (tuple, list)):
            #    responseObject = responseObject
            _LOGGER.debug("...API-Call: response received...")
            _LOGGER.debug("...iterate over all devices in responseObject:")
            for deviceJson in responseObject:
                print("sid: ", deviceJson["sid"], ", name: ", deviceJson["name"], 
                            ", type: ", deviceJson["type"], ", status: ", deviceJson["status"])
                # Attempt to reuse an existing device
                device = self._devices.get(deviceJson["name"])
                _LOGGER.debug("...device: " + deviceJson["name"])
                # No existing device, create a new one
                if device:
                    _LOGGER.debug("...update existing device: " + deviceJson["name"])
                    device.update(deviceJson)
                else:
                    _LOGGER.debug("...newDevice found: " + deviceJson["name"])
                    device = newDevice(deviceJson, self)

                    if not device:
                        _LOGGER.info("Device is unknown")
                        continue

                    self._devices[device.device_id] = device

            # We will be treating the Lupusec panel itself as an armable device.
            #panelJson = self.get_panel()
            #_LOGGER.debug("Get the panel in get_devices: %s", panelJson)
            #self._panel.update(panelJson)

            # alarmDevice = self._devices.get("0")
            #if alarmDevice:
            #    alarmDevice.update(panelJson)
            #else:
            #    alarmDevice = devices.LupusecAlarm.create_alarm(panelJson, self)
            #    self._devices["0"] = alarmDevice

        return list(self._devices.values())


    def get_device(self, device_id, refresh=False):
        """Get a single device."""
        _LOGGER.debug("get_device() called for single device: ")
        if self._devices is None:
            self.get_devices()
            refresh = False

        device = self._devices.get(device_id)

        if device and refresh:
            device.refresh()

        return device


    def get_alarm(self, area="1", refresh=False):
        """Shortcut method to get the alarm device."""
        _LOGGER.debug("get_alarm() called: ")
        if self._devices is None:
            self.get_devices()
            refresh = False

        return self.get_device(CONST.ALARM_DEVICE_ID, refresh)


    def clean_json(textdata):
            # textdata = textdata.replace(chr(245), "")
        return textdata


def newDevice(deviceJson, lupusec):
    """Create new device object for the given type."""
    type_tag = deviceJson.get("type")

    if not type_tag:
        _LOGGER.info("Device has no type")

    if type_tag in CONST.TYPES_BIN_SENSOR:
        _LOGGER.debug("newDevice(): name: " + deviceJson["name"] + "; type: " + str(type_tag) + " = BIN_SENSOR")
        return LupusecBinarySensor(deviceJson, lupusec)
    elif type_tag in CONST.TYPES_SENSOR:
        _LOGGER.debug("newDevice(): name=" + deviceJson["name"] + "; type=" + str(type_tag) + " = SENSOR")        
        return LupusecSensor(deviceJson, lupusec)
    elif type_tag in CONST.TYPES_SWITCH:
        _LOGGER.debug("newDevice(): name=" + deviceJson["name"] + "; type=" + str(type_tag) + "= SWITCH")        
        return LupusecSwitch(deviceJson, lupusec)
    elif type_tag in CONST.TYPES_UPDOWN_SWITCH:
        _LOGGER.debug("newDevice(): name=" + deviceJson["name"] + "; type=" + str(type_tag) + "= UPDOWN_SWITCH")        
        return LupusecThemalSwitch(deviceJson, lupusec)
    elif type_tag in CONST.TYPES_THERMAL_SWITCH:
        _LOGGER.debug("newDevice(): name=" + deviceJson["name"] + "; type=" + str(type_tag) + "= THERMAL_SWITCH")        
        return LupusecUpDownSwitch(deviceJson, lupusec)                
    else:
        _LOGGER.info("Device is not known")
    return None
