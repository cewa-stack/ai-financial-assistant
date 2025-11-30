# 💰 AI Financial Assistant

**[TYTUŁ PRODUKTU]**
## Intelligent Financial Assistant | FastAPI & Streamlit Application

Krótki opis produktu
Kompleksowa aplikacja finansowa wspomagana sztuczną inteligencją do analizy wydatków, generowania rekomendacji i śledzenia celów oszczędnościowych.

❤️ **[Pierwsze zdanie - benefit]** Automatycznie kategoryzuje transakcje i zapewnia inteligentne rekomendacje oszczędnościowe, pomagając osiągnąć cele finansowe.
⭐️ **[Drugie zdanie - cecha]** Zbudowany na solidnej architekturze **FastAPI** (API) i **Streamlit** (Dashboard) z wbudowanymi narzędziami analitycznymi (Pandas, Scikit-learn, Plotly).
✨ **[Trzecie zdanie - zastosowanie]** Idealne rozwiązanie do osobistego zarządzania finansami, umożliwiające importowanie danych CSV, wizualizację kluczowych wskaźników KPI i testowanie nowych modeli ML.

---

### 🚀 Funkcjonalności

* **📊 Importowanie danych**: Wgrywanie transakcji z pliku CSV.
* **🏷️ Kategoryzacja**: Automatyczna kategoryzacja transakcji (reguły + ML).
* **📈 Analiza finansowa**: Obliczanie KPI, wykrycie anomalii, trendy MoM.
* **💡 Rekomendacje**: Inteligentne sugestie oszczędnościowe.
* **📄 Raporty**: Generowanie raportów HTML i PDF (ReportLab).
* **🎯 Cele oszczędnościowe**: Śledzenie postępu w realizacji celów.

### 🛠️ Stos Technologiczny

* **Backend & API:** Python, FastAPI, Uvicorn, SQLAlchemy (SQLite)
* **Frontend & Dashboard:** Streamlit, Plotly, Matplotlib
* **ML & Data:** Pandas, NumPy, Scikit-learn
* **Deployment Tools:** `run_services.py` (Orchestrator), `ngrok` (Public Tunnels)

### 📂 Struktura Projektu

ai-financial-assistant/ ├── api/ # Logika biznesowa, API endpoints (FastAPI) │ └── main.py ├── app/ # Interfejs użytkownika (Streamlit) │ └── streamlit_app.py ├── financial_assistant.db # Baza danych (IGNORED by Git!) ├── ngrok.yml # Konfiguracja tuneli dla ngrok ├── run_services.py # Skrypt Pythona do uruchamiania API i Dashboardu jednocześnie ├── run_all.bat # Skrypt BAT do uruchamiania w Windows ├── run_with_ngrok.bat # Skrypt do uruchamiania z tunelowaniem ├── requirements.txt # Zależności └── README.md


### ⚙️ Szybki Start (Lokalnie)

#### 1. Instalacja

```bash
# Sklonuj repozytorium
git clone [https://github.com/cewa-stack/ai-financial-assistant.git](https://github.com/cewa-stack/ai-financial-assistant.git)
cd ai-financial-assistant

# Stwórz i aktywuj środowisko wirtualne
python -m venv venv
source venv/bin/activate  # lub .\venv\Scripts\activate dla Windows

# Zainstaluj zależności
pip install -r requirements.txt
2. Konfiguracja
Utwórz plik .env i wpisz w nim swój klucz.

# Plik .env
# Jeśli używasz usług AI/LLM, umieść tu klucz:
# GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
SECRET_KEY="A_VERY_SECRET_KEY_FOR_SESSIONS"
3. Uruchomienie
Aby uruchomić oba serwisy (API + Streamlit) jednocześnie w jednym procesie (zalecane):

Bash

python run_services.py
Aby uruchomić oba serwisy z publicznym tunelem ngrok (dla testów zewnętrznych):

Bash

# Upewnij się, że masz ngrok zainstalowany i autoryzowany!
run_with_ngrok.bat
Cechy Asystenta Finansowego:
✔️ Złożona architektura wielousługowa (API + UI). ✔️ Obsługa danych w postaci bazy danych (SQLite) i CSV. ✔️ Automatyzacja uruchamiania za pomocą skryptów.

❓ Pytanie: Jakie jest zastosowanie ML w tym projekcie? ✅ Odpowiedź: Machine Learning (Scikit-learn) jest używany do automatycznej kategoryzacji nieznanych transakcji oraz do wykrywania anomalii w wydatkach (np. nietypowo wysokie/niskie wartości).