# Instrucciones para Agregar Audio

## Problema: No se escucha el audio

El código ahora está configurado para cargar automáticamente los sonidos si existen. Solo necesitas descargar los archivos.

## Sonidos Necesarios

Coloca estos archivos en `assets/sounds/`:

1. **collect.wav** o **collect.mp3**
   - Sonido al recolectar un residuo
   - Debe ser corto (0.5-2 segundos)
   - Tono positivo/divertido
   - Fuentes: Freesound.org, Pixabay, OpenGameArt

2. **claw.wav** o **claw.mp3**
   - Sonido de la garra robótica
   - Mecánico, corto (0.3-1 segundo)
   - Fuentes: Freesound.org (buscar "robot", "mechanical")

3. **background.mp3** (opcional)
   - Música de fondo
   - Debe poder hacer loop
   - Ambiente relajante o energético
   - Colocar en `assets/music/`

## Fuentes Recomendadas

### Efectos de Sonido:
- **Freesound.org**: https://freesound.org/
  - Buscar: "pickup", "collect", "item collect", "game collect"
  - Licencia: Verificar (muchos CC0 o CC BY)

- **Pixabay**: https://pixabay.com/sound-effects/
  - Buscar: "game collect", "pickup", "cartoon"
  - Licencia: Gratis para uso comercial

- **OpenGameArt**: https://opengameart.org/
  - Buscar: "pickup sound", "game sfx"
  - Licencia: Varias, verificar

### Música:
- **Pixabay Music**: https://pixabay.com/music/
- **Incompetech**: https://incompetech.com/music/ (Kevin MacLeod)
- **OpenGameArt**: https://opengameart.org/art/search-advanced?keys=music

## Formato de Archivos

- **Efectos**: WAV o MP3 (WAV recomendado para mejor calidad)
- **Música**: MP3 o WAV
- **Tamaño**: Mantener archivos pequeños para mejor rendimiento

## Verificación

Una vez descargados los archivos, el juego los cargará automáticamente al iniciar.
Si no se escuchan, verifica:
1. Que los archivos estén en las rutas correctas
2. Que el volumen del sistema no esté en 0
3. Que el volumen en `config.json` no esté en 0
4. Que los archivos no estén corruptos (reproducirlos fuera del juego)

## Activar/Desactivar Audio

Puedes ajustar los volúmenes en `config.json`:
```json
{
  "audio": {
    "music_volume": 0.5,
    "sfx_volume": 0.7,
    "voice_volume": 0.8
  }
}
```

