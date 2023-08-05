.. _image_segmentation:


Image Segmentation (`photutils.segmentation`)
=============================================

Introduction
------------
Photutils includes a general-use function to detect sources (both
point-like and extended) in an image using a process called `image
segmentation <https://en.wikipedia.org/wiki/Image_segmentation>`_. After
detecting sources using image segmentation, we can then measure their
photometry, centroids, and morphological properties by using additional
tools in Photutils.


Source Extraction Using Image Segmentation
------------------------------------------
Photutils provides tools to detect astronomical sources using image
segmentation, which is a process of assigning a label to every pixel
in an image such that pixels with the same label are part of the same
source. Detected sources must have a minimum number of connected pixels
that are each greater than a specified threshold value in an image. The
threshold level is usually defined at some multiple of the background
noise (sigma) above the background. The image can also be filtered
before thresholding to smooth the noise and maximize the detectability
of objects with a shape similar to the filter kernel.

Let's start by detecting sources in a synthetic image provided by the
:ref:`photutils.datasets <datasets>` module::

    >>> from photutils.datasets import make_100gaussians_image
    >>> data = make_100gaussians_image()

The source segmentation/extraction is performed using
the :func:`~photutils.segmentation.detect_sources`
function. We will use a convenience function called
:func:`~photutils.segmentation.detect_threshold` to produce a 2D
detection threshold image using simple sigma-clipped statistics to
estimate the background level and RMS.

The threshold level is calculated using the ``nsigma`` input as the
number of standard deviations (per pixel) above the background.  Here
we generate a simple threshold at 2 sigma (per pixel) above the
background::

    >>> from photutils.segmentation import detect_threshold
    >>> threshold = detect_threshold(data, nsigma=2.)

For more sophisticated analyses, one should generate a 2D background and
background-only error image (e.g., from your data reduction or by using
:class:`~photutils.background.Background2D`). In that case, a 2-sigma
threshold image is simply::

    >>> threshold = bkg + (2.0 * bkg_rms)  # doctest: +SKIP

Note that if the threshold includes the background level (as above),
then the image input into :func:`~photutils.segmentation.detect_sources`
should *not* be background subtracted. In other words, the input
threshold value(s) are compared directly to the input image. Because the
threshold returned by :func:`~photutils.segmentation.detect_threshold`
includes the background, we do not subtract the background from the data
here.

Let's find sources that have 5 connected pixels that are each greater
than the corresponding pixel-wise ``threshold`` level defined above
(i.e., 2 sigma per pixel above the background noise). Note that by
default "connected pixels" means "8-connected" pixels, where pixels
touch along their edges or corners. One can also use "4-connected"
pixels that touch only along their edges by setting ``connectivity=4``
in :func:`~photutils.segmentation.detect_sources`.

Here, we convolve the data with a 2D circular Gaussian kernel with a
FWHM of 3 pixels to smooth the image prior to thresholding:

.. doctest-requires:: scipy>=1.6.0

    >>> from astropy.convolution import Gaussian2DKernel, convolve
    >>> from astropy.stats import gaussian_fwhm_to_sigma
    >>> from photutils.segmentation import detect_sources
    >>> sigma = 3.0 * gaussian_fwhm_to_sigma  # FWHM = 3.
    >>> kernel = Gaussian2DKernel(sigma, x_size=3, y_size=3)
    >>> convolved_data = convolve(data, kernel, normalize_kernel=True)
    >>> segm = detect_sources(convolved_data, threshold, npixels=5)

The result is a :class:`~photutils.segmentation.SegmentationImage`
object with the same shape as the data, where detected sources are
labeled by different positive integer values. A value of zero is
always reserved for the background. Let's plot both the image and the
segmentation image showing the detected sources:

