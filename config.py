import os
MQTT_HOST = os.getenv("MQTT_HOST", "192.168.0.253")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USERNAME = os.getenv("MQTT_USERNAME", "")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", "")
MQTT_DYNALITE_PREFIX = os.getenv("MQTT_DYNALITE_PREFIX", "dynalite")
MQTT_HOMEASSISTANT_PREFIX = os.getenv("MQTT_HOMEASSISTANT_PREFIX", "homeassistant")                                         
MQTT_DYNALITE_WILL = os.getenv("MQTT_DYNALITE_WILL","dynalite/status")
MQTT_BRIDGE_WILL =  os.getenv("MQTT_BRIDGE_WILL", "bridges/light_dynalite") 
MQTT_DEBUG =  os.getenv("MQTT_DEBUG", False) 
SW_VER = os.getenv("SW_VER", "0.1a") 
PRESET_NONE_OFF =  os.getenv("PRESET_NONE_OFF", True) #set Preset = None to Preset 4 (OFF). 
CONFIG_PATH = os.getenv("CONFIG_PATH", "dynalite_map.yaml") 
CONFIG_PORT = os.getenv("CONFIG_PORT", 8915) 