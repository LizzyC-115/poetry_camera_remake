from google import genai

API_KEY = "AIzaSyA7PAHeAOothlEnInk59m5y9gioi7Z5zC8"

STYLES = ["Haiku", "Cinquain", "Limerick", "Tanka"]

PROMPT = "Analyze the content, mood," \
" and symbolism of the provided image. " \
"Then, write a poem that reflects what is seen " \
"and felt in the image. Use vivid, sensory " \
"language and emotional tone that corresponds " \
"to the image’s atmosphere. Compose the poem in " \
"the given style." \
"Ensure the style’s form, tone, and structure are respected. " \
"Title the poem appropriately based on the image. Only respond giving the title" \
"and the poem itself. Do not include anything else except the title and the poem."

def uploadImage(image, client):
    file = client.files.upload(file=image)
    return file

def generatePoem(image, style, client):
    file = uploadImage(image, client)
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=[PROMPT, file, style],
    )
    print(response.text)

def main():
    client = genai.Client(api_key=API_KEY)
    image_path = input("Input an image path: ")
    choice = input(f"Poetry Styles:  1) {STYLES[0]},  2) {STYLES[1]},  3) {STYLES[2]}, 4) {STYLES[3]} \
                   \nInput a number to choose a style: ")
    poem_style = STYLES[int(choice) - 1]
    generatePoem(image_path, poem_style, client)

if __name__ == "__main__":
    main()
