import gpt_2_simple.gpt_2_simple as gpt2
import os
import requests

# model_name = "124M"
model_name = "355M"
if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/

filename="./train/hybrid_shuffled_monolithic.txt"

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              filename,
              model_name=model_name,
              steps=666)   # steps is max number of training steps

gpt2.generate(sess)