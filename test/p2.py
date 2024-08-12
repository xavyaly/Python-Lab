#!/usr/bin/env python3.11

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Parameters
image_size = 128  # Size of the image (128x128 pixels)
num_steps = 500   # Number of diffusion steps
sigma_initial = 50.0  # Initial noise level (standard deviation)
sigma_final = 2.0  # Final noise level (standard deviation)

# Start with pure noise
image = np.random.randn(image_size, image_size)

# Generate a target pattern (a circle in the center of the image)
def create_circle(image_size, radius):
    y, x = np.ogrid[:image_size, :image_size]
    center = image_size // 2
    mask = (x - center) ** 2 + (y - center) ** 2 <= radius ** 2
    return mask.astype(float)

# The target pattern we want to achieve
target_image = create_circle(image_size, radius=image_size // 4)

# Simulated diffusion model
def diffusion_step(image, target_image, step, num_steps):
    # Compute interpolation factor
    alpha = step / num_steps
    # Blend the noisy image with the target pattern
    blended_image = (1 - alpha) * image + alpha * target_image
    # Apply a Gaussian filter with gradually decreasing sigma
    sigma = sigma_initial * (1 - step / num_steps) + sigma_final * (step / num_steps)
    smoothed_image = gaussian_filter(blended_image, sigma=sigma)
    return smoothed_image

# Iteratively refine the image
for step in range(num_steps):
    image = diffusion_step(image, target_image, step, num_steps)

# Normalize the image to [0, 1] for display
image = (image - image.min()) / (image.max() - image.min())

# Display the final image
plt.imshow(image, cmap='gray')
plt.title('Generated Image')
plt.axis('off')
plt.show()

