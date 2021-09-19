"""
OCR Util:
 - Read ocr from an image
"""
import gpyocr as ocr
import logging

def get_ocr_str(img_path):
    # whitelist_txt = 'tessedit_char_whitelist=0123456789eroERO.-+%^'
    whitelist_txt='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-+%^'
    ocr_result = ocr.tesseract_ocr(img_path, lang='eng', psm=7, config=whitelist_txt)
    logging.info("----ocr_result: %s", str(ocr_result))
    if type(ocr_result) is tuple:
        return ocr_result[0]
    if ocr_result is None:
        return ""
    else:
        return ocr_result
