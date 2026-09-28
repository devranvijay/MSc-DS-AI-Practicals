# MSc Data Science & AI — Practical Repository

**University:** University of Mumbai (UoM)
**Program:** FYMSc Data Science & Artificial Intelligence
**Author:** Ranvijay Singh

This repository is a running, semester-by-semester archive of every
university practical performed across the MSc DS & AI program. It is
organized **semester-wise, then subject-wise, then practical-wise**,
so it stays navigable as it grows across all four semesters, and
doubles as a GitHub portfolio and viva/interview revision resource.

## Repository Structure

```
MSc-DS-AI-Practicals/
├── README.md                 <- this master index (updated every semester)
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── Semester_1/
│   ├── 502_Essential_Technologies_for_Data_Science_Practical/
│   │   ├── README.md
│   │   └── P01 ... P10        (10 practicals)
│   └── 504_Artificial_Intelligence_Practical/
│       ├── README.md
│       └── P01 ... P10        (10 practicals)
│
├── Semester_2/                <- added when Semester 2 begins
├── Semester_3/
└── Semester_4/
```

Every practical folder contains a self-contained, independently
runnable script, a `README.md` (aim, theory, how to run, sample
output, viva Q&A), and its own `data/`/`outputs/` sub-folder where
applicable.

## Semester 1 — Completed

| Subject | Code | Practicals |
|---|---|---|
| Essential Technologies for Data Science | 502 | 10/10 |
| Artificial Intelligence | 504 | 10/10 |

See `Semester_1/502_.../README.md` and `Semester_1/504_.../README.md`
for the full practical index of each subject.

## How to Run Any Practical

```bash
git clone https://github.com/devranvijay/MSc-DS-AI-Practicals.git
cd MSc-DS-AI-Practicals
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

python Semester_1/502_Essential_Technologies_for_Data_Science_Practical/P05_Univariate_Analysis/univariate_analysis.py
```

## Roadmap

- [x] Semester 1 — 502 (Essential Technologies for Data Science), 504 (Artificial Intelligence)
- [ ] Semester 2 — subjects to be added as the semester progresses
- [ ] Semester 3
- [ ] Semester 4

## Author

Ranvijay Singh — Haitech Medical Solutions Private Limited
