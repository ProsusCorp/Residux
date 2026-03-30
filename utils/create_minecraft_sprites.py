"""Crea sprites estilo Minecraft/pixel art para el juego"""
from PIL import Image, ImageDraw
import os

def create_sprite(size, pixels, transparent=True):
    """Crea un sprite desde una matriz de píxeles"""
    img = Image.new('RGBA', size, (0, 0, 0, 0) if transparent else (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    pixel_size = size[0] // len(pixels[0])

    for y, row in enumerate(pixels):
        for x, color in enumerate(row):
            if color:
                x1 = x * pixel_size
                y1 = y * pixel_size
                x2 = x1 + pixel_size
                y2 = y1 + pixel_size
                draw.rectangle([x1, y1, x2, y2], fill=color)

    return img

def create_plastic_bottle():
    """Crea sprite de botella de plástico estilo Minecraft"""
    # 16x16 pixels
    pixels = [
        [None, None, None, (100, 150, 255, 255), (100, 150, 255, 255), None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, (100, 150, 255, 255), (150, 200, 255, 255), (150, 200, 255, 255), (100, 150, 255, 255), None, None, None, None, None, None, None, None, None, None, None],
        [None, (100, 150, 255, 255), (150, 200, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (150, 200, 255, 255), (100, 150, 255, 255), None, None, None, None, None, None, None, None, None, None],
        [(100, 150, 255, 255), (150, 200, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (150, 200, 255, 255), (100, 150, 255, 255), None, None, None, None, None, None, None, None],
        [(100, 150, 255, 255), (150, 200, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (150, 200, 255, 255), (100, 150, 255, 255), None, None, None, None, None, None, None, None],
        [(100, 150, 255, 255), (150, 200, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (150, 200, 255, 255), (100, 150, 255, 255), None, None, None, None, None, None, None, None],
        [(100, 150, 255, 255), (150, 200, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (150, 200, 255, 255), (100, 150, 255, 255), None, None, None, None, None, None, None, None],
        [(100, 150, 255, 255), (150, 200, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (150, 200, 255, 255), (100, 150, 255, 255), None, None, None, None, None, None, None, None],
        [(100, 150, 255, 255), (150, 200, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (150, 200, 255, 255), (100, 150, 255, 255), None, None, None, None, None, None, None, None],
        [(100, 150, 255, 255), (150, 200, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (150, 200, 255, 255), (100, 150, 255, 255), None, None, None, None, None, None, None, None],
        [None, (100, 150, 255, 255), (150, 200, 255, 255), (200, 220, 255, 255), (200, 220, 255, 255), (150, 200, 255, 255), (100, 150, 255, 255), None, None, None, None, None, None, None, None, None, None],
        [None, None, (100, 150, 255, 255), (150, 200, 255, 255), (150, 200, 255, 255), (100, 150, 255, 255), None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, (100, 150, 255, 255), (100, 150, 255, 255), None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, (200, 200, 200, 255), (200, 200, 200, 255), None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, (150, 150, 150, 255), (150, 150, 150, 255), None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    ]
    img = create_sprite((64, 64), pixels)
    return img

def create_glass_jar():
    """Crea sprite de tarro de vidrio"""
    pixels = [
        [None, None, None, (200, 255, 200, 200), (200, 255, 200, 200), None, None, None],
        [None, None, (200, 255, 200, 200), (220, 255, 220, 220), (220, 255, 220, 220), (200, 255, 200, 200), None, None],
        [None, (200, 255, 200, 200), (220, 255, 220, 220), (240, 255, 240, 240), (240, 255, 240, 240), (220, 255, 220, 220), (200, 255, 200, 200), None],
        [(200, 255, 200, 200), (220, 255, 220, 220), (240, 255, 240, 240), (240, 255, 240, 240), (240, 255, 240, 240), (240, 255, 240, 240), (220, 255, 220, 220), (200, 255, 200, 200)],
        [(200, 255, 200, 200), (220, 255, 220, 220), (240, 255, 240, 240), (255, 200, 100, 255), (255, 200, 100, 255), (240, 255, 240, 240), (220, 255, 220, 220), (200, 255, 200, 200)],
        [(200, 255, 200, 200), (220, 255, 220, 220), (240, 255, 240, 240), (255, 200, 100, 255), (255, 200, 100, 255), (240, 255, 240, 240), (220, 255, 220, 220), (200, 255, 200, 200)],
        [(200, 255, 200, 200), (220, 255, 220, 220), (240, 255, 240, 240), (240, 255, 240, 240), (240, 255, 240, 240), (240, 255, 240, 240), (220, 255, 220, 220), (200, 255, 200, 200)],
        [(200, 255, 200, 200), (220, 255, 220, 220), (240, 255, 240, 240), (240, 255, 240, 240), (240, 255, 240, 240), (240, 255, 240, 240), (220, 255, 220, 220), (200, 255, 200, 200)],
        [None, (200, 255, 200, 200), (220, 255, 220, 220), (240, 255, 240, 240), (240, 255, 240, 240), (220, 255, 220, 220), (200, 255, 200, 200), None],
        [None, None, (200, 255, 200, 200), (220, 255, 220, 220), (220, 255, 220, 220), (200, 255, 200, 200), None, None],
        [None, None, None, (200, 255, 200, 200), (200, 255, 200, 200), None, None, None],
    ]
    img = create_sprite((64, 64), pixels)
    return img

def create_metal_can():
    """Crea sprite de lata de metal"""
    pixels = [
        [None, None, None, (180, 180, 180, 255), (200, 200, 200, 255), (180, 180, 180, 255), None, None],
        [None, None, (150, 150, 150, 255), (200, 200, 200, 255), (220, 220, 220, 255), (200, 200, 200, 255), (150, 150, 150, 255), None],
        [None, (150, 150, 150, 255), (200, 200, 200, 255), (220, 220, 220, 255), (240, 240, 240, 255), (220, 220, 220, 255), (200, 200, 200, 255), (150, 150, 150, 255)],
        [(150, 150, 150, 255), (200, 200, 200, 255), (220, 220, 220, 255), (240, 240, 240, 255), (240, 240, 240, 255), (240, 240, 240, 255), (220, 220, 220, 255), (200, 200, 200, 255)],
        [(150, 150, 150, 255), (200, 200, 200, 255), (220, 220, 220, 255), (100, 150, 255, 255), (100, 150, 255, 255), (220, 220, 220, 255), (200, 200, 200, 255), (150, 150, 150, 255)],
        [(150, 150, 150, 255), (200, 200, 200, 255), (220, 220, 220, 255), (100, 150, 255, 255), (100, 150, 255, 255), (220, 220, 220, 255), (200, 200, 200, 255), (150, 150, 150, 255)],
        [(150, 150, 150, 255), (200, 200, 200, 255), (220, 220, 220, 255), (240, 240, 240, 255), (240, 240, 240, 255), (240, 240, 240, 255), (220, 220, 220, 255), (200, 200, 200, 255)],
        [(150, 150, 150, 255), (200, 200, 200, 255), (220, 220, 220, 255), (240, 240, 240, 255), (240, 240, 240, 255), (240, 240, 240, 255), (220, 220, 220, 255), (200, 200, 200, 255)],
        [None, (150, 150, 150, 255), (200, 200, 200, 255), (220, 220, 220, 255), (220, 220, 220, 255), (200, 200, 200, 255), (150, 150, 150, 255), None],
        [None, None, (150, 150, 150, 255), (180, 180, 180, 255), (180, 180, 180, 255), (150, 150, 150, 255), None, None],
        [None, None, None, (100, 100, 100, 255), (100, 100, 100, 255), None, None, None],
    ]
    img = create_sprite((64, 64), pixels)
    return img

def create_wood_piece():
    """Crea sprite de trozo de madera"""
    pixels = [
        [None, None, (139, 69, 19, 255), (160, 80, 30, 255), (139, 69, 19, 255), None, None, None],
        [None, (139, 69, 19, 255), (160, 80, 30, 255), (180, 100, 40, 255), (160, 80, 30, 255), (139, 69, 19, 255), None, None],
        [(139, 69, 19, 255), (160, 80, 30, 255), (180, 100, 40, 255), (200, 120, 50, 255), (180, 100, 40, 255), (160, 80, 30, 255), (139, 69, 19, 255), None],
        [(160, 80, 30, 255), (180, 100, 40, 255), (200, 120, 50, 255), (100, 50, 10, 255), (100, 50, 10, 255), (200, 120, 50, 255), (160, 80, 30, 255), (139, 69, 19, 255)],
        [(180, 100, 40, 255), (200, 120, 50, 255), (100, 50, 10, 255), (120, 60, 15, 255), (100, 50, 10, 255), (100, 50, 10, 255), (180, 100, 40, 255), (160, 80, 30, 255)],
        [(200, 120, 50, 255), (100, 50, 10, 255), (120, 60, 15, 255), (100, 50, 10, 255), (120, 60, 15, 255), (100, 50, 10, 255), (200, 120, 50, 255), (180, 100, 40, 255)],
        [(180, 100, 40, 255), (200, 120, 50, 255), (100, 50, 10, 255), (100, 50, 10, 255), (100, 50, 10, 255), (200, 120, 50, 255), (180, 100, 40, 255), (160, 80, 30, 255)],
        [(160, 80, 30, 255), (180, 100, 40, 255), (200, 120, 50, 255), (100, 50, 10, 255), (100, 50, 10, 255), (200, 120, 50, 255), (160, 80, 30, 255), (139, 69, 19, 255)],
        [(139, 69, 19, 255), (160, 80, 30, 255), (180, 100, 40, 255), (200, 120, 50, 255), (180, 100, 40, 255), (160, 80, 30, 255), (139, 69, 19, 255), None],
        [None, (139, 69, 19, 255), (160, 80, 30, 255), (180, 100, 40, 255), (160, 80, 30, 255), (139, 69, 19, 255), None, None],
        [None, None, (139, 69, 19, 255), (160, 80, 30, 255), (139, 69, 19, 255), None, None, None],
    ]
    img = create_sprite((64, 64), pixels)
    return img

def create_paper():
    """Crea sprite de periódico/papel"""
    pixels = [
        [None, None, (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), None, None],
        [None, (255, 255, 255, 255), (240, 240, 240, 255), (240, 240, 240, 255), (240, 240, 240, 255), (240, 240, 240, 255), (255, 255, 255, 255), None],
        [(255, 255, 255, 255), (240, 240, 240, 255), (200, 200, 200, 255), (200, 200, 200, 255), (200, 200, 200, 255), (200, 200, 200, 255), (240, 240, 240, 255), (255, 255, 255, 255)],
        [(240, 240, 240, 255), (200, 200, 200, 255), (150, 150, 150, 255), (150, 150, 150, 255), (150, 150, 150, 255), (150, 150, 150, 255), (200, 200, 200, 255), (240, 240, 240, 255)],
        [(240, 240, 240, 255), (200, 200, 200, 255), (150, 150, 150, 255), (150, 150, 150, 255), (150, 150, 150, 255), (150, 150, 150, 255), (200, 200, 200, 255), (240, 240, 240, 255)],
        [(240, 240, 240, 255), (200, 200, 200, 255), (150, 150, 150, 255), (150, 150, 150, 255), (150, 150, 150, 255), (150, 150, 150, 255), (200, 200, 200, 255), (240, 240, 240, 255)],
        [(240, 240, 240, 255), (200, 200, 200, 255), (150, 150, 150, 255), (150, 150, 150, 255), (150, 150, 150, 255), (150, 150, 150, 255), (200, 200, 200, 255), (240, 240, 240, 255)],
        [(255, 255, 255, 255), (240, 240, 240, 255), (200, 200, 200, 255), (200, 200, 200, 255), (200, 200, 200, 255), (200, 200, 200, 255), (240, 240, 240, 255), (255, 255, 255, 255)],
        [None, (255, 255, 255, 255), (240, 240, 240, 255), (240, 240, 240, 255), (240, 240, 240, 255), (240, 240, 240, 255), (255, 255, 255, 255), None],
        [None, None, (230, 230, 230, 255), (230, 230, 230, 255), (230, 230, 230, 255), (230, 230, 230, 255), None, None],
    ]
    img = create_sprite((64, 64), pixels)
    return img

def create_robot_claw():
    """Crea sprite de garra robótica"""
    size = (128, 128)
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Brazo principal
    draw.rectangle([50, 20, 78, 90], fill=(100, 100, 100, 255), outline=(60, 60, 60, 255), width=3)
    # Articulación
    draw.ellipse([58, 85, 70, 97], fill=(80, 80, 80, 255), outline=(50, 50, 50, 255), width=2)

    # Base de la garra
    draw.ellipse([45, 95, 83, 110], fill=(120, 120, 120, 255), outline=(80, 80, 80, 255), width=3)

    # Garras (3 dedos estilo pixel art)
    # Garra izquierda
    draw.polygon([(50, 100), (35, 115), (42, 122), (58, 108)], fill=(100, 100, 100, 255), outline=(70, 70, 70, 255), width=2)
    # Garra central
    draw.rectangle([62, 102, 66, 118], fill=(100, 100, 100, 255), outline=(70, 70, 70, 255), width=2)
    # Garra derecha
    draw.polygon([(78, 100), (93, 115), (86, 122), (70, 108)], fill=(100, 100, 100, 255), outline=(70, 70, 70, 255), width=2)

    # Detalles metálicos (píxeles)
    draw.rectangle([58, 30, 70, 40], fill=(150, 150, 150, 255), outline=(120, 120, 120, 255), width=1)
    draw.rectangle([58, 55, 70, 65], fill=(150, 150, 150, 255), outline=(120, 120, 120, 255), width=1)

    return img

def create_grass_texture():
    """Crea textura de pasto para el suelo"""
    import random as rnd
    size = (256, 256)
    img = Image.new('RGB', size, (34, 139, 34))  # Verde pasto base
    pixels = img.load()

    # Crear variación de verde con ruido
    for y in range(size[1]):
        for x in range(size[0]):
            # Base verde
            base_r, base_g, base_b = 34, 139, 34

            # Agregar variación aleatoria para textura
            variation = rnd.randint(-15, 15)
            r = max(0, min(255, base_r + variation))
            g = max(0, min(255, base_g + variation))
            b = max(0, min(255, base_b + variation))

            # Agregar algunos puntos más oscuros (simulando sombras de hierba)
            if (x + y) % 8 == 0:
                r = max(0, r - 10)
                g = max(0, g - 10)
                b = max(0, b - 10)

            pixels[x, y] = (r, g, b)

    return img

def create_sky_texture():
    """Crea textura de cielo azul con nubes"""
    import random as rnd
    size = (512, 512)  # Más grande para el cielo
    img = Image.new('RGB', size, (135, 206, 235))  # Azul cielo base
    draw = ImageDraw.Draw(img)
    pixels = img.load()

    # Crear gradiente de azul (más claro arriba, más oscuro abajo)
    for y in range(size[1]):
        # Gradiente vertical: más claro en la parte superior
        gradient_factor = y / size[1]
        r = int(135 + gradient_factor * 20)  # 135-155
        g = int(206 + gradient_factor * 10)  # 206-216
        b = int(235 + gradient_factor * 20)  # 235-255

        for x in range(size[0]):
            # Agregar variación sutil
            variation = rnd.randint(-5, 5)
            pixels[x, y] = (
                max(0, min(255, r + variation)),
                max(0, min(255, g + variation)),
                max(0, min(255, b + variation))
            )

    # Agregar algunas nubes simples (círculos blancos semitransparentes)
    cloud_color = (255, 255, 255, 100)
    for _ in range(5):
        cloud_x = rnd.randint(0, size[0])
        cloud_y = rnd.randint(0, size[1] // 2)  # Nubes en la parte superior
        cloud_size = rnd.randint(50, 150)
        # Crear nube con múltiples círculos
        for i in range(3):
            offset_x = rnd.randint(-30, 30)
            offset_y = rnd.randint(-20, 20)
            draw.ellipse(
                [cloud_x + offset_x - cloud_size//2, cloud_y + offset_y - cloud_size//3,
                 cloud_x + offset_x + cloud_size//2, cloud_y + offset_y + cloud_size//3],
                fill=(255, 255, 255, 80)
            )

    return img

def main():
    """Genera todos los sprites"""
    sprites_dir = "assets/sprites"
    os.makedirs(sprites_dir, exist_ok=True)

    print("Creando sprites estilo Minecraft...")

    create_plastic_bottle().save(f"{sprites_dir}/plastico_botella.png")
    print("✓ Botella de plástico creada")

    create_glass_jar().save(f"{sprites_dir}/vidrio_tarro.png")
    print("✓ Tarro de vidrio creado")

    create_metal_can().save(f"{sprites_dir}/metal_lata.png")
    print("✓ Lata de metal creada")

    create_wood_piece().save(f"{sprites_dir}/madera_trozo.png")
    print("✓ Trozo de madera creado")

    create_paper().save(f"{sprites_dir}/papel_periodico.png")
    print("✓ Periódico/papel creado")

    create_robot_claw().save(f"{sprites_dir}/robot_claw.png")
    print("✓ Garra robótica creada")

    # Crear texturas de ambiente
    create_grass_texture().save(f"{sprites_dir}/grass_ground.png")
    print("✓ Textura de pasto creada")

    create_sky_texture().save(f"{sprites_dir}/sky_texture.png")
    print("✓ Textura de cielo creada")

    print("\n¡Todos los sprites y texturas creados exitosamente!")

if __name__ == "__main__":
    main()

