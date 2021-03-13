## Titan Rover Misc

### Launching the Simulation

1. Navigate to the "ros" directory.
    - This directory becomes the catkin workspace.
    - Alternatively, copy the contents of the "src" directory into the "src" directory of an existing catkin workspace, and navigate to the top-level directory of that workspace.

2. Source the setup script.
    - source ./devel/setup.bash
    - This can be added to your bashrc for convenience.

3. Use roslaunch on the launch file.
    - By default, only common components will be simulated (located in common_models).
    - To specify a specific mode to run, add an argument at the end of the roslaunch command:
    - roslaunch sim_world desert.launch mode:=<run_mode>
    - <run_mode> := common_models | arm_mode |auto_mode
