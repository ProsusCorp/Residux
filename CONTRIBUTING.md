# Contribuir a Residux_01

Gracias por contribuir. Este documento define reglas minimas para mantener el proyecto consistente.

## Flujo de trabajo

1. Crea una rama desde `main`:
   - `feat/<descripcion-corta>`
   - `fix/<descripcion-corta>`
2. Haz cambios pequenos y enfocados.
3. Ejecuta validaciones minimas antes de abrir PR.
4. Abre Pull Request con descripcion clara del problema y la solucion.

## Convencion de commits

Usa prefijos simples:

- `feat:` nueva funcionalidad
- `fix:` correccion de bug
- `docs:` cambios de documentacion
- `refactor:` mejora interna sin cambio funcional esperado
- `chore:` tareas de mantenimiento

Ejemplo:

`feat: agregar fallback de configuracion local`

## Validacion minima antes de PR

- El juego inicia con `python main.py`.
- No hay errores de importacion en arranque.
- README y rutas referenciadas estan actualizadas.
- No se incluyen secretos ni configuraciones locales.

## Reglas para configuracion y assets

- No subir `config.local.json`.
- Si agregas nuevos assets, documenta origen y licencia en `assets/ATTRIBUTION.md`.
- Evita archivos multimedia gigantes sin necesidad (comprimir cuando sea posible).

## Checklist sugerido para PR

- [ ] Cambios acotados al objetivo del PR
- [ ] Documentacion actualizada
- [ ] Sin archivos temporales/caches
- [ ] Se verifico ejecucion local
