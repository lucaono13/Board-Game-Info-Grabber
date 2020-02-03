cd Board-Game-Info-Grabber
call venv/scripts/activate venv
pyuic5 main_window.ui -o app.py
pyuic5 info_to_grab.ui -o info.py