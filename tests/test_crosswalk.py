import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import crosswalk


def test_every_theme_maps_every_framework():
    spec = crosswalk.load_frameworks()
    fws = set(spec["frameworks"].keys())
    for theme in spec["themes"]:
        assert set(theme["map"].keys()) == fws
        for entry in theme["map"].values():
            assert entry["level"] in crosswalk.LEVEL_SCORE


def test_osfi_only_for_financial_institutions():
    spec = crosswalk.load_frameworks()
    bank = {"regions": ["canada"], "operator_type": "financial_institution"}
    retailer = {"regions": ["canada"], "operator_type": "retailer"}
    assert "osfi_e23" in crosswalk.applicable_frameworks(bank, spec)
    assert "osfi_e23" not in crosswalk.applicable_frameworks(retailer, spec)


def test_generative_theme_only_when_generative():
    spec = crosswalk.load_frameworks()
    base = {"use_case": "x", "data_types": ["personal"], "decision_impact": "low",
            "regions": ["eu"], "operator_type": "other"}
    plain = crosswalk.build_obligations(dict(base, generative=False), spec)
    gen = crosswalk.build_obligations(dict(base, generative=True), spec)
    assert "generative_ai" not in plain["theme_id"].values
    assert "generative_ai" in gen["theme_id"].values


def test_overlap_matrix_is_symmetric(tmp_path):
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    case = os.path.join(here, "cases", "credit_scoring.json")
    _, _, overlap, _ = crosswalk.run_case(case, out_dir=str(tmp_path))
    assert (overlap.values == overlap.values.T).all()
    assert os.path.exists(tmp_path / "obligations_credit_scoring.md")
