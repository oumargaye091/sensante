from pathlib import Path
import re, zlib
p = Path(r'C:\Users\Lenovo\Documents\sensante\Lab_IMA05_LLM_Groq.pdf')
data = p.read_bytes()
text = []
for m in re.finditer(rb'stream\r?\n', data):
    start = m.end()
    end = data.find(b'endstream', start)
    if end == -1:
        continue
    s = data[start:end].strip(b'\r\n')
    try:
        dec = zlib.decompress(s)
    except Exception:
        continue
    text.append(dec)
    if len(text) >= 10:
        break
print('STREAMS', len(text))
for i, dec in enumerate(text, 1):
    print('--- DECOMPRESSED', i, '---')
    print(dec[:1000])
    print('------')
    for w in [b'Lab_IMA05', b'Groq', b'GROQ', b'predict', b'explain', b'FastAPI', b'LLM', b'cors', b'uvicorn', b'API', b'Groq']:
        if w in dec:
            print('FOUND', w)
