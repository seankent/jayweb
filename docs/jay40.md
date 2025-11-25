
# Jay40 Development Board

The Jay40 is a low-power FPGA development board built around the iCE40LP8K FPGA from Lattice Semiconductor.

The iCE40LP8K comes from the iCE40 LP/HX family of ultra-low power FPGAs. It is the largest FPGA in the family, featuring 7,680 Look-Up Tables (LUTs) and 128 kbits of Embedded Block RAM. The iCE40LP8K also includes two Phase Locked Loops for on-chip clock generation. When idle, the iCE40LP8K consumes just 250 \textmu A of static power. This combination of logic capacity and energy efficiency makes it an ideal choice for low power applications, such as battery-powered devices.

The Jay40 provides a convenient, flexible platform for working with the iCE40LP8K. Our goal was to give the designer as much access to the FPGA's logic resources as possible, while keeping the overhead to a minimum. While feature-rich boards can be appealing, when unused, these features consume precious I/O resources, board space, and power. They also add cost and complexity to the design.

When designing the board, we endeavored to keep the design as simple and modular as possible. We intentionally kept the feature set to a minimum, only including functionality that would be either widely used or add significant flexibility to the design. For the most part, this meant including only components essential to power and program the device. Any additional functionality can be attached through the board's I/O as and when required.

The following subsections provide a brief overview of the Jay40's key features.
