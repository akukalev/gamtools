from .segregation import open_segregation

def get_radial_position(segregation_data):
    """Get the radial position of each genomic window from a segregation table

    :param segregation_data: Segregation table generated by gamtools
    :returns: :class:`pandas.DataFrame` giving the radial position of each window
    """

    # Get the percentage genome coverage for each NP
    cov_per_np = 100 * segregation_data.mean()

    def get_window_radial_pos(segregation_row):
        """Internal function that calculates radial position for each row"""

        # Which NPs are positive for this window?
        nps_with_window = segregation_row.values.astype(bool)

        # Get the mean genome coverage of NPs positive for this window
        return cov_per_np[nps_with_window].mean()

    return segregation_data.apply(get_window_radial_pos, axis=1)

def radial_position_from_args(args):
    """Helper function to call get_radial_position from doit"""

    segregation_data = open_segregation(args.segregation_file)

    radial_position = get_radial_position(segregation_data)

    radial_position.to_csv(args.output_file, sep='\t')
