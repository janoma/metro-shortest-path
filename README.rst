Metro assignment
================

Shortest path with some added restrictions that allow to skip nodes.

Requirements
------------

Python 3. Run ``make init`` to install requirements.

Unit tests
----------

Run with ``nosetests tests`` or ``make test``.

Finding shortest route
======================

File format
-----------

The metro network is represented in a JSON file with the following structure:

* An arbitrary number of "lines" in the form of ``name -> stations``,
  where ``name`` is a string and ``stations`` is an array of objects
* Each station has an ``id`` which is a string, and optionally a ``color`` field,
  which is a string with a value of ``red`` or ``green``, or just ``null``.

If a node id appears two times in the file with different colors, the file is
ill-formed, and a program reading it will have undefined behavior. The absence
of the ``color`` value is equivalent to a ``null`` color.

Example
-------

.. code-block:: JSON

  {
    "line_1" : [
      { "id" : "A" },
      { "id" : "B", "color" : null },
      { "id" : "C" },
      { "id" : "D", "color" : null },
      { "id" : "E", "color" : null },
      { "id" : "F" }
    ],
    "line_2" : [
      { "id" : "C", "color" : null },
      { "id" : "G", "color" : "green" },
      { "id" : "H", "color" : "red" },
      { "id" : "I", "color" : "green" },
      { "id" : "F" }
    ]
  }

Limitations
-----------

The format is painfully limited. It doesn't make sense that the top-level
objects be lines, when it could be something like an actual collection:
``"lines" : [ ... ]``.

For the purposes of the assignment this is enough and it works, but this
is an acknowledgment of the possible improvements.

Also, while it should be possible to just represent a graph in a more minimal
way, such as an adjacency matrix, the thought of lines is more aligned with
the regular real-life representation of metro networks worldwide, and it
satisfies the very simple property that the shortest distance between two
stations from the same line *without getting off a train* is by following
that line.

Running with an arbitrary file
------------------------------

Use ``metro.py`` to run cases from your own JSON files. As a fun example, try

.. code-block:: BASH

  python3 metro.py \
      --network=metro_santiago.json \
      --start="Plaza de Maipú" \
      --end="Plaza de Puente Alto"

then feel free to add ``--color=red`` to notice how it is one station shorter than
the same trip with ``--color=green``, answering a long-standing question I had,
as I used to live 4 blocks from *Plaza de Maipú* and a friend of mine 4 blocks
from *Plaza de Puente Alto* (or, as he would call it, *Alto Puente*).

This trip, which we both made, is one of the longest in the network, and caused
some debate between us as for ways of optimizing it.

Test cases from the assignment
------------------------------

Run and enjoy the colorful display.

.. code-block:: BASH

  python3 metro.py -n tests/network_from_assignment.json -s A -e F
  python3 metro.py -n tests/network_from_assignment.json -s A -e F -c=red
  python3 metro.py -n tests/network_from_assignment.json -s A -e F -c=green
