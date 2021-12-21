#!/usr/bin/python
# # -*- coding:UTF-8 -*-

def clip(text, max_len=80)->str:
    """
        在max_len前面或者后面的第一个空格截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没有找到空格
        end = len(text)
    return text[:end].rstrip()

