# AI regulation crosswalk

This repo turns six AI governance frameworks into one machine readable table and then asks a practical question: given a description of a model (what it does, what data it uses, how much its decisions matter, where it runs, whether it uses generative AI), which frameworks apply, which obligations attach, and how much do the frameworks overlap. The frameworks covered are the EU AI Act, Canada's proposed AIDA, the NIST AI RMF 1.0, ISO/IEC 42001, OSFI Guideline E-23 on model risk management, and the Colorado AI Act. Twelve control themes are mapped across all six, each with a short section reference and a coverage level of required, recommended or not addressed.

## Connection to the research

This is the applied side of "The Governance Lag: Why Slow AI Adoption Is the Larger Risk" (Rehman, 2026). One argument in that paper is that governance lag is partly self inflicted: organisations treat every new framework as a separate compliance project, so the cost of governance rises with the number of jurisdictions rather than with the actual risk of the system. The crosswalk shows that most of the frameworks ask for the same dozen things. Once an organisation has a documented, monitored, bias tested model with a named owner and an incident process, it has done most of the work under all six. The overlap heatmap makes that point visually. The same control themes also appear in the Theory of Change governance framework built for MMAI 803 AI Ethics and Policy.

## Why this matters in financial services

A bank or payments company with Canadian, US and EU exposure faces OSFI E-23 from 2027, the EU AI Act high risk rules for credit scoring, Colorado's consequential decision rules, and whatever replaces AIDA. A model inventory that tags each model with the attributes used here (use case, data types, decision impact, regions, generative) can be run through this script to produce a first pass obligation list for each model, which is the starting point for a gap assessment.

## How to run

```
pip install -r requirements.txt
python crosswalk.py
python crosswalk.py cases/credit_scoring.json
pytest
```

Running with no arguments processes every case in `cases/`. Three examples are included: a credit scoring model, a transaction fraud model, and a generative customer service chatbot.

## Outputs

`outputs/obligations_<case>.md` is a readable report with the frameworks in scope, a coverage table by theme, and each obligation with its section reference. `outputs/obligations_<case>.csv` holds the same rows for loading into a tracker. `outputs/overlap_heatmap.png` counts, for every pair of frameworks, the number of control themes both address, summed across the cases run.

The console prints the number of required controls per framework. NIST shows zero because it is voluntary and everything in it is scored as recommended. OSFI E-23 only appears when the operator is a financial institution in Canada.

## How the mapping works

`data/frameworks.json` holds the frameworks, their regions, and the twelve themes. Each theme has triggers: most apply to any system, human oversight applies when decision impact is medium or high, bias testing applies when personal data is used or decisions matter, and the generative theme applies only when the case says it uses generative AI. `crosswalk.py` picks frameworks by region and operator type, filters themes by trigger, and builds the obligation rows. The overlap matrix counts themes where both frameworks score at least recommended.

## Accuracy note

The section references were written from my reading of the published texts and guidance documents as of late 2026. They are a starting point for a gap assessment, not legal advice. Check every reference against the current text before relying on it. AIDA in particular died on the order paper in January 2025, so its entries reflect the last published draft and the government's companion document. The Colorado effective date and OSFI E-23 implementation date have both moved once and may move again.

## Limitations

Six frameworks and twelve themes is a simplification. Sector rules such as fair lending law, privacy law (PIPEDA, GDPR) and consumer protection are not included even though they drive much of the real obligation set for credit and payments models. The coverage levels are judgement calls at the theme level and hide a lot of variation in how detailed each framework is.

Saif Rehman, MMAI, Smith School of Business, Queen's University
