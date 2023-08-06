from __future__ import annotations

import logging
import random
import re
from time import sleep

from deep_translator import GoogleTranslator
from deep_translator.exceptions import RequestError
from langdetect import detect
from tqdm import tqdm

from plagdef.model.models import Document

log = logging.getLogger(__name__)


def detect_lang(docs: set[Document]) -> None:
    for doc in docs:
        doc.lang = detect(doc.text) if doc.text else None


def docs_in_other_langs(docs: set[Document], expected_lang: str) -> set[Document]:
    return {doc for doc in docs if doc.lang != expected_lang}


def translate(docs: set[Document], target_lang: str, retry_limit=3) -> set[Document]:
    translated = set()
    for doc in tqdm(docs, desc='Translating', unit='doc'):
        if doc.lang != target_lang:
            if len(doc.text) < 50000:
                _translate(doc, target_lang, retry_limit)
                translated.add(doc)
            else:
                log.warning(f'Skipping translation of {doc} because its text length is greater than 50k chars.')
    return translated


def _translate(doc: Document, target_lang: str, retry_limit: int) -> None:
    # The limit of Google Translate Web is less than 5000 chars per request
    chunks = _split_text_at_punct(doc.text, 4999)
    for i, chunk in enumerate(chunks):
        attempt = 0
        while True:
            try:
                chunks[i] = GoogleTranslator(target=target_lang).translate(text=chunk)
                sleep(random.randint(1, 5))
                break
            except RequestError as e:
                if attempt >= retry_limit:
                    raise e
                log.warning(f"Request to Google Translate failed. Retrying ({attempt}/{retry_limit})...")
                attempt += 1
                sleep(10)
    doc.text = "".join(chunks)


def _split_text_at_punct(text: str, max_len: int, chunks: list[str] = None) -> list[str]:
    if chunks is None:
        chunks = []
    if len(text) <= max_len:
        return [*chunks, text]
    match = re.search(r'(?s:.*)[\.!\?]\s', text[:max_len])
    chunk = text[:match.end()] if match else text[:max_len]
    chunks.append(chunk)
    return _split_text_at_punct(text[match.end() if match else max_len:], max_len, chunks)
