import numpy as np

from astropy.modeling import models, fitting, Parameter
from astropy.modeling.optimizers import DEFAULT_ACC, DEFAULT_EPS
from astropy.stats import sigma_clipped_stats, sigma_clip
from astropy.modeling.core import FittableModel, custom_model, Model
from astropy.nddata import CCDData, Cutout2D

from astropy.convolution.utils import (discretize_center_1D, discretize_center_2D, discretize_linear_1D,
                                       discretize_bilinear_2D, discretize_oversample_1D, discretize_oversample_2D,
                                       discretize_integrate_1D, discretize_integrate_2D, DiscretizationError)


from matplotlib import pyplot as plt

__all__ = [
    'fit_model', 'model_to_image', 'fit_background',
    'fit_gaussian2d', 'print_model_params', 'plot_fit'
]


def fit_model(image, model, weights=None, maxiter=5000,
              epsilon=DEFAULT_EPS, acc=DEFAULT_ACC, estimate_jacobian=False):
    """
    Wrapper function to conveniently fit an image to an input model.

    Parameters
    ----------
    image : array
        2D array to fit.

    weights : array
        Weights for fitting.
        For data with Gaussian uncertainties, the weights should be
        1/sigma.

    model : `~astropy.modeling.FittableModel`
        AstroPy model to sample from.

    maxiter : int
        maximum number of iterations

    epsilon : float
        A suitable step length for the forward-difference
        approximation of the Jacobian (if model.fjac=None). If
        epsfcn is less than the machine precision, it is
        assumed that the relative errors in the functions are
        of the order of the machine precision.

    acc : float
        Relative error desired in the approximate solution

    estimate_jacobian : bool
        If False (default) and if the model has a fit_deriv method,
        it will be used. Otherwise the Jacobian will be estimated.
        If True, the Jacobian will be estimated in any case.

    Returns
    -------
    fitted_model, fitter

        * fitted_model : `~astropy.modeling.FittableModel`
            A copy of the input model with parameters set by the fitter.

        * fitter : LevMarLSQFitter
            Fitter used to estimate and set model parameters.
    """

    # Make x and y grid to fit to
    y_arange, x_arange = np.where(~(np.isnan(image)))

    z = image[(y_arange, x_arange)]

    w = None if weights is None else weights[(y_arange, x_arange)]

    # Fit model to grid
    fitter = fitting.LevMarLSQFitter()
    fitted_model= fitter(model, x_arange, y_arange, z, weights=w,
                         maxiter=maxiter, epsilon=epsilon, acc=acc, estimate_jacobian=estimate_jacobian)

    return fitted_model, fitter


def discretize_model(model, x_range, y_range=None, mode='center', factor=10):
    """
    NOTE: This a modified version of astropy's `astropy.convolution.utils.discretize_model`.
    There is a bookkeeping bug that does not allow CompoundModels to to be used in this function.
    A fix PR has been submitted to Astropy and this function will be removed once that PR is released.

    Function to evaluate analytical model functions on a grid.

    So far the function can only deal with pixel coordinates.

    Parameters
    ----------
    model : `~astropy.modeling.Model` or callable.
        Analytic model function to be discretized. Callables, which are not an
        instances of `~astropy.modeling.Model` are passed to
        `~astropy.modeling.custom_model` and then evaluated.
    x_range : tuple
        x range in which the model is evaluated. The difference between the
        upper an lower limit must be a whole number, so that the output array
        size is well defined.
    y_range : tuple, optional
        y range in which the model is evaluated. The difference between the
        upper an lower limit must be a whole number, so that the output array
        size is well defined. Necessary only for 2D models.
    mode : str, optional
        One of the following modes:
            * ``'center'`` (default)
                Discretize model by taking the value
                at the center of the bin.
            * ``'linear_interp'``
                Discretize model by linearly interpolating
                between the values at the corners of the bin.
                For 2D models interpolation is bilinear.
            * ``'oversample'``
                Discretize model by taking the average
                on an oversampled grid.
            * ``'integrate'``
                Discretize model by integrating the model
                over the bin using `scipy.integrate.quad`.
                Very slow.
    factor : float or int
        Factor of oversampling. Default = 10.

    Returns
    -------
    array : `numpy.array`
        Model value array

    Notes
    -----
    The ``oversample`` mode allows to conserve the integral on a subpixel
    scale. Here is the example of a normalized Gaussian1D:

    .. plot::
        :include-source:

        import matplotlib.pyplot as plt
        import numpy as np
        from astropy.modeling.models import Gaussian1D
        from astropy.convolution.utils import discretize_model
        gauss_1D = Gaussian1D(1 / (0.5 * np.sqrt(2 * np.pi)), 0, 0.5)
        y_center = discretize_model(gauss_1D, (-2, 3), mode='center')
        y_corner = discretize_model(gauss_1D, (-2, 3), mode='linear_interp')
        y_oversample = discretize_model(gauss_1D, (-2, 3), mode='oversample')
        plt.plot(y_center, label='center sum = {0:3f}'.format(y_center.sum()))
        plt.plot(y_corner, label='linear_interp sum = {0:3f}'.format(y_corner.sum()))
        plt.plot(y_oversample, label='oversample sum = {0:3f}'.format(y_oversample.sum()))
        plt.xlabel('pixels')
        plt.ylabel('value')
        plt.legend()
        plt.show()


    """
    if not callable(model):
        raise TypeError('Model must be callable.')
    if not isinstance(model, Model):
        model = custom_model(model)()
    ndim = model.n_inputs
    if ndim > 2:
        raise ValueError('discretize_model only supports 1-d and 2-d models.')

    if not float(np.diff(x_range)).is_integer():
        raise ValueError("The difference between the upper and lower limit of"
                         " 'x_range' must be a whole number.")

    if y_range:
        if not float(np.diff(y_range)).is_integer():
            raise ValueError("The difference between the upper and lower limit of"
                             " 'y_range' must be a whole number.")

    if ndim == 2 and y_range is None:
        raise ValueError("y range not specified, but model is 2-d")
    if ndim == 1 and y_range is not None:
        raise ValueError("y range specified, but model is only 1-d.")
    if mode == "center":
        if ndim == 1:
            return discretize_center_1D(model, x_range)
        elif ndim == 2:
            return discretize_center_2D(model, x_range, y_range)
    elif mode == "linear_interp":
        if ndim == 1:
            return discretize_linear_1D(model, x_range)
        if ndim == 2:
            return discretize_bilinear_2D(model, x_range, y_range)
    elif mode == "oversample":
        if ndim == 1:
            return discretize_oversample_1D(model, x_range, factor)
        if ndim == 2:
            return discretize_oversample_2D(model, x_range, y_range, factor)
    elif mode == "integrate":
        if ndim == 1:
            return discretize_integrate_1D(model, x_range)
        if ndim == 2:
            return discretize_integrate_2D(model, x_range, y_range)
    else:
        raise DiscretizationError('Invalid mode.')


