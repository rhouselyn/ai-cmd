import json
import threading
import time
import requests
import config
import ui


def ask_gpt(messages, temperature=0.7):
    stop_event = threading.Event()
    thread = threading.Thread(target=ui.generate_dots, args=(stop_event,))
    thread.start()

    data = {
        "model": config.model,
        "messages": messages,
        'temperature': temperature,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.api_key}"
    }
    try:
        response = requests.post(config.request_url, headers=headers,
                                 data=json.dumps(data), timeout=15)
        response.raise_for_status()  # 将触发异常，如果状态不是 200

        # 停止动态文本显示
        stop_event.set()
        thread.join()

        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        # 停止动态文本显示
        stop_event.set()
        thread.join()

        if 'limit' in str(e) or 'Too Many' in str(e):
            print("API limit reached, please wait a moment.\nRetrying...")
            time.sleep(2)
            return ask_gpt(messages)
        else:
            print("request error: ", e, '\nplease check your api key and network connection, or try again.')
            exit()
