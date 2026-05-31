memory_store = {}


def save_message(
    session_id,
    role,
    message
):

    if session_id not in memory_store:
        memory_store[session_id] = []

    memory_store[session_id].append(
        {
            "role": role,
            "message": message
        }
    )


def get_conversation(
    session_id
):

    return memory_store.get(
        session_id,
        []
    )
