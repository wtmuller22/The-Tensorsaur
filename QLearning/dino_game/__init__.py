import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Dino-v0',
    entry_point='dino_game.envs:DinoEnv',
    timestep_limit=1000,
    reward_threshold=10.0,
    nondeterministic = True,
)