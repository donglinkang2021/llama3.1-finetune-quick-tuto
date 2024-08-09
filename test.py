from unsloth import FastLanguageModel
from config import *
model, tokenizer = FastLanguageModel.from_pretrained(
    # model_name = "unsloth/Meta-Llama-3.1-8B-bnb-4bit",
    # model_name = "/root/autodl-tmp/llama3.1/lora_model",
    model_name = "/root/autodl-tmp/llama3.1/outputs/merged_16bit",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)
FastLanguageModel.for_inference(model)
alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""
inputs = tokenizer(
[
    alpaca_prompt.format(
        "Give three tips for staying healthy.", # instruction
        "", # input
        "", # output - leave this blank for generation!
    )
], return_tensors = "pt").to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer)
_ = model.generate(**inputs, streamer = text_streamer, max_new_tokens = 128)