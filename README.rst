===============================
Nefis
===============================


.. image:: https://img.shields.io/pypi/v/nefis.svg
        :target: https://pypi.python.org/pypi/nefis

.. image:: https://img.shields.io/travis/openearth/nefis-python.svg
        :target: https://travis-ci.org/openearth/nefis-python

.. image:: https://readthedocs.org/projects/nefis/badge/?version=latest
        :target: https://nefis.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/openearth/nefis-python/shield.svg
     :target: https://pyup.io/repos/github/openearth/nefis-python/
     :alt: Updates


NEFIS is a library of functions designed for scientific programs. These programs are characterised by their large volume of input and output data. NEFIS is able to store and retrieve large volumes of data on file or in shared memory. To achieve a good performance when storing and retrieving data, the files are self-describing binary direct access files.

* Free software: Lesser GNU General Public License v3
* Documentation: https://oss.deltares.nl


Building
--------
We aim to provide the binaries for different platforms as wheel files at pypi. If you want to install nefis from source you can follow the following steps:

* Install Delft3D (includes the nefis library)
* Install Anaconda

If you want to install the source code version (for developers) you can use pip install -e .

.. code:: bash

    export LIBRARY_PATH=$D3D_HOME/lib/:$LIBRARY_PATH
    export LD_LIBRARY_PATH=$D3D_HOME/bin/lnx64/flow2d3d/bin/:$LD_LIBRARY_PATH
    conda create --name main python=2.7
    source activate main
    git clone https://github.com/openearth/nefis-python
    cd nefis-python
    pip install -r requirements_dev.txt
    make install
    pip install -e .
    make test


Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

# nefis-python
