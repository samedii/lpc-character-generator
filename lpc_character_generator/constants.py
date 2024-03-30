import importlib.resources
from enum import Enum


class Sex(str, Enum):
    MAN = "Man"
    WOMAN = "Woman"


class Direction(str, Enum):
    SOUTH = "south"
    WEST = "west"
    EAST = "east"
    NORTH = "north"


class Action(str, Enum):
    RUN = "Run"
    WALK = "Walk"
    IDLE = "Idle"
    JUMP = "Jump"
    SWING = "Swing"
    CLIMB = "Climb"
    SLASH = "Slash"
    SITTING_CHAIR = "Sitting chair"
    SITTING_CROSS = "Siting cross-leg"
    SITTING_GROUND = "Sitting ground"
    HANDS_BEHIND = "Hands behind back"
    HANDS_HIPS = "Hands on hips"
    EMOTE_AIR = "Emote in air"
    BACKSLASH = "Backslash"
    FORWARD_SLASH = "Forward slash"
    HALFSLASH = "Halfslash"
    COMBAT_IDLE = "Combat Idle"


class Asset(str, Enum):
    HEAD = "head"
    BODY = "body"
    HAIR = "hair"
    NECK = "neck"
    EYES = "eyes"
    HEAD_ACCESSORY = "head_accessory"
    WINGS = "wings"
    SHIRT = "shirt"
    PANTS = "pants"
    SHOES = "shoes"
    SOCKS = "socks"
    SWORD = "sword"
    EYEBROWS = "eyebrows"
    OVER_SHIRT = "over_shirt"
    FACIAL_HAIR = "facial_hair"
    SHIELD_BASE = "shield_base"
    SHIELD_TRIM = "shield_trim"
    SHIELD_PAINT = "shield_paint"
    SHIELD_PATTERN = "shield_pattern"
    HELMET_ACCESSORY = "helmet_accessory"


class ClothingState(str, Enum):
    NAKED = "naked"
    F_CLOTHED = "fully clothed"
    P_CLOTHED = "partially clothed"


class ProbabilityType(str, Enum):
    FIXED = "fixed"
    DEFAULT = "default"
    UNIFORM = "uniform"


PATH_TO_DATA = importlib.resources.files("lpc_character_generator") / "data"

PATH_TO_ICONS = PATH_TO_DATA / "Icons"
PATH_TO_COLOR_NAMES = PATH_TO_DATA / "color_names.json"

PATH_TO_EDGES = PATH_TO_DATA / "edge_configs.json"
PATH_TO_ROTATION_GROUPS = PATH_TO_DATA / "rotation_groups.json"
PATH_TO_SKELETON_TRACKING = PATH_TO_DATA / "points" / "skeleton"

SHARED_ASSETS = {
    Asset.EYES,
    Asset.HEAD_ACCESSORY,
    Asset.SWORD,
    Asset.WINGS,
    Asset.EYEBROWS,
    Asset.SHIELD_BASE,
    Asset.SHIELD_TRIM,
    Asset.SHIELD_PAINT,
    Asset.SHIELD_PATTERN,
    Asset.HELMET_ACCESSORY,
}

PUT_ON_ORDER = [
    Asset.BODY,
    Asset.SHIRT,
    Asset.OVER_SHIRT,
    Asset.NECK,
    Asset.SOCKS,
    Asset.SHOES,
    Asset.PANTS,
    Asset.HEAD,
    Asset.EYES,
    Asset.EYEBROWS,
    Asset.FACIAL_HAIR,
    Asset.HAIR,
    Asset.HEAD_ACCESSORY,
    Asset.HELMET_ACCESSORY,
    Asset.WINGS,
    Asset.SWORD,
    Asset.SHIELD_BASE,
    Asset.SHIELD_TRIM,
    Asset.SHIELD_PAINT,
    Asset.SHIELD_PATTERN,
]

ASSET_SKIP_PROBABILITIES = {
    Asset.HAIR: ProbabilityType.UNIFORM,
    Asset.NECK: ProbabilityType.FIXED,
    Asset.FACIAL_HAIR: ProbabilityType.FIXED,
}

FIXED_SKIP_PROBABILITIES = {Asset.NECK: 0.95, Asset.FACIAL_HAIR: 0.95}

ACTION_TO_FILENAME = {
    Action.RUN: "Run",
    Action.WALK: "Walk",
    Action.IDLE: "Idle",
    Action.JUMP: "Jump",
    Action.SWING: "Legacy - Swing",
    Action.CLIMB: "Climb",
    Action.SLASH: "Combat 1h - Slash",
    Action.SITTING_CHAIR: "sitting_chair",
    Action.SITTING_CROSS: "sitting_cross",
    Action.SITTING_GROUND: "sitting_ground",
    Action.EMOTE_AIR: "emote_fall",
    Action.HANDS_HIPS: "emote_hips",
    Action.HANDS_BEHIND: "emote_behind",
    Action.BACKSLASH: "Combat 1h - backward",
    Action.FORWARD_SLASH: "Combat 1h - forward",
    Action.HALFSLASH: "Combat 1h - Halfslash",
    Action.COMBAT_IDLE: "Combat 1h - Idle",
}

