# ClimateGPT Evaluation

Prompt templates for climate-specific tasks can be found under `tasks`.  

#### To evaluate an LLM on climate-specific tasks, follow the steps below:  
1. Clone this repo 
2. Clone and install [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/big-refactor) (the big-refactor branch)
3. The templates from this repo can be easily integrated with [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/big-refactor) by either:    
  a. placing the tasks from `tasks` directory under `lm_eval/tasks/` (in [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/big-refactor)) and running evaluation using the following command:  
      ```
      python3 lm-evaluation-harness/main.py \
      	--model hf \
      	--model_args pretrained=tiiuae/falcon-7b \
      	--tasks claim_binary \
      	--output_path /results/falcon-7b.jsonl \
      	--show_config --log_samples \
      	--num_fewshot 5
      ```
**OR**   
b. by directly passing the paths to the tasks as command-line arguments using `--include_path`. An example command is shown below:  
  
     
        python3 lm-evaluation-harness/main.py \
        	--model hf \
        	--model_args pretrained=tiiuae/falcon-7b \
        	--tasks claim_binary \
        	--output_path /results/falcon-7b.jsonl \
        	--show_config --log_samples \
        	--num_fewshot 5 --include_path <path/to/this/repo/tasks/exeter>

### Additional info
[HuggingFace Link to Climate Evaluation Datasets](https://huggingface.co/datasets/eci-io/climate-evaluation) | [Paper Link](https://arxiv.org/abs/2401.09646)

#### Citation Information 
```
@misc{thulke2024climategpt,
      title={ClimateGPT: Towards AI Synthesizing Interdisciplinary Research on Climate Change}, 
      author={David Thulke and Yingbo Gao and Petrus Pelser and Rein Brune and Rricha Jalota and Floris Fok and Michael Ramos and Ian van Wyk and Abdallah Nasir and Hayden Goldstein and Taylor Tragemann and Katie Nguyen and Ariana Fowler and Andrew Stanco and Jon Gabriel and Jordan Taylor and Dean Moro and Evgenii Tsymbalov and Juliette de Waal and Evgeny Matusov and Mudar Yaghi and Mohammad Shihadah and Hermann Ney and Christian Dugast and Jonathan Dotan and Daniel Erasmus},
      year={2024},
      eprint={2401.09646},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}

```


   
      






