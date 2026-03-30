"""Interfaz de usuario para el sistema narrativo"""
import pygame
from narrative.characters import Character

class NarrativeUI:
    """UI para mostrar narración, diálogos y consejos"""
    def __init__(self, screen, config=None):
        self.screen = screen
        self.config = config or {}
        self.current_message = None
        self.message_timer = 0
        self.message_duration = 3000  # 3 segundos por defecto
        self.show_subtitles = self.config.get("show_subtitles", True)
        self.text_speed = self.config.get("text_speed", "normal")

        # Fuentes
        self.font_large = pygame.font.Font(None, 32)
        self.font_medium = pygame.font.Font(None, 24)
        self.font_small = pygame.font.Font(None, 20)

        # Colores
        self.bg_color = (0, 0, 0, 200)  # Negro semi-transparente
        self.text_color = (255, 255, 255)

        # Posición del panel de diálogo
        self.dialog_y = self.screen.get_height() - 150
        self.dialog_height = 120

    def show_message(self, message_data):
        """Muestra un mensaje en la pantalla"""
        if message_data:
            self.current_message = message_data
            self.message_timer = pygame.time.get_ticks()

    def update(self):
        """Actualiza el UI narrativo"""
        if self.current_message:
            elapsed = pygame.time.get_ticks() - self.message_timer
            if elapsed > self.message_duration:
                self.current_message = None

    def draw(self):
        """Dibuja el UI narrativo en la pantalla"""
        if self.current_message and self.show_subtitles:
            self._draw_dialog_box()

    def _draw_dialog_box(self):
        """Dibuja la caja de diálogo"""
        character = self.current_message["character"]
        text = self.current_message["text"]

        # Crear superficie para el fondo del diálogo
        dialog_surface = pygame.Surface((self.screen.get_width() - 40, self.dialog_height))
        dialog_surface.set_alpha(200)
        dialog_surface.fill(self.bg_color[:3])

        # Dibujar nombre del personaje
        name_text = self.font_medium.render(character.name, True, character.color)
        dialog_surface.blit(name_text, (10, 10))

        # Dibujar texto del diálogo (con word wrap)
        words = text.split(' ')
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            test_surface = self.font_small.render(test_line, True, self.text_color)
            if test_surface.get_width() < dialog_surface.get_width() - 20:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word + " "
        if current_line:
            lines.append(current_line)

        # Dibujar líneas de texto
        y_offset = 40
        for line in lines[:3]:  # Máximo 3 líneas
            line_surface = self.font_small.render(line, True, self.text_color)
            dialog_surface.blit(line_surface, (10, y_offset))
            y_offset += 25

        # Dibujar en la pantalla
        self.screen.blit(dialog_surface, (20, self.dialog_y))

    def clear(self):
        """Limpia el mensaje actual"""
        self.current_message = None

