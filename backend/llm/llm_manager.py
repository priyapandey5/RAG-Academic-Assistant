from llm.gemini_client import client
from core.prompts import system_prompt
from rag.retriever import retrieve_chunks


def llm_response(query, conversation=None):

    similar_chunks = retrieve_chunks(query)

    context = ""

    sources = []

    for chunk in similar_chunks:

        if isinstance(chunk, dict):

            context += chunk.get(
                "text",
                ""
            ) + "\n\n"

            source = chunk.get(
                "source",
                "Unknown Source"
            )

            sources.append(source)

        else:

            context += str(chunk) + "\n\n"

    sources = list(set(sources))

    print("\n===== RETRIEVED CONTEXT =====")
    print(context)
    print("============================\n")

    prompt = (
        system_prompt
        + "\n\nContext:\n"
        + context
        + "\n\nUser Question:\n"
        + query
    )

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        answer = response.text

        if sources:

            answer += "\n\n📄 Sources:\n"

            for source in sources:
                answer += f"\n• {source}"

        return answer

    except Exception as e:

        return f"Error generating response: {str(e)}"
