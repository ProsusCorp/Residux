# Residux_01 - Videojuego Educativo con Robot Recolector

Residux_01 es un videojuego educativo en Python (Ursina/Pygame) orientado a reciclaje y conciencia ambiental. Incluye modo de entrenamiento 3D y base para integración con robot real.

## Caracteristicas

- Modo de entrenamiento en primera persona estilo sandbox.
- Sistema narrativo con dialogos, personajes y tips eco-educativos.
- Recoleccion de residuos con objetos visuales y audio.
- Configuracion desacoplada para uso local (`config.local.json`).

## Requisitos

- Python 3.11 recomendado (probado en este proyecto).
- Windows 10/11 (tambien puede funcionar en Linux/Mac con ajustes menores).
- GPU/controladores con soporte OpenGL para Ursina.

## Inicio rapido (5-10 minutos, Windows)

1) Clona o descarga el proyecto.

2) Crea y activa un entorno virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3) Instala dependencias:

```bash
pip install -r requirements.txt
```

4) Configura entorno local:

```bash
copy config.example.json config.local.json
```

5) (Opcional) Ajusta la IP del robot en `config.local.json` si usaras modo terreno.

6) Ejecuta:

```bash
python main.py
```

## Configuracion

El juego carga configuracion en este orden:

1. `config.local.json` (recomendado, no versionado)
2. `config.json` (compatibilidad con versiones previas)
3. `config.example.json` (valores base)

No subas configuraciones con datos de red reales.

## Modos de juego

- **Entrenamiento**: simulacion local para practicar recoleccion.
- **Terreno**: control de robot real (requiere red y hardware compatibles).

## Controles

| Contexto | Tecla/Accion | Funcion |
|---|---|---|
| Entrenamiento | `WASD` | Movimiento |
| Entrenamiento | Flechas | Rotacion de camara |
| Entrenamiento | `Espacio` | Activar garra / recolectar |
| General | `ESC` | Pausa / menu |
| Terreno | Click izquierdo | Activar garra |

## Assets y audio

- Sprites: `assets/sprites/INSTRUCCIONES_SPRITES.md`
- Audio: `assets/sounds/INSTRUCCIONES_AUDIO.md`
- Atribuciones/licencias: `assets/ATTRIBUTION.md`

## Troubleshooting

- **No abre ventana / error OpenGL**: actualiza drivers de GPU y prueba en entorno con aceleracion grafica.
- **No hay audio**: verifica archivos en `assets/sounds/` y `assets/music/`, y volumen en `config.local.json`.
- **Error al importar Ursina/Pygame**: confirma que el entorno virtual esta activo y reinstala `requirements.txt`.
- **Pantalla negra o bajo FPS**: baja resolucion en configuracion (`window_width`, `window_height`) y cierra apps pesadas.

## Estructura del proyecto

- `core/`: sistemas principales
- `modes/`: modos de juego
- `robot/`: integracion con robot
- `ui/`: interfaz
- `narrative/`: historia y dialogos
- `assets/`: recursos multimedia
- `utils/`: utilidades y cargadores

