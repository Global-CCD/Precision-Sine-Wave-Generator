# High-Precision Frequency Sound Generator

A Python tool for generating audio files from exact frequency values with support for high decimal precision (10, 12, 15+ decimal places). Perfect for scientific audio experiments, sound healing, binaural beats, and precise frequency testing.

## Features

- 🎯 **High Precision**: Maintains exact decimal precision (10, 12, 15, 20+ decimal places)
- 🎵 **Pure Sine Waves**: Generates clean sine wave tones at exact frequencies
- 📁 **Multiple Formats**: Supports WAV, FLAC, OPUS, and MP3
- 📝 **Smart Naming**: Filenames include the exact frequency (e.g., `432.123456789012Hz.wav`)
- 🔢 **No Rounding**: Uses `Decimal` class and `float64` to prevent premature rounding
- ⚙️ **Configurable**: Easily adjust sample rate, duration, amplitude, and output formats

## Requirements

### Python Dependencies

```bash
pip install numpy scipy
```

### FFmpeg (Optional but Recommended)

FFmpeg is required for FLAC, OPUS, and MP3 conversion. WAV files will still work without it.

**Installation:**

- **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
- **macOS**: `brew install ffmpeg`
- **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/frequency-sound-generator.git
cd frequency-sound-generator
```

2. Install dependencies:
```bash
pip install numpy scipy
```

3. Install FFmpeg (see above)

## Quick Start

Run the script with default settings:

```bash
python frequency_generator.py
```

This will generate audio files in the `audio_output` directory with example frequencies.

## Usage & Configuration

### 1. Changing the Frequency List

Edit the `frequencies` list in the `main()` function (around line 155):

```python
frequencies = [
    "432.0",                    # Standard precision
    "432.1234567890",           # 10 decimal places
    "440.123456789012",         # 12 decimal places
    "528.123456789012345",      # 15 decimal places
    "639.12345678901234567890", # 20 decimal places
]
```

**Important**: 
- Always use **strings** (with quotes) to maintain precision
- Use as many decimal places as needed
- Example: `"440.123456789012"` ✓ vs `440.12` ✗

### 2. Audio Settings

Modify the `PrecisionToneGenerator` parameters (around line 161):

```python
generator = PrecisionToneGenerator(
    sample_rate=48000,  # Sample rate in Hz
    duration=5.0,       # Duration in seconds
    amplitude=0.5       # Volume (0.0 to 1.0)
)
```

**Parameters:**
- `sample_rate`: Audio quality (44100, 48000, 96000, etc.)
  - Higher = better quality but larger files
  - Recommended: 48000 Hz
- `duration`: Length of each tone in seconds
  - Default: 5.0 seconds
- `amplitude`: Volume level (0.0 = silent, 1.0 = maximum)
  - Recommended: 0.5 to prevent clipping
  - Adjust lower if you hear distortion

### 3. Output Formats

Choose which formats to generate (around line 168):

```python
generator.generate_files(
    frequencies=frequencies,
    formats=['wav', 'flac', 'opus', 'mp3'],  # Choose formats
    output_dir='audio_output',               # Output directory
    keep_wav=True                            # Keep WAV files
)
```

**Format Options:**
- `formats`: List of desired formats
  - Available: `'wav'`, `'flac'`, `'opus'`, `'mp3'`
  - Examples:
    - WAV only: `formats=['wav']`
    - WAV + MP3: `formats=['wav', 'mp3']`
    - All formats: `formats=['wav', 'flac', 'opus', 'mp3']`

- `output_dir`: Where to save files
  - Default: `'audio_output'`
  - Change to any directory: `'my_tones'`, `'output/frequencies'`, etc.

- `keep_wav`: Whether to keep WAV files when converting
  - `True`: Keep WAV files alongside converted formats
  - `False`: Delete temporary WAV files after conversion

### 4. Programmatic Usage

You can also use it as a library in your own scripts:

```python
from frequency_generator import PrecisionToneGenerator

# Initialize generator
gen = PrecisionToneGenerator(sample_rate=48000, duration=3.0, amplitude=0.5)

# Generate for specific frequencies
my_frequencies = [
    "432.1234567890",
    "528.123456789012"
]

gen.generate_files(
    frequencies=my_frequencies,
    formats=['wav', 'mp3'],
    output_dir='custom_output'
)
```

## Examples

### Example 1: Solfeggio Frequencies (High Precision)

```python
frequencies = [
    "174.123456789012",
    "285.234567890123",
    "396.345678901234",
    "417.456789012345",
    "528.567890123456",
    "639.678901234567",
    "741.789012345678",
    "852.890123456789",
    "963.901234567890"
]
```

### Example 2: Scientific Test Tones

```python
frequencies = [
    "1000.0",                   # 1 kHz reference
    "1000.1",                   # Slight deviation
    "1000.123456789012345"      # High precision test
]
```

### Example 3: Custom A4 Tunings

```python
frequencies = [
    "440.0",                    # Standard A4
    "432.0",                    # Alternative A4
    "432.081881730",            # Scientific pitch (C = 256 Hz)
    "444.0"                     # Higher pitch A4
]
```

### Example 4: Binaural Beat Pairs

```python
# Left ear: 200 Hz, Right ear: 210 Hz (10 Hz beat)
frequencies = [
    "200.0",
    "210.0"
]
```

## Output

The script generates files with the following naming convention:

```
audio_output/
├── 432.0Hz.wav
├── 432.0Hz.flac
├── 432.0Hz.opus
├── 432.0Hz.mp3
├── 432.1234567890Hz.wav
├── 432.1234567890Hz.flac
└── ...
```

## Technical Details

### Precision Handling

- **Input**: Frequencies are stored as strings to prevent automatic rounding
- **Processing**: Python's `Decimal` class maintains exact decimal representation
- **Generation**: NumPy's `float64` provides high precision for audio synthesis
- **Result**: No loss of precision throughout the entire pipeline

### Audio Quality

- **Bit Depth**: 16-bit PCM for WAV files
- **Format Quality**:
  - WAV: Lossless, uncompressed
  - FLAC: Lossless, compressed (compression level 8)
  - OPUS: 128 kbps (adjustable)
  - MP3: 320 kbps (adjustable)

## Troubleshooting

### "ffmpeg not found" Warning

**Issue**: FLAC, OPUS, and MP3 conversion will fail without ffmpeg.

**Solution**: Install ffmpeg (see Requirements section). WAV files will still generate correctly.

### Audio Clipping/Distortion

**Issue**: Audio sounds distorted or clipped.

**Solution**: Reduce the `amplitude` parameter (try 0.3 or 0.2 instead of 0.5).

### File Permission Errors

**Issue**: Cannot write to output directory.

**Solution**: Ensure you have write permissions, or change `output_dir` to a writable location.

### Memory Issues with Long Durations

**Issue**: Script crashes with very long durations (e.g., 1 hour).

**Solution**: Reduce `duration` or generate files in batches.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this for any purpose.

## Acknowledgments

Built with:
- NumPy & SciPy for audio generation
- FFmpeg for format conversion
- Python's Decimal module for precision arithmetic

## Support

For issues, questions, or feature requests, please open an issue on GitHub.

---

**Made with precision** 🎵
