"""
Generate and download PlantUML PNGs for wireframes.
Uses the PlantUML online server for rendering.
"""
import os
import requests
import zlib
import base64

OUTPUT_DIR = r"c:\Users\DELL\OneDrive\Desktop\Sophia.1web dev\webdev\bloom-valley-nursery\final_screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PLANTUML_SERVER = "http://www.plantuml.com/plantuml/png/"

def encode_puml(puml_text):
    """
    Standard PlantUML encoding:
    1. Encode in UTF-8
    2. Compress using Deflate algorithm
    3. Re-encode in custom Base64
    """
    zlibbed_str = zlib.compress(puml_text.encode('utf-8'))
    # Skip first 2 bytes (header) and last 4 bytes (checksum) to get raw deflate data
    compressed_str = zlibbed_str[2:-4]
    
    # Custom base64 mapping for PlantUML
    mapper = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    
    def encode_3bytes(b1, b2, b3):
        res = ""
        res += mapper[b1 >> 2]
        res += mapper[((b1 & 0x3) << 4) | (b2 >> 4)]
        res += mapper[((b2 & 0xF) << 2) | (b3 >> 6)]
        res += mapper[b3 & 0x3F]
        return res

    def encode_data(data):
        res = ""
        length = len(data)
        for i in range(0, length, 3):
            if i + 2 < length:
                res += encode_3bytes(data[i], data[i+1], data[i+2])
            elif i + 1 < length:
                res += encode_3bytes(data[i], data[i+1], 0)
                res = res[:-1] # Remove last padding logic
            else:
                res += encode_3bytes(data[i], 0, 0)
                res = res[:-2]
        return res

    return "~1" + encode_data(compressed_str)

DIAGRAMS = {
    "wireframe_desktop": """
@startuml
skinparam handwritten true
skinparam backgroundcolor #F5F0E8
title "Bloom Valley Nursery - Desktop Wireframe"
package "Header" {
  [Logo] - [Home]
  [Home] - [Gallery]
  [Gallery] - [About Us]
  [About Us] - [Community]
}
node "Hero Section" {
  [Tagline: Welcome to Bloom Valley]
  [CTA Button: Explore]
}
node "Main Content" {
  frame "Featured Products" {
    [Product 1] | [Product 2]
  }
  frame "Perks" {
    [Advice] | [Quality] | [Local] | [Custom]
  }
}
footer "Main Footer" {
  [Newsletter Form]
  [Links]
}
@enduml
""",
    "wireframe_mobile": """
@startuml
skinparam handwritten true
skinparam backgroundcolor #F5F0E8
title "Bloom Valley Nursery - Mobile Wireframe"
package "Header" {
  [Logo]
  [Menu Button]
}
node "Hero" {
  [Welcome Tagline]
  [CTA Button]
}
node "Content" {
  [Featured Product 1]
  [Featured Product 2]
  ---
  [Perk 1]
  [Perk 2]
  [Perk 3]
  [Perk 4]
}
@enduml
"""
}

def main():
    for name, puml in DIAGRAMS.items():
        encoded = encode_puml(puml)
        url = PLANTUML_SERVER + encoded
        print(f"Downloading {name} from {url}...")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(os.path.join(OUTPUT_DIR, f"{name}.png"), 'wb') as f:
                    f.write(response.content)
                print(f"Success: {name}.png")
            else:
                print(f"Failed to download {name}: {response.status_code}")
        except Exception as e:
            print(f"Error {name}: {e}")

if __name__ == "__main__":
    main()
