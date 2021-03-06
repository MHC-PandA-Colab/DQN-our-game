## Parameter List
from enum import Enum
from enum import IntEnum

VIZ_FLAG = True
TRAIN_ITER = 100  # 1500000
EVAL_MAX_ITER = 3

EVAL_EPISODE = 1
QNET_FC_LAYERS = [512,128,64]
QNET_CONV_LAYERS = [(32,8,4),(64,4,2),(64,3,1)]        # not used currently, but is a promising future work! 
QVALUE_DISCOUNT = 1.0

ADAM_LR = 1e-3
ADAM_EPSILON = 0.001

DECAY_UPDATE_PERIOD = 2
DECAY_STEPS = 250000
DECAY_LR_INIT = 1.0
DECAY_LR_END = 0.05

AGENT_UPDATE_PERIOD = 2000
AGENT_GAMMA = 0.99

BUFFER_LENGTH = 1000000
DRIVER_STEPS = 7
DATASET_STEPS = 300 # 350000
DATASET_PARALLEL = 3
DATASET_PREFETCH = 3
DATASET_BATCH = 200
DATASET_BUFFER_STEP = 2

CAM_COUNT = 6                       					# number of cameras in the system
CAM_STATE_DIM = 5                                       # number of states needed to describe camera pose (X,Y,Z,Xrot,Yrot)
CAM_INIT_DIST = 0.2                  					# normalized initial camera distance from origin (0~1)
TOOL_COUNT = 1                      					# number of tools in the system
TOOL_STATE_DIM = 7                                      # number of states needed to describe tool pose (X,Y,Z,Xrot,Yrot,Xvel,Yvel)

CAM_STATES = CAM_COUNT*CAM_STATE_DIM					# the tool info starting index in states
TOOL_STATES = TOOL_COUNT*TOOL_STATE_DIM    				# the camgoal starting index in states
TOTAL_STATES = 2*CAM_STATES + TOOL_STATES + 1  	    	# total number of states. Here is a breakdown of what each states are:
														# 0 ~ _cam_states: current camera poses
														# _cam_states ~ _cam_states + _tool_states: current tool poses
														# _cam_states + _tool_states + _cam_states: goal camera poses
														# last one: normalized timestep

BELLY_EDGE_LENGTH = 200              					# the belly border edge length (-200 ~ 200)
ANIMATION_LENGTH = 300                                  # number of iterations in animated point cloud
ANIMATION_FRAMERATE = 33.0/1000.0                       # ms per frame in animation
ANIMATION_FILE = './content/input/SurgicalData_100'     # the matlab file name
VISUALIZE_FILE = './content/input/SurgicalData_3200'    # the matlab file name for visualization
GRIDS_PER_SIDE = 51 									# the number of grid points along each axis
GRIDS_IN_SPACE =  GRIDS_PER_SIDE*GRIDS_PER_SIDE 		# total number of grids
GRID_LENGTH = 1.0/(GRIDS_PER_SIDE//2)                   # how large each grid is (normalized to 0~1)
MOVE_OPTIONS = 9                                        # number of actions per camera
OBS_SPEC_MAX = 2.0                                      # the max value of the observation spec
OBS_SPEC_MIN = -1.0                                     # the min value of the observation spec
EVAL_POLICY_DIR = "./content/20201211-215220"           # the default trained policy for evaluation

RECONST_EPSILON = 0.001                                 # epsilon for the reconstruction reward W function in funcs.py

CONE_LENGTH = 20										# camera viewing cone length (for drawing)
CONE_R0 = 0												# camera viewing cone inner radius (for drawing)
CONE_R1 = 10											# camera viewing cone outer radius (for drawing)
CAM_FOV = 0.523599 										# camera viewing angle (30 degrees)

RANSAC_TRIALS = 10
N_NEIGHBORS = 8


# possible consequences from action
class ActionResult(Enum):
    VALID_MOVE = 1
    ILLEGAL_MOVE = 2
    END_GAME = 3

# possible motion option given an axis
class Move(IntEnum):
    SAME = 0
    POS = 1
    NEG = -1
