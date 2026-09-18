import os
from pathlib import Path
import re

folder = Path("/Users/arielhertz/Desktop/Claw-like Tweezer/reproduction - gaussian, 10 minutes/10 minutes, gaussian - frames_video_6_reproduction")

# Regex para capturar o padrão YYYYMMDD-HHMMSS-fff
pattern = re.compile(r"(\d{8})-(\d{6})-(\d+)")

# Coleta e ordena pelos timestamps extraídos do nome
image_files = sorted(
    [f for f in folder.iterdir() if f.suffix.lower() in ['.jpg', '.jpeg', '.png']],
    key=lambda x: pattern.search(x.stem).groups() if pattern.search(x.stem) else ("99999999", "999999", "999999")
)

# Renomeia em ordem cronológica
for i, img in enumerate(image_files):
    new_name = folder / f"frame_{i:04d}{img.suffix.lower()}"
    print(f"{img.name} -> {new_name.name}")
    img.rename(new_name)

print("✅ Renomeado em ordem cronológica com sucesso.")