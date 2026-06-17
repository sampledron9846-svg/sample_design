/*
 * Copyright (c) 2026 Dron Sankhala
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_4bit_counter (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path
    input  wire       ena,      // Enable
    input  wire       clk,      // Clock
    input  wire       rst_n     // Active-low reset
);

    reg [3:0] counter;

    always @(posedge clk) begin
        if (!rst_n)
            counter <= 4'b0000;
        else if (ena)
            counter <= counter + 1'b1;
    end

    // Display counter on lower four output pins
    assign uo_out = {4'b0000, counter};

    // Unused bidirectional pins
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Prevent unused input warnings
    wire _unused = &{ui_in, uio_in, 1'b0};

endmodule

`default_nettype wire
