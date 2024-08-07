# Pandas assert-index-equal bug with MultiIndex

This repository demonstrates a possible bug in Pandas where `assert_frame_equal` hides the value of the `obj` parameter when there's a `MultiIndex` in the DataFrame, and there's a mismatch in that index. Check `main.py` for more details.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python main.py
```
