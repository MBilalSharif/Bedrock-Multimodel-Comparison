# Amazon Bedrock Multi-Model Comparison

This project evaluates multiple Amazon Bedrock foundation models using the **Bedrock Converse API**. Four different models are tested across common enterprise AI tasks to compare their response quality, reasoning ability, instruction following, and output consistency.

The evaluation includes structured data extraction, business reasoning, and tone adaptation to better understand the strengths and limitations of each model.

---

## Features

* Amazon Bedrock Converse API
* Multi-model evaluation
* Structured JSON extraction
* Business reasoning comparison
* Tone-controlled content generation
* Performance analysis across different AI tasks
* Python implementation using Boto3

---

## Models Evaluated

* Claude 3 Haiku
* Amazon Titan Text
* Mistral
* Llama 3

---

## Evaluation Tasks

### 1. Structured Output

Each model receives a customer support email and extracts:

* Customer name
* Reported issue
* Sentiment
* Urgency

The models are instructed to return **valid JSON only**, allowing comparison of:

* JSON validity
* Instruction adherence
* Extraction accuracy
* Consistency

---

### 2. Reasoning

Each model solves a short business problem involving:

* Simple calculations
* Cost analysis
* Recommendation generation

The evaluation focuses on:

* Calculation accuracy
* Logical reasoning
* Recommendation quality
* Explanation clarity

---

### 3. Tone Control

Each model explains the concept of **Cloud Computing** for two different audiences:

* A 10-year-old child
* A senior cloud engineer

The comparison evaluates:

* Audience adaptation
* Technical depth
* Language complexity
* Overall clarity

---

## Project Structure

```text
.
├── model_comparison.py            
├── results/                 
└── README.md
```

---

## Technologies Used

* Python
* Amazon Bedrock
* Bedrock Converse API
* Boto3

---

## Evaluation Criteria

The models are compared based on:

| Criterion             | Description                                         |
| --------------------- | --------------------------------------------------- |
| Instruction Following | Ability to follow prompt constraints                |
| Output Quality        | Accuracy and completeness of responses              |
| JSON Validity         | Correct structured output generation                |
| Reasoning             | Logical problem-solving and recommendations         |
| Tone Adaptation       | Ability to adjust responses for different audiences |
| Response Consistency  | Stability of outputs across multiple tasks          |

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/<username>/bedrock-multimodel-comparison.git
cd bedrock-multimodel-comparison
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure AWS Credentials

Configure your AWS credentials using the AWS CLI or environment variables.

### Run

```bash
python model_comparison.py
```

---

## Learning Outcomes

This project demonstrates:

* Using the Amazon Bedrock Converse API
* Invoking multiple foundation models with a unified interface
* Designing prompt-based evaluations
* Comparing structured output generation
* Evaluating reasoning capabilities
* Measuring tone adaptation across different audiences
* Benchmarking foundation models for practical AI use cases

---

## Future Improvements

* Add latency and response time benchmarking
* Compare token usage and estimated cost
* Evaluate additional foundation models
* Automate scoring and report generation
* Export results to CSV or Excel dashboards
* Add visualization of model performance metrics

---

## License

This project is intended for educational and learning purposes.
