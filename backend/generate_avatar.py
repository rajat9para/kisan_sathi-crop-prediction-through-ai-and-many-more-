"""
Generates a high-resolution, modern AI Agri-Tech Avatar Badge
for Kisaan_Sathi GitHub profile and application assets.
"""

import os
from PIL import Image, ImageDraw, ImageFont

def generate_avatar(output_path: str, size: int = 512):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. Circular Mask & Gradient Background
    center = size // 2
    radius = size // 2 - 16

    # Draw outer glow ring
    for i in range(12, 0, -1):
        glow_alpha = int(18 * (1 - i / 12))
        draw.ellipse(
            [center - radius - i, center - radius - i, center + radius + i, center + radius + i],
            fill=(46, 125, 50, glow_alpha)
        )

    # Draw vibrant green gradient circles
    for r in range(radius, 0, -1):
        ratio = r / radius
        r_col = int(19 + (46 - 19) * (1 - ratio))
        g_col = int(117 + (147 - 117) * (1 - ratio))
        b_col = int(71 + (60 - 71) * (1 - ratio))
        draw.ellipse([center - r, center - r, center + r, center + r], fill=(r_col, g_col, b_col, 255))

    # 2. Golden Accent Ring (Wheat Gold)
    draw.ellipse(
        [center - radius, center - radius, center + radius, center + radius],
        outline=(216, 151, 60, 255),
        width=8
    )

    # 3. Stylized Farmer Head & Saffron Turban (Pagri)
    # Face (Warm Indian skin tone)
    face_y = int(size * 0.42)
    face_w = int(size * 0.30)
    face_h = int(size * 0.36)
    draw.ellipse(
        [center - face_w // 2, face_y - face_h // 2, center + face_w // 2, face_y + face_h // 2],
        fill=(226, 162, 114, 255)
    )

    # Saffron Turban (Pagri)
    turban_y = int(size * 0.28)
    turban_w = int(size * 0.44)
    turban_h = int(size * 0.26)
    draw.ellipse(
        [center - turban_w // 2, turban_y - turban_h // 2, center + turban_w // 2, turban_y + turban_h // 2],
        fill=(245, 127, 23, 255) # Saffron
    )
    # Turban fold layers
    draw.arc(
        [center - turban_w // 2 + 10, turban_y - turban_h // 2 + 8, center + turban_w // 2 - 10, turban_y + turban_h // 2],
        start=180, end=360, fill=(230, 81, 0, 255), width=6
    )
    draw.arc(
        [center - turban_w // 2 + 20, turban_y - turban_h // 2 + 20, center + turban_w // 2 - 20, turban_y + turban_h // 2 + 10],
        start=180, end=360, fill=(255, 179, 0, 255), width=5
    )

    # Eyes
    eye_y = int(size * 0.42)
    draw.ellipse([center - 32, eye_y - 6, center - 18, eye_y + 6], fill=(40, 25, 15, 255))
    draw.ellipse([center + 18, eye_y - 6, center + 32, eye_y + 6], fill=(40, 25, 15, 255))
    # Eye highlights
    draw.ellipse([center - 28, eye_y - 4, center - 22, eye_y + 2], fill=(255, 255, 255, 255))
    draw.ellipse([center + 22, eye_y - 4, center + 28, eye_y + 2], fill=(255, 255, 255, 255))

    # Moustache & Smile
    moust_y = int(size * 0.48)
    draw.arc([center - 40, moust_y - 8, center, moust_y + 16], start=0, end=180, fill=(45, 30, 20, 255), width=7)
    draw.arc([center, moust_y - 8, center + 40, moust_y + 16], start=0, end=180, fill=(45, 30, 20, 255), width=7)
    # Warm smile
    draw.arc([center - 20, moust_y + 4, center + 20, moust_y + 22], start=10, end=170, fill=(255, 255, 255, 255), width=5)

    # 4. Kurta Body & Jacket
    body_y = int(size * 0.62)
    draw.chord(
        [center - int(size * 0.42), body_y, center + int(size * 0.42), size - 16],
        start=0, end=180, fill=(255, 255, 255, 255)
    )
    # Nehru Jacket (Green Tech)
    draw.polygon([
        (center - 110, size - 20), (center - 70, body_y + 20),
        (center - 25, body_y + 35), (center - 35, size - 20)
    ], fill=(19, 117, 71, 255))
    draw.polygon([
        (center + 110, size - 20), (center + 70, body_y + 20),
        (center + 25, body_y + 35), (center + 35, size - 20)
    ], fill=(19, 117, 71, 255))

    # 5. AI Holographic Leaf / Tech Badge in Center
    badge_y = int(size * 0.78)
    draw.ellipse(
        [center - 54, badge_y - 40, center + 54, badge_y + 68],
        fill=(11, 70, 40, 240), outline=(244, 197, 66, 255), width=4
    )
    # Glowing Leaf Icon inside badge
    leaf_pts = [
        (center, badge_y - 28),
        (center + 32, badge_y + 6),
        (center, badge_y + 44),
        (center - 32, badge_y + 6)
    ]
    draw.polygon(leaf_pts, fill=(46, 204, 113, 255))
    # Leaf central vein
    draw.line([(center, badge_y - 20), (center, badge_y + 36)], fill=(255, 255, 255, 255), width=3)
    draw.line([(center, badge_y - 5), (center + 16, badge_y - 15)], fill=(255, 255, 255, 255), width=2)
    draw.line([(center, badge_y + 10), (center - 16, badge_y)], fill=(255, 255, 255, 255), width=2)

    img.save(output_path, "PNG")
    print(f"[+] Successfully generated Kisaan_Sathi Avatar at {output_path}")

if __name__ == "__main__":
    generate_avatar("docs/assets/kisaan_sathi_avatar.png", size=512)
    generate_avatar("agrisaathi_app/assets/kisaan_sathi_avatar.png", size=512)
