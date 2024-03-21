from openai import OpenAI
import argparse

def MessagesGenerate(SystemContent,UserContent):
    return [
        {
            "role": "system",
            "content": SystemContent
        },
        {
            "role": "user",
            "content": UserContent
        }
    ]
# system_content="你是Kimi，由MoonshotAI提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提安全，有帮助，准确的回答。同时，你会拒绝一些涉及恐怖主义，种族歧视，黄色暴力等问题的回答。MoonshotAI为专有名词，不可翻译成其他语言。"
# user_content="1+10等于几"


def chat(api_key, base_url, model, system_content, user_content, temperature, stream):

    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    response = client.chat.completions.create(
        model=model,
        messages=MessagesGenerate(system_content, user_content),
        temperature=temperature,
        stream=stream,
    )

    collected_messages = []


    for idx, chunk in enumerate(response):
        #print("Chunk received, value: ", chunk)
        chunk_message = chunk.choices[0].delta
        if not chunk_message.content:
            continue
        collected_messages.append(chunk_message)  # save the message
        # 采用逐字输出
        # print(f"#{idx}: {''.join([m.content for m in collected_messages])}")
    print(f"Full conversation received: {''.join([m.content for m in collected_messages])}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_key", type=str, default="sk-h89V188KXxaeOE1EQBmKTiPWM6xkw4jXk9ckHOYvn8s6oB2l")
    parser.add_argument("--base_url", type=str, default="https://api.moonshot.cn/v1")
    parser.add_argument("--model", type=str, default="moonshot-v1-8k")
    parser.add_argument("--system_content", type=str)
    parser.add_argument("--user_content", type=str)
    parser.add_argument("--temperature", type=float, default=0.3)
    parser.add_argument("--stream", type=bool, default=True)
    args = parser.parse_args()
    chat(args.api_key, args.base_url, args.model, args.system_content, args.user_content, args.temperature, args.stream)