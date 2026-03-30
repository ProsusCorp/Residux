"""
Script para descargar sprites estilo Minecraft desde fuentes gratuitas.
Ejecuta este script para descargar sprites automáticamente, o descárgalos manualmente.
"""
import os
import urllib.request
from pathlib import Path

# URLs de sprites estilo Minecraft (ejemplos - reemplazar con URLs reales)
SPRITE_URLS = {
    "plastico_botella": "https://opengameart.org/sites/default/files/styles/thumbnail/public/items_0.png",
    "vidrio_tarro": "https://opengameart.org/sites/default/files/styles/thumbnail/public/items_0.png",
    "metal_lata": "https://opengameart.org/sites/default/files/styles/thumbnail/public/items_0.png",
    "madera_trozo": "https://opengameart.org/sites/default/files/styles/thumbnail/public/items_0.png",
    "papel_periodico": "https://opengameart.org/sites/default/files/styles/thumbnail/public/items_0.png",
    "robot_claw": "https://opengameart.org/sites/default/files/styles/thumbnail/public/items_0.png"
}

def download_sprite(url, filepath):
    """Descarga un sprite desde una URL"""
    try:
        print(f"Descargando {filepath}...")
        urllib.request.urlretrieve(url, filepath)
        print(f"✓ Descargado: {filepath}")
        return True
    except Exception as e:
        print(f"✗ Error descargando {filepath}: {e}")
        return False

def main():
    """Función principal"""
    sprites_dir = Path("assets/sprites")
    sprites_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 50)
    print("DESCARGADOR DE SPRITES ESTILO MINECRAFT")
    print("=" * 50)
    print("\nINSTRUCCIONES MANUALES:")
    print("1. Visita https://opengameart.org/")
    print("2. Busca 'minecraft items' o 'pixel art items'")
    print("3. Descarga sprites de:")
    print("   - Botella de plástico (plastico_botella.png)")
    print("   - Tarro de vidrio (vidrio_tarro.png)")
    print("   - Lata de metal (metal_lata.png)")
    print("   - Trozo de madera (madera_trozo.png)")
    print("   - Periódico/papel (papel_periodico.png)")
    print("   - Garra robótica (robot_claw.png)")
    print("\n4. Coloca los archivos en: assets/sprites/")
    print("\nRECURSOS RECOMENDADOS:")
    print("- Kenney.nl: https://kenney.nl/assets (gratis, CC0)")
    print("- OpenGameArt: https://opengameart.org/ (varias licencias)")
    print("- Itch.io: https://itch.io/game-assets/free (gratis)")
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()

