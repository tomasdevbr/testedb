from math import ceil


class Orders:
    """A class for managing orders and combining them into batches."""
    def combine_orders(self, requests, n_max):
        """
        Combine orders into batches considering maximum batch size.

        Parameters
        ----------
        requests : array_like
            Array-like object containing individual order requests.
        n_max : int
            Maximum batch size.

        Returns
        -------
        int
            Number of batches needed to fulfill all orders.

        Notes
        -----
        This function calculates the number of batches required to fulfill all
        orders based on the given maximum batch size.

        """
        sum_requests = 0
        
        for request in requests:
            sum_requests += request

        if n_max == 0:
            return 0
            
        return ceil(sum_requests/n_max)


def main():
    """
    Main function to demonstrate the functionality of the Orders class.

    """
    orders = [70, 30, 10]
    n_max = 100
    expected_orders = 2

    how_many = Orders().combine_orders(orders, n_max)
    assert how_many == expected_orders


if __name__ == "__main__":
    main()
