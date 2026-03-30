# Instrucciones para Agregar Sonidos

Para mejorar la experiencia del juego, descarga sonidos divertidos de las siguientes fuentes gratuitas:

## Fuentes Recomendadas:

1. **Freesound.org** (https://freesound.org/)
   - Busca: "pickup", "collect item", "game collect", "cartoon sound"
   - Licencia: CC0 o CC BY (verificar licencia antes de usar)

2. **OpenGameArt.org** (https://opengameart.org/)
   - Busca: "pickup sound", "item collect", "game sfx"
   - Licencia: Varias, verificar antes de usar

3. **Pixabay** (https://pixabay.com/sound-effects/)
   - Busca: "game collect", "pickup", "cartoon"
   - Licencia: Gratis para uso comercial

## Sonidos Necesarios:

Coloca los siguientes archivos en esta carpeta (`assets/sounds/`):

- `collect.wav` o `collect.mp3` - Sonido al recolectar un residuo (divertido, positivo)
- `claw.wav` o `claw.mp3` - Sonido de la garra robótica al abrir/cerrar (mecánico)
- `mission_complete.wav` - Sonido al completar una misión (éxito, celebración)
- `background_music.mp3` - Música de fondo (opcional, ambiente relajante o energético)

## Formato:

- Formatos soportados: WAV, MP3, OGG
- Recomendado: WAV para efectos, MP3 para música
- Duración efectos: 0.5-2 segundos
- Música: puede ser loop

## Activar Sonidos:

Una vez descargados los archivos, descomenta las líneas en `modes/training_mode.py`:
- Línea ~118: `self.sound_collect = Audio(...)`
- Línea ~119: `self.sound_claw = Audio(...)`
- Línea ~385-386: Reproducción del sonido de garra
- Línea ~396-397: Reproducción del sonido de recolección

