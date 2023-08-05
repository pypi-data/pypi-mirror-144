# LyBerry dmenu

A simple LBRY client using [lyberry_api](https://git.tristans.cloud/tristan/lyberry_api) and [dmenu](https://tools.suckless.org/dmenu/). The [dmenu wrapper](https://pypi.org/project/dmenu/) from PyPI is an optional dependency, but LyBerry dmenu comes with a minimal emulation of the package.

## Usage

To install the latest version from Codeberg, run `python3 -m pip install git+https://codeberg.org/vertbyqb/lyberry_dmenu.git`.

To install from PyPI, run `python3 -m pip install lyberry_dmenu`.

To install from the cloned repository (can be useful for development), run `python3 -m pip install .`.

To run without installing, run `python3 ./src/start.py`.

Follow the prompts to find a claim. When you select a claim it will open it in your default player, which you can configure with lyberry_api's config file. (e.g. `~/.config/lyberry/conf.toml`).

## Copyright
Copyright (C) 2022 Vertbyqb

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Parts of this program (the `LyBerry_Dmenu.open_external()` function in `src/lyberry_dmenu/lyberrydmenu.py`) are copied from [LyBerry QT](https://git.tristans.cloud/tristan/lyberry_qt), which is Copyright (C) 2022 MyBeansAreBaked and is available under the same license.
