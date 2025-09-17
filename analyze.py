"""
Analyzes transcript sessions → extracts truth + contradictions
Rule-based simple version for Innov8 prelims
"""

import re
from schema import TruthWeaverResult

# --- Helper functions ---

def extract_years(text: str) -> list:
    """
    Find all mentions of years of experience in text.
    Returns a list of 'X years' strings found.
    """
    matches = re.findall(r'(\d+)\s*years?', text.lower())
    return [m + " years" for m in matches]

def extract_languages(text: str) -> list:
    """
    Find programming languages mentioned.
    Extend this list if needed.
    """
    languages = ['python', 'java', 'c++', 'c#', 'javascript', 'go', 'rust']
    found = []
    for lang in languages:
        if lang in text.lower():
            found.append(lang)
    return found

def extract_skill_level(text: str) -> str:
    """
    Detect beginner/intermediate/advanced/expert.
    """
    t = text.lower()
    if 'beginner' in t:
        return 'beginner'
    elif 'intermediate' in t:
        return 'intermediate'
    elif 'advanced' in t or 'expert' in t:
        return 'advanced'
    return ''

def detect_leadership(all_texts: list) -> str:
    """
    Look across all sessions:
    if 'led a team'/'managed' present AND 'work alone' present → fabricated.
    else if only leadership present → true.
    else → 'none'
    """
    joined = " ".join(all_texts).lower()
    leadership_terms = any(x in joined for x in ['led a team', 'managed', 'team lead', 'headed'])
    solo_terms = any(x in joined for x in ['work alone', 'individual contributor', 'never been comfortable with people'])
    if leadership_terms and solo_terms:
        return 'fabricated'
    elif leadership_terms:
        return 'true'
    else:
        return 'none'

def detect_team_experience(all_texts: list) -> str:
    """
    Decide if 'individual contributor' or 'team player'.
    """
    joined = " ".join(all_texts).lower()
    if 'work alone' in joined or 'individual' in joined:
        return 'individual contributor'
    elif 'team' in joined:
        return 'team player'
    return ''

def extract_other_skills(text: str) -> list:
    """
    Any extra tech keywords: 'machine learning', 'ai', etc.
    Extend list if needed.
    """
    keywords = ['machine learning', 'ai', 'deep learning', 'data science', 'nlp']
    found = []
    for kw in keywords:
        if kw in text.lower():
            found.append(kw)
    return found

# --- Main analysis function ---

def analyze_transcript(sessions: dict) -> dict:
    """
    Main function.
    Input: sessions dict {'session_1': 'text', ...}
    Output: JSON dict according to schema
    """
    all_texts = list(sessions.values())

    # 1. Years of experience
    years_list = []
    for txt in all_texts:
        years_list.extend(extract_years(txt))

    # choose the most common or lowest as truth
    truth_years = ''
    if years_list:
        # pick the smallest number as truth
        numbers = [int(y.split()[0]) for y in years_list]
        min_years = min(numbers)
        max_years = max(numbers)
        truth_years = f"{min_years}-{max_years} years" if min_years != max_years else f"{min_years} years"

    # 2. Programming languages
    langs = []
    for txt in all_texts:
        langs.extend(extract_languages(txt))
    primary_lang = langs[0] if langs else 'unknown'

    # 3. Skill mastery
    # pick first found non-empty
    skill_level = ''
    for txt in all_texts:
        level = extract_skill_level(txt)
        if level:
            skill_level = level
            break

    # 4. Leadership claims
    leadership_status = detect_leadership(all_texts)

    # 5. Team experience
    team_experience = detect_team_experience(all_texts)

    # 6. Other skills/keywords
    other_skills = []
    for txt in all_texts:
        other_skills.extend(extract_other_skills(txt))

    # 7. Deception patterns (contradictions)
    deception_patterns = []
    if len(set(years_list)) > 1:
        deception_patterns.append({
            "lie_type": "experience_inflation",
            "contradictory_claims": list(set(years_list))
        })

    # 8. Build final JSON object
    result = TruthWeaverResult(
        shadow_id="phoenix_2024",
        revealed_truth={
            "programming_experience": truth_years,
            "programming_language": primary_lang,
            "skill_mastery": skill_level,
            "leadership_claims": leadership_status,
            "team_experience": team_experience,
            "skills and other keywords": list(set(other_skills))
        },
        deception_patterns=deception_patterns
    )

    return result.to_dict()

