# Carla ROS Object Tracking



The ```carla_ros_object_tracking``` package is used to track objects by converting images from a ROS Topic to an OpenCV image by running the following command:



    roslaunch carla_ros_object_tracking object_tracking.launch



# Carla ROS Bounding Boxes

The ```carla_ros_object_tracking``` package can be used to draw the bounding boxes around the objects present in the CARLA world according to their location/rotation and convert the results into an OpenCV image.

![rviz setup](../assets/images/carla_bounding_box_01.png "box_01")
![rviz setup](../assets/images/carla_bounding_box_02.png "box_02")


# Carla ROS Datasets

The position,location, orientation, rotation of these objects as well as a label for these objects can be recorded via a json file `data.json`.

The json format is defined like this:

    { 
        "vehicle" = [
            {
              "id": "<NAME>",
              "x": 0.0, "y": 0.0, "z": 0.0, "yaw": 0.0, # pose of the sensor, relative to the vehicle
              <ADDITIONAL-VEHICLE-ATTRIBUTES>
            },
            ...
        ]
    }