from sudachipy import tokenizer, dictionary


class TextAugmenter:
    def __init__(self, mode=None):
        self.tokenizer_obj = dictionary.Dictionary().create()
        self._set_mode(mode)

    def _set_mode(self, mode):
        if mode == 'A':
            self.mode = tokenizer.Tokenizer.SplitMode.A
        elif mode == 'B':
            self.mode = tokenizer.Tokenizer.SplitMode.B
        else:
            self.mode = tokenizer.Tokenizer.SplitMode.C

    def _augment_step(self, texts, tokens):
        return list(set([text+token for text in texts for token in tokens]))

    def augment(self, text):
        morphemes = self.tokenizer_obj.tokenize(text, self.mode)
        texts = ['']
        for m in morphemes:
            tokens = [m.surface(), m.normalized_form()]
            texts = self._augment_step(texts, tokens)
        return texts
