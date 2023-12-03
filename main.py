import sys

import requests


def ask(q: str):
    r = requests.post("https://www.llama2.ai/api", headers={
        "Origin": "https://www.llama2.ai",
        "Referer": "https://www.llama2.ai/",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
            "like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0 (Edition GX-CN)"
        )
    }, json={
        "audio": None,
        "image": None,
        "maxTokens": 800,
        "prompt": "[INST] {} [/INST]\n".format(q),
        "systemPrompt": "You are a helpful assistant.",
        "temperature": 0.75,
        "topP": 0.9,
        "version": "02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3"
    }, stream=True)
    
    for chunk in r.iter_content():
        print(chunk.decode('utf-8'), end="", flush=True)

    print()

if __name__ == '__main__':
    ask(" ".join(sys.argv[1:]))
