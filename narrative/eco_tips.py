"""Base de datos de consejos eco-educativos"""
import random

# Consejos por tipo de residuo
TIPS_BY_WASTE_TYPE = {
    "madera": [
        "La madera reciclada puede convertirse en compost o nuevos productos de construcción.",
        "Un árbol tarda años en crecer, pero podemos reutilizar la madera muchas veces.",
        "La madera reciclada reduce la necesidad de talar nuevos árboles."
    ],
    "metal": [
        "El metal puede reciclarse infinitamente sin perder calidad.",
        "Reciclar una lata de aluminio ahorra suficiente energía para hacer funcionar una TV por 3 horas.",
        "El acero reciclado usa 75% menos energía que producir acero nuevo."
    ],
    "plastico": [
        "El plástico tarda entre 100 y 1000 años en degradarse naturalmente.",
        "Solo el 9% del plástico producido ha sido reciclado. ¡Podemos mejorar esto!",
        "Reciclar una botella de plástico ahorra suficiente energía para encender una bombilla por 3 horas."
    ],
    "vidrio": [
        "El vidrio puede reciclarse infinitamente sin perder calidad.",
        "Reciclar una botella de vidrio ahorra suficiente energía para encender una bombilla por 4 horas.",
        "El vidrio reciclado reduce la contaminación del aire en un 20%."
    ],
    "papel": [
        "Reciclar una tonelada de papel salva 17 árboles.",
        "El papel reciclado usa 60% menos energía que producir papel nuevo.",
        "Por cada tonelada de papel reciclado, ahorramos 26,000 litros de agua."
    ]
}

# Consejos generales
GENERAL_TIPS = [
    "Cada residuo que reciclamos es un paso hacia un planeta más limpio.",
    "La separación correcta de residuos facilita el proceso de reciclaje.",
    "Reciclar no solo ayuda al medio ambiente, también crea empleos verdes.",
    "El reciclaje reduce la cantidad de basura en los vertederos.",
    "Cada acción cuenta: pequeños gestos generan grandes cambios.",
    "La economía circular transforma residuos en recursos valiosos.",
    "Reciclar es una forma de cuidar nuestro hogar: la Tierra."
]

# Consejos contextuales por acción
CONTEXTUAL_TIPS = {
    "first_collection": [
        "¡Excelente! Has comenzado tu misión de reciclaje. Cada residuo cuenta.",
        "Bien hecho. Recuerda que la práctica hace al maestro recolector."
    ],
    "combo": [
        "¡Combo! Recolectar varios residuos seguidos aumenta tu eficiencia.",
        "Mantén el ritmo. La velocidad y precisión son clave."
    ],
    "mission_complete": [
        "¡Misión completada! Has contribuido positivamente al medio ambiente.",
        "Felicidades. Tu dedicación al reciclaje marca la diferencia."
    ],
    "low_score": [
        "No te desanimes. Cada intento te acerca a ser un mejor recolector.",
        "La práctica constante mejorará tus habilidades."
    ]
}

def get_tip_by_waste_type(waste_type):
    """Obtiene un consejo aleatorio para un tipo de residuo"""
    if waste_type in TIPS_BY_WASTE_TYPE:
        return random.choice(TIPS_BY_WASTE_TYPE[waste_type])
    return random.choice(GENERAL_TIPS)

def get_general_tip():
    """Obtiene un consejo general aleatorio"""
    return random.choice(GENERAL_TIPS)

def get_contextual_tip(context):
    """Obtiene un consejo contextual para una situación específica"""
    if context in CONTEXTUAL_TIPS:
        return random.choice(CONTEXTUAL_TIPS[context])
    return get_general_tip()

