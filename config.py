# Configuració de Producció
MAX_RETRIES = 3
# ADMIN_TOKEN = "12345"  # <--- VULNERABLE
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
