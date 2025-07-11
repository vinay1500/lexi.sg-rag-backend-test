def generate_answer(query, chunks):
    combined_text = "\n".join([chunk["text"] for chunk in chunks])
    answer = f"(Mock answer) Based on the documents, the answer to '{query}' is likely explained in the following chunks."
    citations = [{"text": c["text"], "source": c["source"]} for c in chunks]
    return answer, citations
