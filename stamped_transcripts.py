import speech_recognition as sr

def transcribe_audio_with_timestamps(file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        duration = source.DURATION  

        text = recognizer.recognize_google(audio_data)

        return text, duration

def create_transcript_with_timestamps(transcript, duration, output_path):
    words = transcript.split()
    word_count = len(words)
    time_per_word = duration / word_count

    timestamps = []
    current_time = 0.0

    for word in words:
        start_time = current_time
        end_time = start_time + time_per_word
        timestamps.append((start_time, end_time, word))
        current_time = end_time

    # Add the path where you want to save the timestamped transcript
    with open(output_path, "w", encoding="utf-8") as file:
        for start_time, end_time, word in timestamps:
            file.write(f"{start_time:.2f} - {end_time:.2f}: {word}\n")

# Example usage:
input_file_path = "test_1.wav"  # Add your input WAV file path here
output_file_path = "timestamped_transcript.txt"  # Add your output file path here

transcript, duration = transcribe_audio_with_timestamps(input_file_path)
create_transcript_with_timestamps(transcript, duration, output_file_path)
