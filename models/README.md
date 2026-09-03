# Simulation models

The Stage 1 model uses only native SPICE elements and therefore requires no
third-party model download. The current switching schematic uses LTspice-native
NE555, 2N3904, LTC4444, 1N5819 and LT1376-5 models. Both half-bridge
MOSFETs use the IRFH5406 model in the full-system simulation. This does not
approve a physical package or guarantee thermal performance.

Future switching-stage models should be downloaded from the component
manufacturer. Record the source URL, document revision, download date, licence and
file checksum in `component-model-manifest.csv`. Do not redistribute a vendor model
unless its licence permits redistribution.

Suggested folder convention:

```text
models/
├── native/          # Original models developed for this project
└── third-party/     # Vendor files permitted for local use
```

If a third-party model cannot be redistributed, keep the directory empty and give
students an official download link plus installation instructions.
