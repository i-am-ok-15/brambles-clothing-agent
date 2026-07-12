
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/i-am-ok-15/brambles-clothing-agent)

---

# Brambles Clothing Agent

An automated decision-support system that generates weather-appropriate clothing
recommendations for young children. It fetches real-time weather data, applies a
rule-based clothing selection engine, and uses an LLM to produce a friendly
Markdown report, which is then rendered into a static website.

---

## How It Works

The system runs as a linear pipeline:

1. **Weather** — Fetches a 5-day forecast from the OpenWeather API and filters
   it to the active hours (09:00–18:00) of the following day.
2. **Clothing selection** — Maps the mean "feels like" temperature to clothing
   items (head, body, legs, feet, hands, etc.) using thresholds defined in
   `clothing.json`.
3. **AI agent** — Passes the selected clothing list and weather data to an LLM
   (via OpenRouter), which returns a structured Markdown report with a
   "Brambles' Tip" for parents.
4. **Static site generator** — Converts the Markdown output into a
   production-ready HTML website.

---

## Project Structure

```
brambles-clothing-agent/
├── main.py                  # Orchestrates the full pipeline
├── main.sh                  # Shell script to run pipeline + SSG build
├── clothing.json            # Clothing rules by temperature threshold
├── clothing_selectors.py    # Rule-based clothing selection logic
├── weather_calls/           # Weather API requests and analysis
├── ai_agent/                # LLM agent and prompt configuration
├── ssg/                     # Static site generator
└── pyproject.toml           # Dependencies and project metadata
```

---

## Requirements

- Python 3.13+
- `uv` (recommended) or `pip`
- An [OpenWeather API](https://openweathermap.org/api) key
- An [OpenRouter](https://openrouter.ai/) API key

---

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   uv sync
   # or
   pip install .
   ```
3. Create a `.env` file in the project root:
   ```
   OPENWEATHER_API_KEY=your_key_here
   OPENROUTER_API_KEY=your_key_here
   ```

---

## Usage

Run the full pipeline (data processing + static site build):

```bash
bash main.sh
```

Or run just the data/AI step:

```bash
python main.py
```

---

## Dependencies

| Package          | Version   |
|------------------|-----------|
| `openai`         | >=2.45.0  |
| `python-dotenv`  | 1.1.0     |
| `requests`       | >=2.34.2  |