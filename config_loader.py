# config_loader.py
import yaml
from utils import log

def load_dynalite_config(path):
    try:
        f = open(path, "r")
        dynalite_map = yaml.safe_load(f) or {}  # fallback to empty dict
        f.close()
        log("✅ Loaded Dynalite config")
        if not isinstance(dynalite_map, dict):
            log("⚠️ Config is not a dictionary")
            return {}

        if "areas" not in dynalite_map:
            log("⚠️ Config missing 'areas' key")

        return dynalite_map

    except Exception as e:
        log(f"❌ Failed to load Dynalite config: {e}")
        return {}
