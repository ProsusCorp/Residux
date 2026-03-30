"""Modo de Entrenamiento - Simulación 3D en primera persona estilo Minecraft"""
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import time
import math
import os
from core.narrative_system import NarrativeSystem
from narrative.story_data import Mission, MissionStatus, ALL_MISSIONS

class Waste3D(Entity):
    """Representa un residuo 3D en el juego con volumen"""
    def __init__(self, position, waste_type, **kwargs):
        # Colores primarios vibrantes por tipo de residuo
        colors_map = {
            "madera": color.brown,                      # Marrón primario
            "metal": color.rgb(220, 220, 220),          # Gris claro brillante (plateado)
            "plastico": color.blue,                     # Azul primario brillante
            "vidrio": color.cyan,                       # Cian brillante
            "papel": color.white                        # Blanco puro
        }

        obj_color = colors_map.get(waste_type, color.white)

        # Mapeo de texturas por tipo de residuo
        texture_map = {
            "madera": "assets/sprites/madera_trozo.png",
            "metal": "assets/sprites/metal_lata.png",
            "plastico": "assets/sprites/plastico_botella.png",
            "vidrio": "assets/sprites/vidrio_tarro.png",
            "papel": "assets/sprites/papel_periodico.png"
        }

        obj_texture = texture_map.get(waste_type, None)

        # Determinar modelo y escala según tipo ANTES de inicializar
        # Nota: Ursina no tiene modelo 'cylinder' nativo, usamos 'cube' con escalas para simular
        if waste_type == "plastico":
            # Botella: cubo alargado verticalmente (simula cilindro)
            obj_model = 'cube'
            obj_scale = (0.5, 1.0, 0.5)  # Alto y estrecho
        elif waste_type == "vidrio":
            # Tarro: cubo más ancho (simula cilindro)
            obj_model = 'cube'
            obj_scale = (0.6, 0.8, 0.6)  # Ancho y medio alto
        elif waste_type == "metal":
            # Lata: cubo pequeño (simula cilindro)
            obj_model = 'cube'
            obj_scale = (0.4, 0.6, 0.4)  # Pequeño y alargado
        elif waste_type == "madera":
            # Trozo de madera: cubo irregular
            obj_model = 'cube'
            obj_scale = (0.6, 0.5, 0.7)
        elif waste_type == "papel":
            # Periódico: cubo muy plano
            obj_model = 'cube'
            obj_scale = (0.7, 0.2, 0.8)
        else:
            # Por defecto: cubo
            obj_model = 'cube'
            obj_scale = (0.6, 0.6, 0.6)

        # Inicializar Entity con TODOS los parámetros necesarios
        # Aplicar textura si está disponible, de lo contrario usar color sólido
        init_params = {
            "model": obj_model,
            "color": obj_color,
            "scale": obj_scale,
            "position": position,
            "collider": "box",
        }

        # Agregar textura si existe
        if obj_texture and os.path.exists(obj_texture):
            init_params["texture"] = obj_texture
            # Usar color blanco cuando hay textura para que la textura se vea con sus colores originales
            # El color se multiplica con la textura, así que blanco = textura sin modificar
            init_params["color"] = color.white
        else:
            # Si no hay textura, usar el color sólido especificado
            init_params["color"] = obj_color

        # Aplicar kwargs adicionales
        init_params.update(kwargs)

        super().__init__(**init_params)

        # Asegurar que el objeto sea visible y tenga iluminación correcta
        self.visible = True
        self.enabled = True

        # Propiedades del objeto
        self.waste_type = waste_type
        self.collected = False
        self.value = {
            "madera": 1000,
            "metal": 500,
            "plastico": 200,
            "vidrio": 300,
            "papel": 100
        }.get(waste_type, 100)

        # Guardar escala original para efectos (después de inicializar)
        self.original_scale = Vec3(obj_scale)
        self.in_focus = False

        # Efecto de flotación
        self.original_y = position[1]
        self.float_offset = 0
        self.float_speed = random.uniform(1, 2)

        # Rotación suave en Y para efecto visual
        self.rotation_speed = random.uniform(20, 40)

        # Asegurar que el objeto sea visible
        self.visible = True

    def update(self):
        """Actualiza la animación del residuo"""
        if self.collected or not self.visible:
            return

        # Rotación suave en Y
        self.rotation_y += self.rotation_speed * time.dt

        # Efecto de flotación
        self.float_offset += self.float_speed * time.dt
        self.y = self.original_y + math.sin(self.float_offset) * 0.3

        # Resaltado cuando está en foco (efecto de pulso suave)
        if self.in_focus:
            # Efecto de pulso cuando está en foco
            pulse = math.sin(time.time() * 5) * 0.1 + 1.0
            self.scale = Vec3(
                self.original_scale.x * pulse,
                self.original_scale.y * pulse,
                self.original_scale.z * pulse
            )
        else:
            # Volver a escala normal
            self.scale = self.original_scale

