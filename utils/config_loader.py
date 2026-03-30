"""Cargador de configuración del juego"""
import json
import os

class ConfigLoader:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.config = self.load_config()
    
    def load_config(self):
        """Carga la configuración desde el archivo JSON"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Configuración por defecto
            return {
                "robot": {
                    "ip": "192.168.149.1",
                    "websocket_port": 7788,
                    "rpc_port": 9030,
                    "video_port": 8080
                },
                "game": {
                    "window_width": 1280,
                    "window_height": 720,
                    "fps": 60,
                    "language": "es"
                },
                "audio": {
                    "music_volume": 0.5,
                    "sfx_volume": 0.7,
                    "voice_volume": 0.8
                },
                "narrative": {
                    "text_speed": "normal",
                    "auto_advance": False,
                    "show_subtitles": True
                }
            }
    
    def get(self, *keys):
        """Obtiene un valor de configuración usando claves anidadas"""
        value = self.config
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return None
        return value
    
    def save_config(self):
        """Guarda la configuración en el archivo"""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)

