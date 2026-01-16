def to_exact_text(page_texts):
    out = []
    for i, text in enumerate(page_texts, start=1):
        out.append(f"┌──────── PAGE {i} ─────────┐")
        out.append(text.rstrip("\n"))
        out.append("└──────────────────────────┘\n")
    return "\n".join(out)
