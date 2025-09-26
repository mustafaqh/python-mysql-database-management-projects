# Star Wars Database (Python + MySQL)

This project is a **Python + MySQL application** that creates and queries a database of **planets and species** (inspired by Star Wars).  
It demonstrates how to combine **Python, SQL, and CSV files** into an interactive command-line tool.

---

##  Description
- Creates a database named **`habeb`**.  
- Two tables are created:
  - **species** → name, classification, designation, average_height, skin_colors, hair_colors, eye_colors, average_lifespan, language, homeworld  
  - **planets** → name, rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population  
- Data is imported from `species.csv` and `planets.csv`.  
- A command-line menu allows users to query the database interactively.

---

##  Files
- `db_setup.py` → Sets up the database and imports data from CSVs.  
- `db_cli.py` → Provides a menu-driven CLI for queries.  
- `species.csv` → Dataset of species (placeholder with headers if missing).  
- `planets.csv` → Dataset of planets (placeholder with headers if missing).  

---

##  Features (Menu Options)
1. List all planets  
2. Search for a planet by name (show all details)  
3. Find species taller than a given height  
4. Find the most likely desired climate of a given species  
5. Show average lifespan per species classification  
6. Exit  

---

##  Requirements
- Python 3.x  
- MySQL Server  
- MySQL Connector for Python  

Install dependencies:
```bash
pip install mysql-connector-python
```

---

##  How to Run
1. Start MySQL server and ensure credentials match in code:
   - **user:** `root`
   - **password:** `root`
   - **host:** `127.0.0.1`

2. Run the CLI program:
```bash
python db_cli.py
```

The program will create the database (if not already created), set up tables, and load data from CSV files.

---

##  Purpose
This project was created to:
- Practice **Python database programming**.  
- Explore **SQL queries (joins, conditions, aggregations)**.  
- Integrate CSV data into a relational database.  
- Build a **menu-driven CLI** for interactive database exploration.  

---

##  Author
**Mustafa Habeb**  
Fresh Software Engineer passionate about **databases, backend systems, and software engineering**.
