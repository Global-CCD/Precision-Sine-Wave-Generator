#!/usr/bin/env python3
"""
High-Precision Frequency Sound File Generator
Generates audio files from a list of frequencies with exact decimal precision
Supports: WAV, FLAC, OPUS, MP3
"""

import numpy as np
from scipy.io import wavfile
import subprocess
import os
from decimal import Decimal, getcontext

# Set high precision for Decimal operations
getcontext().prec = 50


class PrecisionToneGenerator:
    def __init__(self, sample_rate=48000, duration=5.0, amplitude=0.5):
        """
        Initialize the tone generator
        
        Args:
            sample_rate: Sample rate in Hz (default 48000)
            duration: Duration of each tone in seconds (default 5.0)
            amplitude: Amplitude of the wave (0.0 to 1.0, default 0.5)
        """
        self.sample_rate = sample_rate
        self.duration = duration
        self.amplitude = amplitude
        
    def generate_tone(self, frequency_str):
        """
        Generate a pure sine wave tone with exact frequency precision
        
        Args:
            frequency_str: Frequency as string to maintain precision (e.g., "432.123456789012")
            
        Returns:
            numpy array of audio samples
        """
        # Use Decimal for precise frequency representation
        freq_decimal = Decimal(frequency_str)
        
        # Generate time array
        num_samples = int(self.sample_rate * self.duration)
        t = np.arange(num_samples, dtype=np.float64) / self.sample_rate
        
        # Convert frequency to float for numpy operations
        # numpy will use full float64 precision
        freq_float = float(freq_decimal)
        
        # Generate sine wave: amplitude * sin(2 * pi * frequency * time)
        audio = self.amplitude * np.sin(2.0 * np.pi * freq_float * t)
        
        # Convert to 16-bit PCM
        audio_int16 = np.int16(audio * 32767)
        
        return audio_int16
    
    def save_wav(self, audio, filename):
        """Save audio as WAV file"""
        wavfile.write(filename, self.sample_rate, audio)
        print(f"✓ Created: {filename}")
    
    def convert_to_flac(self, wav_file, flac_file):
        """Convert WAV to FLAC using ffmpeg"""
        try:
            subprocess.run([
                'ffmpeg', '-i', wav_file, '-y',
                '-compression_level', '8',
                flac_file
            ], check=True, capture_output=True)
            print(f"✓ Created: {flac_file}")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"✗ FLAC conversion failed: {e}")
            return False
    
    def convert_to_opus(self, wav_file, opus_file):
        """Convert WAV to OPUS using ffmpeg"""
        try:
            subprocess.run([
                'ffmpeg', '-i', wav_file, '-y',
                '-c:a', 'libopus', '-b:a', '128k',
                opus_file
            ], check=True, capture_output=True)
            print(f"✓ Created: {opus_file}")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"✗ OPUS conversion failed: {e}")
            return False
    
    def convert_to_mp3(self, wav_file, mp3_file):
        """Convert WAV to MP3 using ffmpeg"""
        try:
            subprocess.run([
                'ffmpeg', '-i', wav_file, '-y',
                '-codec:a', 'libmp3lame', '-b:a', '320k',
                mp3_file
            ], check=True, capture_output=True)
            print(f"✓ Created: {mp3_file}")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"✗ MP3 conversion failed: {e}")
            return False
    
    def generate_files(self, frequencies, formats=['wav', 'flac', 'opus', 'mp3'], 
                      output_dir='audio_output', keep_wav=True):
        """
        Generate audio files for a list of frequencies
        
        Args:
            frequencies: List of frequency strings with exact precision
            formats: List of desired formats (default: all)
            output_dir: Output directory (default: 'audio_output')
            keep_wav: Keep intermediate WAV files (default: True)
        """
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"\n{'='*60}")
        print(f"High-Precision Frequency Sound Generator")
        print(f"{'='*60}")
        print(f"Sample Rate: {self.sample_rate} Hz")
        print(f"Duration: {self.duration} seconds")
        print(f"Output Directory: {output_dir}")
        print(f"{'='*60}\n")
        
        for freq_str in frequencies:
            print(f"\nProcessing frequency: {freq_str} Hz")
            print("-" * 40)
            
            # Sanitize filename (replace . with underscore for cleaner names)
            safe_freq = freq_str.replace('.', '_')
            base_path = os.path.join(output_dir, f"{freq_str}Hz")
            wav_path = f"{base_path}.flac"
            
            # Generate audio
            audio = self.generate_tone(freq_str)
            
            # Save WAV
            if 'flac' in formats:
                self.save_wav(audio, wav_path)
            else:
                # Create temporary WAV for conversion
                self.save_wav(audio, wav_path)
            
            # Convert to other formats
            if 'flac' in formats:
                self.convert_to_flac(wav_path, f"{base_path}.flac")
            
            if 'opus' in formats:
                self.convert_to_opus(wav_path, f"{base_path}.opus")
            
            if 'mp3' in formats:
                self.convert_to_mp3(wav_path, f"{base_path}.mp3")
            
            # Remove temporary WAV if not needed
            if 'wav' not in formats and not keep_wav:
                os.remove(wav_path)
                print(f"✓ Removed temporary: {wav_path}")
        
        print(f"\n{'='*60}")
        print(f"Generation complete! Files saved to: {output_dir}")
        print(f"{'='*60}\n")


def main():
    # Example: List of frequencies with high precision
    frequencies = [
    '12500.00000000000000000000000000000000000000000000000001',
    '12500.00000000000000000000000000000000000000000000000002',
    '14500.00000000000000000000000000000000000000000000000001',
    '14500.00000000000000000000000000000000000000000000000002',
    '17500.00000000000000000000000000000000000000000000000001',
    '17500.00000000000000000000000000000000000000000000000002',
    '15000.00000000000000000000000000000000000000000000000001',
    '15000.00000000000000000000000000000000000000000000000002',
    '13000.00000000000000000000000000000000000000000000000001',
    '13000.00000000000000000000000000000000000000000000000002',
    '14500.00000000000000000000000000000000000000000000000001',
    '14500.00000000000000000000000000000000000000000000000002',
    '16000.00000000000000000000000000000000000000000000000001',
    '16000.00000000000000000000000000000000000000000000000002'
]
    
    # Initialize generator
    generator = PrecisionToneGenerator(
        sample_rate=48000,  # High quality sample rate
        duration=60.0,       # 5 seconds per tone
        amplitude=0.5       # 50% amplitude to prevent clipping
    )
    
    # Generate files in all formats
    generator.generate_files(
        frequencies=frequencies,
        formats=['flac'],
       # formats=['wav', 'flac', 'opus', 'mp3'],
        output_dir='audio_output',
        keep_wav=True  # Keep WAV files alongside converted formats
    )


if __name__ == "__main__":
    # Check for ffmpeg (required for FLAC, OPUS, MP3)
    try:
        subprocess.run(['ffmpeg', '-version'], 
                      capture_output=True, check=True)
    except FileNotFoundError:
        print("Warning: ffmpeg not found. Install it to enable FLAC/OPUS/MP3 conversion.")
        print("WAV files will still be generated.\n")
    
    main()
