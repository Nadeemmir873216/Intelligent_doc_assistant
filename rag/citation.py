def format_source(chunks):
    sources = set()
    for c in chunks:
        sources.add(f"{c['source']} (page {c['page']})")
    return list(sources)