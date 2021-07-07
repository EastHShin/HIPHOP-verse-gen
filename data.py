import requests
import json


def hiphop_text(context):
    text = context
    num_samples = 1
    length = 30

    headers = {'Content-Type': 'application/json'}
    data = '{{ "context" : "{}" }}'.format(text)
    text2vector = requests.post('https://main-gpt-2-server-gkswjdzz.endpoint.ainize.ai/preprocess', headers=headers,
                                data=data)
    if text2vector:
        text2vector = json.loads(text2vector.json())
    else:
        print("here?")
        print(text2vector.status_code, "error")

    headers = {'Content-Type': 'application/json'}
    data = '{{ "text": {}, "num_samples": {}, "length": {} }}'.format(text2vector, num_samples, length)
    result = requests.post(
        'https://train-28fsu5ldr900ckrct8t1-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-en-medium-finetune',
        headers=headers, data=data)
    if result:
        result = str(result.json())
        print(result)
    else:
        print("here??")
        print(result.status_code, "error")

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    vector2text = requests.post('https://main-gpt-2-server-gkswjdzz.endpoint.ainize.ai/postprocess', headers=headers,
                                data=result)
    if vector2text:
        for key, value in vector2text.json().items():
            return value["text"]
    else:
        print("here???")
        print(vector2text.status_code, "error")
