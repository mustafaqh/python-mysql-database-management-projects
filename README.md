# Database Management Projects

This repository contains projects and exercises related to **Database Management Systems (DBMS)**.  
It includes both **practical code implementations** in Python + MySQL and **theoretical database design exercises** (ER modeling, relational algebra, normalization).

---

##  Contents

###  1. Star Wars Database (Python + MySQL)
A Python-based project that creates and queries a database of planets and species (inspired by Star Wars).  
It demonstrates how to combine **Python, SQL, and CSV data** into an interactive command-line application.

**Files:**
- `db_setup.py` → Creates the database `habeb`, tables (`species`, `planets`), and imports data from CSVs.  
- `db_cli.py` → Provides a CLI menu for querying the database (list planets, search species, find climate, etc.).  
- `species.csv` / `planets.csv` → Dataset files (placeholders with headers if missing).  

**Features (CLI Menu):**
1. List all planets  
2. Search planet details by name  
3. Find species taller than a given height  
4. Discover the most likely desired climate of a species  
5. Show average lifespan per species classification  
6. Exit  

---

###  2. Database Design Exercises (PDF)
A collection of theoretical DBMS problems and solutions, including:  
- Entity-Relationship (ER) modeling  
- Relationship types (one-to-one, one-to-many, many-to-many)  
- Relational algebra queries  
- Functional dependencies (FDs)  
- Keys and normalization (3NF vs BCNF)  
- Schema decomposition  

**File:**  
- `database-design-exercises.pdf`

---

##  Requirements (for Python Project)
- Python 3.x  
- MySQL Server  
- MySQL Connector for Python  

Install dependencies:
```bash
pip install mysql-connector-python
```

---

##  How to Run (Python Project)
1. Start MySQL server and ensure credentials match:
   - **user:** `root`
   - **password:** `root`
   - **host:** `127.0.0.1`

2. Run the CLI program:
```bash
python db_cli.py
```

The program will create the database if not already present and load data from CSV files.

---

##  Purpose
These projects were created to:
- Practice **database creation, schema design, and normalization**.  
- Explore **SQL queries, joins, and aggregation**.  
- Learn how to integrate **Python with MySQL** for database applications.  
- Strengthen both **theoretical DBMS concepts** and **practical implementation**.

---

##  License
This repository is licensed under the [MIT License](LICENSE).

---

##  Author
 **Mustafa Habeb**  
Fresh Software Engineer passionate about **databases, backend systems, and software engineering**.
