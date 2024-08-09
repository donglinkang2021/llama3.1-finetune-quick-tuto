# LLAMA 3.1 Finetune Quick Start

<div align=center>
<img src = https://img.shields.io/badge/-Llama3.1%20Meta-0467DF?style=flat-square&logo=meta&logoColor=FFFFFF>
<img src = https://img.shields.io/badge/-RTX%204090-76B900?style=flat-square&logo=nvidia&logoColor=FFFFFF>
<img src = https://img.shields.io/badge/-HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=FFFFFF>
<img src = https://img.shields.io/badge/-WandB-FFBE00?style=flat-square&logo=weightsandbiases&logoColor=FFFFFF>
</div>

Use unsloth to fine-tune llama3.1 on your own dataset.

## 1. Install


## 2. Finetune

Run the following command to finetune with dataset `yahma/alpaca-cleaned`:

```bash
python main.py
```

## 3. Test

And you can test the finetuned model with the following command:

```bash
python test.py
```

For example, we test the prompt of `Give three tips for staying healthy.`:

```markdown
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Give three tips for staying healthy.

### Input:

### Response:
```

And we expect the output to look like(from `yahma/alpaca-cleaned`):

```markdown
1. Eat a balanced and nutritious diet: Make sure your meals are inclusive of a variety of fruits and vegetables, lean protein, whole grains, and healthy fats. This helps to provide your body with the essential nutrients to function at its best and can help prevent chronic diseases.
2. Engage in regular physical activity: Exercise is crucial for maintaining strong bones, muscles, and cardiovascular health. Aim for at least 150 minutes of moderate aerobic exercise or 75 minutes of vigorous exercise each week.
3. Get enough sleep: Getting enough quality sleep is crucial for physical and mental well-being. It helps to regulate mood, improve cognitive function, and supports healthy growth and immune function. Aim for 7-9 hours of sleep each night.
```

And different models will generate different outputs:

- `unsloth/Meta-Llama-3.1-8B-bnb-4bit`[origin model]

```markdown
One tip for staying healthy is to eat healthy food. Another tip is to exercise regularly. Another tip is to get enough sleep.
```

- `/root/autodl-tmp/llama3.1/lora_model`[finetuned model, no merge]

```markdown
1. Eat a balanced and nutritious diet: Consume a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats to provide your body with the necessary nutrients to function optimally.

2. Exercise regularly: Engage in physical activity for at least 30 minutes a day, five days a week, to maintain a healthy weight, boost your immune system, and improve your overall physical and mental health.

3. Get enough sleep: Aim for 7-9 hours of sleep each night to allow your body to rest and recharge. Quality sleep is essential for your physical and mental health.
```

- `/root/autodl-tmp/llama3.1/outputs/merged_16bit`[finetuned model, merged]

```markdown
1. Get enough sleep.
2. Eat a healthy diet.
3. Exercise regularly.
```


