from transformers import MBartForConditionalGeneration, AutoTokenizer
from pathlib import Path


tokenize_path = Path(r'src\nlp\MBart\tokenize')

if not (tokenize_path / 'sentencepiece.bpe.model').exists():
    AutoTokenizer.from_pretrained("facebook/mbart-large-50-many-to-many-mmt", use_fast=False).save_pretrained(str(tokenize_path))
# tokenizer = AutoTokenizer.from_pretrained(str(tokenize_path), use_fast=False) 

model_path = Path(r'src\nlp\MBart\model')

if not (model_path / 'model.safetensors').exists():
    MBartForConditionalGeneration.from_pretrained('facebook/mbart-large-50-many-to-many-mmt').save_pretrained(str(model_path))
# model = MBartForConditionalGeneration.from_pretrained(str(model_path))


def get_model():
    model = MBartForConditionalGeneration.from_pretrained(str(model_path))
    try:
        yield model
    finally:
        del model


def get_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(str(tokenize_path), use_fast=False) 
    try:
        yield tokenizer
    finally:
        del tokenizer
