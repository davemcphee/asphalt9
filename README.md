# Nintendo Switch // Asphalt 9 Controller Emulation

Switch controllers communicate with the Switch using bluetooth. With the right hardware (or OS),
Brickwerk's nxbt python package, and a bit of python code, we can define complex macros to run on the
Switch. [ https://github.com/Brikwerk/nxbt ]

## The right hardware or OS?

nxbt needs low-level access to the computer's bluetooth controller. On Windows and MacOS, it isn't possible
to get this low-level access to the built-in bluetooth controller, so an external bluetooth adapter is needed.

On linux, the built-in controller can be used, as long as you're running as root.

The nxbt repo comes with a Virtual machine config (using Vagrant) that attempts to get around this OS limitation,
but even with my fairly extensive experience of using Vagrant, I couldn't get this to work cleanly.

So: you'll either need a $20 bluetooth adapter (see nxbt docs for suggestions), or run this on linux. An old laptop
or even a raspberry Pi should work.

## Macros

nxbt macros look like this (this is an old MP1 loop):

```
COMPLETE_MP1_LOOP = """
A 0.2s
6s
LOOP 70
    Y 0.1s
    0.2s
    Y 0.1s
    1.6s
LOOP 7
    B 0.2s
    1.8s
A 0.2s
2.5s
A 0.2s
4.5s
PLUS 0.2s
1.5s
B 0.2s
2.5s
A 0.2s
3.5s"""
```

Each line contains either button / stick instructions (`A 0.2s`: Pres the A button for 0.2s), loop definitions (`LOOP 70`:
run the following indented lines 70 times) or pause instructions (`6s`: wait 6 seconds).

Your code can define multiple macros, and switch back and forth between different activities. You could run a car
hunt macro, then switch to MP1 for long enough for your tickets to refill. You could even exit the game and restart
it once an hour, in case of crashes, etc. 

## Running macros in python
The setup code looks a bit like this:

```python
args = get_args()
nx = nxbt.Nxbt()
target = reconnect_target(args)

controller = nx.create_controller(
    nxbt.PRO_CONTROLLER,
    reconnect_address=target,
)

nx.wait_for_connection(ci)

# Run our MACRO forever
while True:
    nx.macro(ci, COMPLETE_MP1_LOOP)
```

The very first time you run this, you'll need to configure the Switch to add this new controller, see this guide: 
https://github.com/Brikwerk/nxbt/blob/master/docs/img/change-grip-order-menu.png
