from ai_gateway import AIGateway

ai = AIGateway(provider="deepseek")

answer = ai.chat(
    system_prompt="你是 ThaiBridge AI Gateway 测试助手。",
    user_prompt="请只回复一句话：AI Gateway V1 已经正式完成。"
)

print(answer)
