# FlexWrfInput
Tool read, manipulate, and write input files for FLEXPART-WRF

## Installation
### Requirements:
At the moment the installation is **only works for Linux systems**. Requrements are:
 * `python3.10`	
 * `poetry`

### Download
You need to download the module from the git repository. You can do this with the following command:
```bash
git clone git@github.com:ATMO-IUP-UHEI/FlexWrfInput.git [--branch <branch>]
```
where `<branch>` is the name of the branch you want to download. If you don't specify the branch, the `main` branch will be downloaded.

### Installation
To install the module you can use `poetry` or `pip` from the main folder of the directory. The installation with `poetry` is recommended. To install the module with `poetry` you can use the following command:
```bash
poetry install
```
To install the module with `pip` you can use the following command:
```bash
pip install .
```

### Testing
Tests are written in `pytest`. To run the tests in your environment you can use the following command:
```bash
python -m pytest
```

## Usage
`FlexWrfInput` is a python module. It offers utilities to read, manipulate, and write input files for FLEXPART-WRF. 

### Reading input files
The module is build around the class `FlexwrfInput`. It can be initialized and can then read the data of an `flexwrf.input` file. Usage example:
```python
from flexwrfinput import FlexwrfInput

# Initialize the class
flexwrf_input = FlexwrfInput()
# Read the data from the file
flexwrf_input.read('flexwrf.input')
```
Alternatively, you can **read the file directly using the `read_input` function, which is recommended:**
```python
from flexwrfinput import read_input

# Read the data from the file
flexwrf_input = read_input('flexwrf.input')
```

### Manipulating input files
The class `FlexwrfInput` has attributes that represent the division in the `flexwrf.input` files. These attributes are:
 * `pathnames`
 * `command`
 * `ageclasses`
 * `outgrid`
 * `outgrid_nest`
 * `receptor`
 * `species`
 * `releases`
They can be manipulated directly. For example:
```python
from flexwrfinput import read_input

# Read the data from the file
flexwrf_input = read_input('flexwrf.input')

# Change output directory
flexwrf_input.pathnames.outputpath = '/path/to/output'
```

#### Adding releases
Attributes that have multiple values assigned, such as the variables saved in `releases`, are saved as `list` objects (So e.g. `xpoint1` is a list that contains the values for all different particle releases.). If you want to add a new release, it is recommended to **start with a copy of an existing one using the `add_copy` method, and change the values afterwards**. So to add a new release and only change the releases x position would go as follows:
```python
from flexwrfinput import read_input

# Read the data from the file
flexwrf_input = read_input('flexwrf.input')

# Add a new release as copy of the first one (with index 0)
flexwrf_input.releases.add_copy(0)
# Change the x position of the new release
flexwrf_input.releases.xpoint1[-1] = 10
flexwrf_input.releases.xpoint2[-1] = 10
```

#### Saving input files
To save the manipulated input file you can use the `write` method of the `FlexwrfInput` class. Usage example:
```python
from flexwrfinput import read_input

# Read the data from the file
flexwrf_input = read_input('flexwrf.input')

# Change output directory
flexwrf_input.pathnames.outputpath = '/path/to/output'

# Save the file
flexwrf_input.write('flexwrf.input')
```