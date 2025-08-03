from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id: str) -> str:
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id)
        text = " ".join([snippet.text for snippet in transcript])
        return text
    except Exception as e:
        return f"Error: {str(e)}"
