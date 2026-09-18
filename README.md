# Cell Reproduction in a Dark Optical Trap

Data, analysis code and trained models for the paper *Cell Reproduction in a
Dark Optical Trap*, in which single living *Saccharomyces cerevisiae* cells are
confined in a claw dark tweezer — a dark optical trap formed by three displaced
Gaussian beams operating in the repulsive regime of light–matter interactions
($m = n_{\text{cell}}/n_{\text{medium}} < 1$).

**Preprint:** arXiv:2609.06193
**Paper:** DOI to be added upon publication
**Raw video recordings:** archived separately on Zenodo, DOI 10.5281/zenodo.22833929

---

## What is in this repository

```
.
├── analysis/                  Jupyter notebooks and scripts
│   ├── YOLO_YeastDetection.ipynb       training of the cell detector
│   ├── results_yolo.ipynb              detector performance metrics
│   ├── plots_hold2free.ipynb           confinement traces (Fig. 2a,c)
│   ├── distributions-traces.ipynb      position distributions (Fig. 2b,d)
│   ├── multiple-growing_analysis.ipynb reproduction curves (Fig. 3)
│   ├── single-growing_analysis.ipynb   single-cell growth curves
│   ├── cell_viability.ipynb            Iodixanol viability assay (Fig. S2)
│   ├── frames.ipynb                    frame extraction from recordings
│   ├── rename_frames.py                frame renaming utility
│   └── plot+video.py                   overlay of tracking on video
│
├── data/
│   ├── traces/                 per-cell position traces, trapped interval
│   ├── complete-traces/        per-cell traces, trapped + free intervals
│   ├── reproduction/           total-area curves per experimental condition
│   ├── detections/             raw YOLO detections per recording
│   ├── optprep.csv             Iodixanol viability assay, raw absorbance
│   └── Valores.xlsx            viability assay, original spreadsheet
│
├── model/
│   └── my_model.pt             YOLOv11s weights for yeast cell detection
│
└── figures/                    figures as published, in PDF
```

## Experimental conditions

Trace and reproduction files are named by condition:

| Prefix / folder | Condition |
|---|---|
| `trace_sNvM_claw` | confinement trace, solution *N*, recording *M* |
| `rep_1*` | claw dark tweezer, 10 min trapping |
| `rep_4*` | claw dark tweezer, 4 h trapping |
| `rep_0*` | claw dark tweezer, 1 h trapping |
| `rep_gaussian_*` | conventional Gaussian tweezer, 10 min trapping |
| `rep_control_*` | free-growing cells, no laser |

Solutions 1 to 9 are the trapping media described in the Supplementary
Materials; solution 7 ($n = 1.401$) was used for all trapping experiments and
solution 9 ($n = 1.338$) for the Gaussian comparison.

## Reproducing the analysis

```bash
pip install -r requirements.txt
jupyter lab
```

Each notebook reads from `data/` and writes its figure to `figures/`. The
notebooks are independent of one another and can be run in any order, with one
exception: `YOLO_YeastDetection.ipynb` produces the weights in `model/`, which
the tracking notebooks consume.

Frame-by-frame image sequences are **not** included here — they are extracted
from the recordings archived on Zenodo using `analysis/frames.ipynb`.

## Data description

Position traces are given in pixels; the calibrated scale is
0.053 µm per pixel and recordings were acquired at 30 fps. Columns
`Centro_X` and `Centro_Y` are the centre of the detected bounding box and
`Confiança` is the detector confidence score. Cell areas in the reproduction
files are bounding-box areas, normalised by the area of the mother cell in
each realisation.

## Citation

```bibtex
@article{hertz2026cell,
  title   = {Cell Reproduction in a Dark Optical Trap},
  author  = {Hertz, Ariel and Dias, Gabriel and Fragoso, Carlos L. R.
             and De Falco, Anna and Khoury, A. Z. and Guerreiro, Thiago},
  journal = {},
  year    = {2026},
  doi     = {}
}
```

## License

Code released under the MIT License; data released under CC BY 4.0.
