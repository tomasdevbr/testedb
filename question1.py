class Contract:
    """
    Represent a contract with an identifier and debt value.
    
    Attributes
    ----------
    id : int
        The identifier of the contract.
    debt : int
        The debt value of the contract.

    """
    def __init__(self, id, debt):
        """
        Initialize a new Contract instance.

        Parameters
        ----------
        id : int
            The identifier of the contract.
        debt : int
            The debt value of the contract.

        """
        self.id = id
        self.debt = debt

    def __str__(self):
        """
        Return a string representation of the Contract instance.

        Returns
        -------
        str
            A string representation in the format 'id=id, debt=debt'.

        """
        return 'id={}, debt={}'.format(self.id, self.debt)

    @staticmethod
    def get_debt(contract):
        """
        Return the debt value of the contract.

        Parameters
        ----------
        contract : Contract
            The contract object.

        Returns
        -------
        int
            The debt value of the contract.

        """
        return contract.debt


class Contracts:
    """Represent a collection of contracts and provides methods for contract operations."""
    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        """
        Select the top N open contracts sorted by debt in descending order, excluding renegotiated contracts.

        Parameters
        ----------
        open_contracts : list of Contract
            List of open contracts.
        renegotiated_contracts : list of int
            List of IDs of renegotiated contracts.
        top_n : int
            Number of top contracts to select.

        Returns
        -------
        list of int
            List of IDs of the top N open contracts, sorted by debt in descending order.

        """
        contracts = sorted(
            (contract for contract in open_contracts if contract.id not in renegotiated_contracts), 
            key=Contract.get_debt,
            reverse=True
        )
        return [contract.id for contract in contracts[:top_n]]


def main():
    """Main function to demonstrate the functionality of the Contracts class."""
    contracts = [
        Contract(1, 1),
        Contract(2, 2),
        Contract(3, 3),
        Contract(4, 4),
        Contract(5, 5)
    ]
    renegotiated = [3]
    top_n = 3
    expected_open_contracts = [5, 4, 2]

    actual_open_contracts = Contracts().get_top_N_open_contracts(contracts, renegotiated, top_n)
    assert expected_open_contracts == actual_open_contracts


if __name__ == "__main__":
    main()