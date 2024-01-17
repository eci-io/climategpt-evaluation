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
        	--num_fewshot 5 \
          --include_path <path/to/this/repo/tasks/task_dir>
   
      






