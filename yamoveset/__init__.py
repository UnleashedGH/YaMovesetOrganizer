BLACKLISTED_WORDS = ['BAS', 'GRD', 'DEM']

KNOWN_ENTRIES = {
    0: 'STAND',
    1: 'STAND_S',
    2: 'RUN',
    3: 'BUKKU_F_S',
    4: 'BUKKU_B_S',
    5: 'BUKKU_L_S',
    6: 'BUKKU_R_S',
    7: 'BOOST_F_00',
    8: 'BOOST_F_01',
    9: 'BOOST_F_02',
    14: 'STEP_F_S',
    16: 'STEP_R_S',
    18: 'STEP_L_S',
    20: 'STEP_B_S',
    21: 'BUKKU_UP',
    23: 'BUKKU_DOWN',
    24: 'JUMP',
    25: 'JUMP',
    26: 'BUKKU_DOWN',
    28: 'JUMP',
    30: 'JUMP_FRONT_00',
    31: 'JUMP_FRONT_01',
    33: 'JUMP_FRONT_02',
    35: 'JUMP_BACK_00',
    36: 'JUMP_BACK_01',
    38: 'JUMP_BACK_02',
    44: 'BUKKU_F_S + STEP_F_S * 2',
    45: 'BOOST_F_02',
    46: 'BOOST_F_02',
    47: 'BOOST_F_02',
    48: 'BOOST_F_02',
    49: 'BOOST_F_00',
    50: 'GRD_KAMAE',
    51: 'GRD_KAMAE_S',
    52: 'STEP_F_S',
    54: 'GRD_KAMAE',
    55: 'GRD_KAMAE',
    56: 'GRD_KAMAE',
    57: 'GRD_KAMAE_S',
    58: 'GRD_KAMAE_S',
    59: 'GRD_KAMAE_S',
    60: 'GRD_L',
    61: 'GRD_L_S',
    62: 'GRD_L_L',
    63: 'GRD_L_L_S',
    64: 'GRD_L_R',
    65: 'GRD_L_R_S',
    66: 'GRD_BREAK',
    67: 'GRD_BREAK_S',
    68: 'STUN_00',
    69: 'STUN_01',
    70: 'STUN_02',
    71: 'STUN_00_S',
    72: 'STUN_01_S',
    73: 'STUN_02_S',
    190: 'STAND_00_S',
    191: 'STAND_01_S',
    210: 'DEM_START',
    224: 'STAND_SSJ3',
    225: 'STAND_SSJ3_S',
    300: 'Light Combo 1',
    301: 'Light Combo 2',
    302: 'Light Combo 3',
    303: 'Light Combo 4',
    304: 'Light Combo 5',
    310: 'Light Combo Alt 6',
    311: 'Light Combo Alt 7',
    312: 'Light Combo Alt 8',
    320: 'Light Combo Charge (70%)',
    321: 'Light Combo Charge (85%)',
    322: 'Light Combo Charge (100%)',
    325: 'Light Combo Charge Followup',
    330: 'Heavy Combo 1',
    331: 'Heavy Combo Charge (85%)',
    332: 'Heavy Combo Charge (100%)',
    333: 'Guard Break Charge',
    335: 'Heavy Combo 2',
    336: 'Heavy Combo 3',
    337: 'Heavy Combo 4',
    338: 'Heavy Combo 5',
    340: 'Light Combo 6',
    341: 'Light Combo 7',
    342: 'Light Combo 8',
    343: 'Light Combo 9',
    350: 'Heavy Combo Alt 3',
    351: 'Heavy Combo Alt 4',
    352: 'Heavy Combo Alt 5',
    360: 'Turn Back Attack 1',
    361: 'Turn Back Attack 1',
    362: 'Turn Back Attack 1',
    365: 'Turn Back Attack 2',
    366: 'Turn Back Attack 2',
    367: 'Turn Back Attack 2',
    370: 'Jumping Attack',
    372: 'Jumping Attack',
    373: 'Jump Front_02',
    375: 'Boost + LC',
    376: 'Boost + LC',
    377: 'Boost + RC',
    378: 'Boost + RC',
    410: 'Boost F_02 + Step_F_S',
    411: 'Boost F_02 + Step_F_S',
    415: 'Boost F_02 + Step_B_S',
    419: 'Step_F_S + Knock Away',
    420: 'Knock Away',
    426: 'Knock Away + LC',
    427: 'Knock Away + RC',
    441: 'Aura Boost Attack',
    446: 'Aura Boost Back Attack',
    450: 'Stance Change 1',
    451: 'Stance Change 2',
    460: 'Light Stamina Break Start',
    461: 'Heavy Stamina Break Start',
    462: 'Light Stamina Break End',
    463: 'Heavy Stamina Break End',
    475: 'Dual Ultimate Initiate',
    476: 'Dual Ultimate Join',
    520: 'SHOT_N',
    521: 'SHOT_N_LOOP',
    522: 'SHOT_F',
    523: 'SHOT_B',
    524: 'SHOT_L',
    525: 'SHOT_R',
    526: 'SHOT_F_LOOP',
    527: 'SHOT_B_LOOP',
    528: 'SHOT_L_LOOP',
    529: 'SHOT_R_LOOP',
    600: 'Grab Opponent',
    601: 'Grab Reaction 1',
    602: 'Grab Reaction 2',
    603: 'Grab Reaction 3',
    604: 'Grab Reaction 4',
}