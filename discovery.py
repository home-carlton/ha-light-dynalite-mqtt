# discovery.py
import json
from config import SW_VER, MQTT_HOMEASSISTANT_PREFIX
from utils import log


def publish_light_discovery(mqtt_client, dynalite_map):
    for area_id, area_cfg in dynalite_map.get("areas", {}).items():
        try:
            area_name = area_cfg.get("name", f"Area {area_id}")
            uid = f"dynet_area_{area_id}"
            device_id = {
                "device": {
                    "identifiers": [uid],
                    "name": f"Area {area_id} - {area_name}",
                    "manufacturer": "Nerih82",
                    "model": "Philips Dynalite MQTT Bridge",
                    "sw_version": f"{SW_VER}"
                }
            }

            for channel_str, light in area_cfg.get("channels", {}).items():
                try:
                    light_name = light.get("name", f"Light {channel_str}")
                    style = light.get("style", dynalite_map.get("defaults", {}).get("light_style", "dimmable"))
                    l_uid = f"channel_{channel_str}"
                    base_topic = f"{MQTT_HOMEASSISTANT_PREFIX}/light/{uid}/{l_uid}"
                    topic = f"{base_topic}/config"

                    payload = {
                        "platform": "light",
                        "name": light_name,
                        "unique_id": f"{uid}_{l_uid}",
                        "availability_topic": "bridges/light_dynalite/status",
                        "retain": False,
                        "icon": light.get("icon", "mdi:lightbulb")
                    }
                    payload.update(device_id)

                    if style.lower() == "dimmable":
                        payload.update({
                            "brightness_state_topic": f"{base_topic}/brightness",
                            "brightness_command_topic": f"{base_topic}/brightness/set",
                            "brightness_value_template": "{{ value | int }}",
                            "state_topic": f"{base_topic}/brightness",
                            "state_value_template": "{{ 'ON' if value | int > 0 else 0 }}",
                            "command_topic": f"{base_topic}/brightness/set",
                            "on_command_type": "brightness",
                            "payload_off": 0
                        })

                    mqtt_client.publish(topic, json.dumps(payload), retain=True)
                    log(f"📡 Published light discovery → {payload['name']}")

                except Exception as e:
                    log(f"❌ Failed to publish light #{channel_str} in area {area_id}: {e}")

        except Exception as e:
            log(f"❌ Failed to process area {area_id}: {e}")
