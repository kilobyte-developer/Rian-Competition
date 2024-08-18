import os

def create_srt(subtitles, output_srt):
    with open(output_srt, 'w', encoding='utf-8') as f:
        for i, (start_time, end_time, text) in enumerate(subtitles):
            # Convert seconds to the format needed by SRT (hours:minutes:seconds,milliseconds)
            start_time_str = f"{int(start_time//3600):02}:{int((start_time%3600)//60):02}:{int(start_time%60):02},000"
            end_time_str = f"{int(end_time//3600):02}:{int((end_time%3600)//60):02}:{int(end_time%60):02},000"
            
            f.write(f"{i+1}\n")
            f.write(f"{start_time_str} --> {end_time_str}\n")
            f.write(f"{text}\n\n")

# Example usage for Spanish subtitles
spanish_subtitles = [
    (0, 5, "La IA tiene un muy ocupado aquí para hablar sobre"),
    (5, 10, "Vamos a comenzar a hacer que nuestros productos sean radicalmente más útiles"),
    (10, 15, "durante un tiempo que generativo estamos dando el siguiente paso usando una combinación de comprensión semántica"),
    # Add more subtitle lines with their corresponding start and end times in seconds
]

create_srt(spanish_subtitles, "spanish_subtitles.srt")

# Example usage for English subtitles
english_subtitles = [
    (0, 6, "AI having a very busy here to talk about"),
    (7, 12, "Let's get started to make our products radically more helpful for a while"),
    (12, 18, "which generative we are taking the next step using a combination of semantic understanding"),
    (18, 25, "and generally where you can do much more with a new experience call magic"),
    # Add more subtitle lines with their corresponding start and end times in seconds
]

create_srt(english_subtitles, "english_subtitles.srt")