ACTION_TO_COLUMNS = {
    Action.RUN: 8,
    Action.WALK: 8,
    Action.IDLE: 3,
    Action.JUMP: 6,
    Action.SWING: 6,
    Action.CLIMB: 6,
    Action.SLASH: 7,
    Action.SITTING_CHAIR: 1,
    Action.SITTING_CROSS: 1,
    Action.SITTING_GROUND: 1,
    Action.EMOTE_AIR: 1,
    Action.HANDS_HIPS: 1,
    Action.HANDS_BEHIND: 1,
    Action.BACKSLASH: 6,
    Action.FORWARD_SLASH: 6,
    Action.HALFSLASH: 6,
    Action.COMBAT_IDLE: 2,
}

DEFAULT_DIRECTION_ROW = {
    Direction.NORTH: 0,
    Direction.WEST: 1,
    Direction.SOUTH: 2,
    Direction.EAST: 3,
}

CLIMB_DIRECTION_ROW = {Direction.NORTH: 0}
DIRECTION_ROW = {Action.CLIMB: CLIMB_DIRECTION_ROW}

CONFLICTING_ASSETS = {
    Asset.HAIR: {Asset.HELMET_ACCESSORY, Asset.HEAD_ACCESSORY},
    Asset.HEAD_ACCESSORY: {Asset.HAIR},
    Asset.HELMET_ACCESSORY: {Asset.HAIR},
}
ASSET_COMPLEMENTARITY = {
    Asset.HELMET_ACCESSORY: (Asset.HEAD_ACCESSORY, {"Bascinet", "Morion"}),
    Asset.SHIELD_TRIM: (Asset.SHIELD_BASE, {}),
    Asset.SHIELD_PAINT: (Asset.SHIELD_BASE, {}),
    Asset.SHIELD_PATTERN: (Asset.SHIELD_BASE, {}),
}

FRAME_SIZE = 128
ROTATION_ORDER = [Direction.SOUTH, Direction.EAST, Direction.NORTH, Direction.WEST]
NON_ROTATION_ACTIONS = {Action.CLIMB}
NON_OPTIONAL_ASSETS = {
    Asset.HEAD,
    Asset.BODY,
    Asset.SHOES,
    Asset.SHIRT,
    Asset.SWORD,
    Asset.PANTS,
}

UNAVAILABLE_ACTIONS = {
    Direction.SOUTH: {Action.CLIMB},
    Direction.EAST: {Action.CLIMB},
    Direction.WEST: {Action.CLIMB},
}
ALLOWED_DIRECTIONS = {Action.CLIMB: [Direction.NORTH]}
GENDERED_ASSETS = {Sex.WOMAN: {Asset.FACIAL_HAIR}}

ASSET_TO_FILENAME = {
    Asset.HEAD: "Head",
    Asset.BODY: "Body",
    Asset.HAIR: "Hair",
    Asset.NECK: "Neck",
    Asset.EYES: "Eyes",
    Asset.HEAD_ACCESSORY: "Head Accessory",
    Asset.WINGS: "Wings",
    Asset.SHIRT: "Shirt",
    Asset.PANTS: "Pants",
    Asset.SHOES: "Shoes",
    Asset.SOCKS: "Socks",
    Asset.SWORD: "Sword",
    Asset.EYEBROWS: "Eyebrows",
    Asset.OVER_SHIRT: "Over Shirt",
    Asset.FACIAL_HAIR: "Facial Hair",
    Asset.SHIELD_BASE: "Shield Base",
    Asset.SHIELD_TRIM: "Shield Trim",
    Asset.SHIELD_PAINT: "Shield Paint",
    Asset.SHIELD_PATTERN: "Shield Pattern",
    Asset.HELMET_ACCESSORY: "Helmet Accessory",
}

NO_DESCRIPTION_ASSETS = {
    Asset.EYEBROWS,
    Asset.SHIELD_PAINT,
    Asset.SHIELD_TRIM,
    Asset.SHIELD_PAINT,
    Asset.SHIELD_BASE,
    Asset.SHIELD_PATTERN,
}
WITH_ASSETS = [
    Asset.HAIR,
    Asset.HEAD_ACCESSORY,
    Asset.WINGS,
    Asset.SOCKS,
    Asset.EYES,
    Asset.SHIRT,
    Asset.NECK,
    Asset.PANTS,
    Asset.SHOES,
    Asset.OVER_SHIRT,
    Asset.HELMET_ACCESSORY,
]
MAX_ITEMS = 2

ACTION_DESCRIPTIONS = {
    Action.RUN: "run",
    Action.WALK: "walk",
    Action.IDLE: "idle",
    Action.JUMP: "jump",
    Action.SWING: "horizontal slash attack",
    Action.CLIMB: "climb",
    Action.SLASH: "horizontal slash attack",
    Action.SITTING_CHAIR: "sitting on invisible chair",
    Action.SITTING_CROSS: "sitting cross-legged",
    Action.SITTING_GROUND: "sitting on ground",
    Action.HANDS_BEHIND: "hands behind back",
    Action.HANDS_HIPS: "hands on hips",
    Action.EMOTE_AIR: "falling",
    Action.BACKSLASH: "backslash attack",
    Action.FORWARD_SLASH: "slash attack",
    Action.HALFSLASH: "half slash attack",
    Action.COMBAT_IDLE: "idle",
}
