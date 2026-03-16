# 🎵 Sheet Music to Notes

Convert sheet music images into plain note letters for beginner pianists.

**No music theory required. Just upload and play.**

---

## What It Does

Most sheet music is unreadable if you never learned how to read it. This tool takes a sheet music image and converts it into plain letters — `C D E F G A B` — grouped by bar.

Upload an image. Get your notes. Sit at the keyboard and play.

---



## Tech Stack

- **Python** — backend logic
- **Flask** — web server
- **oemer** — open source Optical Music Recognition model
- **HTML / CSS / JS** — frontend UI

---

## How It Works

1. User uploads a sheet music PNG
2. [oemer](https://github.com/BreezeWhite/oemer) runs OMR on the image and produces a MusicXML file
3. The app parses the MusicXML, extracts only the treble clef (Staff 1)
4. Notes are grouped by measure and returned as plain letters
5. Frontend displays them in a clean UI with a piano keyboard highlighting active notes

---

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repo
git clone https://github.com/Raksha4-ux/sheet-to-notes.git
cd sheet-to-notes

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install flask oemer
```

### Run

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

---

## Usage

1. Take a screenshot of any sheet music (PNG format)
2. Upload it on the webpage
3. Click **Decode Notes**
4. Wait ~2 minutes (runs on CPU)
5. Notes appear grouped by bar

---

## Limitations

- Processing takes 1–2 minutes (no GPU)
- Works best on clean, printed sheet music
- Complex songs with many accidentals may have errors
- Currently supports PNG only

---

## Project Structure

```
sheet-to-notes/
├── app.py                  # Flask backend
├── parse.py                # Standalone note parser
├── templates/
│   └── index.html          # Frontend UI
└── README.md
```


