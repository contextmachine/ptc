# ptc

## run 
run e57 converter:
```
$python /path/to/dir/e57_reader.py
```
---
### run with options
custom set voxel_size = 0.01 and custom path to data:
```
$python /path/to/dir/e57_reader.py -v 0.01  -p /path/to/files
```

```-h, --help``` get help.\
```-p, --data_path```  Set path to e57 data folder.\
```-s, --save_path```   Set folder path to save .ply.\
```-v, --voxel_size```   Enter a value for pre-compression\
```-r, --render_size```   Enter a down sample value for render

to get help:
```
$python /path/to/dir/e57_reader.py -h
```