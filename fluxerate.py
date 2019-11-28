import gpt_2_simple.gpt_2_simple as gpt2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--prefix", "-p", default="flux",help="beginning of generated text")
parser.add_argument("--truncate", "-t", default="",help="beginning of generated text")

arguments = parser.parse_args()

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

gpt2.generate(sess,prefix=arguments.prefix,truncate=arguments.truncate,length=666)