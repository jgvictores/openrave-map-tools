#!/usr/bin/env python

from __future__ import with_statement # for python 2.5
__author__ = 'Juan G Victores'

import time, threading
import openravepy
if not __openravepy_build_doc__:
    from openravepy import *

def main(env,options):
    env.Load(options.scene)
    robots = env.GetRobots()
    for robotIdx, robot in enumerate(robots):
        print("Robot [%d]: %s" % (robotIdx, robot.GetName()))
        manipulators = robot.GetManipulators()
        for manipulatorIdx, manipulator in enumerate(manipulators):
            print("* Manipulator [%d,%d]: %s" % (robotIdx, manipulatorIdx, manipulator.GetName()))
            manipulatorJointIDs = manipulator.GetArmIndices()
            links = robot.GetLinks()
            for jointIdx, joint in enumerate(manipulatorJointIDs):
                print("** Joint [%d,%d,%d]: %s" % (robotIdx, manipulatorIdx, jointIdx, robot.GetJointFromDOFIndex(manipulatorJointIDs[jointIdx]).GetName()))
                for linkIdx, link in enumerate(links):
                    if( robot.DoesAffect(manipulatorJointIDs[jointIdx],link.GetIndex()) ):
                        print("*** Affects: %s" % (link.GetName()))

    while True:
        pass

from optparse import OptionParser
from openravepy.misc import OpenRAVEGlobalArguments

@openravepy.with_destroy
def run(args=None):
    """Command-line execution of the example.

    :param args: arguments for script to parse, if not specified will use sys.argv
    """
    parser = OptionParser(description='Displays all.')
    OpenRAVEGlobalArguments.addOptions(parser)
    parser.add_option('--scene',
                      action="store",type='string',dest='scene',default='data/lab1.env.xml',
                      help='OpenRAVE scene to load')
    (options, leftargs) = parser.parse_args(args=args)
    OpenRAVEGlobalArguments.parseAndCreateThreadedUser(options,main,defaultviewer=True)

if __name__=='__main__':
    run()
