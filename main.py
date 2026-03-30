"""Punto de entrada principal de Residux_01"""
import os
from ursina import *
from utils.config_loader import ConfigLoader
from modes.training_mode import TrainingMode

# Crear aplicación Ursina
app = Ursina()

# Configurar ventana
window.title = 'Residux_01 - Robot Recolector'
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True

# Cargar configuración
# Prioriza configuración local no versionada.
if os.path.exists("config.local.json"):
    config_path = "config.local.json"
elif os.path.exists("config.json"):
    config_path = "config.json"
else:
    config_path = "config.example.json"

config_loader = ConfigLoader(config_path)
config = config_loader.config

# Crear modo entrenamiento
training_mode = TrainingMode(app, config)

def update():
    """Función de actualización global"""
    training_mode.update()

# Ejecutar el juego
app.run()
