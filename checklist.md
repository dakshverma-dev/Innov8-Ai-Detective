| **Section**             | **Field**                   | **What You Must Detect in Transcript**                                          | **Example Output**           |
| ----------------------- | --------------------------- | ------------------------------------------------------------------------------- | ---------------------------- |
| **Top Level**           | `shadow_id`                 | A fixed ID you assign to the candidate (given in the problem or you choose).    | `"phoenix_2024"`             |
| **revealed\_truth**     | `programming_experience`    | Number of years mentioned (handle contradictory claims, pick the truth).        | `"3-4 years"`                |
|                         | `programming_language`      | Primary programming language claimed.                                           | `"python"`                   |
|                         | `skill_mastery`             | Level of skill (beginner / intermediate / advanced).                            | `"intermediate"`             |
|                         | `leadership_claims`         | Did they claim leadership? If later they deny → `"fabricated"`, else `"true"`.  | `"fabricated"`               |
|                         | `team_experience`           | Solo contributor or worked in team?                                             | `"individual contributor"`   |
|                         | `skills and other keywords` | Other skills/keywords like “Machine Learning”, “AI”, etc.                       | `["Machine Learning", "AI"]` |
| **deception\_patterns** | `lie_type`                  | The category of lie: e.g. `"experience_inflation"`, `"leadership_fabrication"`. | `"experience_inflation"`     |
|                         | `contradictory_claims`      | List of contradictory statements found.                                         | `["6 years", "3 years"]`     |
