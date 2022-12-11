import argparse

from train import get_gym_environment


def load_trained_policy(args):
    from torch import load

    from pathlib import Path
    import os

    POLICY_NAME = "trained_policy.pt"
    root_path = str( Path(__file__).resolve().parent )
    path = os.path.join(root_path, "networks", args.name, POLICY_NAME)
    return load(path)


def run_evaluation(args, env, agent):
    from train import wrap_environment

    env = wrap_environment(env, args)

    training_steps = 150
    episode_length = 50
    for i in range(training_steps):
        if i % episode_length == 0:
            print('Reset Episode')
            obs = env.reset()

        action = agent.get_action(obs['observation'])[0]

        input("press enter to take action...")

        # print("[DEBUG] %d action = " % i, type(action), action)

        obs, reward, terminate, _ = env.step(action)
        env.render()  # Note: rendering increases step time.



def main(args):
    evaluation_env = get_gym_environment(args)
    policy = load_trained_policy(args)

    print('[DEBUG] Loaded all, ready to run simulation')

    run_evaluation(args, evaluation_env, policy)
    
    # NOTE: Always close the environment
    evaluation_env.close()



if __name__ == "__main__":
    print('[INFO] Running main script')

    parser = argparse.ArgumentParser(description="Testing script for ISE 7202 final project")

    # ----------------------  The core arguments  ---------------------- #
    parser.add_argument(
        "--name", "-n",
        type = str,
        required = True,
        help = "Name for this network. Used in saving the weights. Default is the timestamp when training started."
    )

    parser.add_argument(
        "--display", "-d",
        action  = 'store_false',
        default = True,
        help = "Include this flag run the CoppeliaSim environment but not display it."
    )

    parser.add_argument(
        '--domain-randomization','-dr',
        action='store_true',
        default=False,
        help="Include this flag to use the chosen environment with domain randomization"
    )

    # NOTE: The following are network-specific attributes which _should_ be saved with the network.
    #       But I don't have the time nor the energy to do this right now. Best to put them in the
    #       network name so you don't forget. Or implement it yourself! Sorry about that.
    parser.add_argument(
        "--depth",
        action  = 'store_true',
        default = False,
        help = "Include this flag to train the agent on depth instead of RGB."
    )

    parser.add_argument(
        "--image-size", "-sz",
        type = int,
        default = 64,
        help = "Number of pixels in the square RGB and Depth image. Recommended values are 64 or 256."
    )

    args = parser.parse_args()
    main(args)
