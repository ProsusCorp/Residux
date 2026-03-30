"""Estructura de datos para la historia episódica y misiones"""
from enum import Enum

class MissionStatus(Enum):
    LOCKED = "locked"
    AVAILABLE = "available"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Mission:
    """Representa una misión episódica"""
    def __init__(self, id, title, description, objectives, narrative_intro, narrative_outro):
        self.id = id
        self.title = title
        self.description = description
        self.objectives = objectives  # Lista de objetivos
        self.narrative_intro = narrative_intro  # Texto narrativo de introducción
        self.narrative_outro = narrative_outro  # Texto narrativo de conclusión
        self.status = MissionStatus.LOCKED
        self.progress = {}  # Progreso de cada objetivo

    def check_completion(self):
        """Verifica si la misión está completada"""
        return all(
            self.progress.get(obj["id"], 0) >= obj["target"]
            for obj in self.objectives
        )

# Misiones episódicas
EPISODE_1 = Mission(
    id="episode_1",
    title="Primeros Pasos",
    description="Aprende los fundamentos de la recolección de residuos",
    objectives=[
        {"id": "collect_5", "name": "Recolecta 5 residuos", "target": 5},
        {"id": "collect_wood", "name": "Recolecta 2 piezas de madera", "target": 2}
    ],
    narrative_intro={
        "narrator": "Bienvenido, joven recolector. En este mundo, cada residuo cuenta. Tu misión comienza aquí.",
        "mentor": "Hola, soy el Dr. Robins. Te guiaré en tus primeros pasos. Recuerda: la práctica hace al maestro."
    },
    narrative_outro={
        "narrator": "Has completado tu primera misión. El camino hacia un planeta más limpio ha comenzado.",
        "mentor": "¡Excelente trabajo! Estás aprendiendo rápido. Prepárate para desafíos mayores."
    }
)

EPISODE_2 = Mission(
    id="episode_2",
    title="Diversidad de Materiales",
    description="Aprende a identificar y recolectar diferentes tipos de residuos",
    objectives=[
        {"id": "collect_10", "name": "Recolecta 10 residuos", "target": 10},
        {"id": "collect_all_types", "name": "Recolecta al menos uno de cada tipo", "target": 5}
    ],
    narrative_intro={
        "narrator": "Ahora que conoces lo básico, es momento de expandir tus conocimientos.",
        "scientist": "Cada material tiene propiedades únicas. Aprender a identificarlos es crucial."
    },
    narrative_outro={
        "narrator": "Tu conocimiento crece. Ahora entiendes la importancia de la diversidad en el reciclaje.",
        "scientist": "Bien hecho. La clasificación correcta es el primer paso hacia un reciclaje efectivo."
    }
)

EPISODE_3 = Mission(
    id="episode_3",
    title="Velocidad y Precisión",
    description="Mejora tu eficiencia recolectando residuos rápidamente",
    objectives=[
        {"id": "collect_20", "name": "Recolecta 20 residuos", "target": 20},
        {"id": "time_limit", "name": "Completa en menos de 5 minutos", "target": 1}
    ],
    narrative_intro={
        "narrator": "La velocidad es importante, pero nunca a costa de la precisión.",
        "mentor": "Enfócate en mejorar tu técnica. La velocidad vendrá con la práctica."
    },
    narrative_outro={
        "narrator": "Has demostrado que puedes ser rápido y preciso. Una combinación poderosa.",
        "mentor": "¡Impresionante! Tu progreso es notable. Estás listo para desafíos reales."
    }
)

# Lista de todas las misiones
ALL_MISSIONS = [EPISODE_1, EPISODE_2, EPISODE_3]

# Eventos narrativos por modalidad
TRAINING_EVENTS = {
    "start": {
        "narrator": "Bienvenido al modo de entrenamiento. Aquí perfeccionarás tus habilidades antes de enfrentar el mundo real.",
        "mentor": "No te preocupes si cometes errores. Este es el lugar perfecto para aprender."
    },
    "first_collection": {
        "narrator": "Has recolectado tu primer residuo. Un pequeño paso para ti, un gran paso para el planeta.",
        "eco_expert": "¡Bien hecho! Cada residuo que reciclas ayuda a reducir la contaminación."
    },
    "level_complete": {
        "narrator": "Nivel completado. Tu dedicación al reciclaje es admirable.",
        "mentor": "Sigue así. Estás mejorando constantemente."
    }
}

TERRAIN_EVENTS = {
    "start": {
        "narrator": "Ahora estás en el terreno real. Aquí cada acción tiene consecuencias reales.",
        "scientist": "Usa todos los sensores del robot. La información es tu mejor aliada."
    },
    "connection_lost": {
        "narrator": "Se ha perdido la conexión con el robot. Mantén la calma.",
        "mentor": "Esto puede pasar. Verifica la conexión y vuelve a intentar."
    }
}

