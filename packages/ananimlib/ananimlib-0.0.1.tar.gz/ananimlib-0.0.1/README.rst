
============================================================
Welcome to *An*\ other *Anim*\ ation *Lib*\ rary (AnAnimLib)
============================================================

AnAnimlib, was inspired by `ManimLib <https://github.com/3b1b/manim>`_ by Grant
Sanderson of 3 Blue 1 Brown.  The aim of AnAnimlib is to facilitate the creation
of mathematically preceise animations through an intuitive and extensible API.

The following code spins a square it as it moves across the canvas.

.. code-block:: python

    import ananimlib as al

     rect = al.Rectangle([1,1])

     al.Animate(
         al.AddAnObject(rect),
         al.MoveTo(rect,[-3.0,0.0]),
         al.RunParallel(
             al.Move(rect, [6,0], duration=1.0),
             al.Rotate(rect, 2*3.1415, duration=1.0),
         ),
         al.Wait(1.0)
    )

    al.play_movie()


.. image:: quickstart_ex3.gif
    :width: 95%
    :align: center



