# MCP Server für Facade API

Ein Model Context Protocol (MCP) Server in Python, der drei Facade-Endpoints bereitstellt.

## 🎯 Features

- **tamara**: Tool für v1/tamara Endpoint
- **ask**: Tool für v1/ask Endpoint  
- **hybrid_search**: Tool für v1/hybridSearch Endpoint

## 📋 Voraussetzungen

- Python 3.10 oder höher
- pip

## 🚀 Installation

### 1. Virtuelle Umgebung erstellen

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 2. Dependencies installieren

```bash
pip install -r requirements.txt
```

### 3. Server konfigurieren

Öffne `mcp_server.py` und passe die Konfiguration an:

```python
# Deine Facade Base URL
FACADE_BASE_URL = "http://localhost:8080"  # Anpassen!

# Falls Authentication benötigt wird
API_KEY = "dein-api-key"  # Optional
```

## 🔧 Nutzung mit Tabnine

### Schritt 1: Tabnine AI Extension installieren

Falls noch nicht geschehen, installiere die Tabnine Extension in deinem Editor (VS Code, JetBrains, etc.).

### Schritt 2: MCP Server in Tabnine konfigurieren

1. Öffne die Tabnine Settings
2. Navigiere zu "Advanced" oder "MCP Servers"
3. Füge einen neuen MCP Server hinzu:

```json
{
  "mcpServers": {
    "facade-api": {
      "command": "python",
      "args": ["/absoluter/pfad/zu/mcp_server.py"],
      "env": {}
    }
  }
}
```

**Wichtig**: Ersetze `/absoluter/pfad/zu/mcp_server.py` mit dem tatsächlichen Pfad zu deiner Datei.

Beispiel Windows:
```json
"args": ["C:\\Users\\DeinName\\projekt\\mcp_server.py"]
```

Beispiel macOS/Linux:
```json
"args": ["/home/username/projekt/mcp_server.py"]
```

### Schritt 3: Tabnine neu starten

Starte Tabnine neu, damit die Konfiguration geladen wird.

### Schritt 4: MCP Server testen

In Tabnine kannst du nun die Tools nutzen:

```
Nutze das tamara Tool um folgende Anfrage zu stellen: "Zeige mir die neuesten Updates"
```

```
Verwende hybrid_search um nach "Python tutorials" zu suchen
```

## 📝 Tool-Beschreibungen

### tamara

Für Tamara-spezifische Anfragen.

**Parameter:**
- `query` (string, erforderlich): Die Anfrage
- `parameters` (object, optional): Zusätzliche Parameter

**Beispiel:**
```json
{
  "query": "Zeige mir die neuesten Updates",
  "parameters": {
    "limit": 5
  }
}
```

### ask

Für allgemeine Fragen.

**Parameter:**
- `question` (string, erforderlich): Die Frage
- `context` (string, optional): Zusätzlicher Kontext
- `parameters` (object, optional): Zusätzliche Parameter

**Beispiel:**
```json
{
  "question": "Was sind die wichtigsten Features?",
  "context": "Produkt XYZ"
}
```

### hybrid_search

Für hybride Suchvorgänge.

**Parameter:**
- `search_query` (string, erforderlich): Die Suchanfrage
- `filters` (object, optional): Suchfilter
- `limit` (integer, optional): Max. Anzahl Ergebnisse (default: 10)

**Beispiel:**
```json
{
  "search_query": "Python tutorials",
  "filters": {
    "category": "programming",
    "difficulty": "beginner"
  },
  "limit": 5
}
```

## 🧪 Lokales Testen (ohne Tabnine)

Du kannst den Server auch standalone testen:

```bash
python mcp_server.py
```

Der Server wartet dann auf Eingaben über stdio (Standard Input/Output).

## 🔍 Debugging

Falls der Server nicht funktioniert:

1. **Prüfe die Logs**: Tabnine zeigt meist Logs in den Developer Tools
2. **Teste die Facade-Endpoints manuell**: Nutze curl oder Postman
3. **Überprüfe die URL**: Stelle sicher, dass `FACADE_BASE_URL` korrekt ist
4. **Python-Version**: Mindestens Python 3.10 erforderlich

### Facade-Endpoint manuell testen

```bash
curl -X POST http://localhost:8080/v1/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Test"}'
```

## 📦 Payload-Anpassungen

Falls deine Facade andere Payload-Strukturen erwartet, passe die `payload` Objekte in `mcp_server.py` an:

```python
# Beispiel: Andere Struktur für v1/ask
payload = {
    "q": arguments.get("question"),  # statt "question"
    "ctx": arguments.get("context")  # statt "context"
}
```

## 🤝 Support

Bei Fragen oder Problemen:
1. Überprüfe die Facade API-Dokumentation
2. Teste die Endpoints direkt (ohne MCP)
3. Prüfe Tabnine Logs für Fehler

## 📄 Lizenz

MIT License - nutze den Code wie du möchtest!
