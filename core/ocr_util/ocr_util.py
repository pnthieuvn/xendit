"""
OCR Util:
 - Scan image then return as string
"""
import gpyocr as ocr
import logging

def get_ocr_str(img_path):
    whitelist_txt='tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzBCDEFGHIJKLMNOPQRSTUVWXYZ.-+%^'
    ocr_result = ocr.tesseract_ocr(img_path, lang='eng', psm=7, config=whitelist_txt)
    if type(ocr_result) is tuple:
        return ocr_result[0]
    if ocr_result is None:
        return ""
    else:
        return ocr_result
