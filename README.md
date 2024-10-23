# IAS Machine Simulation
***

This is a simulation of an IAS (Institute for Advanced Study) machine, commonly referred to as the von Neumann machine, which follows the von Neumann architecture.

The machine processes a 40-bit word, which can be split into two 20-bit instructions.

The purpose of this study is to simulate the logic involved in receiving these words, primarily focusing on the following instructions ([Reference](https://www.ecs.csun.edu/~cputnam/Comp546/Stallings/tables/T02-Vertical.pdf)):

| Opcode | Instruction |
|:-----:|:-----|
| 00000001 | LOAD |
| 00100001 | STORE |
| 00001101 | JUMP LEFT |
| 00001110 | JUMP RIGHT |
| 00000101 | ADD |
| 00000110 | SUB |

For example, if the user wants to compute the sum of 1 + 1, both numbers are stored in memory, and the following instructions would need to be simulated:

| Instruction (hex) |
|:-----:|
| 106405065 |
| 2106600000 |

## Next objective
The next goal is to enable the "computer" to receive the instruction and configure itself accordingly.