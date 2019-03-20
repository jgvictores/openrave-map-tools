# openrave-tools

OpenRAVE tools

## openrave-map-from-csv.py

## openrave-pp-to-stl.py
This script is designed to do the conversion between the `.pp` files obtained with the OpenRAVE convex decomposition model used/created [here](https://github.com/roboticslab-uc3m/teo-openrave-models/blob/875f4080f8d563b71bf8eea7aa75bb9037735084/scripts/python/generateConvexDecomposition.py) to the `.stl` file format, in order to be used with other frameworks (e.g. ArmarX).

To use, change [this line](https://github.com/roboticslab-uc3m/openrave-tools/blob/48e0d22b1fea083956eb7cb512849975a3523a8a/openrave-pp-to-stl.py#L21) to be the filename of the pp file you want to convert. Then run the python script in this folder:
```bash
python openrave-pp-to-stl.py
```
