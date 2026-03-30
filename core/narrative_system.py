"""Sistema de narración y gestión de diálogos"""
import random
from narrative.characters import CHARACTERS, CharacterType
from narrative.eco_tips import get_tip_by_waste_type, get_contextual_tip, get_general_tip
from narrative.story_data import Mission, MissionStatus

class NarrativeSystem:
    """Sistema principal de narración del juego"""
    def __init__(self, config=None):
        self.config = config or {}
        self.current_mission = None
        self.message_queue = []
        self.active_character = None
        self.text_speed = self.config.get("text_speed", "normal")
        self.auto_advance = self.config.get("auto_advance", False)

    def set_mission(self, mission):
        """Establece la misión actual"""
        self.current_mission = mission
        if mission:
            # Mostrar introducción narrativa
            self.trigger_narrative_event("mission_start", mission)

    def trigger_narrative_event(self, event_type, context=None):
        """Dispara un evento narrativo"""
        if event_type == "mission_start" and context:
            # Mostrar introducción de la misión
            intro = context.narrative_intro
            for char_key, text in intro.items():
                if char_key in CHARACTERS:
                    self.add_message(CHARACTERS[char_key], text)

        elif event_type == "mission_complete" and context:
            # Mostrar conclusión de la misión
            outro = context.narrative_outro
            for char_key, text in outro.items():
                if char_key in CHARACTERS:
                    self.add_message(CHARACTERS[char_key], text)
            # Consejo contextual
            tip = get_contextual_tip("mission_complete")
            self.add_message(CHARACTERS["eco_expert"], tip)

        elif event_type == "waste_collected":
            waste_type = context.get("type") if context else None
            if waste_type:
                tip = get_tip_by_waste_type(waste_type)
                self.add_message(CHARACTERS["eco_expert"], tip)

        elif event_type == "first_collection":
            tip = get_contextual_tip("first_collection")
            self.add_message(CHARACTERS["mentor"], tip)

        elif event_type == "combo":
            tip = get_contextual_tip("combo")
            self.add_message(CHARACTERS["narrator"], tip)

    def add_message(self, character, text):
        """Añade un mensaje a la cola"""
        self.message_queue.append({
            "character": character,
            "text": text,
            "timestamp": 0  # Se actualizará cuando se muestre
        })

    def get_next_message(self):
        """Obtiene el siguiente mensaje de la cola"""
        if self.message_queue:
            return self.message_queue.pop(0)
        return None

    def has_pending_messages(self):
        """Verifica si hay mensajes pendientes"""
        return len(self.message_queue) > 0

    def clear_messages(self):
        """Limpia todos los mensajes pendientes"""
        self.message_queue = []

    def get_narrator_message(self, text):
        """Obtiene un mensaje del narrador"""
        return {
            "character": CHARACTERS["narrator"],
            "text": text
        }

    def get_character_tip(self, character_key, context=None):
        """Obtiene un consejo de un personaje específico"""
        if character_key in CHARACTERS:
            if context:
                tip = get_contextual_tip(context)
            else:
                tip = get_general_tip()
            return {
                "character": CHARACTERS[character_key],
                "text": tip
            }
        return None

