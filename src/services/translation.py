from transformers import MBartForConditionalGeneration, AutoTokenizer
from fastapi import Depends
from src.nlp.MBart.mbart import get_model, get_tokenizer
import typing as t
import torch
from src.schemas.translation.translation_request import TranslationRequest


class TranslationService:
    def __init__(self,
                 model: MBartForConditionalGeneration = Depends(get_model),
                 tokenizer: AutoTokenizer = Depends(get_tokenizer)):

        self.model: MBartForConditionalGeneration = model
        self.tokenizer: AutoTokenizer = tokenizer

    def translate(self, translation_request: TranslationRequest) -> str:
        return self.__decode(
            self.__generate(
                self.__tokenize(
                    text=translation_request.text, 
                    src_lang=translation_request.src_lang), 
                trg_lang=translation_request.trg_lang)
        )

    def __tokenize(self, text: str, src_lang: str) -> t.Dict[str, torch.Tensor]:
        self.tokenizer.src_lang = src_lang
        return self.tokenizer(text, return_tensors="pt")

    def __generate(self,
                   tokenizer_output: t.Dict[str, torch.Tensor],
                   trg_lang: str) -> torch.Tensor:
        return self.model.generate(
            **tokenizer_output,
            forced_bos_token_id=self.tokenizer.lang_code_to_id[trg_lang]
        )

    def __decode(self, model_output: torch.Tensor) -> str:
        return self.tokenizer.batch_decode(model_output, skip_special_tokens=True)[0]
