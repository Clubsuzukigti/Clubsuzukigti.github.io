"""Convierte las 7 siluetas Swift GTi a WebP optimizado (Regla 17).
Conserva PNG originales en assets-original-backup/siluetas/.

Output: WebP q92 lossless cuando hay transparencia, sino q88 lossy.
"""
from pathlib import Path
from PIL import Image
import shutil

SRC = Path(r"c:/Users/PcTec/Claude Code/suzuki owners/sitio-web/docs/assets/img/siluetas")
BACKUP = Path(r"c:/Users/PcTec/Claude Code/suzuki owners/assets-original-backup/siluetas")
BACKUP.mkdir(parents=True, exist_ok=True)

for png in sorted(SRC.glob("*.png")):
    img = Image.open(png)
    has_alpha = img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info)
    # backup
    bkp = BACKUP / png.name
    if not bkp.exists():
        shutil.copy2(png, bkp)
    # convert
    webp_path = png.with_suffix(".webp")
    if has_alpha:
        img.save(webp_path, "WEBP", quality=92, method=6, lossless=False)
    else:
        img.save(webp_path, "WEBP", quality=88, method=6)
    new_size = webp_path.stat().st_size
    old_size = png.stat().st_size
    pct = 100 * (1 - new_size / old_size)
    print(f"  {png.name:35s} {old_size:>8,}B -> {new_size:>8,}B  ({pct:5.1f}% smaller)")

print("Done.")
