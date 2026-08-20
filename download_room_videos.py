import os
import gdown

videos = {
    "ashoka": "1bWC42dNJDA1CpmTqe0_XD7JHkLtFp1we",
    "bael": "1HZ34lUyuRJK0cjgeuGzEU9t4m7B3A6a2",
    "bilva": "1ThNXRqI6vD0XgXXXOfBRaerPBjAjCK9m",
    "bodhi-tree": "1u9paPkepfLpJ-qyCEPuIgR6Qw4oLsUpI",
    "chandana": "1O5a2KPonoCXZOrX5Iub176wOwJkO5vFD",
    "datura": "1yr4afRB4pF9QA1Ey1dwyoslmHiVGvKk3",
    "mallige": "1aM4FHpngZ3CsYyttwiwS9Uzcfpd9GDIV",
    "parijata": "1kTvR94tfLu1E9fiVMZBslY7Phl2sYU-N",
    "spatika": "1olpd7A4jysHGB7BG6pz_S_P5MSDE_xQI",
    "tulsi": "17Gl7alMM0tT5XPGwBg2bGvLnb4tfqfup"
}

out_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\images\uploads"

for room, file_id in videos.items():
    out_path = os.path.join(out_dir, f"{room}_vid.mp4")
    if not os.path.exists(out_path):
        print(f"Downloading {room}...")
        gdown.download(id=file_id, output=out_path, quiet=True)
    else:
        print(f"Already exists: {out_path}")
print("Done downloading room videos.")
