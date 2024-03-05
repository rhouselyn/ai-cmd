import sys
import time

import pyautogui
import pyperclip


def generate_dots(stop_event):
    dots = ""
    while not stop_event.is_set():
        dots = dots + "." if len(dots) < 3 else ""
        sys.stdout.write(f"\rGenerating{dots}   ")  # 确保足够的空格覆盖之前的文本
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\r" + " " * 20 + "\r")  # 清除行
    sys.stdout.flush()


def display_code_blocks(reply):
    code_blocks = []

    for line in reply.split('\n'):
        if line.strip().startswith('>'):
            code_blocks.append(line.strip('>'))

    if code_blocks:
        code = '\n'.join(code_blocks).strip()
        pyperclip.copy(code)
        print("\n```copied```\n", code, "\n````````````")


def polish_reply(reply):
    if "UNKNOWN" in reply:
        print("UNKNOWN: please try another instruction")
        return

    polished_reply = ""
    for content in reply.split('\n'):
        if content.startswith('>'):
            polished_reply += content[1:] + "\n"
            pyperclip.copy(polished_reply)
        elif content == "DANGEROUS":
            polished_reply += "CAUTION: This command is dangerous!"

        polished_reply += "\n"

    else:
        print(polished_reply.strip())


def get_clipboard_content():
    pyautogui.hotkey('ctrl', 'shift', 'a')
    # pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('left')
    clipboard_text = pyperclip.paste().strip()
    pyperclip.copy("")

    paragraphs = clipboard_text.split('\r\n\r\n')[1:-1]  # 按段落分割
    total_words = 0
    selected_paragraphs = []

    # 从后向前遍历段落，累计单词数直到达到或超过1000
    for paragraph in reversed(paragraphs):
        words = paragraph.split()
        total_words += len(words)
        selected_paragraphs.append(paragraph)
        if total_words >= 1000:
            break

    # 确保段落顺序与原文一致
    selected_paragraphs.reverse()

    # 如果段落总数不超过1000个单词，则返回整个文本
    return selected_paragraphs if total_words >= 1000 else paragraphs
