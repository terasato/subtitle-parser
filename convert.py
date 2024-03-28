import webvtt
from io import StringIO

async def convert_vtt(content:str):
	buffer = StringIO(content)

	return {"caption":webvtt.read_buffer(buffer)}
