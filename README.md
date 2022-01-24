# AA_victoria

Let's use GPT-3 to generate text in the style of Victorian authors.

Methodology 1/24/22:
  1) Tokenize the author's bibliography into sentences. 
  2) Fine-tune a model to take in a randomly selected sentence and output the next sentence.
  3) Feed the model randomly selected sentences and collect the output.
  
To-do: 
      -Ensure GPT-3 does not overfit and give us a sentence from the author verbatim.
      -Strip new lines '\n'.
      -Guarentee that GPT-3 returns a full sentence.
      -Attempt to make the outputs larger - difficult with tokens constraint.
