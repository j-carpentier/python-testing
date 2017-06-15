# a few necessary imports
import json
from flask import Flask, make_response
from tendo import singleton
from multiprocessing import Process
import random

# first of all we create the Flask object
api_app = Flask(__name__)

# now we create an API entry point to create the list
@api_app.route('/output', methods=['GET'])
def share_output():
    output1 = {"count": "16","text": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text."}
    output2 = {"count": "51","text": "All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet."}
    output3 = {"count": "15","text": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."}
    output4 = {"count": "22","text": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."}
    output5 = {"count": "61","text": "If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text."}
    output6 = {"count": "35","text": "It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."}
    output7 = {"count": "56","text": "This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32."}
    output8 = {"count": "43","text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."}
    output9 = {"count": "26","text": "It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."}
    output10 = {"count": "76","text": "The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from de Finibus Bonorum et Malorum by Cicero are also reproduced in their exact original form"}


    outputs = [output1,output2,output3,output4,output5,output6,output7,output8,output9,output10]
    result = random.sample(outputs, 1)
    data = json.dumps(result)
    return data

def run():

    # first we check if there are other instances running
    myself = singleton.SingleInstance()

    # now we populate the local copy of galaxy upon start
    populate_process = Process(target=share_output)
    populate_process.start()

    # finally we run the api service as a daemon
    api_app.run(host="0.0.0.0", port=80, threaded=True)

if __name__ == '__main__':
    run()