def _validate_image_size(size):
    """
    Helper function to validate image size.
    Input size (pixels) should be an integers or a tuple of two integers.
    """

    error_message = "Input size (pixels) should be an integers or a tuple of two integers."

    if type(size) in [list, tuple, np.array]:
        assert len(size) == 2, error_message
        x_size, y_size = size

    elif np.issubdtype(type(size), np.number):
        x_size = size
        y_size = size

    else:
        raise ValueError(error_message)

    assert not x_size % 1 and not y_size % 1, error_message

    x_size = int(x_size)
    y_size = int(y_size)

    return x_size, y_size


def model_center_to_image_origin(center, size):
    """
    Given the center and size of an image, find the origin coordnate of the image.
    """

    x_size, y_size = _validate_image_size(size)

    center_error_message = "Center should be a tuple of two integers."
    assert type(center) in [list, tuple, np.array], center_error_message
    assert len(center) == 2, center_error_message

    origin = np.array(center) - np.floor_divide(np.array([x_size, y_size]), 2)

    return tuple(origin)


def model_to_image(model, size, mode='center', factor=1, center=None):
    """
    Converts 2D models into images using `astropy.convolution.utils.discretize_model`.

    Parameters
    ----------
    model : `~astropy.modeling.FittableModel` or callable.
        Analytic model function to be discretized. Callables, which are not an
        instances of `~astropy.modeling.FittableModel` are passed to
        `~astropy.modeling.custom_model` and then evaluated.

    size : int or tuple
        The x and y size (in pixels) of the image in pixels (must be an whole number).
        If only a single integer is provided, an image of equal x and y size
        is generated. If tuple is provided (x_size, y_size) is assumed (N.B reverse of `numpy.array.shape` output).

    mode : str, optional
        One of the following modes (`astropy.convolution.utils.discretize_model`):
            * ``'center'`` (default)
                Discretize model by taking the value
                at the center of the bin.
            * ``'linear_interp'``
                Discretize model by linearly interpolating
                between the values at the corners of the bin.
                For 2D models interpolation is bilinear.
            * ``'oversample'``
                Discretize model by taking the average
                on an oversampled grid.
            * ``'integrate'``
                Discretize model by integrating the model
                over the bin using `scipy.integrate.quad`.
                Very slow.

    factor : float or int
        Factor of oversampling. Default = 1 (no oversampling).

    center : tuple
        (x, y) Coordinate of the center of the image (in pixels).
        The origin of the image is defined as `origin = center - floor_divide(size, 2)`
        (i.e the image will range from (origin -> origin + size)). If None, the origin
        of the image is assumed to be at (0, 0) (i.e `center = floor_divide(size, 2)`).


    Returns
    -------
    array : `numpy.array`
        Model image
    """

    x_size, y_size = _validate_image_size(size)

    if center is None:
        x_origin, y_origin = (0, 0)
    else:
        x_origin, y_origin = model_center_to_image_origin(center, size)

    return discretize_model(
        model=model,
        x_range=[x_origin, x_origin + x_size],
        y_range=[y_origin, y_origin + y_size],
        mode=mode,
        factor=factor)


