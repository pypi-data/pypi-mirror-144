# SPDX-FileCopyrightText: 2022 UChicago Argonne, LLC
# SPDX-License-Identifier: MIT

from pathlib import Path
import shutil
from typing import List, Union
from warnings import warn

import platformdirs

from .results import Results


class Database:
    """Database of simulation results

    Parameters
    ----------
    path
        Path to database directory

    Attributes
    ----------
    path
        Base path for the database directory
    default_path
        Path used by default when creating instances if no path is specified
    results
        List of simulation results in database

    """

    _default_path = platformdirs.user_data_path('watts')
    _instances = {}

    def __new__(cls, path=None):
        # If no path specified, use global default
        if path is None:
            path = cls._default_path

        # If this class has already been instantiated before, return the
        # corresponding instance
        abs_path = Path(path).resolve()
        if abs_path in Database._instances:
            return Database._instances[abs_path]
        else:
            return super().__new__(cls)

    def __init__(self, path=None):
        # If no path specified, use global default
        if path is None:
            path = self._default_path

        # If instance has already been created, no need to perform setup logic
        if path in Database._instances:
            return

        # Create database directory if it doesn't already
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        self._path = path

        # Read previous results
        self._results = []
        for dir in sorted(self.path.iterdir(), key=lambda x: x.stat().st_ctime):
            try:
                self._results.append(Results.from_pickle(dir / ".result_info.pkl"))
            except Exception:
                warn(f"Could not read results from {dir}")

        # Add instance to class-wide dictionary
        Database._instances[path.resolve()] = self

    @property
    def path(self) -> Path:
        return self._path

    @property
    def default_path(self) -> Path:
        return self.get_default_path()

    @default_path.setter
    def default_path(self, path):
        self.set_default_path(path)

    @classmethod
    def set_default_path(cls, path: Union[str, Path]):
        """Set the default path used when instances are created

        Parameters
        ----------
        path
            Default path to use
        """

        cls._default_path = Path(path).resolve()

    @classmethod
    def get_default_path(cls) -> Path:
        """Get the default path used when instances are created

        Returns
        -------
        Default path
        """
        return cls._default_path

    @property
    def results(self) -> List[Results]:
        return self._results

    def add_result(self, result: Results):
        """Add a result to the database

        Parameters
        ----------
        result
            Simulation results to add

        """
        self._results.append(result)

        # Save result info that can be recreated
        result.save(result.base_path / ".result_info.pkl")

    def clear(self):
        """Remove all results from database"""
        for dir in self.path.iterdir():
            shutil.rmtree(dir)
        self.results.clear()

    def show_summary(self):
        """Show a summary of results in database"""
        for result in self.results:
            rel_path = result.base_path.relative_to(self.path)
            print(result.time, result.plugin, str(rel_path),
                  f"({len(result.inputs)} inputs)",
                  f"({len(result.outputs)} outputs)")
