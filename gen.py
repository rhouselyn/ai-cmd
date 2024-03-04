import sys
import generate
import prompts
import ui


def form_messages():
    messages = prompts.gen_prompts.copy()
    messages.append({"role": "user", "content": ' '.join(sys.argv[1:])})
    return messages


def main():
    reply = generate.ask_gpt(form_messages(), 0.4)
    ui.polish_reply(reply)


if __name__ == "__main__":
    main()
