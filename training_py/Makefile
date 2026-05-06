.PHONY=training


TRAINING ?= "projects"
EXERCISE ?= "e04"

training:
	@clear
	@date
	python3 training_py/main.py --training $(TRAINING) --exercise $(EXERCISE)
	@date

training-conditional: TRAINING="conditional"
training-conditional: training

training-loop: TRAINING="loop"
training-loop: training

training-regex: TRAINING="regex"
training-regex: training

training-lists-tuples: TRAINING="lists_tuples"
training-lists-tuples: training

training-sets-dicts: TRAINING="sets_dicts"
training-sets-dicts: training

training-fn: TRAINING="fn"
training-fn: training

training-async: TRAINING="async"
training-async: training

training-projects: TRAINING="projects"
training-projects: training

