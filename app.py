from fastapi import FastAPI
from starlette.responses import FileResponse

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

app = FastAPI()

@app.get("/")
async def read_root():
    return FileResponse('template/index.html')

@app.get("/transcript/{video_id}")
async def transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['de', 'en'])
    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(transcript)
    return text_formatted