# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    
    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)
#     print(f"Output value 1: {dut.uo_out.value}")

#     await ClockCycles(dut.clk, 1)
#     print(f"Output value 2: {dut.uo_out.value}")

#     await ClockCycles(dut.clk, 1)
#     print(f"Output value 3: {dut.uo_out.value}")

#     await ClockCycles(dut.clk, 1)
#     print(f"Output value 4: {dut.uo_out.value}")

#     await ClockCycles(dut.clk, 1)
#     print(f"Output value 5: {dut.uo_out.value}")

#     await ClockCycles(dut.clk, 5)
#     print(f"Output value 10: {dut.uo_out.value}")

#     dut.ui_in.value = 9
#     await ClockCycles(dut.clk, 1000)
#     print(f"Output value 1: {dut.uo_out.value}")
#     dut.ui_in.value = 1

#     await ClockCycles(dut.clk, 1)
#     print(f"Output value 2: {dut.uo_out.value}")

#     await ClockCycles(dut.clk, 1)
#     print(f"Output value 3: {dut.uo_out.value}")

#     await ClockCycles(dut.clk, 1)
#     print(f"Output value 4: {dut.uo_out.value}")

#     await ClockCycles(dut.clk, 1)
#     print(f"Output value 5: {dut.uo_out.value}")

#     await ClockCycles(dut.clk, 5)
#     print(f"Output value 10: {dut.uo_out.value}")
#     # The following assersion is just an example of how to check the output values.
#     # Change it to match the actual expected output of your module:
#     # assert dut.uo_out.value == 50

#     # Keep testing the module by changing the input values, waiting for
#     # one or more clock cycles, and asserting the expected output values.
# # Reset
#     dut._log.info("Reset")
#     dut.ena.value = 1
#     dut.ui_in.value = 0
#     dut.uio_in.value = 0
#     dut.rst_n.value = 0
#     print("Starting conversion...")
#     type(dut.uo_out.value)
#     await ClockCycles(dut.clk, 10)
#     dut.rst_n.value = 1

#     dut._log.info("Test project behavior")

#     # Set the input values you want to test
#     dut.ui_in.value = 0
#     dut.uio_in.value = 0

#     # Wait for one clock cycle to see the output values
#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 0

#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 1

#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 4

#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 9

#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 16

#     await ClockCycles(dut.clk, 5)
#     assert dut.uo_out.value == 81

#     dut.ui_in.value = 8+1
#     await ClockCycles(dut.clk, 1000)
#     dut.ui_in.value = 1
#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 1
#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 3
#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 9
#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 27
#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 81

#     dut.ui_in.value = 8+2
#     await ClockCycles(dut.clk, 1000)
#     dut.ui_in.value = 2
#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 0
#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 1
#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 3
#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 6
#     await ClockCycles(dut.clk, 1)
#     assert dut.uo_out.value == 10

    expected_values = [
    [(1, 0), (2, 1), (3, 4), (4, 9), (5, 16),(65536,1)],
    [(1, 1), (2, 3), (3, 9), (4, 27), (5, 81),(65536,171)],
    [(1, 0), (2, 1), (3, 3), (4, 6), (5, 10),(65536,0)],
    [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5),(65536,59)],
    [(1, 0), (2, 1), (3, 2), (4, 5), (5, 12),(65536,1)],
    [(1, 2), (2, 1), (3, 3), (4, 4), (5, 7),(65536,148)],
    [(1, 1), (2, 1), (3, 1), (4, 2), (5, 2),(65536,113)],
    [(1, 2), (2, 3), (3, 7), (4, 43), (5, 15),(65536,91)]]
    # ... add more tuples for other input values

    for i in range(0, 8):
        dut.ui_in.value = 8 + i
        await ClockCycles(dut.clk, 1000)
        dut.ui_in.value = i
        previous_term = 0
        for j, (term, expected) in enumerate(expected_values[i]):
            clock_cycles = term - previous_term
            await ClockCycles(dut.clk, clock_cycles)
            print(f"Term: {term}, Expected: {expected}, Actual: {dut.uo_out.value}")
            assert dut.uo_out.value == expected
            previous_term = term