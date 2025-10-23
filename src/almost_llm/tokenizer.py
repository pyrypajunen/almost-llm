"""Tokenizer implementation for text processing.

This module handles:
- Text to token conversion
- Vocabulary management
- Encoding and decoding
- Special tokens (BOS, EOS, PAD, UNK)
- Training tokenizer on corpus
"""

# %%
import re 

class Tokenizer:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text: str) -> list[int]:
        preprocessed = re.sub(r'[,.:;?_!"()\']|--', ' ', text)
        words = [word.strip() for word in preprocessed.split() if word.strip()]
        # return ids
        ids = [self.str_to_int[word] for word in words]
        # return ids and words
        return ids

    def decode(self, ids: list[int]) -> str:
        return " ".join([self.int_to_str[id] for id in ids])


# %%
if __name__ == "__main__":
    text = """
    "On a bright and sunny morning, Alice decided to take a stroll in the city park. "
    "The trees were lush and green, birds chirped harmoniously from the branches, and a gentle breeze carried the scent of blooming flowers. "
    "As she walked along the winding path, she noticed children laughing as they played near the pond, their shouts echoing in the clear air. "
    "Alice paused to watch a pair of ducks gliding gracefully across the water, reflecting on the tranquility of the scene. "
    "Soon, her friend Ben joined her, and together they talked about their upcoming vacation, work projects, and dreams for the future. "
    "The hours passed quickly, filled with conversation, laughter, and the simple joys of being surrounded by nature."
"""
    # Preprocess text before building vocab (same as in encode method)
    preprocessed = re.sub(r'[,.:;?_!"()\']|--', ' ', text)
    words = [word.strip() for word in preprocessed.split() if word.strip()]
    vocab = {token: integer for integer, token in enumerate(sorted(set(words)))}
    
    for i, item in enumerate(vocab.items()):
        print(f"{item}")
        if i >= 50:
            break


    tokenizer = Tokenizer(vocab)
    tokens = tokenizer.encode(text)
    print(tokens)
    text = tokenizer.decode(tokens)
    print(text)
# %%