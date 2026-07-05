import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

system_prompt = """
你是 ThaiBridge CEO Office 的 CEO 助理。
你的职责：
1. 帮 CEO 梳理项目优先级
2. 整理客户、达人、任务和每日复盘
3. 输出清晰、可执行、可复制的中文方案
4. 不说空话，直接给下一步行动
"""

messages = [
    {"role": "system", "content": system_prompt}
]

print("✅ ThaiBridge CEO Assistant 已启动")
print("输入问题后按回车；输入 exit 退出。")

while True:
    user_input = input("\nCEO：")
    if user_input.lower() in ["exit", "quit", "退出"]:
        print("CEO Office 已关闭。")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )

    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})

    print("\nCEO Assistant：")
    print(answer)
