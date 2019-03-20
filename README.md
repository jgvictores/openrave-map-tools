# openrave-tools

OpenRAVE tools

## openrave-map-from-csv.py

## openrave-pp-to-stl.py
This script is designed to do the conversion between the `.pp` files obtained with the OpenRAVE convex decomposition model used/created [here](https://github.com/roboticslab-uc3m/openrave-yarp-plugins/blob/develop/examples/openrave-YarpRobot-collision-sim.py) to the `.stl` file format, in order to be used with other frameworks (e.g. ArmarX).

To use, change [this line](https://github.com/roboticslab-uc3m/tools/blob/b565045f11cd0b2f0ec0fc403823d679b8a79fd3/programs/openraveppToSTL/openraveppToSTL.py#L21) to be the filename of the pp file you want to convert. Then run the python script in this folder:
```bash
python openrave-pp-to-stl.py
```