.. doctest-skip::

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> from astropy.visualization import SqrtStretch
    >>> from astropy.visualization.mpl_normalize import ImageNormalize
    >>> norm = ImageNormalize(stretch=SqrtStretch())
    >>> fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12.5))
    >>> ax1.imshow(data, origin='lower', cmap='Greys_r', norm=norm)
    >>> ax1.set_title('Data')
    >>> cmap = segm.make_cmap(seed=123)
    >>> ax2.imshow(segm, origin='lower', cmap=cmap, interpolation='nearest')
    >>> ax2.set_title('Segmentation Image')

.. plot::

    from astropy.convolution import Gaussian2DKernel, convolve
    from astropy.stats import gaussian_fwhm_to_sigma
    from astropy.visualization import SqrtStretch
    from astropy.visualization.mpl_normalize import ImageNormalize
    import matplotlib.pyplot as plt
    from photutils.datasets import make_100gaussians_image
    from photutils.segmentation import detect_threshold, detect_sources

    data = make_100gaussians_image()
    threshold = detect_threshold(data, nsigma=2.)
    sigma = 3.0 * gaussian_fwhm_to_sigma  # FWHM = 3.
    kernel = Gaussian2DKernel(sigma, x_size=3, y_size=3)
    convolved_data = convolve(data, kernel, normalize_kernel=True)
    segm = detect_sources(convolved_data, threshold, npixels=5)
    norm = ImageNormalize(stretch=SqrtStretch())
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12.5))
    ax1.imshow(data, origin='lower', cmap='Greys_r', norm=norm)
    ax1.set_title('Data')
    cmap = segm.make_cmap(seed=123)
    ax2.imshow(segm, origin='lower', cmap=cmap, interpolation='nearest')
    ax2.set_title('Segmentation Image')
    plt.tight_layout()

When the segmentation image is generated using image thresholding (e.g.,
using :func:`~photutils.segmentation.detect_sources`), the source
segments represent the isophotal footprints of each source.


Source Deblending
-----------------
In the example above, overlapping sources are detected as single
sources. Separating those sources requires a deblending procedure,
such as a multi-thresholding technique used by `SourceExtractor`_.
Photutils provides a :func:`~photutils.segmentation.deblend_sources`
function that deblends sources uses a combination
of multi-thresholding and `watershed segmentation
<https://en.wikipedia.org/wiki/Watershed_(image_processing)>`_. Note
that in order to deblend sources, they must be separated enough such
that there is a saddle between them.

The amount of deblending can be controlled with the two
:func:`~photutils.segmentation.deblend_sources` keywords ``nlevels``
and ``contrast``.  ``nlevels`` is the number of multi-thresholding
levels to use.  ``contrast`` is the fraction of the total source flux
that a local peak must have to be considered as a separate object.

Here's a simple example of source deblending:

.. doctest-requires:: scipy>=1.6.0, skimage

    >>> from photutils.segmentation import deblend_sources
    >>> segm_deblend = deblend_sources(convolved_data, segm, npixels=5,
    ...                                nlevels=32, contrast=0.001)

where ``segm`` is the :class:`~photutils.segmentation.SegmentationImage`
that was generated by :func:`~photutils.segmentation.detect_sources`.
Note that the ``convolved_data`` and ``npixels`` input values should
match those used in :func:`~photutils.segmentation.detect_sources`
to generate ``segm``. The result is a new
:class:`~photutils.segmentation.SegmentationImage` object containing the
deblended segmentation image:

