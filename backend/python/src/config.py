# Adjust below for play adjustments
EPISODES = 30
MCTS_SIMS = 50
MEMORY_SIZE = 30000
TAU_TURNS = 10 # Noise tolerance, when should it play deterministically
CPUCT = 1
EPSILON = 0.2
ALPHA = 0.8


# Adjust below for Retraining adjustments
BATCH_SIZE = 256
EPOCHS = 1
REG_CONST = 0.0001
LEARNING_RATE = 0.1
MOMENTUM = 0.9
TRAINING_LOOPS = 10

HIDDEN_CNN_LAYERS = [
        {'filters':75, 'kernel_size':(4,4)},
        {'filters':75, 'kernel_size':(4,4)},
        {'filters':75, 'kernel_size':(4,4)},
        {'filters':75, 'kernel_size':(4,4)},
        {'filters':75, 'kernel_size':(4,4)},
        {'filters':75, 'kernel_size':(4,4)}
        ]

# Adjust below for evaluation
EVAL_EPISODES = 20
SCORING_THRESHOLD = 1.3
