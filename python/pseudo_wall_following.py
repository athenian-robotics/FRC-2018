def navigate(current_dist, target_dist, orientation):
    # orientation is the angle of the robot relative to the target line
    # < 0 when outside of parallel but turned toward target       // Going to intersect
    # > 0 when outside of parallel but turned away from target    // Not going to intersect
    # == 0 when parallel with target                              // Not going to intersect
    # < 0 when inside of parallel but turned away from target     // Not going to intersect
    # > 0 when outside of parallel but turned toward target       // Going to intersect

    error = current_dist - target_dist
    dist_from_target_threshold = 10

    minimum_angular_when_not_intersecting = .4
    maximum_angular_when_not_intersecting = .8

    minimum_angular_when_intersecting = .2
    maximum_angular_when_intersecting = .6

    minimum_angular_when_parallel = .1
    maximum_angular_when_parallel = .2

    minimum_linear_when_not_intersecting = 0.0
    maximum_linear_when_not_intersecting = .4

    minimum_linear_when_intersecting = .5
    maximum_linear_when_intersecting = .7

    # Outside the target distance
    if error > dist_from_target_threshold:
        # Robot is parallel or point away from target line
        if orientation >= 0:
            # Not intersecting
            # A robot pointed far away from target line will almost rotate in place until it gets to parallel
            # Angular is more dominant in this position
            #
            # Turn left proportional to orientation
            # Angular will scale between minimum_angular_when_not_intersecting and maximum_angular_when_not_intersecting
            # Linear is inversely proportional to orientation
            # Linear will scale between minimum_linear_when_not_intersecting and maximum_linear_when_not_intersecting
            pass
        else:
            # Intersecting
            # Linear is more dominant in this position
            #
            # Turn left proportional to orientation
            # Angular will scale between minimum_angular_when_intersecting and maximum_angular_when_intersecting
            # Linear is proportional to orientation
            # Linear will scale between minimum_linear_when_intersecting and maximum_linear_when_intersecting
            pass

    # Inside the target distance
    elif error < -dist_from_target_threshold:
        # Robot is parallel or point away from target line
        if orientation <= 0:
            # Not intersecting
            # A robot pointed far away from target line will almost rotate in place until it gets to parallel
            # Angular is more dominant in this position
            #
            # Turn right proportional to orientation
            # Angular will scale between minimum_angular_when_not_intersecting and maximum_angular_when_not_intersecting
            # Linear is inversely proportional to orientation
            # Linear will scale between minimum_linear_when_not_intersecting and maximum_linear_when_not_intersecting
            pass
        else:
            # Intersecting
            # Linear is more dominant in this position
            #
            # Turn right proportional to orientation
            # Angular will scale between minimum_angular_when_intersecting and maximum_angular_when_intersecting
            # Linear is proportional to orientation
            # Linear will scale between minimum_linear_when_intersecting and maximum_linear_when_intersecting
            pass

    # Correct distance from the wall
    else:
        # Robot can go linear as fast as you want and minimal angular
        # Angular will scale between minimum_angular_when_parallel and maximum_angular_when_parallel
        pass