.. plot::

    from astropy.convolution import Gaussian2DKernel, convolve
    from astropy.stats import gaussian_fwhm_to_sigma
    from astropy.visualization import SqrtStretch
    from astropy.visualization.mpl_normalize import ImageNormalize
    import matplotlib.pyplot as plt
    from photutils.datasets import make_100gaussians_image
    from photutils.segmentation import (detect_threshold, detect_sources,
                                        deblend_sources)

    data = make_100gaussians_image()
    threshold = detect_threshold(data, nsigma=2.)
    sigma = 3.0 * gaussian_fwhm_to_sigma  # FWHM = 3.
    kernel = Gaussian2DKernel(sigma, x_size=3, y_size=3)
    convolved_data = convolve(data, kernel, normalize_kernel=True)
    segm = detect_sources(convolved_data, threshold, npixels=5)
    segm_deblend = deblend_sources(convolved_data, segm, npixels=5)

    norm = ImageNormalize(stretch=SqrtStretch())
    fig, ax = plt.subplots(1, 1, figsize=(10, 6.5))
    cmap = segm_deblend.make_cmap(seed=123)
    ax.imshow(segm_deblend, origin='lower', cmap=cmap, interpolation='nearest')
    ax.set_title('Deblended Segmentation Image')
    plt.tight_layout()

Let's plot one of the deblended sources:

.. plot::

    from astropy.convolution import Gaussian2DKernel, convolve
    from astropy.stats import gaussian_fwhm_to_sigma
    import matplotlib.pyplot as plt
    from photutils.datasets import make_100gaussians_image
    from photutils.segmentation import (detect_threshold, detect_sources,
                                        deblend_sources)

    data = make_100gaussians_image()
    threshold = detect_threshold(data, nsigma=2.)
    sigma = 3.0 * gaussian_fwhm_to_sigma  # FWHM = 3.
    kernel = Gaussian2DKernel(sigma, x_size=3, y_size=3)
    convolved_data = convolve(data, kernel, normalize_kernel=True)
    segm = detect_sources(convolved_data, threshold, npixels=5)
    segm_deblend = deblend_sources(convolved_data, segm, npixels=5)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 4))
    slc = (slice(273, 297), slice(425, 444))
    ax1.imshow(data[slc], origin='lower')
    ax1.set_title('Data')
    cmap1 = segm.make_cmap(seed=123)
    ax2.imshow(segm.data[slc], origin='lower', cmap=cmap1,
               interpolation='nearest')
    ax2.set_title('Original Segment')
    cmap2 = segm_deblend.make_cmap(seed=123)
    ax3.imshow(segm_deblend.data[slc], origin='lower', cmap=cmap2,
               interpolation='nearest')
    ax3.set_title('Deblended Segments')
    plt.tight_layout()


Modifying a Segmentation Image
------------------------------
The :class:`~photutils.segmentation.SegmentationImage` object provides
several methods that can be used to visualize or modify itself (e.g.,
combining labels, removing labels, removing border segments) prior to
measuring source photometry and other source properties, including:

  * :meth:`~photutils.segmentation.SegmentationImage.reassign_label`:
    Reassign one or more label numbers.

  * :meth:`~photutils.segmentation.SegmentationImage.relabel_consecutive`:
    Reassign the label numbers consecutively, such that there are no
    missing label numbers (up to the maximum label number).

  * :meth:`~photutils.segmentation.SegmentationImage.keep_labels`:
    Keep only the specified labels.

  * :meth:`~photutils.segmentation.SegmentationImage.remove_labels`:
    Remove one or more labels.

  * :meth:`~photutils.segmentation.SegmentationImage.remove_border_labels`:
    Remove labeled segments near the image border.

  * :meth:`~photutils.segmentation.SegmentationImage.remove_masked_labels`:
    Remove labeled segments located within a masked region.

  * :meth:`~photutils.segmentation.SegmentationImage.outline_segments`:
    Outline the labeled segments for plotting.


Centroids, Photometry, and Morphological Properties
---------------------------------------------------
The :class:`~photutils.segmentation.SourceCatalog` class is the primary
tool for measuring the centroids, photometry, and morphological
properties of sources defined in a segmentation image. When the
segmentation image is generated using image thresholding (e.g., using
:func:`~photutils.segmentation.detect_sources`), the source segments
represent the isophotal footprint of each source and the resulting
photometry is effectively isophotal photometry.

