"""Crea sonidos simples para el juego usando síntesis de audio"""
import numpy as np
from scipy.io import wavfile
import os

def create_collect_sound():
    """Crea sonido de recolección (tono ascendente positivo)"""
    sample_rate = 44100
    duration = 0.4
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # Tono ascendente (do a sol)
    freq_start = 440  # La4
    freq_end = 660    # Mi5
    frequencies = np.linspace(freq_start, freq_end, len(t))

    # Generar onda con múltiples armónicos para sonido más rico
    sound = np.zeros_like(t)
    for harmonic in [1, 2, 3]:
        amplitude = 0.3 / harmonic
        sound += amplitude * np.sin(2 * np.pi * frequencies * harmonic * t)

    # Envolvente ADSR (Attack, Decay, Sustain, Release)
    attack = int(0.05 * sample_rate)
    decay = int(0.1 * sample_rate)
    sustain = int(0.15 * sample_rate)
    release = len(t) - attack - decay - sustain

    envelope = np.ones_like(t)
    envelope[:attack] = np.linspace(0, 1, attack)
    envelope[attack:attack+decay] = np.linspace(1, 0.7, decay)
    envelope[attack+decay:attack+decay+sustain] = 0.7
    envelope[attack+decay+sustain:] = np.linspace(0.7, 0, release)

    sound = sound * envelope

    # Normalizar
    sound = sound / np.max(np.abs(sound)) * 0.7

    # Convertir a 16-bit
    sound = (sound * 32767).astype(np.int16)

    return sample_rate, sound

def create_claw_sound():
    """Crea sonido mecánico de garra robótica"""
    sample_rate = 44100
    duration = 0.3
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # Sonido mecánico con frecuencias bajas
    sound = np.zeros_like(t)

    # Frecuencias mecánicas
    freqs = [200, 400, 600]
    for i, freq in enumerate(freqs):
        amplitude = 0.2 / (i + 1)
        sound += amplitude * np.sin(2 * np.pi * freq * t)

    # Agregar ruido mecánico
    noise = np.random.normal(0, 0.05, len(t))
    sound += noise

    # Envolvente rápida
    envelope = np.exp(-8 * t)
    sound = sound * envelope

    # Normalizar
    sound = sound / np.max(np.abs(sound)) * 0.6

    # Convertir a 16-bit
    sound = (sound * 32767).astype(np.int16)

    return sample_rate, sound

def create_background_music():
    """Crea música de fondo simple y relajante"""
    sample_rate = 44100
    duration = 30  # 30 segundos (se repetirá)
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # Progresión de acordes simple (Am, F, C, G)
    music = np.zeros_like(t)

    # Dividir en 4 compases
    beats_per_measure = 4
    beat_duration = duration / (beats_per_measure * 4)

    # Acordes (frecuencias fundamentales)
    chords = [
        [220, 261, 330],  # Am (La menor)
        [175, 220, 262],  # F (Fa)
        [262, 330, 392],  # C (Do)
        [196, 247, 294],  # G (Sol)
    ]

    for measure in range(4):
        chord = chords[measure % len(chords)]
        start_idx = int(measure * beat_duration * beats_per_measure * sample_rate)
        end_idx = int((measure + 1) * beat_duration * beats_per_measure * sample_rate)

        if end_idx > len(t):
            end_idx = len(t)

        measure_t = t[start_idx:end_idx] - t[start_idx]

        for freq in chord:
            # Onda suave con múltiples armónicos
            wave = 0.1 * np.sin(2 * np.pi * freq * measure_t)
            wave += 0.05 * np.sin(2 * np.pi * freq * 2 * measure_t)
            music[start_idx:end_idx] += wave

    # Envolvente suave
    fade_in = int(2 * sample_rate)
    fade_out = int(2 * sample_rate)
    envelope = np.ones_like(music)
    envelope[:fade_in] = np.linspace(0, 1, fade_in)
    envelope[-fade_out:] = np.linspace(1, 0, fade_out)
    music = music * envelope

    # Normalizar
    if np.max(np.abs(music)) > 0:
        music = music / np.max(np.abs(music)) * 0.3

    # Convertir a 16-bit
    music = (music * 32767).astype(np.int16)

    return sample_rate, music

def main():
    """Genera todos los sonidos"""
    sounds_dir = "assets/sounds"
    music_dir = "assets/music"
    os.makedirs(sounds_dir, exist_ok=True)
    os.makedirs(music_dir, exist_ok=True)

    print("Creando sonidos...")

    # Sonido de recolección
    sample_rate, sound = create_collect_sound()
    wavfile.write(f"{sounds_dir}/collect.wav", sample_rate, sound)
    print("✓ Sonido de recolección creado")

    # Sonido de garra
    sample_rate, sound = create_claw_sound()
    wavfile.write(f"{sounds_dir}/claw.wav", sample_rate, sound)
    print("✓ Sonido de garra creado")

    # Música de fondo
    sample_rate, music = create_background_music()
    wavfile.write(f"{music_dir}/background.wav", sample_rate, music)
    print("✓ Música de fondo creada")

    print("\n¡Todos los sonidos creados exitosamente!")

if __name__ == "__main__":
    main()

