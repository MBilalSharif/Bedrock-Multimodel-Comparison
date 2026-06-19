import boto3
import time

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")


# MODELS
models = {
    "Claude Sonnet 4": "us.anthropic.claude-sonnet-4-20250514-v1:0",
}

prompts = {
    "Structured Output": """
You are a strict information extraction system.

Task:
Extract structured data from the customer email.

Return ONLY valid JSON. No explanations. No extra text.

JSON format:
{
  "name": "",
  "issue": "",
  "sentiment": "",
  "urgency": ""
}

Email:
Customer: Muhammad Bilal Sharif
Issue: My laptop shuts down randomly during work. I am losing files and it is affecting my job. I need urgent help.
""",

    "Reasoning": """
A small business problem:

A company currently spends:
- $50,000 per month on manual data entry

An AI system costs:
- $80,000 one-time implementation
- $10,000 monthly operating cost

AI reduces workload by 70%.

Tasks:
1. Calculate monthly savings
2. Calculate payback period
3. Recommend whether to adopt AI or not

Show step-by-step reasoning clearly.
""",

    "Tone Control - Child": """
Explain cloud computing to a 10-year-old child.

Rules:
- Use simple words
- Use analogies
- Keep under 150 words
""",

    "Tone Control - Engineer": """
Explain cloud computing to a senior software engineer.

Must include:
- virtualization
- scalability
- elasticity
- distributed systems
- IaaS, PaaS, SaaS

Keep under 150 words.
"""
}

# INVOKE FUNCTION

def invoke(model_id, prompt):

    response = bedrock.converse(
        modelId=model_id,

        messages=[
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ],

        inferenceConfig={
            "temperature": 1,
            "maxTokens": 2048
        },

        additionalModelRequestFields={
            "thinking": {
                "type": "enabled",
                "budget_tokens": 1024
            }
        }
    )

    reasoning = ""
    answer = ""

    for block in response["output"]["message"]["content"]:

        if "reasoningContent" in block:
            rc = block["reasoningContent"]
            if "reasoningText" in rc:
                reasoning += rc["reasoningText"].get("text", "")

        elif "text" in block:
            answer += block["text"]

    return reasoning.strip(), answer.strip()



# RUN COMPARISON
for model_name, model_id in models.items():

    print("\n" + "=" * 90)
    print(f"MODEL: {model_name}")
    print("=" * 90)

    all_results = {}

    for task, prompt in prompts.items():

        print("\n" + "-" * 90)
        print(f"TASK: {task}")
        print("-" * 90)

        try:
            reasoning, answer = invoke(model_id, prompt)

            # store for comparison summary
            all_results[task] = {
                "reasoning": reasoning,
                "answer": answer
            }

            # print reasoning
            print("\n🧠 REASONING:\n")
            print(reasoning if reasoning else "No reasoning returned")

            # print final answer
            print("\n📌 FINAL ANSWER:\n")
            print(answer)

        except Exception as e:
            print("Error:", e)

        time.sleep(1)

    # ---------------------------
    # MODEL SUMMARY
    # ---------------------------
    print("\n" + "=" * 90)
    print(f"SUMMARY FOR {model_name}")
    print("=" * 90)

    for task, result in all_results.items():
        print(f"\n[{task}]")
        print("Answer Preview:", result["answer"][:200], "...")