# astro_data.py - Update Orekit astrodynamics data files.
# Copyright (C) 2019-2022 University of Texas
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tarfile
import requests
from os import path, remove
from orbdetpy import _root_dir, _data_dir
from orbdetpy.version import __version__

def format_weather(lines: str)->str:
    """Re-format space weather data into a more efficient form.
    """

    output = []
    c1 = [0, 5,  8, 11, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 47, 51, 55, 59, 63, 67,
          71, 75, 79, 83, 87, 89, 93,  99, 101, 107, 113, 119, 125]
    c2 = [5, 8, 11, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 47, 51, 55, 59, 63, 67, 71,
          75, 79, 83, 87, 89, 93, 99, 101, 107, 113, 119, 125, 131]
    for line in lines.splitlines():
        if (line == "END DAILY_PREDICTED"):
            break
        if (line and line[0].isnumeric()):
            output.append(",".join((line[i:j].strip() for i, j in zip(c1, c2))))
    return("\n".join(output))

def update_data()->None:
    """Download and re-format astrodynamics data from multiple sources.
    """

    if (not path.isdir(_data_dir)):
        uri = f"https://github.com/ut-astria/orbdetpy/releases/download/{__version__}/orekit-data.tar.gz"
        print(f"{_data_dir} not found; downloading {uri}")
        resp = requests.get(uri, timeout=10.0, stream=True)
        if (resp.status_code == requests.codes.ok):
            tgz = path.join(_root_dir, "orekit-data.tar.gz")
            with open(tgz, "wb") as fp:
                fp.write(resp.raw.read())
            tar = tarfile.open(tgz, "r:gz")
            tar.extractall()
            tar.close()
            remove(tgz)
        else:
            print(f"HTTP error: {resp.status_code}")

    updates = [["https://maia.usno.navy.mil/ser7/finals.all",
                path.join(_data_dir, "Earth-Orientation-Parameters", "IAU-1980", "finals.all"), None],
               ["https://maia.usno.navy.mil/ser7/finals2000A.all",
                path.join(_data_dir, "Earth-Orientation-Parameters", "IAU-2000", "finals2000A.all"), None],
               ["https://maia.usno.navy.mil/ser7/tai-utc.dat", path.join(_data_dir, "tai-utc.dat"), None],
               ["http://www.celestrak.com/SpaceData/SW-All.txt", path.join(_data_dir, "SpaceWeather.dat"), format_weather]]
    for u in updates:
        print(f"Updating {u[1]}")
        try:
            resp = requests.get(u[0], timeout=10.0)
            if (resp.status_code == requests.codes.ok):
                with open(u[1], "w") as fp:
                    fp.write(u[2](resp.text) if (u[2]) else resp.text)
            else:
                print(f"HTTP error: {resp.status_code}")
        except Exception as exc:
            print(exc)

if (__name__ == "__main__"):
    update_data()
