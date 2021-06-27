import os
import json

import responder

from text_augment import TextAugmenter


env = os.environ
DEBUG = env['DEBUG'] in ['1', 'True', 'true']
MODE = env.get('MODE')

api = responder.API(debug=DEBUG)
text_augmenter = TextAugmenter(MODE)


@api.route("/")
async def index(req, resp):
    body = await req.text
    texts = json.loads(body)
    docs = [text_augmenter.augment(text) for text in texts]
    resp.media = dict(data=docs)


if __name__ == "__main__":
    api.run()
