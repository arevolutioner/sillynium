<p align="center">
  <img src="images/logo_wide.jpg" alt="Sillynium Logo" width=100%>
</p>

# sillynium 

Automatically generate python selenium scripts by drawing coloured boxes around elements on a webpage. Please see the [ROADMAP](ROADMAP.md) 

## Status

***Work-in-progress:***
- sillynium.py: Currently loads a URL, and injects JavaScript to allow you to draw on top of the webpage

***Contributing***
- Community contributions to any files in **sillynium directory** are open! 



## Usage

***Read the [ROADMAP](ROADMAP.md) first*** 

### sillynium.py

Simply run as you would any other python file




NOTE: [sillynium_lite](sillynium_lite) is a proof of concept only.
- It was created just to test the concept of auto-generating selenium scripts
- It does not cover most use cases or elements in its current form
- It may **fail on your OS as it was only coded to handle Windows 10 and Chrome**
- Is severely limited in both scope and function.

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

