def extract_text_blocks(page):
    raw = page.get_text("rawdict")
    result = []

    for block in raw["blocks"]:
        if "lines" not in block:
            continue
        for line in block["lines"]:
            s = ""
            for span in line["spans"]:
                s += span["text"]
            result.append(s)

    return result
