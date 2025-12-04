# 🎵 Precision Sine Wave Generator

This project generates **high-precision sine-wave audio files** (WAV format) using Python.
It supports **arbitrary frequencies**, including frequencies with **8–10+ decimal places**, and produces clean, continuous tones of any duration.

---

## 🚀 Features

* Generates one or multiple sine-wave tones.
* Supports extremely high-precision frequencies (beyond 10 decimal places).
* Produces 16-bit PCM WAV audio.
* Adjustable:

  * Frequency (Hz)
  * Duration (seconds)
  * Sample rate (Hz)
  * Amplitude
  * Output filename format
* Easy to extend or integrate into audio generation pipelines.

---

## 📦 Requirements

Python 3.9+

Install dependencies:

```bash
pip install numpy
```

*(The built-in `wave` module is used for WAV writing — no install required.)*

---

## 📁 Project Structure

```
/
├─ generate_sine.py
└─ README.md
```

---

## ▶️ Usage

Run the generator:

```bash
python generate_sine.py
```

The script will create WAV files in the same directory (or in `/output` if configured).

---

## 🛠 Editing User Inputs / Variables

You can modify user-configurable settings inside **generate_sine.py**.

Below is a standard variable section you will find at the top of the script:

```python
sample_rate = 44100        # Samples per second
duration = 60              # Length of each tone (seconds)
amplitude = 0.5            # Output volume (0.0 – 1.0)

frequencies = [
    250.0000000001,
    250.0000000002,
    450.0000000001,
    450.0000000002,
    # Add or remove frequencies as needed
]
```

### 🔧 Changing the Duration

```python
duration = 30   # makes each file 30 seconds long
```

### 🔧 Changing the Sample Rate

Common values:

* `44100` — standard audio
* `48000` — video/audio standard
* `96000` — high-resolution
* `192000` — ultra-high resolution

Example:

```python
sample_rate = 96000
```

### 🔧 Adding / Removing Frequencies

Frequencies are simply values in a Python list:

```python
frequencies = [
    123.4567890123,
    789.0000000001,
    6000.1234567890,
]
```

Decimal precision is unlimited.

### 🔧 Changing Output Filenames

By default, filenames are generated with fixed decimal precision:

```python
filename = f"sine_{f:.10f}Hz.wav"
```

Increase decimal places:

```python
filename = f"sine_{f:.15f}Hz.wav"
```

Or remove formatting entirely:

```python
filename = f"sine_{f}Hz.wav"
```

---

## 📤 Output

Files are generated in WAV format:

* **16-bit PCM**
* **Mono (1 channel)**
* **Accurate sample-aligned waveforms**
* **No clicks / no artifacts**

Example output file:

```
sine_250.0000000001Hz.wav
```

---

## 🧩 Example: Generate a Single Tone

Modify the frequency list:

```python
frequencies = [ 440.0 ]  # Single A4 tone
```

Run:

```bash
python generate_sine.py
```

---

## 🧩 Example: Generate 100 Frequencies Automatically

```python
frequencies = [ 100 + i*0.00000001 for i in range(100) ]
```

---

## 📝 License

MIT License — free for personal, academic, and commercial use.

---

If you'd like, I can also:

✔ generate the actual `generate_sine.py` file
✔ create a `/output` directory structure
✔ add examples, badges, or setup scripts
✔ package this as a CLI tool (e.g., `sinegen 1000Hz`)

Just tell me!