The source properties can be accessed using
`~photutils.segmentation.SourceCatalog` attributes or
output to an Astropy `~astropy.table.QTable` using the
:meth:`~photutils.segmentation.SourceCatalog.to_table` method. Please
see :class:`~photutils.segmentation.SourceCatalog` for the the many
properties that can be calculated for each source. More properties are
likely to be added in the future.

Let's detect sources and measure their properties in a synthetic
image. `~photutils.segmentation.SourceCatalog` requires that the
input data be background-subtracted, so for this example we will use
the :class:`~photutils.background.Background2D` class to produce a
background and background noise image. After subtracting the background,
we define a 2D detection threshold image using only the background RMS
image. We set the threshold at the 2-sigma (per pixel) noise level.
In this example, the threshold does not include the background level
because it was already subtracted from the data:

.. doctest-requires:: scipy>=1.6.0

    >>> from photutils.datasets import make_100gaussians_image
    >>> from photutils.background import Background2D, MedianBackground
    >>> data = make_100gaussians_image()
    >>> bkg_estimator = MedianBackground()
    >>> bkg = Background2D(data, (50, 50), filter_size=(3, 3),
    ...                    bkg_estimator=bkg_estimator)
    >>> data -= bkg.background  # subtract the background
    >>> threshold = 2. * bkg.background_rms  # above the background

Now we find sources that have 5 connected pixels (``npixels`` keyword)
that are each greater than the corresponding threshold image defined
above. We also smooth the data with a 2D circular Gaussian kernel with a
FWHM of 3 pixels to filter the image prior to thresholding:

.. doctest-requires:: scipy>=1.6.0, skimage

    >>> from astropy.convolution import Gaussian2DKernel, convolve
    >>> from astropy.stats import gaussian_fwhm_to_sigma
    >>> from photutils.segmentation import detect_threshold, detect_sources
    >>> sigma = 3.0 * gaussian_fwhm_to_sigma  # FWHM = 3.
    >>> kernel = Gaussian2DKernel(sigma, x_size=3, y_size=3)
    >>> convolved_data = convolve(data, kernel, normalize_kernel=True)
    >>> npixels = 5
    >>> segm = detect_sources(convolved_data, threshold, npixels=npixels)
    >>> segm_deblend = deblend_sources(convolved_data, segm, npixels=npixels,
    ...                                nlevels=32, contrast=0.001)

As described earlier, the result is a
:class:`~photutils.segmentation.SegmentationImage` where sources are
labeled by different positive integer values.

Now let's measure the properties of the detected sources
defined in the segmentation image using a simple call
to :class:`~photutils.segmentation.SourceCatalog`. The
output `~astropy.table.QTable` of source properties is
generated by the :class:`~photutils.segmentation.SourceCatalog`
:meth:`~photutils.segmentation.SourceCatalog.to_table` method. Each row
in the table represents a source. The columns represent the calculated
source properties. Note that the only a subset of the source properties
are shown below. Please see `~photutils.segmentation.SourceCatalog` for
the list of the many properties that are calculated for each source:

.. doctest-requires:: scipy>=1.6.0, skimage

    >>> from photutils.segmentation import SourceCatalog
    >>> cat = SourceCatalog(data, segm_deblend, convolved_data=convolved_data)
    >>> tbl = cat.to_table()
    >>> tbl['xcentroid'].info.format = '.2f'  # optional format
    >>> tbl['ycentroid'].info.format = '.2f'
    >>> tbl['kron_flux'].info.format = '.2f'
    >>> print(tbl)
    label xcentroid ycentroid ... segment_fluxerr kron_flux kron_fluxerr
                              ...
    ----- --------- --------- ... --------------- --------- ------------
        1    235.21      1.25 ...             nan    512.09          nan
        2    494.00      5.76 ...             nan    544.60          nan
        3    207.32     10.02 ...             nan    695.14          nan
        4    364.80     11.19 ...             nan    736.52          nan
        5    258.29     11.84 ...             nan    664.64          nan
      ...       ...       ... ...             ...       ...          ...
       91    427.08    147.42 ...             nan    892.63          nan
       92    426.61    211.12 ...             nan    895.20          nan
       93    419.75    216.64 ...             nan    871.92          nan
       94    433.90    280.71 ...             nan    646.42          nan
       95    434.08    288.88 ...             nan    931.40          nan
    Length = 95 rows