class ParticleEffect(Entity):
    """Efecto de partículas al recolectar"""
    def __init__(self, position, color, **kwargs):
        super().__init__(**kwargs)
        self.position = position
        self.model = 'sphere'
        self.color = color
        self.scale = 0.2
        self.lifetime = 0.5
        self.time_alive = 0
        self.velocity = Vec3(
            random.uniform(-2, 2),
            random.uniform(2, 4),
            random.uniform(-2, 2)
        )
        self.gravity = 0.5

    def update(self):
        self.time_alive += time.dt
        if self.time_alive >= self.lifetime:
            destroy(self)
            return

        self.position += self.velocity * time.dt
        self.velocity.y -= self.gravity * time.dt
        self.scale *= 0.95
        alpha = 1 - (self.time_alive / self.lifetime)
        self.color = color.rgba(
            self.color.r,
            self.color.g,
            self.color.b,
            alpha
        )

class TrainingMode:
    """Modo de entrenamiento 3D en primera persona"""
    def __init__(self, app, config):
        self.app = app
        self.config = config

        # Sistema narrativo
        narrative_config = config.get("narrative", {})
        self.narrative = NarrativeSystem(narrative_config)

        # Variables del juego
        self.score = 0
        self.wastes_collected = 0
        self.combo_count = 0
        self.last_collection_time = 0
        self.first_collection = True
        self.particles = []

        # Sonidos
        audio_config = config.get("audio", {})
        self.sfx_volume = audio_config.get("sfx_volume", 0.7)
        self.music_volume = audio_config.get("music_volume", 0.5)

        # Cargar sonidos si existen
        self.sound_collect = None
        self.sound_claw = None
        self.music_background = None

        # Intentar cargar sonidos
        if os.path.exists('assets/sounds/collect.wav'):
            self.sound_collect = Audio('assets/sounds/collect.wav', autoplay=False, volume=self.sfx_volume)
        elif os.path.exists('assets/sounds/collect.mp3'):
            self.sound_collect = Audio('assets/sounds/collect.mp3', autoplay=False, volume=self.sfx_volume)

        if os.path.exists('assets/sounds/claw.wav'):
            self.sound_claw = Audio('assets/sounds/claw.wav', autoplay=False, volume=self.sfx_volume)
        elif os.path.exists('assets/sounds/claw.mp3'):
            self.sound_claw = Audio('assets/sounds/claw.mp3', autoplay=False, volume=self.sfx_volume)

        # Música de fondo (opcional)
        if os.path.exists('assets/music/background.mp3'):
            self.music_background = Audio('assets/music/background.mp3', loop=True, autoplay=True, volume=self.music_volume)
        elif os.path.exists('assets/music/background.wav'):
            self.music_background = Audio('assets/music/background.wav', loop=True, autoplay=True, volume=self.music_volume)

        # Misión actual
        self.current_mission = None
        self.available_missions = ALL_MISSIONS.copy()
        self.select_mission(0)

        # Crear escenario 3D
        self.create_scene()

        # Crear jugador (primera persona)
        self.player = FirstPersonController()
        self.player.gravity = 0.5
        self.player.jump_height = 0  # Deshabilitar salto (usaremos espacio para la garra)
        self.player.jump_duration = 0.5
        self.player.speed = 5

        # Deshabilitar control de mouse para cámara (usaremos flechas)
        self.player.mouse_sensitivity = Vec2(0, 0)  # Sin movimiento de mouse
        mouse.visible = True  # Mouse visible para clics en UI
        self.mouse_locked = False

        # Crear residuos
        self.wastes = []
        self.create_wastes(20)

        # Crear UI
        self.create_ui()

        # Variable para controlar el diálogo de confirmación
        self.dialogo_confirmacion = None
        self.mouse_locked = True
        mouse.visible = False

    def create_scene(self):
        """Crea el escenario 3D"""
        # Suelo campestre verde con textura
        base_color_grass = color.rgb(34, 139, 34)  # Verde pasto brillante

        # Terreno base con textura de pasto
        grass_texture_path = 'assets/sprites/grass_ground.png'
        if os.path.exists(grass_texture_path):
            self.terrain = Entity(
                model='plane',
                scale=(100, 1, 100),
                texture=grass_texture_path,
                color=color.white,  # Color blanco para que la textura se vea completa
                collider='box'
            )
        else:
            # Fallback a color sólido si no hay textura
            self.terrain = Entity(
                model='plane',
                scale=(100, 1, 100),
                color=base_color_grass,
                collider='box'
            )

        # Agregar parches de pasto aleatorios con variación de verde
        self.grass_patches = []
        for _ in range(30):
            # Variación de verde para más realismo
            grass_variation = color.rgb(
                30 + random.randint(0, 20),  # 30-50
                130 + random.randint(0, 30),  # 130-160
                30 + random.randint(0, 20)    # 30-50
            )
            patch = Entity(
                model='plane',
                scale=(random.uniform(5, 15), 1, random.uniform(5, 15)),
                position=(
                    random.uniform(-45, 45),
                    0.01,  # Ligeramente arriba del terreno base
                    random.uniform(-45, 45)
                ),
                color=grass_variation,  # Variación de verde
                rotation_y=random.uniform(0, 360)
            )
            self.grass_patches.append(patch)

        # Cielo con textura
        sky_texture_path = 'assets/sprites/sky_texture.png'
        if os.path.exists(sky_texture_path):
            Sky(texture=sky_texture_path, color=color.white)
        else:
            # Fallback a color sólido si no hay textura
            Sky(color=color.rgb(135, 206, 235))  # Azul cielo

        # Iluminación mejorada (más brillante para mejor visibilidad y colores)
        DirectionalLight(direction=(0.5, -1, 0.5), color=color.rgb(255, 255, 255), shadows=False)
        AmbientLight(color=color.rgb(180, 180, 180))  # Más brillante para que los colores se vean mejor

        # Rocas decorativas (usando esferas escaladas para forma irregular)
        self.rocks = []
        for _ in range(10):
            rock = Entity(
                model='sphere',
                position=(
                    random.uniform(-45, 45),
                    0.5,  # Altura para que se vean
                    random.uniform(-45, 45)
                ),
                scale=(
                    random.uniform(1.0, 2.0),  # Más grandes para que se vean
                    random.uniform(0.5, 1.5),
                    random.uniform(1.0, 2.0)
                ),
                color=color.rgb(80, 80, 80),
                texture='white_cube',
                collider='box'
            )
            # Rotar ligeramente para más variación
            rock.rotation = (
                random.uniform(0, 360),
                random.uniform(0, 360),
                random.uniform(0, 360)
            )
            self.rocks.append(rock)

    def create_wastes(self, count):
        """Crea residuos aleatorios en el mapa"""
        waste_types = ["madera", "metal", "plastico", "vidrio", "papel"]
        for _ in range(count):
            x = random.uniform(-45, 45)
            z = random.uniform(-45, 45)
            y = 0.5  # Altura adecuada para objetos 3D
            waste_type = random.choice(waste_types)
            try:
                waste = Waste3D(position=(x, y, z), waste_type=waste_type)
                # Asegurar que el objeto se renderice correctamente
                waste.visible = True
                waste.enabled = True
                self.wastes.append(waste)
            except Exception as e:
                print(f"Error creando residuo {waste_type}: {e}")
                continue

    def select_mission(self, mission_index):
        """Selecciona una misión"""
        if 0 <= mission_index < len(self.available_missions):
            mission = self.available_missions[mission_index]
            if mission.status == MissionStatus.LOCKED and mission_index > 0:
                prev_mission = self.available_missions[mission_index - 1]
                if prev_mission.status == MissionStatus.COMPLETED:
                    mission.status = MissionStatus.AVAILABLE

            if mission.status != MissionStatus.LOCKED:
                self.current_mission = mission
                mission.status = MissionStatus.IN_PROGRESS
                self.narrative.set_mission(mission)
                # Mostrar mensaje de introducción
                if self.narrative.has_pending_messages():
                    msg = self.narrative.get_next_message()
                    if msg:
                        self.show_narrative_message(msg)

    def create_ui(self):
        """Crea la interfaz de usuario"""
        # Puntuación (esquina superior izquierda, con margen seguro)
        self.texto_puntuacion = Text(
            text='Puntuación: 0',
            position=(-0.75, 0.45),
            scale=2,
            color=color.white,
            origin=(-0.5, 0.5)  # Anclar a esquina superior izquierda
        )

        # Residuos recolectados
        self.texto_recolectados = Text(
            text='Recolectados: 0',
            position=(-0.75, 0.38),
            scale=2,
            color=color.white,
            origin=(-0.5, 0.5)  # Anclar a esquina superior izquierda
        )

        # Misión actual
        self.texto_mision = Text(
            text='Misión: -',
            position=(-0.75, 0.31),
            scale=1.5,
            color=color.yellow,
            origin=(-0.5, 0.5)  # Anclar a esquina superior izquierda
        )

        # Recuadro de enfoque en el centro de la pantalla (como cámara)
        # Crear marco con líneas (más visible y estético - MÁS GRANDE)
        frame_size = 0.15  # Aumentado de 0.08 a 0.15 (casi el doble)
        frame_thickness = 0.005  # Más grueso

        # Líneas del marco (esquinas estilo cámara)
        self.focus_frame_lines = []
        # Esquina superior izquierda
        self.focus_frame_lines.append(Entity(
            parent=camera.ui,
            model='quad',
            color=color.red,
            scale=(frame_thickness, frame_size * 0.3),
            position=(-frame_size * 0.5, frame_size * 0.5),
            rotation_z=0
        ))
        self.focus_frame_lines.append(Entity(
            parent=camera.ui,
            model='quad',
            color=color.red,
            scale=(frame_size * 0.3, frame_thickness),
            position=(-frame_size * 0.5, frame_size * 0.5),
            rotation_z=0
        ))
        # Esquina superior derecha
        self.focus_frame_lines.append(Entity(
            parent=camera.ui,
            model='quad',
            color=color.red,
            scale=(frame_thickness, frame_size * 0.3),
            position=(frame_size * 0.5, frame_size * 0.5),
            rotation_z=0
        ))
        self.focus_frame_lines.append(Entity(
            parent=camera.ui,
            model='quad',
            color=color.red,
            scale=(frame_size * 0.3, frame_thickness),
            position=(frame_size * 0.5, frame_size * 0.5),
            rotation_z=0
        ))
        # Esquina inferior izquierda
        self.focus_frame_lines.append(Entity(
            parent=camera.ui,
            model='quad',
            color=color.red,
            scale=(frame_thickness, frame_size * 0.3),
            position=(-frame_size * 0.5, -frame_size * 0.5),
            rotation_z=0
        ))
        self.focus_frame_lines.append(Entity(
            parent=camera.ui,
            model='quad',
            color=color.red,
            scale=(frame_size * 0.3, frame_thickness),
            position=(-frame_size * 0.5, -frame_size * 0.5),
            rotation_z=0
        ))
        # Esquina inferior derecha
        self.focus_frame_lines.append(Entity(
            parent=camera.ui,
            model='quad',
            color=color.red,
            scale=(frame_thickness, frame_size * 0.3),
            position=(frame_size * 0.5, -frame_size * 0.5),
            rotation_z=0
        ))
        self.focus_frame_lines.append(Entity(
            parent=camera.ui,
            model='quad',
            color=color.red,
            scale=(frame_size * 0.3, frame_thickness),
            position=(frame_size * 0.5, -frame_size * 0.5),
            rotation_z=0
        ))

        # Objeto actualmente en el foco
        self.object_in_focus = None
        self.focus_frame_highlighted = False

        # Indicador de proximidad bajo el recuadro de enfoque
        self.proximity_text = Text(
            parent=camera.ui,
            text='',
            position=(0, -0.15),  # Más abajo para no interferir con la garra
            scale=2,
            color=color.white,
            origin=(0, 0),
            background=True,
            background_color=color.rgba(0, 0, 0, 150)
        )

        # Minimapa (más visible)
        self.minimap_expanded = False

        # Borde del minimapa para mejor visibilidad (primero, para que esté detrás)
        # Posición ajustada para estar dentro de los márgenes visibles
        self.minimap_border = Entity(
            parent=camera.ui,
            model='quad',
            color=color.rgba(255, 255, 0, 200),  # Borde amarillo más visible
            scale=(0.25, 0.12),
            position=(-0.7, -0.7),  # Más hacia adentro para estar visible
            z=-0.1
        )

        # Botón del minimapa
        self.minimap = Button(
            parent=camera.ui,
            text='🗺️ Mapa',
            color=color.rgba(0, 0, 0, 255),  # Negro sólido para máximo contraste
            scale=(0.23, 0.1),
            position=(-0.7, -0.7),  # Más hacia adentro para estar visible
            highlight_color=color.rgba(100, 100, 100, 255),
            text_scale=1.8,  # Texto ligeramente más pequeño
            text_color=color.yellow,  # Amarillo para destacar
            z=-0.09  # Delante del borde
        )
        self.minimap.on_click = self.toggle_minimap

        # Asegurar que ambos sean visibles
        self.minimap.visible = True
        self.minimap_border.visible = True

        # Personaje "Amigo Dron"
        self.drone_friend_quotes = [
            "¡Hola! Soy el Amigo Dron. He detectado varios objetos reciclables en esta zona.",
            "Recuerda: cada residuo que recolectas ayuda a mantener limpio nuestro planeta.",
            "Veo oportunidades de recolección por todas partes. ¡Vamos a limpiar esta área!",
            "La eficiencia es clave. Enfócate en los objetos más cercanos primero.",
            "¡Excelente trabajo! Estás mejorando el medio ambiente con cada recolección.",
            "Hay más objetos esperando ser reciclados. ¡Sigue adelante!",
            "Cada botella, lata y papel cuenta. Tu esfuerzo marca la diferencia.",
            "El reciclaje es un acto de amor hacia nuestro planeta. ¡Continúa así!"
        ]

        # Panel de minimapa expandido
        self.expanded_minimap_panel = None
        self.expanded_minimap_text = None

        # Garra robótica en la UI (centro inferior, 3x más grande, rotada)
        self.robot_claw = Entity(
            parent=camera.ui,
            model='quad',
            texture='assets/sprites/robot_claw.png',
            scale=(0.45, 0.45),  # 3x más grande (0.15 * 3 = 0.45)
            position=(0, -0.35),  # Un poco más arriba para no interferir con otros elementos
            rotation_z=180  # Rotar 180 grados para que los dedos vayan hacia arriba
        )

        # Posición original de la garra para animación de estiramiento
        self.claw_original_position = Vec3(0, -0.4, 0)
        self.claw_extended_position = Vec3(0, -0.2, 0)  # Se estira hacia arriba
        self.claw_current_position = self.claw_original_position

        # Animación de la garra
        self.claw_animation_state = 'idle'  # 'idle', 'opening', 'closing', 'extending', 'retracting'
        self.claw_rotation = 0
        self.claw_opening = False  # Estado de apertura de la garra
        self.space_pressed = False  # Control de tecla espacio
        self.claw_extended = False  # Si la garra está estirada

        # Panel de diálogo narrativo
        self.dialog_panel = Entity(
            parent=camera.ui,
            model='quad',
            scale=(1.2, 0.3),
            position=(0, -0.35),
            color=color.rgba(0, 0, 0, 200),
            visible=False
        )

        self.dialog_character_name = Text(
            parent=camera.ui,
            text='',
            position=(-0.5, -0.2),  # Más arriba para estar visible
            scale=1.5,
            color=color.white,
            origin=(-0.5, 0),
            visible=False
        )

        self.dialog_text = Text(
            parent=camera.ui,
            text='',
            position=(-0.5, -0.25),  # Más arriba para estar visible
            scale=1.2,
            color=color.white,
            origin=(-0.5, 0),
            visible=False
        )
        # Nota: wordwrap se configurará cuando se asigne texto, no aquí

        # Botón de salida (esquina superior derecha, con margen seguro)
        self.boton_salir = Button(
            text='Salir (ESC)',
            color=color.red,
            scale=(0.15, 0.05),
            position=(0.7, 0.45),  # Más hacia adentro para estar visible
            parent=camera.ui,
            origin=(0.5, 0.5)  # Anclar a esquina superior derecha
        )
        self.boton_salir.on_click = self.mostrar_confirmacion_salida

    def show_narrative_message(self, message_data):
        """Muestra un mensaje narrativo"""
        if message_data:
            character = message_data["character"]
            text = message_data["text"]

            # Dividir texto largo en líneas manualmente si es necesario
            if len(text) > 50:
                words = text.split(' ')
                lines = []
                current_line = ''
                for word in words:
                    if len(current_line + ' ' + word) <= 50:
                        current_line += ' ' + word if current_line else word
                    else:
                        if current_line:
                            lines.append(current_line)
                        current_line = word
                if current_line:
                    lines.append(current_line)
                text = '\n'.join(lines)

            self.dialog_panel.visible = True
            self.dialog_character_name.visible = True
            self.dialog_text.visible = True

            self.dialog_character_name.text = character.name
            # Convertir tupla de color a objeto color de Ursina
            if isinstance(character.color, tuple):
                self.dialog_character_name.color = color.rgb(*character.color[:3])
            else:
                self.dialog_character_name.color = character.color
            self.dialog_text.text = text

            # Auto-ocultar después de 5 segundos
            invoke(self.hide_narrative_message, delay=5)

    def hide_narrative_message(self):
        """Oculta el mensaje narrativo"""
        self.dialog_panel.visible = False
        self.dialog_character_name.visible = False
        self.dialog_text.visible = False

    def update(self):
        """Actualiza el estado del juego"""
        # Control de cámara con flechas (si no está expandido el minimapa)
        if not self.minimap_expanded:
            self.handle_camera_controls()

        # Detectar objetos en el foco (centro de la pantalla)
        self.detect_object_in_focus()

        # Actualizar recuadro de enfoque
        self.update_focus_frame()

        # Control de la garra con barra espaciadora
        space_currently_pressed = held_keys['space']

        # Al presionar espacio: abrir garra y estirar si hay objeto en foco
        if space_currently_pressed and not self.space_pressed:
            self.space_pressed = True
            if self.object_in_focus:
                self.open_claw_and_extend()
            else:
                self.open_claw()

        # Al soltar espacio: cerrar garra y recolectar
        if not space_currently_pressed and self.space_pressed:
            self.space_pressed = False
            self.close_claw_and_collect()

        # Actualizar animación de la garra
        self.update_claw_animation()

        # Actualizar minimapa
        if not self.minimap_expanded:
            self.update_minimap()

        # Actualizar UI
        self.texto_puntuacion.text = f'Puntuación: {self.score}'
        self.texto_recolectados.text = f'Recolectados: {self.wastes_collected}'

        if self.current_mission:
            self.texto_mision.text = f'Misión: {self.current_mission.title}'

        # Verificar progreso de misión
        if self.current_mission:
            self.update_mission_progress()

        # Verificar tecla Escape
        if held_keys['escape']:
            if self.minimap_expanded:
                self.toggle_minimap()  # Cerrar minimapa si está expandido
            else:
                self.mostrar_confirmacion_salida()

        # Verificar si hay mensajes pendientes
        if not self.dialog_panel.visible and self.narrative.has_pending_messages():
            msg = self.narrative.get_next_message()
            if msg:
                self.show_narrative_message(msg)

    def handle_camera_controls(self):
        """Maneja el control de cámara con flechas"""
        # Rotación horizontal (izquierda/derecha)
        if held_keys['left arrow']:
            self.player.rotation_y -= 60 * time.dt
        if held_keys['right arrow']:
            self.player.rotation_y += 60 * time.dt

        # Rotación vertical (arriba/abajo) - limitada
        # Nota: En Ursina, rotation_x positivo mira hacia abajo
        if held_keys['up arrow']:
            self.player.camera_pivot.rotation_x = max(-45, self.player.camera_pivot.rotation_x - 60 * time.dt)
        if held_keys['down arrow']:
            self.player.camera_pivot.rotation_x = min(45, self.player.camera_pivot.rotation_x + 60 * time.dt)

    def update_minimap(self):
        """Actualiza el minimapa con los objetos disponibles"""
        # El minimapa se actualiza visualmente (por ahora solo muestra el fondo)
        # En una versión más avanzada se podrían dibujar puntos para cada objeto
        pass

    def toggle_minimap(self):
        """Expande o contrae el minimapa"""
        if not self.minimap_expanded:
            # Expandir minimapa
            self.minimap_expanded = True
            self.minimap.scale = (1.8, 1.8)
            self.minimap.position = (0, 0)
            self.minimap.color = color.rgba(0, 0, 0, 230)
            self.minimap_border.visible = False

            # Mostrar parlamento del Amigo Dron
            quote = random.choice(self.drone_friend_quotes)

            # Crear panel de texto del dron
            if not self.expanded_minimap_panel:
                self.expanded_minimap_panel = Entity(
                    parent=camera.ui,
                    model='quad',
                    color=color.rgba(50, 50, 50, 240),
                    scale=(1.5, 0.3),
                    position=(0, 0.6),
                    z=-1
                )

            if not self.expanded_minimap_text:
                self.expanded_minimap_text = Text(
                    parent=camera.ui,
                    text='',
                    position=(0, 0.6),
                    scale=1.2,
                    color=color.white,
                    origin=(0, 0)
                )

            # Dividir texto largo en líneas si es necesario
            quote_text = f'"Amigo Dron": {quote}'
            if len(quote_text) > 60:
                words = quote_text.split(' ')
                lines = []
                current_line = ''
                for word in words:
                    if len(current_line + ' ' + word) <= 60:
                        current_line += ' ' + word if current_line else word
                    else:
                        if current_line:
                            lines.append(current_line)
                        current_line = word
                if current_line:
                    lines.append(current_line)
                quote_text = '\n'.join(lines)
            self.expanded_minimap_text.text = quote_text
            self.expanded_minimap_text.visible = True
            self.expanded_minimap_panel.visible = True

            # Deshabilitar movimiento del jugador mientras el minimapa está expandido
            self.player.disable()
            mouse.visible = True
        else:
            # Contraer minimapa
            self.minimap_expanded = False
            self.minimap.scale = (0.23, 0.1)
            self.minimap.position = (-0.7, -0.7)
            self.minimap.color = color.rgba(0, 0, 0, 255)
            self.minimap_border.scale = (0.25, 0.12)
            self.minimap_border.position = (-0.7, -0.7)
            self.minimap_border.visible = True
            self.minimap.visible = True

            # Ocultar panel del dron
            if self.expanded_minimap_text:
                self.expanded_minimap_text.visible = False
            if self.expanded_minimap_panel:
                self.expanded_minimap_panel.visible = False

            # Rehabilitar movimiento del jugador
            self.player.enable()
            mouse.visible = False

    def detect_object_in_focus(self):
        """Detecta si hay un objeto en el foco usando raycast mejorado"""
        self.object_in_focus = None

        # Usar raycast desde la cámara para detección precisa
        try:
            # Raycast desde la posición de la cámara hacia adelante
            ray_origin = self.player.camera_pivot.world_position
            ray_direction = self.player.forward

            # Hacer raycast con distancia extendida
            hit_info = raycast(
                origin=ray_origin,
                direction=ray_direction,
                distance=20,  # Distancia máxima
                debug=False
            )

            # Si el raycast golpea un residuo, usarlo directamente
            if hit_info.hit and hasattr(hit_info.entity, 'waste_type'):
                if not hit_info.entity.collected:
                    self.object_in_focus = hit_info.entity
                    return
        except:
            pass  # Si raycast falla, usar método alternativo

        # Método alternativo: buscar objeto más cercano al centro del campo de visión
        closest_waste = None
        closest_distance = float('inf')
        focus_angle_threshold = 12  # Ángulo más generoso (12 grados)
        max_distance = 20  # Distancia máxima aumentada

        for waste in self.wastes:
            if waste.collected:
                continue

            # Calcular dirección y distancia
            direction_to_waste = waste.position - self.player.position
            dist = direction_to_waste.length()

            if dist > max_distance:
                continue

            direction_to_waste = direction_to_waste.normalized()
            camera_forward = self.player.forward

            # Calcular ángulo entre la dirección de la cámara y el objeto
            dot_product = direction_to_waste.dot(camera_forward)
            dot_product = max(-1, min(1, dot_product))  # Clamp para evitar errores
            angle = math.degrees(math.acos(dot_product))

            # Si el objeto está cerca del centro (ángulo pequeño)
            if angle < focus_angle_threshold:
                # Priorizar objetos más cercanos y más centrados
                score = dist + (angle * 2)  # Puntuación: distancia + ángulo
                if score < closest_distance:
                    closest_distance = score
                    closest_waste = waste

        self.object_in_focus = closest_waste

    def get_focus_position(self):
        """Calcula la posición del foco (30cm = 0.3 unidades frente a la cámara)"""
        # El foco está a 30cm (0.3 unidades) frente a la cámara
        focus_distance = 0.3
        # Posición de la cámara
        camera_pos = self.player.camera_pivot.world_position
        # Dirección hacia adelante de la cámara
        camera_forward = self.player.forward
        # Calcular posición del foco
        focus_position = camera_pos + camera_forward * focus_distance
        return focus_position

    def update_focus_frame(self):
        """Actualiza el recuadro de enfoque según si hay objeto en foco"""
        # Marcar objetos que están en foco
        for waste in self.wastes:
            if waste == self.object_in_focus:
                waste.in_focus = True
            else:
                waste.in_focus = False
                if hasattr(waste, 'original_scale'):
                    waste.scale = waste.original_scale

        if self.object_in_focus:
            # Cambiar a color verde cuando hay objeto en foco
            if not self.focus_frame_highlighted:
                for line in self.focus_frame_lines:
                    line.color = color.green
                self.focus_frame_highlighted = True

            # Animación de pulso del recuadro
            pulse_alpha = int(150 + math.sin(time.time() * 3) * 50)
            for line in self.focus_frame_lines:
                if hasattr(line.color, 'a'):
                    line.color = color.rgba(0, 255, 0, pulse_alpha)

            # Calcular distancia desde el objeto hasta el foco (30cm frente a la cámara)
            focus_pos = self.get_focus_position()
            dist_to_focus = distance(self.object_in_focus.position, focus_pos)

            # Convertir distancia a centímetros (1 unidad = 100 cm aproximadamente)
            # Dividir por 10 para corregir la escala
            dist_cm = int(dist_to_focus * 100 / 10)

            # Determinar si está dentro del rango de agarre (menor a 50 cm, ajustado por la división por 10)
            grab_threshold_cm = 50
            is_within_grab_range = dist_cm < grab_threshold_cm

            # Actualizar texto de proximidad
            if is_within_grab_range:
                self.proximity_text.text = f"✓ {dist_cm} cm - Presiona ESPACIO"
                self.proximity_text.color = color.green
                self.proximity_text.scale = 2.8  # Más grande cuando está listo
            else:
                # Mostrar distancia cuando está fuera de rango
                self.proximity_text.text = f"{dist_cm} cm del foco (acércate más)"
                self.proximity_text.color = color.yellow
                self.proximity_text.scale = 2.2

            self.proximity_text.visible = True
        else:
            # Volver a rojo cuando no hay objeto
            if self.focus_frame_highlighted:
                for line in self.focus_frame_lines:
                    line.color = color.red
                self.focus_frame_highlighted = False

            # Ocultar indicador de proximidad
            self.proximity_text.visible = False

    def open_claw(self):
        """Abre la garra (animación) sin estirar"""
        self.claw_animation_state = 'opening'
        self.claw_opening = True
        self.claw_extended = False
        # Reproducir sonido de garra al abrir
        if self.sound_claw:
            self.sound_claw.play()

    def open_claw_and_extend(self):
        """Abre la garra y la estira hacia el objeto en foco"""
        self.claw_animation_state = 'extending'
        self.claw_opening = True
        self.claw_extended = True
        # Reproducir sonido de garra al abrir
        if self.sound_claw:
            self.sound_claw.play()

    def close_claw_and_collect(self):
        """Cierra la garra y recolecta objeto en foco"""
        self.claw_animation_state = 'closing'
        self.claw_opening = False

        # Solo recolectar si hay objeto en el foco Y está dentro del rango de agarre
        if self.object_in_focus and not self.object_in_focus.collected:
            # Calcular distancia desde el objeto hasta el foco (30cm frente a la cámara)
            focus_pos = self.get_focus_position()
            dist_to_focus = distance(self.object_in_focus.position, focus_pos)

            # Convertir distancia a centímetros (1 unidad = 100 cm aproximadamente)
            # Dividir por 10 para corregir la escala
            dist_cm = int(dist_to_focus * 100 / 10)

            # Recolectar si está dentro del rango de agarre (menor a 50 cm, ajustado por la división por 10)
            grab_threshold_cm = 50
            if dist_cm < grab_threshold_cm:
                # Recolectar el objeto en foco
                self.recolectar_residuo(self.object_in_focus)
                # Retraer la garra después de recolectar
                self.claw_extended = False
            else:
                # Objeto en foco pero aún no está dentro del rango de agarre
                self.claw_extended = False
                invoke(lambda: setattr(self, 'claw_animation_state', 'idle'), delay=0.2)
        else:
            # Solo cerrar la garra si no hay objeto en foco
            self.claw_extended = False
            invoke(lambda: setattr(self, 'claw_animation_state', 'idle'), delay=0.2)

    def update_claw_animation(self):
        """Actualiza la animación de la garra"""
        if self.claw_animation_state == 'opening':
            # Abrir: rotar hacia afuera (los dedos se separan)
            self.claw_rotation = lerp(self.claw_rotation, 20, time.dt * 8)
            # Mantener posición original
            self.claw_current_position = lerp(self.claw_current_position, self.claw_original_position, time.dt * 5)
        elif self.claw_animation_state == 'extending':
            # Estirar: abrir dedos y mover hacia arriba
            self.claw_rotation = lerp(self.claw_rotation, 20, time.dt * 8)
            # Estirar la garra hacia arriba (hacia el objeto)
            self.claw_current_position = lerp(self.claw_current_position, self.claw_extended_position, time.dt * 6)
        elif self.claw_animation_state == 'closing':
            # Cerrar: rotar hacia adentro (los dedos se juntan)
            self.claw_rotation = lerp(self.claw_rotation, -15, time.dt * 10)
            # Retraer la garra
            if self.claw_extended:
                self.claw_current_position = lerp(self.claw_current_position, self.claw_original_position, time.dt * 8)
            # Volver a idle después de cerrar
            if abs(self.claw_rotation - (-15)) < 1 and not self.claw_extended:
                self.claw_animation_state = 'idle'
        else:  # idle
            # Volver a posición neutral
            self.claw_rotation = lerp(self.claw_rotation, 0, time.dt * 5)
            self.claw_current_position = lerp(self.claw_current_position, self.claw_original_position, time.dt * 5)

        if hasattr(self, 'robot_claw'):
            # Aplicar rotación adicional a la rotación base (180 grados)
            self.robot_claw.rotation_z = 180 + self.claw_rotation
            # Aplicar posición (estiramiento)
            self.robot_claw.position = self.claw_current_position

    def intentar_recoleccion(self):
        """Intenta recolectar un residuo cercano (método antiguo, ahora se usa espacio)"""
        # Este método ya no se usa, pero lo mantenemos por compatibilidad
        pass

    def recolectar_residuo(self, waste):
        """Recolecta un residuo"""
        if waste.collected:
            return  # Ya fue recolectado

        waste.collected = True
        waste.visible = False  # Ocultar el objeto
        waste.enabled = False  # Deshabilitar actualizaciones
        self.score += waste.value
        self.wastes_collected += 1

        # Reproducir sonido de recolección
        if self.sound_collect:
            self.sound_collect.play()

        # Efecto de partículas
        for _ in range(10):
            particle = ParticleEffect(
                position=waste.position,
                color=waste.color
            )
            self.particles.append(particle)

        # Combo system
        current_time = time.time()
        if current_time - self.last_collection_time < 2:  # 2 segundos
            self.combo_count += 1
            if self.combo_count > 1:
                self.narrative.trigger_narrative_event("combo")
        else:
            self.combo_count = 0
        self.last_collection_time = current_time

        # Primera recolección
        if self.first_collection:
            self.first_collection = False
            self.narrative.trigger_narrative_event("first_collection")

        # Evento de recolección con tipo
        self.narrative.trigger_narrative_event("waste_collected", {"type": waste.waste_type})

        # Destruir el residuo
        destroy(waste)
        self.wastes.remove(waste)

        # Mostrar mensaje inmediatamente si no hay uno activo
        if not self.dialog_panel.visible and self.narrative.has_pending_messages():
            msg = self.narrative.get_next_message()
            if msg:
                self.show_narrative_message(msg)

    def update_mission_progress(self):
        """Actualiza el progreso de la misión actual"""
        if not self.current_mission:
            return

        # Actualizar objetivos
        for obj in self.current_mission.objectives:
            obj_id = obj["id"]
            if obj_id == "collect_5" or obj_id == "collect_10" or obj_id == "collect_20":
                self.current_mission.progress[obj_id] = self.wastes_collected
            elif obj_id == "collect_wood":
                # Simplificado: asumimos progreso basado en recolecciones totales
                self.current_mission.progress[obj_id] = min(self.wastes_collected // 3, obj["target"])
            elif obj_id == "collect_all_types":
                # Simplificado: asumimos que se recolectaron todos los tipos
                self.current_mission.progress[obj_id] = min(self.wastes_collected // 2, obj["target"])

        # Verificar si la misión está completada
        if self.current_mission.check_completion() and self.current_mission.status == MissionStatus.IN_PROGRESS:
            self.current_mission.status = MissionStatus.COMPLETED
            self.narrative.trigger_narrative_event("mission_complete", self.current_mission)
            # Mostrar mensaje de conclusión
            if self.narrative.has_pending_messages():
                msg = self.narrative.get_next_message()
                if msg:
                    self.show_narrative_message(msg)

    def mostrar_confirmacion_salida(self):
        """Muestra diálogo de confirmación para salir"""
        if not self.dialogo_confirmacion:
            self.mouse_locked = False
            mouse.visible = True
            self.player.disable()

            self.dialogo_confirmacion = Entity(
                parent=camera.ui,
                model='quad',
                color=color.black66,
                scale=(0.5, 0.3),
                z=-1
            )

            Text(
                '¿Estás seguro de que quieres salir?',
                parent=self.dialogo_confirmacion,
                origin=(0, 0),
                position=(0, 0.05),
                scale=2
            )

            Button(
                text='Sí',
                color=color.red,
                scale=(0.2, 0.05),
                position=(-0.1, -0.05),
                parent=self.dialogo_confirmacion
            ).on_click = self.salir_juego

            Button(
                text='No',
                color=color.gray,
                scale=(0.2, 0.05),
                position=(0.1, -0.05),
                parent=self.dialogo_confirmacion
            ).on_click = self.cerrar_dialogo

    def cerrar_dialogo(self):
        """Cierra el diálogo de confirmación"""
        if self.dialogo_confirmacion:
            destroy(self.dialogo_confirmacion)
            self.dialogo_confirmacion = None
            self.mouse_locked = True
            mouse.visible = False
            self.player.enable()

    def salir_juego(self):
        """Sale del juego"""
        application.quit()
