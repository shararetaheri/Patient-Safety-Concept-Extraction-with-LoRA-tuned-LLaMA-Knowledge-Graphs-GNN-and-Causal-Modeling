from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class LLaMAModel:

    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )

    def generate(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=512,
            temperature=0.2
        )
        return self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )
