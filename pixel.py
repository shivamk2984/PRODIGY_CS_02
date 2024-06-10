from PIL import Image
import numpy as np

def load_image(image_path):
    """Load an image from a file path."""
    try:
        image = Image.open(image_path)
        print(f"Image {image_path} loaded successfully.")
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def save_image(image, output_path):
    """Save an image to a file path."""
    try:
        image.save(output_path)
        print(f"Image saved to {output_path}.")
    except Exception as e:
        print(f"Error saving image: {e}")

def process_pixels(pixels, key, encrypt=True):
    """Encrypt or decrypt pixel values with XOR and swapping."""
    height, width, channels = pixels.shape
    processed_pixels = pixels.copy()

    # Apply XOR operation with the key
    processed_pixels ^= key
    
    # Swap pixel values in a predefined pattern
    for i in range(height):
        for j in range(0, width - 1, 2):
            processed_pixels[i, j], processed_pixels[i, j + 1] = processed_pixels[i, j + 1], processed_pixels[i, j]
    
    return processed_pixels

def encrypt_image(image_path, key, output_path):
    """Encrypt the image by manipulating pixel values."""
    image = load_image(image_path)
    if image is None:
        return

    pixels = np.array(image)
    encrypted_pixels = process_pixels(pixels, key, encrypt=True)

    encrypted_image = Image.fromarray(encrypted_pixels, mode=image.mode)
    save_image(encrypted_image, output_path)

def decrypt_image(image_path, key, output_path):
    """Decrypt the image by reversing pixel manipulation."""
    image = load_image(image_path)
    if image is None:
        return

    pixels = np.array(image)
    decrypted_pixels = process_pixels(pixels, key, encrypt=False)

    decrypted_image = Image.fromarray(decrypted_pixels, mode=image.mode)
    save_image(decrypted_image, output_path)

# Example usage
key = 123  # Simple integer key for XOR operation
input_image_path = r'image-path'
encrypted_image_path = r'encrypted-image-path'
decrypted_image_path = r'decrypted-image-path'

# Encrypt the image
encrypt_image(input_image_path, key, encrypted_image_path)

# Decrypt the image
decrypt_image(encrypted_image_path, key, decrypted_image_path)
