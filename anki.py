import os

import requests

def download_images(query, output_folder):
    access_key = 'hoTBbYCjxxxxxx_xxxxxxxxxxxxxxxxx'  # Replace with your Unsplash access key
    headers = {
        'Authorization': f'Client-ID {access_key}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    url = f'https://api.unsplash.com/search/photos?query={query}&per_page=1'  # Fetch only 1 image per word

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        images = data['results']

        if images:
            image_url = images[0]['urls']['regular']
            if image_url and image_url.startswith('http'):
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    with open(os.path.join(output_folder, f'{query}_image.jpg'), 'wb') as f:
                        f.write(image_response.content)
                    print(f"Download of image for '{query}' is complete.")
                else:
                    print(f"Failed to download the image for '{query}'.")
            else:
                print(f"No valid image URL found for '{query}'.")
        else:
            print(f"No images found for '{query}'.")
    else:
        print(f"Failed to fetch images related to '{query}'.")

if __name__ == "__main__":
    queries =mylist = ['book',
                       'door',
                       'help']

    output_folder = 'word_images'  # Replace with the folder path where you want to save the images

    for query in queries:
        download_images(query, output_folder)

    print("All downloads are finished.")


    file_name = "replace.txt"

    # Open the file in write mode
    with open(file_name, "w") as file:
        # Iterate through each character of the word
        for item in mylist:
            # Write the item to the file followed by a new line character
            file.write(item +f",<br> <img src='{item}_image.jpg'>;"+ "\n")

    print(f"Successfully created '{file_name}' and wrote each letter on a separate line.")

    input_file_path = 'AIoutput.txt'
    if __name__ == '__main__':

        try:
            # Open the input file for reading
            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                file_content = input_file.read()
                lines = file_content
            # Replace all commas with <br><br>
            replaced_content = file_content.replace(",", "<br><br>")

            # Open the output CSV file for writing
            with open("Anki import.CSV", "w", encoding="utf-8") as output_file:
                # Write the modified content to the output file
                output_file.write(replaced_content)

            print("Replacement complete. Output saved as word.txt")
        except FileNotFoundError:
            print(f"File not found: {input_file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")











