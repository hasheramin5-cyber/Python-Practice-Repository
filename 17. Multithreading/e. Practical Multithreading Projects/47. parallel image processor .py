# A Program to simulate parallel image processing

from concurrent.futures import ThreadPoolExecutor
import time


images = [
    "image_01.jpg",
    "image_02.jpg",
    "image_03.jpg",
    "image_04.jpg",
    "image_05.jpg"
]


def process_image(filename):
    print(f"Processing {filename}")

    time.sleep(0.8)

    return f"{filename} processed"


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [
        executor.submit(process_image, image)
        for image in images
    ]

    for future in futures:
        print(future.result())


print("Image processing completed.")


# Explanation:
# Each image is represented by a filename.
# process_image() simulates an image-processing operation using sleep().
# Every image is submitted as an independent Future.
# The thread pool can process several images concurrently.
# The main thread retrieves each completed result using future.result().
# This example focuses on the concurrency structure rather than actual image manipulation.

# Real-Life Use:
# Similar patterns can be used for image loading, file conversion, preprocessing, metadata extraction, and other I/O-heavy image workflows.