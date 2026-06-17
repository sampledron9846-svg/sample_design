# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Starting 4-bit counter test")

    # 100 kHz clock
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Initialize inputs
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Apply reset
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)

    # Counter should be 0 after reset
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0

    # Count from 1 to 15
    for i in range(1, 16):
        await ClockCycles(dut.clk, 1)
        expected = i & 0xF
        assert dut.uo_out.value == expected, \
            f"Expected {expected}, got {int(dut.uo_out.value)}"

    # Counter should wrap around to 0
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0

    dut._log.info("4-bit counter test PASSED!")
