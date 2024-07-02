HALPE28_KEYPOINTS = [
    'nose',
    'left_eye',
    'right_eye',
    'left_ear',
    'right_ear',
    'left_shoulder',
    'right_shoulder',
    'left_elbow',
    'right_elbow',
    'left_wrist',
    'right_wrist',
    'left_hip',
    'right_hip',
    'left_knee',
    'right_knee',
    'left_ankle',
    'right_ankle',
    'head',
    'neck',
    'pelvis',
    'left_bigtoe',
    'right_bigtoe',
    'left_smalltoe',
    'right_smalltoe',
    'left_heel',
    'right_heel',
    'left_middle_1',
    'right_middle_1'
]

HALPE28_LIMBS={
    'body': [
        ['left_ankle', 'left_knee'],
        ['left_knee', 'left_hip'],
        ['left_hip', 'pelvis'],
        ['right_ankle', 'right_knee'],
        ['right_knee', 'right_hip'],
        ['right_hip', 'pelvis'],
        ['head', 'neck'],
        ['neck', 'pelvis'],
        ['neck', 'left_shoulder'],
        ['left_shoulder', 'left_elbow'],
        ['left_elbow', 'left_wrist'],
        ['neck', 'right_shoulder'],
        ['right_shoulder', 'right_elbow'],
        ['right_elbow', 'right_wrist'],
        ['nose', 'left_eye'],
        ['nose', 'right_eye'],
        ['left_eye', 'left_ear'],
        ['right_eye', 'right_ear'],
        ['left_ankle', 'left_bigtoe'],
        ['left_ankle', 'left_smalltoe'],
        ['left_ankle', 'left_heel'],
        ['right_ankle', 'right_bigtoe'],
        ['right_ankle', 'right_smalltoe'],
        ['right_ankle', 'right_heel'],
        ['left_wrist', 'left_middle_1'],
        ['right_wrist', 'right_middle_1']
    ]
}

HALPE28_LIMBS_INDEX = {}
for k in HALPE28_LIMBS:
    HALPE28_LIMBS_INDEX[k] = [[
        HALPE28_KEYPOINTS.index(limb[0]),
        HALPE28_KEYPOINTS.index(limb[1])
    ] for limb in HALPE28_LIMBS[k]]
