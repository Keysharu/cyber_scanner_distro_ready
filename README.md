# Cyber Scanner Distro Ready

Un escáner táctico de telemetría de hardware en un entorno seguro y sin dependencias externas.
Ha sido diseñado para conocer a detalle las características del hardware disponible, con la finalidad de optimizar la creación de una distribución Linux personalizada.

## 🚀 Características
- **Auditoría rápida y sin dependencias:** Utiliza librerías nativas de Python (`os`, `platform`, `subprocess`, etc.).
- **Interfaz de terminal (Cyberpunk / Metal Gear Solid):** Salida formateada con colores ANSI para una mejor legibilidad.
- **Telemetría completa:**
  - Subsistema logístico y procesamiento (OS, CPU, Núcleos).
  - Subsistema gráfico (Controladores de GPU y vídeo).
  - Subsistema de memoria volátil (RAM).
  - Subsistema de almacenamiento (Discos y particiones).
  - Subsistema de conectividad (Adaptadores de red y Bluetooth).
  - Subsistema de energía (Batería vs alimentación AC).

## 🛠️ Uso

El script no requiere la instalación de paquetes adicionales (como `pip install`). Solo necesitas tener **Python 3** instalado en tu sistema.

Ejecuta el script desde tu terminal:

```bash
python cyber_scanner_distro_ready.py
```

## 🧑‍💻 Autor

Creado por **Keysharu / El taller de la gatita tech**.

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