The error columns are NaN because we did not input an error array (see
the Photometric Errors section below).

Let's now plot the calculated elliptical Kron apertures (based on the
shapes of each source) on the data:

.. doctest-skip::

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> from astropy.visualization import simple_norm
    >>> norm = simple_norm(data, 'sqrt')
    >>> fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12.5))
    >>> ax1.imshow(data, origin='lower', cmap='Greys_r', norm=norm)
    >>> ax1.set_title('Data')
    >>> cmap = segm_deblend.make_cmap(seed=123)
    >>> ax2.imshow(segm_deblend, origin='lower', cmap=cmap,
    ...            interpolation='nearest')
    >>> ax2.set_title('Segmentation Image')
    >>> cat.plot_kron_apertures((2.5, 1.0), axes=ax1, color='white', lw=1.5)
    >>> cat.plot_kron_apertures((2.5, 1.0), axes=ax2, color='white', lw=1.5)

.. plot::

    from astropy.convolution import Gaussian2DKernel, convolve
    from astropy.stats import gaussian_fwhm_to_sigma
    from astropy.visualization import simple_norm
    import matplotlib.pyplot as plt
    from photutils.datasets import make_100gaussians_image
    from photutils.background import Background2D, MedianBackground
    from photutils.segmentation import (detect_sources, deblend_sources,
                                        SourceCatalog)

    data = make_100gaussians_image()
    bkg_estimator = MedianBackground()
    bkg = Background2D(data, (50, 50), filter_size=(3, 3),
                       bkg_estimator=bkg_estimator)
    data -= bkg.background
    threshold = 2. * bkg.background_rms
    sigma = 3.0 * gaussian_fwhm_to_sigma  # FWHM = 3.
    kernel = Gaussian2DKernel(sigma, x_size=3, y_size=3)
    convolved_data = convolve(data, kernel, normalize_kernel=True)
    npixels = 5
    segm = detect_sources(convolved_data, threshold, npixels=npixels)
    segm_deblend = deblend_sources(convolved_data, segm, npixels=npixels,
                                   nlevels=32, contrast=0.001)
    cat = SourceCatalog(data, segm_deblend, convolved_data=convolved_data)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12.5))
    norm = simple_norm(data, 'sqrt')
    ax1.imshow(data, origin='lower', cmap='Greys_r', norm=norm)
    ax1.set_title('Data with Kron apertures')
    cmap = segm_deblend.make_cmap(seed=123)
    ax2.imshow(segm_deblend, origin='lower', cmap=cmap,
               interpolation='nearest')
    ax2.set_title('Segmentation Image with Kron apertures')
    cat.plot_kron_apertures((2.5, 1.0), axes=ax1, color='white', lw=1.5)
    cat.plot_kron_apertures((2.5, 1.0), axes=ax2, color='white', lw=1.5)
    plt.tight_layout()


We can also create a `~photutils.segmentation.SourceCatalog` object
containing only a specific subset of sources, defined by their
label numbers in the segmentation image:

