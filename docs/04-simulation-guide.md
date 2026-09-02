# 4. LTspice simulation guide

## 4.1 Open the model

Open `circuits/ltspice/01-resonant-link.asc`. The initial schematic contains:

- a 5 V peak, 100 kHz sine source;
- 2 ohm source resistance;
- two 30 microhenry inductors;
- 0.3 ohm winding resistance on each inductor;
- two 82 nanofarad series compensation capacitors;
- a 10 ohm AC load; and
- parameterised magnetic coupling.

## 4.2 Transient analysis

The included directive is:

```spice
.tran 0 2m 0 50n
```

Two milliseconds contains about 200 cycles at 100 kHz. The maximum timestep is
50 ns, giving approximately 200 points per switching period.

Run the simulation and plot:

1. `V(in)` — source voltage;
2. `V(out)` — load voltage;
3. `I(L1)` — transmitter current; and
4. `I(L2)` — receiver current.

Ignore the initial transient when reading steady-state amplitude.

## 4.3 Coupling sweep

The schematic contains:

```spice
.step param K list 0.02 0.05 0.10 0.15 0.20
K1 L1 L2 {K}
```

Use **View > Step Legend** to identify each trace. Observe that receiver voltage
and power generally rise with coupling in this operating range.

## 4.4 Frequency sweep

For a simple stepped transient exercise, change the source value to:

```spice
SINE(0 5 {F})
```

Temporarily disable the coupling sweep and add:

```spice
.param K=0.10
.step param F 80k 125k 5k
```

For finer results, use the portable AC netlist or the Python reference script.

## 4.5 Power calculation

For a resistor, instantaneous power is obtained by Alt-clicking the component.
Average the steady-state load power rather than reading a single instantaneous
point. LTspice measurement directives can also be added:

```spice
.meas tran Pload AVG V(out)*I(Rload) FROM 1.5m TO 2m
.meas tran Vin_rms RMS V(in) FROM 1.5m TO 2m
.meas tran Vout_rms RMS V(out) FROM 1.5m TO 2m
```

Depending on symbol orientation, LTspice may report resistor power with the
opposite sign. Use the passive sign convention and verify the component pin order.

## 4.6 Required screenshots and exports

For each student run, save:

- the schematic;
- the source and receiver waveforms;
- the coupling-step legend;
- the error log containing measured values;
- a CSV export of the principal waveforms; and
- a completed copy of the student result template.

## 4.7 Model limitations

The Stage 1 model does not yet include frequency-dependent coil resistance,
parasitic capacitance, inverter harmonics, rectifier nonlinearity, regulation,
misalignment geometry, electromagnetic compatibility or thermal behaviour.

## 4.8 Full-system schematic under construction

The switching transmitter and rectifying receiver are documented in
[`09-full-circuit-build-log.md`](09-full-circuit-build-log.md). The agreed workflow
is to finish the complete circuit first, then test it in the following order:

1. supply and NE555 oscillator;
2. complementary logic signals;
3. LTC4444 gate-driver outputs;
4. unloaded half bridge with a current-limited setup;
5. transmitter resonator;
6. coupled resonators;
7. receiver bridge and filter;
8. 5 V regulator with a dummy load; and
9. complete-system power, efficiency and thermal checks.

No screenshot or waveform from the under-construction schematic is labelled as
a simulation result until the model runs and the relevant measurements have been
recorded.
