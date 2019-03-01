import jieba

def segment_text(text:str) -> [] :
    """使用jieba对中文句子进行分词"""
    if text:
        return jieba.lcut(text)
    else:
        return []