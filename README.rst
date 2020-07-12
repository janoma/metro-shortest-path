Metro assignment
================

Shortest path with some added restrictions that allow to skip nodes.

Requirements
------------

Python (duh). Run `make init` to install requirements.

Unit tests
----------

Run with `nosetests tests`

Finding shortest route
======================

File format
-----------

The metro network is represented in a JSON file with the following structure:

* An arbitrary number of "lines" in the form of `name -> stations`,
  where `name` is a string and `stations` is an array of objects
* Each station has an `id` which is a string, and optionally a `color` field,
  which is a string with a value of `red` or `green`, or just `null`.

If a node id appears two times in the file with different colors, the file is
ill-formed, and a program reading it will have undefined behavior. The absence
of the `color` value is equivalent to a `null` color.

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
`"lines" : [ ... ]`.

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

Cue ominous music.
