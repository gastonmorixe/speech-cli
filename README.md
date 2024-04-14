# speech-cli
Speech cli for all online, offline, AI, non-AI, free and paid  TTS models & Ranking

## Ranking 

- #1 OpenAI (it's the only one we have here far)

## Models

- OpenAI [Text to speech with Streaming and Playback](https://platform.openai.com/docs/guides/text-to-speech): `openai-tts-streaming-v1.py`
- [ ] ElevenLabs
- [ ] Native Apple's macOS TTS

## Instructions
We want to make this versatile so we always accept STDIN. 
For example we can get text from clipboard and pipe it to speech-cli. 
As of today we only have OpenAI's it would work like this:

```bash
$ pbpaste | python openai-tts-streaming-v1.py
```

## Authors
Gaston Morixe

## License
MIT
