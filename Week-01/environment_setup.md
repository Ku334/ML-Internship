# Environment Setup

## System
- OS: Windows 11
- Python version: 3.x.x
- Editor: VS Code

## Virtual Environment
- Created with: `python -m venv venv`
- Activated with: `venv\Scripts\activate`
- The `venv/` folder is excluded from Git using `.gitignore`.

## Installed Libraries
| Library | Version |
|---------|---------|
| numpy | 2.3.3 |
| pandas | 2.3.3 |
| matplotlib | 3.10.7 |
| scikit-learn | 1.7.2 |

## Installed with:

```
pip install numpy pandas matplotlib scikit-learn
```

All exact package versions are saved in `requirements.txt`. To recreate this environment:

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Verification
Ran `python test.py`, which imports all four libraries and prints their versions. Everything imported without errors.

## Project Structure
```
ML-Internship/
├── venv/
├── Week-01/
│   ├── exercises/
│   │   ├── python_exercises_part1.py
│   │   ├── python_exercises_part2.py
│   │   └── data/
│   ├── environment_setup.md
│   └── weekly_log.md
├── .gitignore
├── README.md
├── requirements.txt
└── test.py
```