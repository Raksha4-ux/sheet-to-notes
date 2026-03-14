import xml.etree.ElementTree as ET

tree = ET.parse("Image.musicxml")
root = tree.getroot()

notes = []

for note in root.iter("note"):
    # Skip rests
    rest = note.find("rest")
    if rest is not None:
        continue

    # Only take staff 1 (treble/melody)
    staff = note.find("staff")
    if staff is not None and staff.text != "1":
        continue

    pitch = note.find("pitch")
    if pitch is not None:
        step = pitch.find("step").text
        notes.append(step)

print("Melody notes only:")
print(" ".join(notes))
