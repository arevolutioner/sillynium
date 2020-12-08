<div style="text-align:center">
  <img src="images/logo_black.jpg" alt="Sillynium Logo" width="300" height="300">
</div>

# sillynium 

Automatically generate python selenium scripts by drawing coloured boxes around elements on a webpage.


## Installation

Ideally one would create a virtual environment and pip install -r requirements.txt from the directory.
```bash
C:/Path/To/sillynium: pip install -r requirements.txt
```
Then run [sillynium_lite.py](sillynium_lite.py)

## Usage

Read the [ROADMAP](ROADMAP.md) 

NOTE: [sillynium_lite.py](sillynium_lite.py) is a proof of concept open to the community to further develop:
- It was created just to test the concept of auto-generating selenium scripts
- It does not cover most use cases or elements in its current form
- In its current state it may **fail on your OS as it was only coded to handle Windows 10 and Chrome**
- Is severely limited in both scope and function.



Download / Clone the repo and run [sillynium_lite.py](sillynium_lite.py).

When the OpenCV window appears, click into it:
- Press '1' : Red : For Input boxs
- Press '2' : Orange : For grabbing text
- Press '3' : Green : For clicking a button
- Click + Hold 'Left Mouse Button' and drag to draw a box
- Press 'r' to reset the canvas and cache and start again
- Press 'q' to finish drawing and generate the script

After running check the generated script: [generated_script.py](generated_script.py)

## Roadmap

Please see [ROADMAP](ROADMAP.md)

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md)

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

Distributed under the [GNU-GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) License. See [LICENSE](LICENSE) for more information.

