# verktyg för att utvärdera metoderna

def build_alias_to_canonical(
    tier1_phrases,
    tier2_exact_case,
    tier3_custom
):
    alias_to_canonical = {}

    # Tier 1
    for skill in tier1_phrases:
        alias_to_canonical[skill.casefold()] = skill

    # Tier 2
    for canonical, spellings in tier2_exact_case.items():
        for spelling in spellings:
            alias_to_canonical[spelling.casefold()] = canonical

    # Tier 3
    for canonical, aliases in tier3_custom.items():

        for alias in aliases.get("any_case", []):
            alias_to_canonical[alias.casefold()] = canonical

        for alias in aliases.get("exact_case", []):
            alias_to_canonical[alias.casefold()] = canonical

    return alias_to_canonical



def normalize_skills(skills, alias_to_canonical):
    normalized = set()

    for skill in skills:
        clean_skill = skill.strip()

        canonical = alias_to_canonical.get(
            clean_skill.casefold(),
            clean_skill
        )

        normalized.add(canonical)

    return normalized


# metrics:
def calculate_metrics(gold_dict, prediction_dict):
    total_tp = 0
    total_fp = 0
    total_fn = 0

    for ad_id, gold_skills in gold_dict.items():
        predicted_skills = prediction_dict.get(ad_id, set())

        tp = gold_skills & predicted_skills
        fp = predicted_skills - gold_skills
        fn = gold_skills - predicted_skills

        total_tp += len(tp)
        total_fp += len(fp)
        total_fn += len(fn)

    precision = (
        total_tp / (total_tp + total_fp)
        if total_tp + total_fp > 0
        else 0
    )

    recall = (
        total_tp / (total_tp + total_fn)
        if total_tp + total_fn > 0
        else 0
    )

    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall > 0
        else 0
    )

    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "tp": total_tp,
        "fp": total_fp,
        "fn": total_fn
    }


# felanalys:
def create_error_analysis(gold_dict, prediction_dict):
    errors = []

    for ad_id, gold_skills in gold_dict.items():
        predicted_skills = prediction_dict.get(ad_id, set())

        false_positives = predicted_skills - gold_skills
        false_negatives = gold_skills - predicted_skills

        if false_positives or false_negatives:
            errors.append({
                "id": ad_id,
                "false_positives": sorted(false_positives),
                "false_negatives": sorted(false_negatives)
            })

    return errors