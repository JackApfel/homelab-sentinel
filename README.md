# homelab-sentinel

Ein kleines Hobby-Projekt in Python für meinen Homeserver.

## Ziel

- Hardware- und Software-Monitoring
- spätere Anbindung an Home Assistant

## Aktueller Stand

Das Projekt liest aktuell Systemwerte aus und bewertet sie über Schwellwerte:

- CPU
- RAM
- Speicher

## Voraussetzungen

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Installation

```bash
uv sync
```

## Konfiguration

Lege im Projektverzeichnis eine `.env` mit folgenden Werten an:

- `CPU_THRESHOLD_WARNING`
- `CPU_THRESHOLD_CRITICAL`
- `MEMORY_THRESHOLD_WARNING`
- `MEMORY_THRESHOLD_CRITICAL`
- `STORAGE_THRESHOLD_WARNING`
- `STORAGE_THRESHOLD_CRITICAL`
- `GPU_THRESHOLD_WARNING`
- `GPU_THRESHOLD_CRITICAL`

## Nutzung

```bash
uv run homelab-sentinel check
uv run homelab-sentinel status
```

- `check` zeigt die aktuellen Werte inklusive Status.
- `status` gibt den höchsten Status zurück und beendet mit passendem Exit-Code.
