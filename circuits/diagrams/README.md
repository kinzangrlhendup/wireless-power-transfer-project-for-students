# Circuit diagrams

| File | Description |
|---|---|
| [transmitter-schematic.png](transmitter-schematic.png) | Captured LTspice transmitter: supply, NE555, inverter, LTC4444, half bridge and TX resonator |
| [receiver-schematic.png](receiver-schematic.png) | Captured LTspice receiver: RX resonator, rectifier, protection, LT1376-5 and load |
| [system-block-diagram.svg](system-block-diagram.svg) | Overall system architecture |
| [resonant-link-schematic.svg](resonant-link-schematic.svg) | Stage 1 series-series resonant link |
| [full-prototype-block-diagram.svg](full-prototype-block-diagram.svg) | Development-stage overview |

The PNG files are visual records, not editable LTspice schematics. The receiver
capture contains a 5 ohm load and an ideal SHDN pulse source from the failed
5 V/1 A target trial. For the retained simulation conclusion and proposed
hardware UVLO, see [the full-system results](../../docs/10-full-system-results.md).
