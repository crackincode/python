from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont
import json
import os

def drawImage(index1, index2):
    img = Image.open('card.png')
    I1 = ImageDraw.Draw(img)
    fontImage = ImageFont.truetype("courbd.ttf", 46,)
    I1.text((1000, 900), f'{index1+1}/{index2+1}', fill=(255, 255, 255), font=fontImage)

    dirPath = f'result/image/Batch {index2+1}'

    path = os.path.exists(dirPath)

    if not path:
        os.makedirs(dirPath)
        print(dirPath)

    img.save(f'{dirPath}/card{index1+1}-{index2+1}.png')
    print(f'{dirPath}/card{index1+1}-{index2+1}.png created')

def writeJsonFile(index1, index2, title, desc):
    data = {
    "description": desc,
    "attributes": [
            {
            "trait_type": "Batch",
            "value": index2,
            },
            {
            "trait_type": "Edition",
            "value": index1
            }
        ],
        "collection": f"ipfsCID/card{index1+1}-{index2+1}.json"
    }
    jsonObject = json.dumps(data, indent=4)

    dirPath = f'result/json/Batch {index2+1}'

    path = os.path.exists(dirPath)

    if not path:
        os.makedirs(dirPath)
        print(dirPath)


    with open(f'{dirPath}/card{index1+1}-{index2+1}.json', 'w') as outfile:
        outfile.write(jsonObject)
        print(f'{dirPath}/card{index1+1}-{index2+1}.json created')


def startGenerate():
    batchSize = 10
    editionSize= 2000
    for batch in range(batchSize):
        for edition in range(editionSize):
            drawImage(edition, batch)
            writeJsonFile(edition, batch, f'Card {edition} / {batch}', f'Card {edition} / {batch}')



startGenerate()