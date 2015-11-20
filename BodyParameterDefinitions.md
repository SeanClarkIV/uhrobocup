
```
    HeadYawAngle       = + 00.0     #head rotation sideways +left -right
    HeadPitchAngle     = + 00.0     #head up and down +down -up

    ShoulderPitchAngle = + 00.0     #arms +down and -up
    ShoulderRollAngle  = + 00.0     #arms sideways +up -down(0)
    ElbowYawAngle      = + 00.0     #forarm rotation -right clockwise +right counterclockwise
    ElbowRollAngle     = + 00.0     #forarm -up +down
    WristYawAngle      = + 00.0     #hand +clockwise - counterclockwise
    HandAngle          = + 00.0     #fingers +open -close

    HipYawPitchAngle   = + 00.0     #roll hip +in -out
    HipRollAngle       = + 00.0     #leg +out -in
    HipPitchAngle      = + 00.0     #body -forward +backward
    KneePitchAngle     = + 00.0     #forleg +back(120) -forward(0)
    AnklePitchAngle    = + 00.0     #foot +rollforward - rollbackward
    AnkleRollAngle     = + 00.0     #foot +left -right


    Head     = [HeadYawAngle, HeadPitchAngle]

    LeftArm  = [ShoulderPitchAngle, +ShoulderRollAngle, +ElbowYawAngle, +ElbowRollAngle, WristYawAngle, HandAngle]
    RightArm = [ShoulderPitchAngle, -ShoulderRollAngle, -ElbowYawAngle, -ElbowRollAngle, WristYawAngle, HandAngle]

    LeftLeg  = [HipYawPitchAngle, +HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, +AnkleRollAngle]
    RightLeg = [HipYawPitchAngle, -HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, +AnkleRollAngle]
```