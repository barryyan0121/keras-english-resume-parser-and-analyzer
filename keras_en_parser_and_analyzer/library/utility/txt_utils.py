from keras_en_parser_and_analyzer.library.utility.text_utils import preprocess_text


def txt_to_text(file_path):
    result = []
    with open(file_path, errors='ignore') as fp:
        lines = fp.readlines()
        for txt in lines:
            txt = txt.strip()
            if txt != '':
                txt = preprocess_text(txt)
                result.append(txt)
    return result
