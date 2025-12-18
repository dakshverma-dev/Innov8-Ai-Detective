# Innov8-AI-Detective

Rule-based transcript intelligence for spotting contradictions in technical interviews. The toolkit pairs fast audio transcription (Whisper) with lightweight heuristics that surface a candidate's likely truth, contradictions, and exaggerations.

## What it does
- Transcribes audio or video to text via Whisper (see `transcribe.py`).
- Parses one or more transcript sessions and extracts declared skills, experience ranges, leadership claims, and team dynamics (see `analyze.py`).
- Emits a structured JSON object captured by `TruthWeaverResult` in `schema.py`.
- Includes a reference `sample.txt` transcript and a checklist table (`checklist.md`) describing expected fields.

## Prerequisites
- Python 3.10+ recommended.
- FFmpeg available on your PATH (required by Whisper).
- A CUDA-capable GPU speeds up transcription; CPU also works but is slower.

## Setup
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
### 1) Transcribe audio to text
```bash
python transcribe.py path\to\interview.mp3 output_transcript.txt --model_name small
```
Notes: `output_file` is optional; defaults to the input name with `.txt`. Model sizes include tiny, base, small, medium, large.

### 2) Analyze transcripts
Provide one or more session transcripts as a dictionary. Example with the provided sample:
```python
from analyze import analyze_transcript

with open("sample.txt", encoding="utf-8") as f:
		sessions = {"session_1": f.read()}

result = analyze_transcript(sessions)
print(result)
```
Example output structure:
```json
{
	"shadow_id": "phoenix_2024",
	"revealed_truth": {
		"programming_experience": "3-6 years",
		"programming_language": "unknown",
		"skill_mastery": "",
		"leadership_claims": "fabricated",
		"team_experience": "individual contributor",
		"skills and other keywords": []
	},
	"deception_patterns": [
		{
			"lie_type": "experience_inflation",
			"contradictory_claims": ["6 years", "3 years", "4 years"]
		}
	]
}
```

## Data model
- `shadow_id`: Identifier you assign to the candidate or scenario.
- `revealed_truth`: Extracted signals (experience, primary language, mastery level, leadership and team claims, other skills).
- `deception_patterns`: Categories of contradictions plus the conflicting statements that triggered them.

## Notes and next steps
- Extend the keyword lists in `analyze.py` to cover additional languages, domains, or deception categories.
- Add CI-ready tests around `analyze_transcript` before production use.
- Whisper downloads model weights on first run; cache them to avoid repeat downloads.
