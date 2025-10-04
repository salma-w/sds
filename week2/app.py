from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
import gradio as gr
from dotenv import load_dotenv

MODEL = "gpt-4.1-mini"
db_name = "vector_db"
knowledge_base_path = "knowledge-base/*"

load_dotenv(override=True)

# create a new Chat with OpenAI
llm = ChatOpenAI(temperature=0.7, model_name=MODEL)

vectorstore = Chroma(persist_directory=db_name, embedding_function=OpenAIEmbeddings())
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

SYSTEM_PROMPT = """
You are a knowledgeable, friendly assistant representing the company Insurellm.
You are chatting with a user about Insurellm.
If relevant, use the given context to answer any question.
If you don't know the answer, say so.

Context:
{context}
"""


def chat(message, history):
    messages = [("system", SYSTEM_PROMPT)]
    for h in history:
        if h["role"] == "user":
            messages.append(("user", h["content"]))
        else:
            messages.append(("assistant", h["content"]))

    messages.append(("user", message))
    prompt = ChatPromptTemplate.from_messages(messages)
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    response = rag_chain.invoke({"input": message})
    return response["answer"]


def main():
    gr.ChatInterface(fn=chat, type="messages").launch(inbrowser=True)


if __name__ == "__main__":
    main()
