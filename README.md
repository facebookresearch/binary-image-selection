# [Binary Image SelectiON (BISON)](https://hexiang-hu.github.io/bison)

This repository implements an evaluation script for measuring the mean BISON accuracy on the val2014 split of the COCO-caption dataset. If you use BISON to analyze your image-captioning system, please cite:

- Hexiang Hu, Ishan Misra, and Laurens van der Maaten. **Binary Image Selection (BISON): Interpretable Evaluation of Visual Grounding.** _arXiv:1901.06595, 2019.

## Requirements

- Python 3+
- Numpy 1.10.0+

## Usage

Please put your prediction file (format as shown in later section) in the folder **predictions/**, and specify the current annotation filepath, as well as the prediction filepath. The usage is listed as following:

```bash
python bison_eval.py [-h] [--anno_path ANNO_PATH] [--pred_path PRED_PATH]

optional arguments:
  -h, --help            show this help message and exit
  --anno_path ANNO_PATH
                        Path to the annotation file
  --pred_path PRED_PATH
                        Path to the prediction file
```

## File format for predictions

The model predictions used as input into the BISON evaluation script should be in the following file format:

```javascript
[
	{
		"bison_id": 0,
		"predicted_image_id": 50965,
	},
	...
]
```

## References

- [Binary Image Selection (BISON): Interpretable Evaluation of Visual Grounding](https://hexiang-hu.github.io/bison)
- [COCO captions](https://github.com/tylin/coco-caption)

## License
BISON is CC-BY-NC 4.0 licensed, as found in the LICENSE file.
