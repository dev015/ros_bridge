#!/usr/bin/env python

#
# Copyright (c) 2018-2019 Intel Corporation
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.
#

"""
Classes to handle Carla spectator
"""

# ------------------------
#   IMPORTS
# ------------------------
from carla_ros_bridge.actor import Actor


class Spectator(Actor):
    """
    Actor Implementation Details for Spectators
    """

    @staticmethod
    def create_actor(carla_actor, parent):
        """
        Static Factory Method to create vehicle actors
        :param carla_actor: Carla Sensor Actor Object
        :type carla_actor: carla.Sensor
        :param parent: Parent of the new traffic actor,
        :type parent: carla_ros_bridge.Parent
        :return: Created sensor Actor
        :rtype: carla_ros_bridge.Sensor or derived type.
        """
        return Spectator(carla_actor=carla_actor, parent=parent)

    def __init__(self, carla_actor, parent, topic_prefix=None, append_role_name_topic_postfix=True):
        """
        Constructor for Spectator Class
        :param carla_actor: carla actor object
        :type carla_actor: carla.Actor
        :param parent: the parent of this
        :type parent: carla_ros_bridge.Parent
        :param topic_prefix: the topic prefix to be used for this actor
        :type topic_prefix: string
        :param append_role_name_topic_postfix: if this flag is set True,
            the role_name of the actor is used as topic postfix
        :type append_role_name_topic_postfix: boolean
        """
        if topic_prefix is None:
            topic_prefix = 'spectator'
        super(Spectator, self).__init__(
                        carla_actor=carla_actor,
                        parent=parent,
                        topic_prefix=topic_prefix,
                        append_role_name_topic_postfix=append_role_name_topic_postfix
        )
