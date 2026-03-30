"""Definición de personajes del juego"""
from enum import Enum

class CharacterType(Enum):
    NARRATOR = "narrator"
    MENTOR = "mentor"
    SCIENTIST = "scientist"
    ECO_EXPERT = "eco_expert"

class Character:
    """Clase base para personajes del juego"""
    def __init__(self, name, character_type, personality, color=(255, 255, 255)):
        self.name = name
        self.type = character_type
        self.personality = personality
        self.color = color  # Color para el texto del personaje
        self.dialogs = []

    def add_dialog(self, dialog_text, context=None):
        """Añade un diálogo al personaje"""
        self.dialogs.append({
            "text": dialog_text,
            "context": context
        })

# Personajes principales
NARRATOR = Character(
    name="Narrador",
    character_type=CharacterType.NARRATOR,
    personality="omnisciente, sabio, educativo",
    color=(200, 200, 255)
)

MENTOR = Character(
    name="Dr. Robins",
    character_type=CharacterType.MENTOR,
    personality="amigable, motivador, paciente",
    color=(100, 255, 100)
)

SCIENTIST = Character(
    name="Dra. Martínez",
    character_type=CharacterType.SCIENTIST,
    personality="técnica, precisa, entusiasta",
    color=(255, 200, 100)
)

ECO_EXPERT = Character(
    name="Eco-Guía",
    character_type=CharacterType.ECO_EXPERT,
    personality="apasionado, informativo, inspirador",
    color=(100, 255, 200)
)

# Diccionario de personajes
CHARACTERS = {
    "narrator": NARRATOR,
    "mentor": MENTOR,
    "scientist": SCIENTIST,
    "eco_expert": ECO_EXPERT
}