def fit_background(image, model=models.Planar2D(), sigma=3.0):
    """
    Fit sigma clipped background image using a user provided model.

    Parameters
    ----------
    image : array
        2D array to fit.

    model : `~astropy.modeling.FittableModel`
        AstroPy model to sample from. `Planar2D` is used by default.

    sigma : float or None
        The sigma value used to determine noise pixels. Once the pixels above this value are masked,
        the model provided is fit to determine the background.

    Returns
    -------
    fitted_model, fitter

        * fitted_model : `~astropy.modeling.FittableModel`
            A copy of the input model with parameters set by the fitter.

        * fitter : LevMarLSQFitter
            Fitter used to estimate and set model parameters.
    """
    fit_bg_image = image
    if sigma is not None:
        fit_bg_image = sigma_clip(image, sigma)
    return fit_model(fit_bg_image, model)


def fit_gaussian2d(image):
    """
    Fit a 2D gaussian to a source in an image.

    Parameters
    ----------
    image : array
        2D array to fit.

    Returns
    -------
    fitted_model : `~astropy.modeling.models.Gaussian2D`
        AstroPy Gaussian2D model with parameters set by the fitter.
    """

    # Estimate center of target
    y_mean, x_mean = np.array(image.shape) // 2  # Center guess

    # Create model to fit
    model = models.Gaussian2D(amplitude=image.max(),
                              x_mean=x_mean,
                              y_mean=y_mean,
                              fixed={}
                              )

    # Fit model to grid
    fitted_model, fit = fit_model(image, model)

    return fitted_model


def print_model_params(model):
    """Print the params and values of an AstroPy model"""
    for param, value in zip(model.param_names, model.parameters):
        print("{:0.4f}\t{}".format(value,param))


def plot_fit(model, image, mode='center', center=None,
             vmin=None, vmax=None, figsize=None, return_images=False):
    """
    Plot fitted model, its 1D fit profile and residuals.
    If trying to convert a model to image, use `petrofit.modeling.fitting.model_to_image` instead.
    This function dose not call `plt.show()`.

    Parameters
    ----------
    image : array
        2D array that was fit by the model.

    mode : str, optional
        One of the following modes (`astropy.convolution.utils.discretize_model`):
            * ``'center'`` (default)
                Discretize model by taking the value
                at the center of the bin.
            * ``'linear_interp'``
                Discretize model by linearly interpolating
                between the values at the corners of the bin.
                For 2D models interpolation is bilinear.
            * ``'oversample'``
                Discretize model by taking the average
                on an oversampled grid.
            * ``'integrate'``
                Discretize model by integrating the model
                over the bin using `scipy.integrate.quad`.
                Very slow.

    model : `~astropy.modeling.FittableModel`
        Original data that was fitted by the model.

        mode : str, optional
        One of the following modes (`astropy.convolution.utils.discretize_model`):
            * ``'center'`` (default)
                Discretize model by taking the value
                at the center of the bin.
            * ``'linear_interp'``
                Discretize model by linearly interpolating
                between the values at the corners of the bin.
                For 2D models interpolation is bilinear.
            * ``'oversample'``
                Discretize model by taking the average
                on an oversampled grid.
            * ``'integrate'``
                Discretize model by integrating the model
                over the bin using `scipy.integrate.quad`.
                Very slow.

    center : tuple
        (x, y) Coordinate of the center of the image (in pixels).
        The origin of the image is defined as `origin = center - floor_divide(size, 2)`
        (i.e the image will range from (origin -> origin + size)). If None, the origin
        of the image is assumed to be at (0, 0) (i.e `center = floor_divide(size, 2)`).

    vmin : float
        Min plot value

    vmax : float
        Max plot value

    figsize : tuple
        Figure size, should be (3*size, size).

    return_images : bool
        If true, this function returns a list of subplot Axes,
        Model-image and the residual (input image - model-image).

    Returns
    -------
    axs, model_image, residual_image : (array of `.axes.Axes`, array, array)
        If `return_images`, this function returns a list of subplot Axes,
        Model-image and the residual (input image - model-image).
    """

    if isinstance(image, CCDData) or isinstance(image, Cutout2D):
        image = image.data
    # Make Model Image
    # ----------------

    # Set the size of the model image equal to the fitted image
    fitted_image_size = (image.shape[1], image.shape[0])

    # Generate a model image from the model
    model_image = model_to_image(
        model=model,
        size=fitted_image_size,
        mode=mode,
        center=center
    )

    residual_image = image - model_image

    # Plot Model Image
    # ----------------

    fig, axs = plt.subplots(1, 3, figsize=figsize)

    axs[0].imshow(image, vmin=vmin, vmax=vmax)
    axs[0].set_title("Data")

    axs[1].imshow(model_image, vmin=vmin, vmax=vmax)
    axs[1].set_title("Model")

    axs[2].imshow(residual_image, vmin=vmin, vmax=vmax)
    axs[2].set_title("Residual")

    if return_images:
        return axs, model_image, residual_image
