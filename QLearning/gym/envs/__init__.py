from gym.envs.registration import registry, register, make, spec


# Classic
# ----------------------------------------

register(
    id='DinoEnv-v0',
    entry_point='gym.envs.classic_control:DinoEnv',
)

