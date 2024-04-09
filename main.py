from PIL import Image
import sys, os, pillow_avif

input_folder = "input/"
output_folder = "output/"

def convert_to_avif(file):
    image = Image.open(input_folder + file)

    file = file.split(".")[0] + ".avif"
    image.save(output_folder +file, format="AVIF")

if __name__ == "__main__":
    args = sys.argv
    input_folder = "input/"
    output_folder = "output/"

    if len(args) < 2:
        sys.exit()

    if len(args) == 3:
        output_folder = args[2] + "/"
    
    os.makedirs(output_folder, exist_ok=True)

    input_folder = args[1] + "/"
    files = os.listdir(input_folder)
    for file in files:
        convert_to_avif(file)


    print("--> Conversion terminée")

    default_cost = sum(os.path.getsize(os.path.join(input_folder, file)) for file in files)
    finally_cost = sum(os.path.getsize(os.path.join(output_folder, file)) for file in os.listdir(output_folder))
                       
    print(f"Coût d'espace au début : {default_cost}")
    print(f"Coût d'espace à la fin : {finally_cost}")



    