.. doctest-requires:: scipy>=1.6.0, skimage

    >>> cat = SourceCatalog(data, segm_deblend, convolved_data=convolved_data)
    >>> labels = [1, 5, 20, 50, 75, 80]
    >>> cat_subset = cat.get_labels(labels)
    >>> tbl2 = cat_subset.to_table()
    >>> tbl2['xcentroid'].info.format = '.2f'  # optional format
    >>> tbl2['ycentroid'].info.format = '.2f'
    >>> tbl2['kron_flux'].info.format = '.2f'
    >>> print(tbl2)
    label xcentroid ycentroid ... segment_fluxerr kron_flux kron_fluxerr
                              ...
    ----- --------- --------- ... --------------- --------- ------------
        1    235.21      1.25 ...             nan    512.09          nan
        5    258.29     11.84 ...             nan    664.64          nan
       20    346.99     66.87 ...             nan    820.40          nan
       50    145.07    168.55 ...             nan    702.45          nan
       75    301.92    239.25 ...             nan    520.75          nan
       80     43.20    250.01 ...             nan    643.78          nan

By default, the :meth:`~photutils.segmentation.SourceCatalog.to_table`
includes only a small subset of source properties. The output table
properties can be customized in the `~astropy.table.QTable` using the
``columns`` keywords:

.. doctest-requires:: scipy>=1.6.0, skimage

    >>> cat = SourceCatalog(data, segm_deblend, convolved_data=convolved_data)
    >>> labels = [1, 5, 20, 50, 75, 80]
    >>> cat_subset = cat.get_labels(labels)
    >>> columns = ['label', 'xcentroid', 'ycentroid', 'area', 'segment_flux']
    >>> tbl3 = cat_subset.to_table(columns=columns)
    >>> tbl3['xcentroid'].info.format = '.4f'  # optional format
    >>> tbl3['ycentroid'].info.format = '.4f'
    >>> tbl3['segment_flux'].info.format = '.4f'
    >>> print(tbl3)
    label xcentroid ycentroid area segment_flux
                              pix2
    ----- --------- --------- ---- ------------
        1  235.2101    1.2460 38.0     421.5376
        5  258.2890   11.8421 55.0     370.8626
       20  346.9938   66.8697 73.0     480.2523
       50  145.0675  168.5479 33.0     714.4084
       75  301.9203  239.2540 37.0     210.0043
       80   43.1994  250.0146 55.0     340.2903

A `~astropy.wcs.WCS` transformation can also be input to
:class:`~photutils.segmentation.SourceCatalog` via the ``wcs`` keyword,
in which case the sky coordinates of the source centroids can be
calculated.


Background Properties
^^^^^^^^^^^^^^^^^^^^^
Like with :func:`~photutils.aperture.aperture_photometry`, the ``data``
array that is input to :class:`~photutils.segmentation.SourceCatalog`
should be background subtracted. If you input the background image
that was subtracted from the data into the ``background`` keyword
of :class:`~photutils.segmentation.SourceCatalog`, the background
properties for each source will also be calculated:

.. doctest-requires:: scipy>=1.6.0, skimage

    >>> cat = SourceCatalog(data, segm_deblend, background=bkg.background)
    >>> labels = [1, 5, 20, 50, 75, 80]
    >>> cat_subset = cat.get_labels(labels)
    >>> columns = ['label', 'background_centroid', 'background_mean',
    ...            'background_sum']
    >>> tbl4 = cat_subset.to_table(columns=columns)
    >>> tbl4['background_centroid'].info.format = '{:.10f}'  # optional format
    >>> tbl4['background_mean'].info.format = '{:.10f}'
    >>> tbl4['background_sum'].info.format = '{:.10f}'
    >>> print(tbl4)
    label background_centroid background_mean background_sum
    ----- ------------------- --------------- --------------
        1        5.2031158074    5.2024840319 197.6943932116
        5        5.2369739745    5.2231049504 287.2707722718
       20        5.2393038724    5.2702114208 384.7254337205
       50        5.1749011227    5.1984776900 171.5497637688
       75        5.1184051931    5.1235119327 189.5699415102
       80        5.2010035835    5.2251343812 287.3823909639


