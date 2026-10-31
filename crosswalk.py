"""Map a described AI system to the obligations it picks up under six AI
governance frameworks and show where the frameworks overlap.

Usage:
    python crosswalk.py                 runs every case in cases/
    python crosswalk.py cases/credit_scoring.json
"""

import json
import os
import sys

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data", "frameworks.json")
OUT = os.path.join(HERE, "outputs")

LEVEL_SCORE = {"required": 2, "recommended": 1, "not addressed": 0}

# OSFI E-23 only binds federally regulated financial institutions, so the
# operator type matters for that one. Everything else is keyed on region.
REGION_FRAMEWORKS = {
    "eu": ["eu_ai_act"],
    "canada": ["aida", "osfi_e23"],
    "us": ["colorado_ai_act", "nist_ai_rmf"],
    "global": ["nist_ai_rmf", "iso_42001"],
}


def load_frameworks(path=DATA):
    with open(path) as f:
        return json.load(f)


def applicable_frameworks(case, spec):
    found = set(["nist_ai_rmf", "iso_42001"])
    for region in case.get("regions", []):
        for fw in REGION_FRAMEWORKS.get(region, []):
            found.add(fw)
    if case.get("operator_type") != "financial_institution":
        found.discard("osfi_e23")
    order = list(spec["frameworks"].keys())
    return [fw for fw in order if fw in found]


def theme_applies(theme, case):
    triggers = theme.get("triggers", ["any"])
    if "any" in triggers:
        return True
    for t in triggers:
        key, val = t.split(":")
        if key == "generative":
            if str(case.get("generative", False)).lower() == val:
                return True
        elif key == "data_types":
            if val in case.get("data_types", []):
                return True
        else:
            if str(case.get(key, "")) == val:
                return True
    return False


def build_obligations(case, spec):
    frameworks = applicable_frameworks(case, spec)
    rows = []
    for theme in spec["themes"]:
        if not theme_applies(theme, case):
            continue
        for fw in frameworks:
            entry = theme["map"].get(fw)
            if entry is None:
                continue
            rows.append({
                "theme_id": theme["id"],
                "theme": theme["name"],
                "framework": fw,
                "framework_name": spec["frameworks"][fw]["name"],
                "level": entry["level"],
                "reference": entry["ref"],
                "obligation": entry["text"],
            })
    return pd.DataFrame(rows)


def overlap_matrix(obligations):
    """Count themes where both frameworks are at least 'recommended'."""
    pivot = obligations.pivot_table(index="theme_id", columns="framework",
                                    values="level", aggfunc="first")
    scored = pivot.apply(lambda col: col.map(LEVEL_SCORE)).fillna(0)
    active = (scored > 0).astype(int)
    overlap = active.T.dot(active)
    return overlap, scored


def coverage_table(scored):
    return (scored == 2).sum().sort_values(ascending=False)


def write_markdown(case, obligations, scored, spec, path):
    lines = []
    lines.append("# Obligations for case: %s" % case["name"])
    lines.append("")
    lines.append(case.get("description", ""))
    lines.append("")
    lines.append("Inputs: use case %s, data types %s, decision impact %s, regions %s, generative %s."
                 % (case["use_case"], ", ".join(case["data_types"]), case["decision_impact"],
                    ", ".join(case["regions"]), case.get("generative", False)))
    lines.append("")
    lines.append("## Frameworks in scope")
    lines.append("")
    for fw in obligations["framework"].unique():
        info = spec["frameworks"][fw]
        lines.append("%s (%s). %s" % (info["name"], info["type"], info["note"]))
        lines.append("")
    lines.append("## Coverage by theme")
    lines.append("")
    header = "| Theme | " + " | ".join(scored.columns) + " |"
    lines.append(header)
    lines.append("|" + "---|" * (len(scored.columns) + 1))
    names = {t["id"]: t["name"] for t in spec["themes"]}
    for theme_id, row in scored.iterrows():
        cells = []
        for v in row:
            cells.append({2: "required", 1: "recommended", 0: "no"}[int(v)])
        lines.append("| %s | %s |" % (names[theme_id], " | ".join(cells)))
    lines.append("")
    lines.append("## Obligations")
    lines.append("")
    for theme_id, group in obligations.groupby("theme_id", sort=False):
        lines.append("### " + names[theme_id])
        lines.append("")
        for _, r in group.iterrows():
            if r["level"] == "not addressed":
                lines.append("%s: not addressed. %s" % (r["framework_name"], r["obligation"]))
            else:
                lines.append("%s (%s, %s): %s" % (r["framework_name"], r["level"], r["reference"], r["obligation"]))
            lines.append("")
    with open(path, "w") as f:
        f.write("\n".join(lines))


def plot_overlap(overlap, spec, path):
    labels = [spec["frameworks"][fw]["name"].split(" (")[0] for fw in overlap.columns]
    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(overlap.values, cmap="Blues")
    ax.set_xticks(range(len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_yticklabels(labels)
    for i in range(len(labels)):
        for j in range(len(labels)):
            ax.text(j, i, int(overlap.values[i, j]), ha="center", va="center",
                    color="white" if overlap.values[i, j] > overlap.values.max() / 2 else "black")
    ax.set_title("Shared control themes between frameworks")
    fig.colorbar(im, ax=ax, label="themes both address")
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def run_case(case_path, spec=None, out_dir=OUT):
    if spec is None:
        spec = load_frameworks()
    with open(case_path) as f:
        case = json.load(f)
    obligations = build_obligations(case, spec)
    overlap, scored = overlap_matrix(obligations)
    os.makedirs(out_dir, exist_ok=True)
    write_markdown(case, obligations, scored, spec,
                   os.path.join(out_dir, "obligations_%s.md" % case["name"]))
    obligations.to_csv(os.path.join(out_dir, "obligations_%s.csv" % case["name"]), index=False)
    return case, obligations, overlap, scored


def main(args):
    spec = load_frameworks()
    if args:
        paths = args
    else:
        case_dir = os.path.join(HERE, "cases")
        paths = sorted(os.path.join(case_dir, p) for p in os.listdir(case_dir) if p.endswith(".json"))
    combined = None
    for p in paths:
        case, obligations, overlap, scored = run_case(p, spec)
        required = coverage_table(scored)
        print("case %s: %d frameworks, %d themes, %d obligations"
              % (case["name"], obligations["framework"].nunique(), scored.shape[0], len(obligations)))
        print("  required controls per framework:")
        for fw, n in required.items():
            print("    " + fw.ljust(18) + " " + str(n))
        combined = overlap if combined is None else combined.add(overlap, fill_value=0)
    if combined is not None:
        plot_overlap(combined, spec, os.path.join(OUT, "overlap_heatmap.png"))
        print("wrote outputs/overlap_heatmap.png")


if __name__ == "__main__":
    main(sys.argv[1:])
