import json
from pathlib import Path

CACHE_DIR = Path.home() / ".cache/qtile"
SETTINGS_FILE = CACHE_DIR / "settings.json"

def init_cache():
    """Inicializa o diretório de cache."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

def load_settings():
    """Carrega as configurações do arquivo JSON."""
    init_cache()
    if SETTINGS_FILE.exists():
        try:
            with open(SETTINGS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

def save_settings(data: dict):
    """Salva as configurações no arquivo JSON."""
    init_cache()
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_setting(key: str, default=None):
    """Recupera uma configuração."""
    settings = load_settings()
    return settings.get(key, default)

def set_setting(key: str, value):
    """Define uma configuração."""
    settings = load_settings()
    settings[key] = value
    save_settings(settings)