# Using a PLL 


## pll_blinky.sv

```systemverilog
module pll_blinky
(
    input clk,
    input rst,
    output logic out
);

logic pll_clk;
logic pll_lock;
logic blinky_rst;

assign blinky_rst = rst | ~pll_lock;

blinky u_blinky
(
    .clk(pll_clk),
    .rst(blinky_rst),
    .out(out)
);

// F_pll_clk = (F_clk * (DIVF + 1))/(2**DIVQ * (DIVR + 1))
SB_PLL40_CORE #(
    .FEEDBACK_PATH("SIMPLE"),
    .DIVF(7'h1),
    .DIVQ(3'h0),
    .DIVR(4'h0),
    .FILTER_RANGE(3'b001)
) u_sb_pll40_core (
    .REFERENCECLK(clk),
    .PLLOUTCORE(pll_clk),
    .LOCK(pll_lock),
    .RESETB(1'b1),
    .BYPASS(1'b0)
);

endmodule
```

## blinky.sv

```systemverilog
module pll_blinky
#(parameter MAX_COUNT = 6000000)
(
    input clk,
    input rst,
    output logic out
);

logic [23:0] cnt;
logic [23:0] cnt__nxt;
logic out__nxt;

assign cnt__nxt = (cnt == MAX_COUNT) ? 0 : cnt + 1;
assign out__nxt = (cnt == MAX_COUNT) ? ~out : out;

always @(posedge clk)
begin
    cnt <= rst ? 0 : cnt__nxt;
end

always @(posedge clk)
begin
    out <= rst ? 0 : out__nxt;
end

endmodule
```

## pll_blinky.pcf

```
set_io clk C4
set_io rst G1
set_io out E1
```

## Synthesis Command 

```bash
$ mkdir -p gen/
$ yosys -p "synth_ice40 -top pll_blinky -json gen/blinky.json" pll_blinky.sv blinky.sv
```



