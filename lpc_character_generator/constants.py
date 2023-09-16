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
    HALFSLASH = "Halfslash"
    COMBAT_IDLE = "Combat Idle"


class Asset(str, Enum):
    BODY = "Body"
    HAIR = "Hair"
    NECK = "Neck"
    EYES = "Eyes"
    HEAD = "Head"
    WINGS = "Wings"
    SHIRT = "Shirt"
    PANTS = "Pants"
    SHOES = "Shoes"
    SOCKS = "Socks"
    SWORD = "Sword"
    EYEBROWS = "Eyebrows"
    OVER_SHIRT = "Over Shirt"
    FACIAL_HAIR = "Facial Hair"
    SHIELD_BASE = "Shield Base"
    SHIELD_TRIM = "Shield Trim"
    SHIELD_PAINT = "Shield Paint"
    SHIELD_PATTERN = "Shield Pattern"
    HEAD_ACCESSORY = "Head Accessory"


SHARED_ASSETS = {
    Asset.EYES,
    Asset.HEAD,
    Asset.SWORD,
    Asset.WINGS,
    Asset.EYEBROWS,
    Asset.SHIELD_BASE,
    Asset.SHIELD_TRIM,
    Asset.SHIELD_PAINT,
    Asset.SHIELD_PATTERN,
    Asset.HEAD_ACCESSORY,
}

PUT_ON_ORDER = [
    Asset.BODY,
    Asset.EYES,
    Asset.EYEBROWS,
    Asset.HAIR,
    Asset.FACIAL_HAIR,
    Asset.HEAD,
    Asset.HEAD_ACCESSORY,
    Asset.SHIRT,
    Asset.OVER_SHIRT,
    Asset.NECK,
    Asset.SOCKS,
    Asset.SHOES,
    Asset.PANTS,
    Asset.WINGS,
    Asset.SWORD,
    Asset.SHIELD_BASE,
    Asset.SHIELD_TRIM,
    Asset.SHIELD_PAINT,
    Asset.SHIELD_PATTERN,
]

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
    Action.BACKSLASH: "Combat 1h - Backslash",
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
    Action.BACKSLASH: 12,
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
    Asset.HAIR: {Asset.HEAD, Asset.HEAD_ACCESSORY},
    Asset.HEAD: {Asset.HAIR},
    Asset.HEAD_ACCESSORY: {Asset.HAIR},
}
ASSET_COMPLEMENTARITY = {
    Asset.HEAD_ACCESSORY: Asset.HEAD
}

PATH_TO_DATA = importlib.resources.files("lpc_character_generator") / "data"

FRAME_SIZE = 128
ROTATION_ORDER = [Direction.SOUTH, Direction.EAST, Direction.NORTH, Direction.WEST]
NON_ROTATION_ACTIONS = [Action.CLIMB]
NON_OPTIONAL_ASSETS = {Asset.BODY, Asset.SHOES, Asset.SHIRT, Asset.SWORD}

ALLOWED_DIRECTIONS = {
    Action.CLIMB: [Direction.NORTH]
}
GENDERED_ASSETS = {Sex.WOMAN: {Asset.FACIAL_HAIR}}
ASSET_TO_PARAM = {
    Asset.BODY: "body",
    Asset.HAIR: "hair",
    Asset.NECK: "neck",
    Asset.EYES: "eyes",
    Asset.HEAD: "head",
    Asset.WINGS: "wings",
    Asset.SHIRT: "shirt",
    Asset.PANTS: "pants",
    Asset.SHOES: "shoes",
    Asset.SOCKS: "socks",
    Asset.SWORD: "sword",
    Asset.EYEBROWS: "eyebrows",
    Asset.OVER_SHIRT: "over_shirt",
    Asset.FACIAL_HAIR: "facial_hair",
    Asset.SHIELD_BASE: "shield_base",
    Asset.SHIELD_TRIM: "shield_trim",
    Asset.SHIELD_PAINT: "shield_paint",
    Asset.SHIELD_PATTERN: "shield_pattern",
    Asset.HEAD_ACCESSORY: "head_accessory",
}
