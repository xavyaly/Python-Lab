#!/usr/bin/env python3.11

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Parameters
image_size = 64  # Size of the image (64x64 pixels)
num_steps = 500  # Number of diffusion steps
sigma_initial = 25.0  # Initial noise level (standard deviation)

# Start with pure noise
image = np.random.randn(image_size, image_size)

# Simulated diffusion model
def diffusion_step(image, step, num_steps):
    # Gradually reduce noise by applying a Gaussian filter with decreasing sigma
    sigma = sigma_initial * (1 - step / num_steps)
    image = gaussian_filter(image, sigma=sigma)
    return image

# Iteratively refine the image
for step in range(num_steps):
    image = diffusion_step(image, step, num_steps)

# Normalize the image to [0, 1] for display
image = (image - image.min()) / (image.max() - image.min())

# Display the final image
plt.imshow(image, cmap='gray')
plt.title('Generated Image')
plt.axis('off')
plt.show()
