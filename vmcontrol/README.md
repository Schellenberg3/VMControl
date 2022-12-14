# VMControl an ISE 7202 Class project

The code for this project utilizes several prominent code repositories. For environment simulation we utilize CoppeliaSim and its Python APIs PyRep and RLBench, projects by Stephen James. For the reinforcement learning algorithms we rely on RL Kit by RAIL Berkeley. In addition we adapt a large part of the repo (and the specific versions of PyRep, RLBench, and RLKit) from work done by Bryan Chen and Alexander Sax. See their inspirational paper [here](https://sites.google.com/view/mid-level-representations/home). We are grateful for the availability of other's works.

This project is it not robust. It will not be esy to adapt. But should you want to, first install CoppeliaSim V4.1 and then follow the installation instructions in the directories for: rlkit,  PyRep, the RLBench. Be sure to use the `pip install -e [package]` so and local changes you make will be used.

There are sure to be more dependencies missing that you'll need to fix. I'm sorry for this. Just run it and hope for the best. 

The relevant code is in `ISE_7202/`. Good luck.


---

## Robust Policies via Mid-Level Visual Representations

Anonymized code in submission for CoRL 2020

Paper ID:526

All citations for the code can be found in this README. 

### Requirements

Set up RLKit: https://github.com/vitchyr/rlkit

    (RLKit is in this github)
    
    Use the conda env setup from this. 
    
Set up RLBench/PyRep/CoppeliaSim: https://github.com/stepjam/RLBench

    (RLBench/PyRep are in this github)
    
    Need to install the right version of CoppeliaSim, and have a working display for your setup, i.e. using XVFB. 
    
Install OpenAI Gym: https://github.com/openai/gym

### Instructions

To train a policy:
```
python mid_level_train.py --feature_task normal --env reach \
--models_path /path/to/representations
--noise eps --lr 1e-4 --max_path_length 50 --min_num_steps_before_training 1000 --special_name ExpName
```
Representation should be put in a path such as /pathname/segment_img/bestModel.pth. Sample policies will be uploaded with main release. 

The results will be saved to rlkit/data/ExpName/, where debug.log will show training details in a human-readable format, and progress.csv will contain full information. 

The mid-level representation training is asynchronous. To do so, first, generate a dataset:
```
python -m environments.dataset_generator --name=reach --env=reach \
    -f --max_steps_per_epoch 150 --num-episode 25 \
    --save-path save_path_here/ 
```

Train / finetune the representation networks on the dataset

```
python train.py --name insert_name --feature_task normal --batch_size 32 --num_epochs 500 --data_path /path/to/train/data/ --lr 3e-4

```

### Citations

rlkit/ code was adapted from https://github.com/vitchyr/rlkit.

We use RLBench, PyRep, and CoppeliaSim: https://github.com/stepjam/RLBench, https://github.com/stepjam/PyRep, https://coppeliarobotics.com/

robotics-rl-srl/ code was adapted from https://github.com/araffin/robotics-rl-srl

gym from https://github.com/openai/gym

VisualPriors package https://github.com/alexsax/midlevel-reps

midlevel_features/ code adapted from PyTorch docs
