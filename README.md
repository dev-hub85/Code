# 🧠 AI Algorithm Problems

> A collection of classic Artificial Intelligence problems implemented in **Python** and **Prolog** — covering search, constraint satisfaction, and knowledge-based reasoning.

---

## 📁 Project Structure

```
├── Python Scripts
│   ├── 01problem.py            # 0/1 Knapsack problem
│   ├── 1's.py                  # 1s problem
│   ├── 4q.py                   # 4 Queens problem
│   ├── 8q.py                   # 8 Queens problem
│   ├── CSP_Aus_MapColoring.py  # CSP — Australia map coloring
│   ├── csp_cities.py           # CSP — cities constraint problem
│   ├── f.py                    # Helper / utility script
│   ├── file.py                 # General problem script
│   ├── map.py                  # Map coloring problem
│   ├── q2.py                   # Queens variant
│   ├── q22.py                  # Queens variant
│   ├── queen.py                # N-Queens solution
│   ├── queenproblemg.py        # Queens problem (graphical)
│   └── s.py                    # Search / utility script
│
└── Prolog Scripts
    ├── a1l4.pl                  # Prolog logic problem
    ├── file.pl                  # General Prolog facts & rules
    ├── resistance.pl            # Resistance / circuit reasoning
    ├── s.pl                     # Prolog search script
    ├── symptoms.pl              # Symptom-based diagnosis (expert system)
    └── symptoms.pl~             # Backup of symptoms.pl
```

---

## 🧩 Problems Overview

### 🐍 Python

| File | Problem | Technique |
|------|---------|-----------|
| `01problem.py` | 0/1 Knapsack | Dynamic Programming |
| `1's.py` | 1s Problem | — |
| `4q.py` | 4 Queens | Backtracking |
| `8q.py` | 8 Queens | Backtracking |
| `queen.py` | N-Queens | Backtracking |
| `queenproblemg.py` | N-Queens (Graphical) | Backtracking + Visualization |
| `q2.py` | Queens Variant | Backtracking |
| `q22.py` | Queens Variant | Backtracking |
| `CSP_Aus_MapColoring.py` | Australia Map Coloring | Constraint Satisfaction (CSP) |
| `csp_cities.py` | Cities CSP | Constraint Satisfaction (CSP) |
| `map.py` | Map Coloring | Constraint Satisfaction (CSP) |

### 📜 Prolog

| File | Problem | Description |
|------|---------|-------------|
| `symptoms.pl` | Medical Expert System | Diagnoses based on symptom rules |
| `resistance.pl` | Circuit Reasoning | Calculates resistance using logical rules |
| `s.pl` | Search Problem | Prolog-based search |
| `a1l4.pl` | Logic Problem | Prolog facts and inference |
| `file.pl` | General Rules | General Prolog facts & queries |

---

## ⚙️ Prerequisites

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Run `.py` scripts |
| SWI-Prolog | Run `.pl` scripts |

**Install SWI-Prolog:**
- **macOS:** `brew install swi-prolog`
- **Ubuntu/Linux:** `sudo apt install swi-prolog`
- **Windows:** Download from [swi-prolog.org](https://www.swi-prolog.org/Download.html)

---

## 🚀 Running the Scripts

### Python

```bash
python <filename>.py
```

**Examples:**
```bash
python 8q.py
python CSP_Aus_MapColoring.py
python 01problem.py
```

### Prolog

```bash
swipl <filename>.pl
```

**Examples:**
```bash
swipl symptoms.pl
swipl resistance.pl
```

Once inside the Prolog shell, query the knowledge base:

```prolog
?- diagnose(X).
?- resistance(series, [10, 20, 30], R).
?- halt.
```

---

## 📌 Notes

- Files ending in `~` (e.g. `symptoms.pl~`, `file.pl~`) are editor backup files and can be ignored.
- Multiple Queens files (`q2.py`, `q22.py`, `queen.py`, `queenproblemg.py`) represent different implementations and visualizations of the same problem.
