import xml.etree.ElementTree as ET

tree = ET.parse("Image.musicxml")
root = tree.getroot()

# Check how many parts exist
parts = root.findall(".//part")
print(f"Number of parts: {len(parts)}")

# Check staff numbers used
staffs = set()
for s in root.iter("staff"):
    staffs.add(s.text)
print(f"Staff numbers found: {staffs}")
