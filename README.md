# PES2UG24CS665 – Software Engineering Lab Submissions

Lab submissions for the Software Engineering course (Section K), SRN **PES2UG24CS665**.

## Repository structure

```
Labs/
├── Lab 1/   Problem statement and UML diagram
├── Lab 2/   JIRA setup and learning submission
├── Lab 3/   Component diagram and architectural style justification
├── Lab 4/   Flappy Bird (Pygame) – vibe coding lab
│   ├── game/     game_engine.py, bird.py, pipe.py
│   └── sounds/   flap.wav, score.wav, death.wav
├── Lab 5/   Static code analysis of the bank account system
├── Lab 6/   Code and branch coverage for the ride-share fare application
└── Lab 7/   Fuzz testing (Hypothesis) of the ride-share fare application
```

## Lab summaries

| Lab | Topic | Key files |
|-----|-------|-----------|
| 1 | Problem statement and UML | `PES2UG24CS665_LAB1_SE.pdf`, `PES2UG24CS665_UMLDIAGRAM.pdf` |
| 2 | JIRA | `SE_Lab-2_JIRA_SectionK_PES2UG24CS665_VANISHREE.pdf` |
| 3 | Component diagram (layered architecture) | `SE_Lab-3_CompDiag_SectionK_PES2UG24CS665_VANISHREE.pdf` |
| 4 | Flappy Bird vibe coding | `main.py`, `README.md`, `requirements.txt`, `Flappy_Bird_Before_After.webm`, `chathistory.pdf` |
| 5 | Static analysis (pylint, flake8, bandit) | `bank_account_system_before.py`, `bank_account_system.py`, `*_report_before.txt`, `*_report_after.txt`, `issues.md`, `reflection.md` |
| 6 | Code and branch coverage | `ride_share_fare.py`, `*CoverageTest_*.py`, `Coverage_Analysis_BEFORE_AFTER_PES2UG24CS665.pdf`, `GitCommits_PES2UG24CS665.pdf`, `PES2UG24CS665_codeandbranch.odt`, coverage screenshots |
| 7 | Fuzz testing with Hypothesis | `ride_share_fare.py`, `test_ride_share_fare.py`, `PES2UG24CS665_LAB07SCREENSHOTS.pdf` |

## Running the tests

Lab 6 and Lab 7 use the ride-share fare application:

```bash
cd "Labs/Lab 7"
python -m pytest test_ride_share_fare.py -v
```

Lab 4 requires Pygame:

```bash
cd "Labs/Lab 4"
pip install -r requirements.txt
python main.py
```
