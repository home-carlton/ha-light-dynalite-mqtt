# 🧠 HA Light Dynalite MQTT Bridge

This project bridges a **Dynalite lighting system** to **Home Assistant** using **MQTT**. It listens to Dynet packets, maps them to Home Assistant lights, and vice versa — with full support for brightness presets, area/channel mappings, and bidirectional sync.

It also includes a lightweight **Web UI editor** to modify `dynalite_map.yaml` at runtime.

---

## 🚀 Features

- 🧠 **Bi-directional sync** between Dynalite (via Dynet1/2) and Home Assistant
- 🛠️ **Web-based YAML config editor** (`dynalite_map.yaml`)
- 🧩 Auto publishes Home Assistant light discovery topics
- 🧾 Preset ↔ Brightness level mapping with caching
- 🕵️ Dynamic response tracking with UUID-based correlation
- 🧘 Clean async architecture and MQTT handling

---

## 📁 Project Structure

ha-light-dynalite-mqtt/
│
├── App/
│ ├── app.py # Main entrypoint for the bridge
│ ├── message_handlers.py # Dynet packet processing logic
│ ├── mqtt_handlers.py # MQTT pub/sub setup
│ ├── config_loader.py # Loads YAML config
│ ├── utils.py # Logging and helper functions
│ └── discovery.py # Home Assistant MQTT discovery publisher
│
├── webui.py # Embedded Flask UI to edit dynalite_map.yaml
├── dynalite_map.yaml # Editable runtime config (areas, channels, presets)
├── requirements.txt # Python dependencies
└── README.md # You’re here!

---

## 🧰 Requirements

- Python 3.10+
- MQTT broker (e.g. Mosquitto)
- Home Assistant with MQTT integration
- Dynalite PDEG or IP gateway

---

## 🛠️ Installation

```bash
git clone https://github.com/yourname/ha-light-dynalite-mqtt.git
cd ha-light-dynalite-mqtt
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Requirements.txt
paho-mqtt
flask
pyyaml

🧾 dynalite_map.yaml Format
yaml
defaults:
  presets: [1, 2, 3, 4]
  levels: [255, 178, 26, 0]

areas:
  16:
    name: Show Kitchen
    channels:
      all:
        name: Show Kitchen (Master)
        presets: [1, 2, 3, 4]
        levels: [255, 178, 26, 0]
      "1":
        name: Spot Lights
      "2":
        name: Cove Lights
      "3":
        name: Shelves
        presets: [1, 4]
        levels: [255, 0]
🖥️ Run the Bridge
bash
python3 main.py
You will see logs like:

bash
📡 Published light discovery → Spot Lights
📡 Subscribed to homeassistant/light/dynet_area_16/channel_2/brightness/set
🌐 Web UI Editor
Edit dynalite_map.yaml live at:

arduino
http://localhost:8915
After saving:

Config is reloaded

Home Assistant lights are republished

🔄 Dynamic Reloads
When the config is updated via the Web UI:

dynalite_map.yaml is parsed

Discovery is re-published

New settings take effect instantly (no restart needed)

💡 Tip
To make edits safer, use preset-level mappings carefully, especially for channel: all master definitions. Every change is live!

📜 License
MIT License © 2025 Hiren Amin

