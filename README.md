# PSE‑data‑pipeline

**ETL pipeline dla danych z PSE** — projekt automatyzujący pobieranie, transformację i ładowanie danych m.in. krajowej generacji KSE, parametrów mocy bilansujących itp. do bazy danych PostgreSQL. Daje możliwość kofiguracji pod preferowane dane z PSE API.

## 🧰 Co to jest  

- Projekt pobiera dane z publicznego API Polskich Sieci Elektroeneretycznych dotyczących rynku energii
- Transformuje dane — waliduje, porządkuje strukturę, normalizuje formaty  
- Ładuje przetworzone dane do bazy PostgreSQL i zapasowych plików CSV
- Może być odpalany jako harmonogram — idealny jako ETL do dalszej analizy lub dashboardów  

## 🚀 Technologie  

- Python
- Pandas  
- SQLAlchemy + psycopg2 (PostgreSQL)  
- Struktura projektu: foldery `extract/`, `transform/`, `load/`, `config/`, `db/`
- Plik `requirements.txt` z wymaganymi bibliotekami  
- Plik `.gitignore` aby nie dublować danych, cache, itp.  
- Licencja: MIT  

## 📦 Jak uruchomić we własnym środowisku

1. Sklonuj repozytorium  
   ```bash
   git clone https://github.com/KrPData/PSE-data-pipeline.git
   cd PSE-data-pipeline
2. pip install -r requirements.txt

    ```
    DB_HOST=localhost  
    DB_PORT=5432  
    DB_NAME=<nazwa_bazy>  
    DB_USER=<użytkownik>  
    DB_PASS=<hasło>  
    ```

3. python run_pipeline.py

## 🗂️ Struktura katalogów
```
PSE-data-pipeline/
├── extract/ # pobieranie danych
├── transform/ # przetwarzanie danych
├── load/ # ładowanie do bazy i plików CSV
├── db/ # pliki db / schematy / migracje
├── config/ # konfiguracje, pliki .env
├── utils/ # funkcje pomocnicze
├── run_pipeline.py # główny skrypt wykonawczy
├── requirements.txt
└── .gitignore
```

Licencja MIT

