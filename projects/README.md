# AND Gate

This project demonstrates the implementation of an AND Gate using both Python and Verilog.

## Files

- and_gate.py → Python implementation
- and_gate.v → Verilog module
- and_gate_tb.v → Verilog testbench

## Truth Table

| A | B | Output |
|---|---|--------|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

## Python

Run:

```bash
python and_gate.py
```

## Verilog

Compile:

```bash
iverilog and_gate.v and_gate_tb.v
```

Run:

```bash
vvp a.out
```

## Expected Output

```
A B | Y
0 0 | 0
0 1 | 0
1 0 | 0
1 1 | 1
```

## Author

Your Name

## License

MITs