from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import BaseMessage
import gradio as gr
from dotenv import load_dotenv
import logging
from typing import Any
from colorama import Fore, Style, init

from answer import answer_question

init(autoreset=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

load_dotenv(override=True)

COLORS = {"system": Fore.YELLOW, "human": Fore.GREEN, "ai": Fore.BLUE}


class MessageLoggingCallback(BaseCallbackHandler):
    """Custom callback handler to log actual messages sent to LLM."""

    def on_chat_model_start(
        self, serialized: dict[str, Any], messages: list[list[BaseMessage]], **kwargs: Any
    ) -> None:
        for batch_idx, message_list in enumerate(messages):
            for msg_idx, msg in enumerate(message_list, 1):
                color = COLORS.get(msg.type, Fore.WHITE)
                logger.info(f"{color}{msg.content}{Style.RESET_ALL}")


def format_context(context):
    result = "## Relevant Context\n\n"
    for doc in context:
        result += f"### From {doc.metadata['source']}\n\n"
        result += doc.page_content + "\n\n"
    return result


async def chat(history):
    # Get the last user message
    last_message = history[-1]["content"]

    # Use shared answer_question function
    answer, context = await answer_question(last_message)

    history.append({"role": "assistant", "content": answer})
    return history, format_context(context)


def main():
    def put_message_in_chatbot(message, history):
        return "", history + [{"role": "user", "content": message}]

    theme = gr.themes.Soft(font=["Inter", "system-ui", "sans-serif"])

    with gr.Blocks(title="Insurellm Expert Assistant", theme=theme) as ui:
        gr.Markdown("# 🏢 Insurellm Expert Assistant\nAsk me anything about Insurellm!")

        with gr.Row():
            with gr.Column(scale=1):
                chatbot = gr.Chatbot(
                    label="💬 Conversation", height=600, type="messages", show_copy_button=True
                )
                message = gr.Textbox(
                    label="Your Question",
                    placeholder="Ask about Insurellm products, employees, contracts...",
                    show_label=False,
                )

            with gr.Column(scale=1):
                context_markdown = gr.Markdown(
                    label="📚 Retrieved Context",
                    value="*Retrieved context will appear here*",
                    container=True,
                    height=600,
                )

        message.submit(
            put_message_in_chatbot, inputs=[message, chatbot], outputs=[message, chatbot]
        ).then(chat, inputs=chatbot, outputs=[chatbot, context_markdown])

    ui.launch(inbrowser=True)


if __name__ == "__main__":
    main()