Photometric Errors
^^^^^^^^^^^^^^^^^^
:class:`~photutils.segmentation.SourceCatalog` requires inputting a
*total* error array, i.e., the background-only error plus Poisson noise
due to individual sources. The :func:`~photutils.utils.calc_total_error`
function can be used to calculate the total error array from a
background-only error array and an effective gain.

The ``effective_gain``, which is the ratio of counts (electrons or
photons) to the units of the data, is used to include the Poisson noise
from the sources. ``effective_gain`` can either be a scalar value or a
2D image with the same shape as the ``data``. A 2D effective gain image
is useful for mosaic images that have variable depths (i.e., exposure
times) across the field. For example, one should use an exposure-time
map as the ``effective_gain`` for a variable depth mosaic image in
count-rate units.

Let's assume our synthetic data is in units of electrons per
second. In that case, the ``effective_gain`` should be the
exposure time (here we set it to 500 seconds). Here we use
:func:`~photutils.utils.calc_total_error` to calculate the total error
and input it into the :class:`~photutils.segmentation.SourceCatalog`
class. When a total ``error`` is input, the
`~photutils.segmentation.SourceCatalog.segment_fluxerr` property is
calculated. `~photutils.segmentation.SourceCatalog.segment_flux`
and `~photutils.segmentation.SourceCatalog.segment_fluxerr` are the
instrumental flux and propagated flux error within the source segments:

.. doctest-requires:: scipy>=1.6.0, skimage

    >>> from photutils.utils import calc_total_error
    >>> effective_gain = 500.
    >>> error = calc_total_error(data, bkg.background_rms, effective_gain)
    >>> cat = SourceCatalog(data, segm_deblend, error=error)
    >>> labels = [1, 5, 20, 50, 75, 80]
    >>> cat_subset = cat.get_labels(labels)  # select a subset of objects
    >>> columns = ['label', 'xcentroid', 'ycentroid', 'segment_flux',
    ...            'segment_fluxerr']
    >>> tbl5 = cat_subset.to_table(columns=columns)
    >>> tbl5['xcentroid'].info.format = '{:.4f}'  # optional format
    >>> tbl5['ycentroid'].info.format = '{:.4f}'
    >>> tbl5['segment_flux'].info.format = '{:.4f}'
    >>> tbl5['segment_fluxerr'].info.format = '{:.4f}'
    >>> for col in tbl5.colnames:
    ...     tbl5[col].info.format = '%.8g'  # for consistent table output
    >>> print(tbl5)
    label xcentroid ycentroid segment_flux segment_fluxerr
    ----- --------- --------- ------------ ---------------
        1 235.15975 1.1019039    421.53765       13.163281
        5 258.28461  11.82915     370.8626       15.906871
       20  347.0215 66.918884    480.25233       18.710973
       50 145.06198 168.54152    714.40843       11.835923
       75 301.91639 239.25306    210.00431       12.230255
       80 43.219501 250.03333    340.29029       16.000811


Pixel Masking
^^^^^^^^^^^^^
Pixels can be completely ignored/excluded (e.g., bad pixels) when
measuring the source properties by providing a boolean mask image
via the ``mask`` keyword (`True` pixel values are masked) to the
:class:`~photutils.segmentation.SourceCatalog` class.


Filtering
^^^^^^^^^

`SourceExtractor`_'s centroid and morphological parameters are
always calculated from a convolved, or filtered, "detection" image
(``convolved_data``), i.e., the image used to define the segmentation
image. The usual downside of the filtering is the sources will be
made more circular than they actually are. If you wish to reproduce
`SourceExtractor`_ centroid and morphology results, then input the
``convolved_data`` (or ``kernel``, but not both). If ``convolved_data``
and ``kernel`` are both `None`, then the unfiltered ``data`` will be
used for the source centroid and morphological parameters. Note that
photometry is *always* performed on the unfiltered ``data``.


Reference/API
-------------
.. automodapi:: photutils.segmentation
    :no-heading:


.. _SourceExtractor:  https://sextractor.readthedocs.io/en/latest/
