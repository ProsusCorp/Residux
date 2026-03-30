# Instrucciones para Obtener Sprites Estilo Minecraft

## Objetivo
Obtener sprites atractivos estilo Minecraft/pixel art para los objetos recolectables.

## Sprites Necesarios

Coloca estos archivos en `assets/sprites/`:

1. **plastico_botella.png** - Botella de plástico
2. **vidrio_tarro.png** - Tarro/frasco de vidrio
3. **metal_lata.png** - Lata de metal
4. **madera_trozo.png** - Trozo de madera
5. **papel_periodico.png** - Periódico o papel
6. **robot_claw.png** - Garra robótica

## Fuentes Recomendadas

### 1. Kenney.nl (Recomendado - CC0)
- **URL**: https://kenney.nl/assets
- **Búsqueda**: "items", "game items", "pixel art"
- **Ventaja**: Todos los assets son CC0 (uso libre)
- **Pack recomendado**: "Tiny Swords" o "Micro Roguelike"

### 2. OpenGameArt.org
- **URL**: https://opengameart.org/
- **Búsqueda**: "minecraft items", "pixel items", "16x16 items"
- **Licencia**: Varias, verificar antes de usar
- **Filtros**: Tamaño 16x16, 32x32, o 64x64 píxeles

### 3. Itch.io (Game Assets)
- **URL**: https://itch.io/game-assets/free
- **Búsqueda**: "pixel art items", "minecraft style"
- **Ventaja**: Muchos packs gratuitos

### 4. Craftpix.net
- **URL**: https://craftpix.net/freebies/
- **Búsqueda**: "free game assets", "pixel art"
- **Nota**: Algunos son gratis, otros de pago

## Especificaciones Técnicas

- **Tamaño recomendado**: 32x32, 64x64, o 128x128 píxeles
- **Formato**: PNG con transparencia (alpha channel)
- **Estilo**: Pixel art, estilo Minecraft/cartoon
- **Fondo**: Transparente

## Proceso de Descarga

1. Visita una de las fuentes recomendadas
2. Busca sprites de items/objetos estilo pixel art
3. Descarga los sprites que más te gusten
4. Renombra los archivos según la lista de arriba
5. Coloca los archivos en `assets/sprites/`
6. Si los sprites son de diferentes tamaños, puedes redimensionarlos con:
   - GIMP (gratis)
   - Paint.NET (Windows, gratis)
   - Online: https://www.iloveimg.com/resize-image

## Alternativa: Usar Sprites Existentes

Si ya tienes sprites de otro proyecto, puedes:
1. Copiarlos a `assets/sprites/`
2. Renombrarlos según la lista
3. Asegurarte de que tengan fondo transparente

## Verificación

Una vez colocados los sprites, el juego los cargará automáticamente.
Si no se ven, verifica:
1. Que los archivos estén en `assets/sprites/`
2. Que los nombres sean exactos (case-sensitive en algunos sistemas)
3. Que los archivos no estén corruptos
4. Que tengan formato PNG

## Nota sobre el Código

El código actual usa estos sprites como billboards (siempre miran a la cámara),
similar a cómo Minecraft muestra items en el mundo 3D.

