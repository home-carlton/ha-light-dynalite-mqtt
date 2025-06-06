# web_ui.py
from flask import Flask, request, render_template_string, redirect, url_for, flash
import yaml
import os
import time
from threading import Thread
from config import (
     CONFIG_PATH, CONFIG_PORT
)

_reload_func = None

def init_web_ui(config_path, reload_func):
    global _reload_func
    _reload_func = reload_func

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/", methods=["GET", "POST"])
def editor():
    if request.method == "POST":
        new_yaml = request.form.get("yaml_content", "")
        try:
            yaml.safe_load(new_yaml)  # Validate YAML
            f = open(CONFIG_PATH, "w")
            f.write(new_yaml)
            f.close()
            _reload_func()  # Call injected function
            flash("✅ Saved successfully!", "success")
        except yaml.YAMLError as e:
            flash(f"❌ YAML Error: {str(e)}", "danger")
        return redirect(url_for("editor"))
    else:
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH) as f:
                content = f.read()
        else:
            content = ""
        return render_template_string(TEMPLATE, yaml_content=content)

TEMPLATE = """
<!doctype html>
<title>Dynalite Map Editor</title>
<style>
    textarea { width: 100%; height: 80vh; font-family: monospace; font-size: 1em; }
    .flash { padding: 10px; margin-bottom: 10px; border-radius: 5px; }
    .success { background: #d4edda; color: #155724; }
    .danger { background: #f8d7da; color: #721c24; }
</style>
<h2>📝 Dynalite Config Editor</h2>
{% with messages = get_flashed_messages(with_categories=true) %}
  {% for category, message in messages %}
    <div class="flash {{ category }}">{{ message }}</div>
  {% endfor %}
{% endwith %}
<form method="post">
    <textarea name="yaml_content">{{ yaml_content }}</textarea><br>
    <button type="submit">💾 Save</button>
</form>
"""

def run_web_ui():
    def run():
        app.run(port=CONFIG_PORT, host="0.0.0.0", use_reloader=False)
    Thread(target=run, daemon=True).start()
