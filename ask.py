import sys
import generate
import prompts
import ui


def form_messages():
    history = '\n'.join(ui.get_clipboard_content())
    question = ' '.join(sys.argv[1:])
    messages = [{"role": "system", "content": prompts.ask_prompt},
                {"role": "user",
                 "content": 'History command that has been run：' + history + '\n\nmy question：' + question}]
    return messages


def main():
    reply = generate.ask_gpt(form_messages())
    print(reply)
    ui.display_code_blocks(reply)


if __name__ == "__main__":
    main()
