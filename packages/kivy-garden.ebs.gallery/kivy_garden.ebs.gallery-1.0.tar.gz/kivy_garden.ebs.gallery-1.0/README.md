Gallery Widget for Kivy
=======================

[![Github Build Status](https://github.com/ebs-universe/kivy_garden.ebs.gallery/workflows/Garden%20flower/badge.svg)](https://github.com/ebs-universe/kivy_garden.ebs.gallery/actions)

This package provides half of a simple Image Gallery / Carousel widget for 
Kivy. The other half is provided by the EBS linuxnode GalleryManager class. 

Most non-EBS applications would not benefit from this widget. The functionality 
provided here can just as easily be obtained by use of the Kivy ScreenManager 
widget, which also considerably more flexible. The reason ScreenManager was not
used here is primarily because I hadn't seen ScreenManager yet when the Image Gallery 
was first written. This widget may not be used in the future by the EBS Image Gallery, 
and if it is not, it will no longer be maintained.

This package is part of the EBS widget collection for Kivy. It is written in 
mostly Python and depends on the EBS core widgets and widget infrastructure package. 
For more information, see [kivy_garden.ebs.core](https://github.com/ebs-universe/kivy_garden.ebs.core)

See https://kivy-garden.github.io/ebs.flower/ for the rendered flower docs.

Please see the garden [instructions](https://kivy-garden.github.io) for 
how to use kivy garden flowers.


CI
--

Every push or pull request run the [GitHub Action](https://github.com/kivy-garden/flower/actions) CI.
It tests the code on various OS and also generates wheels that can be released on PyPI upon a
tag. Docs are also generated and uploaded to the repo as well as artifacts of the CI.


TODO
-------

* add your code

Contributing
--------------

Check out our [contribution guide](CONTRIBUTING.md) and feel free to improve the flower.

License
---------

This software is released under the terms of the MIT License.
Please see the [LICENSE.txt](LICENSE.txt) file.

How to release
===============

See the garden [instructions](https://kivy-garden.github.io/#makingareleaseforyourflower) for how to make a new release.
