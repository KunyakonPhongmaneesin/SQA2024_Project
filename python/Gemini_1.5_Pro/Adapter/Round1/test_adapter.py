from adapter  import EuropeanSocket, USAdapter, USAppliance

def test_us_appliance_with_adapter( ):
    # Arrange
    european_socket = EuropeanSocket()
    us_adapter = USAdapter(european_socket)
    us_appliance = USAppliance(us_adapter)

    # Act
    result = us_appliance.power_on()

    # Assert
    assert result == "US Appliance powered on."  

def test_us_appliance_without_adapter( ):
    # Arrange
    european_socket = EuropeanSocket()
    us_appliance = USAppliance(european_socket) # Directly using EuropeanSocket

    # Act
    result = us_appliance.power_on()

    # Assert
    assert result == "Incompatible power source!" 