from transformers import TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model
from datasets import load_dataset
from models.llama_loader import LLaMAModel

class LoraTrainer:

    def __init__(self, model_name):
        base = LLaMAModel(model_name).model

        lora_config = LoraConfig(
            r=16,
            lora_alpha=32,
            target_modules=["q_proj","v_proj"],
            lora_dropout=0.1,
            task_type="CAUSAL_LM"
        )

        self.model = get_peft_model(base, lora_config)

    def train(self, dataset_path):

        dataset = load_dataset("json",
                               data_files=dataset_path)

        args = TrainingArguments(
            output_dir="lora_output",
            per_device_train_batch_size=2,
            num_train_epochs=3,
            fp16=True,
            logging_steps=20
        )

        trainer = Trainer(
            model=self.model,
            args=args,
            train_dataset=dataset["train"]
        )

        trainer.train()
        self.model.save_pretrained("lora_output")
