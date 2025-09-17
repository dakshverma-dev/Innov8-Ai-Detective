# transcribe.py
import whisper
import sys
from pathlib import Path

def transcribe_audio(input_file: str, output_file: str = None, model_name: str = "small"):
    """
    Transcribe an audio/video file into text using OpenAI Whisper.

    Args:
        input_file (str): Path to audio/video file (e.g. .mp4, .wav, .mp3).
        output_file (str, optional): Path to save transcript (.txt). Defaults to same name as input.
        model_name (str, optional): Whisper model size ("tiny", "base", "small", "medium", "large").
    """
    print(f"🔄 Loading Whisper model: {model_name} (this may take a minute)...")
    model = whisper.load_model(model_name)

    print(f"🎙️ Transcribing: {input_file}")
    result = model.transcribe(input_file)

    transcript = result["text"]

    # Default output file
    if not output_file:
        output_file = Path(input_file).with_suffix(".txt")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transcript.strip())

    print(f"✅ Transcription complete! Saved to {output_file}")
    return output_file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <input_file> [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    transcribe_audio(input_file, output_file)
